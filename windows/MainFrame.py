import tkinter as tk
from tkinter import ttk
from presenters.MainPresenter import MainPresenter
from windows.LoadModelDialog import LoadModelDialog
from windows.ModelManagerFrame import ModelManagerFrame


class MainFrame(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.presenter = MainPresenter(self)
        self.initialize_components()

    def on_double_click_item(self, event):
        item = self.table_model.selection()[0]
        key = self.table_model.item(item, "text")
        self.presenter.on_click_open_model(key)

    def initialize_components(self):
        self.master.title("Gerenciador de Dados")

        '''
            Inicializando labels e botões
        '''
        self.load_button = tk.Button(self, text="Carregar Modelo")
        self.load_button.grid(row=0, column=0, sticky=tk.W)
        self.load_button.bind("<Button-1>", lambda e: self.presenter.on_click_load_model_btn())

        '''
            Inicializando a tabela e nomeando suas colunas
        '''
        self.table_model = ttk.Treeview(self, columns=('Modelo', 'Campos', 'Qtd.'))
        self.table_model.heading('#0', text='Modelo')
        self.table_model.heading('#1', text='Campos')
        self.table_model.heading('#2', text='Qtd.')
        self.table_model.column('#0', stretch=tk.YES)
        self.table_model.column('#1', stretch=tk.YES)
        self.table_model.column('#2', stretch=tk.YES)
        self.table_model.bind("<Double-1>", self.on_double_click_item)
        self.table_model.grid(row=1, columnspan=1)

        self.presenter.on_create()

    def add_model_to_list(self, model, name, count):
        attributes = "|".join([a.name() for a in model.fields()])
        self.table_model.insert('', 'end', text=name, values=(attributes, count))

    def open_load_model_dialog(self):
        dialog = LoadModelDialog()
        try:
            file, model = dialog.open()
            self.presenter.on_load_model(file, model)
        except:
            pass

    def show(self):
        self.tkraise()
        self.presenter.on_show()

    def clear_list(self):
        self.table_model.delete(*self.table_model.get_children())

    def open_model_manager_screen(self, model_key):
        frame = ModelManagerFrame(self.master, model_key)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()