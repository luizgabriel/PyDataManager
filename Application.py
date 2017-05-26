from tkinter import Tk

from services.PreferencesService import PreferencesService
from windows.MainManagerWindow import MainManagerWindow


class Application(Tk):
    def __init__(self):
        super().__init__()
        self.title("Gerenciador de Dados")
        self.preferences = PreferencesService()
        self.mainManagerWindow = MainManagerWindow(self)

    def run(self):
        self.mainloop()
