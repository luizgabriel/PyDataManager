from unittest import *

from services.ModelManager import ModelManager


class ModelManagerTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.mock = ModelManager('mocks/models/')

    def testLoadsWallModels(self):
        self.assertEquals(self.mock.count(), 1)

    def testGetModel(self):
        self.assertIsNotNone(self.mock.get('TestModel'))

    def testGetModelData(self):
        model = self.mock.get('TestModel')
        self.assertEquals(model.title(), "Teste de Modelo")
        self.assertEquals(model.singular(), "Teste")
        self.assertEquals(model.plural(), "Testes")
        self.assertEquals(model.attributes_count(), 2)

    def testGetModelAttributes(self):
        model = self.mock.get('TestModel')
        param1, param2 = model.attributes()
        self.assertEquals(param1.name(), "param1")
        self.assertEquals(param1.type(), "text")
        self.assertTrue(param1.required())
        self.assertIsNone(param1.default())

        self.assertEquals(param2.name(), "param2")
        self.assertEquals(param2.type(), "number")
        self.assertFalse(param2.required())
        self.assertEquals(param2.default(), 5)

        self.assertEquals(model.attribute(0), model.attribute(name="param1"))



