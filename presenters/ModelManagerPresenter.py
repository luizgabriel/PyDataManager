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
            for idx, row in self.data.read().iterrows():
                self.view.add_data_row(idx, row)
        except EmptyDataError:
            pass

    def on_click_back_btn(self):
        self.data.close()
        app.Application.instance().open_main()

    def on_click_add_btn(self):
        self.view.open_add_window()