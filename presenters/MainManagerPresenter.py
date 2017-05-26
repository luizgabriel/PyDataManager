from presenters.BasePresenter import BasePresenter

class MainManagerPresenter(BasePresenter):

    def onClickLoadModelBtn(self):
        self.view.openLoadModelDialog()

    def onClickOpenModelManager(self, modelKey):
        model = self.view.master.modelManager.get(modelKey)
        self.view.openModelManager(model)
