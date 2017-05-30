import tkinter as tk

from presenters.ModelPresenter import ModelPresenter


class ModelFrame(tk.Frame):

    def __init__(self, master, manager_presenter, idx = None):
        super().__init__(master)
        print(idx)
        self.presenter = ModelPresenter(self, manager_presenter.model, manager_presenter.data.get(idx))
        self.inputs_values = {}
        self.initialize_components()

    def initialize_components(self):
        self.title = tk.StringVar()

        self.label1 = tk.Label(self, textvariable=self.title)
        self.label1.grid(row=0, column=0)

        self.presenter.on_create()

    def set_title(self, title):
        self.title.set(title)
        self.master.title(title)

    def add_text_input(self, field, value):
        row = len(self.inputs_values) + 1
        label = tk.Label(self, text="%s:" % field.name())
        label.grid(row=row, column=0)

        entry_value = tk.StringVar()
        entry_value.set(str(value))
        tk.Entry(self, textvariable=entry_value).grid(row=row, column=1)

        self.inputs_values[field.name()] = entry_value

    def add_save_button(self, text):
        row = len(self.inputs_values) + 1
        btn = tk.Button(self, text=text)
        btn.grid(row=row, column=1)
        btn.bind("<Button-1>", self.on_click_save)

    def on_click_save(self, e):
        self.presenter.on_click_save()

    def get_input_data(self):
        data = {}
        for field, s in self.inputs_values.items():
            data[field] = s.get()

        return data

    def close(self):
        self.master.destroy()

    def add_delete_button(self):
        row = len(self.inputs_values) + 1
        tk.Button(self, "Deletar").grid(row=row, column=0)

