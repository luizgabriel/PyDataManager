import json, os

def get(data, key, default):
    try:
        return data[key]
    except KeyError:
        return default

class Attribute:

    def __init__(self, data):
        self._name = get(data, 'name', None)
        self._type = get(data, 'type', None)
        self._required = get(data, 'required', True)
        self._default = get(data, 'default', None)

    def name(self):
        return self._name

    def type(self):
        return self._type

    def required(self):
        return self._required

    def default(self):
        return self._default

    def has_default(self):
        return self.default() != None

    def data(self):
        return {
            'name': self.name(),
            'type': self.type(),
            'required': self.required(),
            'default': self.default()
        }

class Model:

    def __init__(self, data):
        self._title = get(data, 'title', None)
        self._singular = get(data, 'singular', None)
        self._plural = get(data, 'plural', None)
        self._fields = []

        for attr in data['fields']:
            self.add_attribute(attr)

    def title(self):
        return self._title

    def singular(self):
        return self._singular

    def plural(self):
        return self._plural

    def add_attribute(self, data):
        self._fields.append(Attribute(data))

    def fields(self):
        return self._fields

    def field(self, i=0, name=None):
        if name is not None:
            for attr in self.fields():
                if attr.name() == name:
                    return attr

            return None
        else:
            return self._fields[i]

    def data(self):
        return {
            'title': self.title(),
            'singular': self.singular(),
            'plural': self.plural(),
            'fields': [t.data() for t in self.fields()]
        }

class ModelManager:

    def __init__(self, folder):
        self._folder = folder
        self._models = {}
        self.load()

    def load(self):
        for (dirpath, dirnames, filenames) in os.walk(self._folder):
            for file in filenames:
                self.add_model_file(file)

    def save(self, name, model):
        with open(self._folder + name, 'w+') as f:
            f.write(json.dumps(model.data()))
        self.load()

    def add_model_file(self, file):
        with open(self._folder + file) as f:
            self._models[file] = Model(json.load(f))

    def count(self):
        return len(self._models)

    def get(self, model_key):
        if '.json' in model_key:
            key = model_key
        else:
            key = model_key
        return self._models[key]

    def models(self):
        return self._models.items()