import Application as app
from presenters.BasePresenter import BasePresenter

class MainPresenter(BasePresenter):

    def __init__(self, view):
        super().__init__(view)
        self.manager = app.Application.instance().model_manager()

    def on_create(self):
        for name, model in self.manager.models():
            self.view.add_model_to_list(model, name, 0)

    def on_click_load_model_btn(self):
        self.view.open_load_model_dialog()

    def on_click_open_model(self, model_key):
        model = self.manager.get(model_key)
        self.view.open_model_manager_screen(model)

    def on_load_model(self, name, model):
        self.manager.save(name, model)