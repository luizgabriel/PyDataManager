from pandas.io.common import EmptyDataError

from presenters.BasePresenter import BasePresenter
import Application as app
from services.DataManager import DataManager


class ModelManagerPresenter(BasePresenter):

    def __init__(self, view, model_key):
        super().__init__(view)
        self.manager = app.Application.instance().model_manager()
        self.model = self.manager.get(model_key)
        self.data = DataManager(self.model)

    def on_create(self):
        self.view.set_model_config(self.model)
        self.view.init_header(self.model.fields())

        try:
            for idx, data in self.data.all():
                values = [data.value(f) for f in self.model.fields()]
                self.view.add_data_row(idx, values)
        except EmptyDataError:
            pass

    def on_click_back_btn(self):
        app.Application.instance().open_main()

    def on_click_add_btn(self):
        self.view.open_model_window()

    def on_click_edit_item(self, idx):
        self.view.open_model_window(idx)