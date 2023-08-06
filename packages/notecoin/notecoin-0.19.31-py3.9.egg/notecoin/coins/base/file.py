import copy
import logging
import os
from datetime import datetime, timedelta

from notecoin.base.database.lanzou import LanzouDirectory
from notecoin.coins.base.load import LoadDataKline
from notecoin.utils.time import day_during, month_during, week_during
from notefile.compress import tarfile

logger = logging.getLogger()


class FileProperty:
    def __init__(self,
                 exchange_name='okex',
                 data_type='kline',
                 path='~/workspace/tmp',
                 start_date=datetime.today(),
                 end_date=datetime.today(),
                 freq='daily',
                 timeframe='1m',
                 file_format='%Y%m%d'):
        self.path = path
        self.freq = freq
        self.data_type = data_type
        self.timeframe = timeframe
        self.start_date = start_date
        self.end_date = end_date
        self.file_format = file_format
        self.exchange_name = exchange_name

    def file_path_dir(self, absolute=True):
        path = f"notecoin/{self.exchange_name}/{self.data_type}-{self.freq}-{self.timeframe}"
        if absolute:
            path = f"{self.path}/{path}"
            if not os.path.exists(path):
                os.makedirs(path)
        return path

    @property
    def filename_prefix(self):
        return f"{self.exchange_name}-{self.data_type}-{self.freq}-{self.timeframe}-{self.start_date.strftime(self.file_format)}"

    def file_path_csv(self, absolute=True):
        return f"{self.file_path_dir(absolute)}/{self.filename_prefix}.csv"

    def file_path_tar(self, absolute=True):
        return f"{self.file_path_dir(absolute)}/{self.filename_prefix}.tar"

    def arcname(self, file):
        return os.path.join(self.file_path_dir(False), os.path.basename(file))


class DataFileProperty:
    def __init__(self, exchange, data_type='kline', path='~/workspace/tmp', start_date=datetime.today(),
                 end_date=datetime.today(), freq='daily', timeframe='1m', file_format='%Y%m%d'):
        self.exchange = exchange
        self.file_pro = FileProperty(exchange_name=exchange.name.lower(), path=path, freq=freq,
                                     data_type=data_type, timeframe=timeframe, start_date=start_date, end_date=end_date,
                                     file_format=file_format)
        self.drive = LanzouDirectory(fid=5679873)

    def sync(self, path):
        self.drive.scan_all_file()
        self.drive.sync(f'{path}/notecoin')

    def tar_exists(self):
        if self.drive.file_exist(self.file_pro.file_path_tar(False)):
            return True
        if os.path.exists(self.file_pro.file_path_tar()):
            return False

    def _daily_load_and_save(self, file_pro: FileProperty) -> bool:
        self.sync(self.file_pro.path)
        if self.tar_exists():
            return False

        logger.info(f'download for {file_pro.file_path_tar(absolute=False)}')
        exchan = LoadDataKline(self.exchange)
        exchan.table.delete_all()
        unix_start, unix_end = int(file_pro.start_date.timestamp() * 1000), int(file_pro.end_date.timestamp() * 1000)
        # 下载
        exchan.load_all(timeframe=file_pro.timeframe, unix_start=unix_start, unix_end=unix_end)
        # 保存
        exchan.table.to_csv_all(file_pro.file_path_csv(), page_size=100000)
        # 压缩
        with tarfile.open(file_pro.file_path_tar(), "w:xz") as tar:
            tar.add(file_pro.file_path_csv(), arcname=file_pro.arcname(file_pro.file_path_csv()))
        # 删除
        os.remove(file_pro.file_path_csv())
        exchan.table.delete_all()
        return True

    def _merge_and_save(self, file_pro: FileProperty) -> bool:
        self.sync(self.file_pro.path)
        if self.tar_exists():
            return False

        logger.info(f'download for {file_pro.file_path_tar(absolute=False)}')

        result = []
        for i in range(1000):
            day = copy.deepcopy(file_pro)
            day.freq = 'daily'
            day.start_date, day.end_date = file_pro.start_date + timedelta(days=i), file_pro.start_date + timedelta(
                days=i + 1)
            if day.start_date < file_pro.start_date:
                continue
            if day.start_date > file_pro.end_date:
                break
            # download
            fid = self.drive.file_fid(day.file_path_tar(False))
            if fid == -1:
                self._daily_load_and_save(day)
            else:
                self.drive.drive.down_file_by_id(fid, save_path=self.file_pro.path, overwrite=True)
                # unzip
                with tarfile.open(day.file_path_tar(), "r:xz") as tar:
                    tar.extractall(path=day.path)

            result.extend([line for line in open(day.file_path_csv(), 'r').read().split('\n') if len(line) > 0])
            os.remove(day.file_path_csv())
            os.remove(day.file_path_tar())
            # remove
        with open(file_pro.file_path_csv(), 'w') as fw:
            fw.write('\n'.join(result))
        # 压缩
        with tarfile.open(file_pro.file_path_tar(), "w:xz") as tar:
            tar.add(file_pro.file_path_csv(), arcname=file_pro.arcname(file_pro.file_path_csv()))
        # 删除
        os.remove(file_pro.file_path_csv())
        return True

    def _load(self, start_end_fun):
        index = 1
        for i in range(1, 10000):
            self.file_pro.start_date, self.file_pro.end_date = start_end_fun(-i)
            if self._daily_load_and_save(self.file_pro):
                index += 1
            if index > 3650:
                break

    def _merge(self, start_end_fun):
        index = 1
        for i in range(1, 10):
            self.file_pro.start_date, self.file_pro.end_date = start_end_fun(-i)
            if self._merge_and_save(self.file_pro):
                index += 1
            if index > 3650:
                break

    def load(self):
        if self.file_pro.freq == 'daily':
            self.file_format = '%Y%m%d'
            self._load(day_during)
        elif self.file_pro.freq == 'weekly':
            self.file_format = '%Y%m%d'
            self._merge(week_during)
        elif self.file_pro.freq == 'monthly':
            self.file_format = '%Y%m'
            self._merge(month_during)
