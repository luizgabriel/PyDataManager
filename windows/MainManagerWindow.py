import tkinter as tk

from presenters.MainManagerPresenter import MainManagerPresenter


class MainManagerWindow(tk.Frame):
    def __init__(self, app):
        super().__init__(app)
        self.presenter = MainManagerPresenter(self)
        self.initializeComponents()

    def initializeComponents(self):
        self.loadModelBtn = tk.Button(self.master, text="Carregar Modelo").grid(row=0, column=0)
