import tkinter as tk
from tkinter import ttk

from presenters.ModelManagerPresenter import ModelManagerPresenter


class ModelManagerFrame(tk.Frame):

    def __init__(self, master, model_key):
        super().__init__(master)
        self.presenter = ModelManagerPresenter(self, model_key)
        self.initializeComponents()

    def initializeComponents(self):
        self.title_label = tk.StringVar()
        self.label1 = tk.Label(self, textvariable=self.title_label)
        self.label1.pack(side="top")

        self.button1 = tk.Button(self, text="Voltar para a tela principal")
        self.button1.pack(side="top")
        self.button1.bind("<Button-1>", lambda e: self.presenter.on_click_back_btn())

        self.add_button = tk.StringVar()
        self.button2 = tk.Button(self, textvariable=self.add_button)
        self.button2.pack(side="top")
        self.button2.bind("<Button-1>", lambda e: self.presenter.on_click_add_btn())

        self.presenter.on_create()

    def set_model_config(self, model):
        self.title_label.set(model.title())
        self.add_button.set("Adicionar %s" % model.singular())

    def open_add_window(self):
        pass

    def init_header(self, fields):
        cols = [f.name() for f in fields]
        self.tableGeneral = ttk.Treeview(self, columns=cols)

        self.tableGeneral.heading('#0', text="#ID")
        self.tableGeneral.column('#0', width=10)
        i = 1
        for field in fields:
            self.tableGeneral.heading('#%d' % i, text="%s" % field.name())
            self.tableGeneral.column('#%d' % i, stretch=tk.YES)
            i += 1

        self.tableGeneral.pack(side="bottom", fill="both")

    def add_data_row(self, idx, row):
        self.tableGeneral.insert('', 'end', text=idx, values=tuple(row))



