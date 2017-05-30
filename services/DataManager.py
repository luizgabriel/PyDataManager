import pandas as pd
import csv

class ModelData:

    defaults = {
        "number": 0,
        "text": ""
    }

    def __init__(self, manager, model, data = None, idx = None):
        self.manager = manager
        self.model = model
        self.idx = idx
        self._data = {}

        for f in self.model.fields():
            try:
                self._data[f.name()] = data[f.name()]
            except:
                self._data[f.name()] = self.default_type(f)

    def id(self):
        return self.idx

    def data(self):
        return self._data

    def set(self, data):
        self._data = data

    def value(self, field):
        if isinstance(field, (str, int)):
            return self.data()[field]
        else:
            return self.data()[field.name()]

    def default_type(self, field):
        if field.has_default():
            return field.default()
        else:
            if field.required():
                try:
                    return self.defaults[field.type()]
                except KeyError:
                    return None
            else:
                return None


    def save(self):
        self.manager.save(self)

class DataManager:

    def __init__(self, model):
        self.model = model
        self._file = 'storage/data/%s.csv' % self.model.plural()
        self._data = self.all()

    def all(self):
        cols = [f.name() for f in self.model.fields()]
        with open(self._file) as fp:
            pf = pd.read_csv(fp, sep=',', lineterminator='\n', names=cols, error_bad_lines=False)
            return [(idx, ModelData(self, self.model, d, idx)) for (idx, d) in pf.iterrows()]

    def data(self):
        return [(idx, d.data()) for (idx, d) in self._data]

    def save(self, data):
        if data.id() is None:
            self._data.append(data)

        with open(self._file, 'w+') as fp:
            writer = csv.writer(fp, delimiter=',', lineterminator='\n')
            for idx, d in self._data:
                writer.writerow(d.data().values())

    def get(self, idx):
        try:
            id, data = self._data[idx]
            return data
        except:
            return ModelData(self, self.model)





