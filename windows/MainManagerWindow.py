import tkinter as tk


class MainManagerWindow(tk.Frame):
    def __init__(self, app):
        super().__init__(app)

    def initializeComponents(self):
        self.loadModelBtn = tk.Button(self.master, text="Carregar Modelo")

