import tkinter as tk

from presenters.ModelManagerPresenter import ModelManagerPresenter

class ModelManagerWindow(tk.Frame):

    def __init__(self, root):
        super().__init__(root)
        self.presenter = ModelManagerPresenter(self)
        self.initializeComponents()

    def initializeComponents(self):
        self.loadModelBtn = tk.Button(self.master, text="Criar Modelo").grid(row=0, column=0)
        #TODO: Create view elements here