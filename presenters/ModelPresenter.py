from presenters.BasePresenter import BasePresenter


class ModelPresenter(BasePresenter):

    def __init__(self, view, model, data):
        super().__init__(view)
        self.model = model
        self.data = data

    def on_create(self):
        if self.data.id() is not None:
            self.view.set_title("%s [ID %d]" % (self.model.singular(), self.data.id()))
        else:
            self.view.set_title(self.model.singular())

        for field in self.model.fields():
            value = self.data.value(field)
            self.view.add_text_input(field, value)

        if self.data.id() is not None:
            self.view.add_save_button("Salvar")
        else:
            self.view.add_save_button("Adicionar")


    def on_click_save(self):
        self.data.set(self.view.get_input_data())
        self.data.save()
        self.view.close()