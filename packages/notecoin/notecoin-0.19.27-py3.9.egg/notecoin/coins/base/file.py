import logging
import os
from datetime import datetime

from notecoin.base.database.lanzou import LanzouDirectory
from notecoin.coins.base.load import LoadDataKline
from notecoin.utils.time import day_during, month_during, week_during
from notefile.compress import tarfile

logger = logging.getLogger()


class FileProperty:
    def __init__(self, exchange_name, data_type='kline', path='~/workspace/tmp', start_date=datetime.today(),
                 end_date=datetime.today(), freq='daily', timeframe='1m', file_format='%Y%m%d'):
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
        self.file_pro = FileProperty(exchange_name=exchange.name.lower(), path=path,
                                     freq=freq, data_type=data_type, timeframe=timeframe,
                                     start_date=start_date, end_date=end_date, file_format=file_format)
        self.drive = LanzouDirectory(fid=5679873)

    def sync(self):
        self.drive.scan_all_file()
        self.drive.sync(f'{self.file_pro.path}/notecoin')

    def tar_exists(self):
        if self.drive.file_exist(self.file_pro.file_path_tar(False)):
            return True
        if os.path.exists(self.file_pro.file_path_tar()):
            return False

    def _load_and_save(self) -> bool:
        self.sync()
        if self.tar_exists():
            return False

        logger.info(f'download for {self.file_pro.file_path_tar(absolute=False)}')
        exchan = LoadDataKline(self.exchange)
        exchan.table.delete_all()
        unix_start, unix_end = int(self.file_pro.start_date.timestamp() * 1000), int(
            self.file_pro.end_date.timestamp() * 1000)
        # 下载
        exchan.load_all(timeframe=self.file_pro.timeframe, unix_start=unix_start, unix_end=unix_end)
        # 保存
        exchan.table.to_csv_all(self.file_pro.file_path_csv(), page_size=100000)
        # 压缩
        with tarfile.open(self.file_pro.file_path_tar(), "w:xz") as tar:
            tar.add(self.file_pro.file_path_csv(),
                    arcname=self.file_pro.arcname(self.file_pro.file_path_csv()))
        # 删除
        os.remove(self.file_pro.file_path_csv())
        exchan.table.delete_all()
        return True

    def _load(self, start_end_fun):
        index = 1
        for i in range(1, 10000):
            self.file_pro.start_date, self.file_pro.end_date = start_end_fun(-i)
            if self._load_and_save():
                index += 1
            if index > 3650:
                break

    def load(self):
        if self.file_pro.freq == 'daily':
            self.file_format = '%Y%m%d'
            self._load(day_during)
        elif self.file_pro.freq == 'weekly':
            self.file_format = '%Y%m%d'
            self._load(week_during)
        elif self.file_pro.freq == 'monthly':
            self.file_format = '%Y%m'
            self._load(month_during)
