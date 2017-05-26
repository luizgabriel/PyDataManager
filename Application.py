from tkinter import Tk
from singleton.singleton import Singleton
from services.ModelManager import ModelManager
from windows.MainManagerWindow import MainManagerWindow

@Singleton
class Application():

    def __init__(self):
        super().__init__()
        self.root = Tk()
        self.root.title("Gerenciador de Dados")
        self.modelManager = ModelManager('storage/models/')
        self.mainManagerWindow = MainManagerWindow(self.root)

    def run(self):
        self.root.mainloop()
