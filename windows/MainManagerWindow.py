import tkinter as tk

from presenters.MainManagerPresenter import MainManagerPresenter

class MainManagerWindow(tk.Frame):

    def __init__(self, root):
        super().__init__(root)
        self.presenter = MainManagerPresenter(self)
        self.initializeComponents()


    def initializeComponents(self):
        self.createModelBtn = tk.Button(self.master, text="Criar Modelo").grid(row=0, column=0)
        #TODO: Create view elements here