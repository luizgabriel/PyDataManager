import pandas as pd
import os

class DataManager:

    def __init__(self, model):
        self._file = 'storage/data/%s.csv' % model.plural()
        self.open()

    def open(self):
        try:
            self._fp = open(self._file)
        except IOError:
            self._fp = open(self._file, 'w+')

    def __enter__(self):
        self.open()

    def read(self):
        return pd.read_csv(self._fp, sep=',', lineterminator='\n', header=None, error_bad_lines=False)

    def close(self):
        self._fp.close()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


