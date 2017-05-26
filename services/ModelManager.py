import os

class ModelManager:

    def __init__(self):
        self._folder = 'storage/models/'
        self._models = {}
        self.load()

    def load(self):
        #TODO: load model files in _folder

    def get(self, model_key):
        return self._models[model_key]