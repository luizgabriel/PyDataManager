from tkinter import Tk

from singleton.singleton import Singleton
from services.ModelManager import ModelManager
from windows.MainFrame import MainFrame

@Singleton
class Application():

    def __init__(self):
        super().__init__()
        self._root = Tk()
        self._root.title("Gerenciador de Dados")
        self._model_manager = ModelManager('storage/models/')

    def model_manager(self):
        return self._model_manager

    def open_main(self):
        self._main_window.tkraise()

    def run(self):
        self._main_window = MainFrame(self._root)
        self._main_window.grid(row=0, column=0, sticky="nsew")
        self._root.mainloop()