import json

class PreferencesService():

    def __init__(self):
        self._file = "storage/preferences.json"
        self._data = {}
        self.load()

    def load(self):
        with open(self._file) as f:
            self._data = json.load(f)

    def get(self, key):
        return self._data[key]