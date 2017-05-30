import tkinter as tk
from tkinter import ttk

from presenters.ModelManagerPresenter import ModelManagerPresenter
from windows.ModelFrame import ModelFrame


class ModelManagerFrame(tk.Frame):

    def __init__(self, master, model_key):
        super().__init__(master)
        self.model_key = model_key
        self.presenter = ModelManagerPresenter(self, self.model_key)
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

    def open_model_window(self, idx = None):
        new_window = tk.Toplevel(width=200, height=400)
        ModelFrame(new_window, self.presenter, idx).pack()
        new_window.mainloop()

    def init_header(self, fields):
        cols = [f.name() for f in fields]
        self.table_general = ttk.Treeview(self, columns=cols)

        self.table_general.heading('#0', text="#ID")
        self.table_general.column('#0', width=10)
        i = 1
        for field in fields:
            self.table_general.heading('#%d' % i, text="%s" % field.name())
            self.table_general.column('#%d' % i, stretch=tk.YES)
            i += 1

        self.table_general.bind("<Double-1>", self.on_double_click_item)
        self.table_general.pack(side="bottom", fill="both")

    def on_double_click_item(self, event):
        item = self.table_general.selection()[0]
        idx = self.table_general.item(item, "text")
        self.presenter.on_click_edit_item(int(idx))


    def add_data_row(self, idx, values):
        self.table_general.insert('', 'end', text=idx, values=tuple(values))



