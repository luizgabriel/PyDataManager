from tkinter import filedialog
import json
from services.ModelManager import Model

class LoadModelDialog():

    def __init__(self):
        self.options = {
            'defaultextension': '.json',
            'filetypes': [('all files', '.*'), ('json files', '.json')],
            'title': 'Selecione o arquivo do modelo'
        }

    def open(self):
        with filedialog.askopenfile('r', **self.options) as file:
            name = file.name.split('/')[-1]
            return name, Model(json.load(file))
