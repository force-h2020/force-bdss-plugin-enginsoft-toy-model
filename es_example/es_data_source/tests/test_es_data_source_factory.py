import unittest

from es_example.es_data_source.es_data_source import \
    ESDataSource
from es_example.es_data_source.es_data_source_model import \
    ESDataSourceModel
from es_example.es_plugin import ESPlugin


class DataSourceFactoryTestMixin(unittest.TestCase):
    def setUp(self):
        self.plugin = ESPlugin()
        self.factory = self.plugin.data_source_factories[0]

    def test_initialization(self):
        print("DataSourceFactoryTestMixin - test_initialization")
        self.assertNotEqual(self.factory.id, "")
        self.assertEqual(self.factory.plugin, self.plugin)

    def test_create_model(self):
        model = self.factory.create_model({})
        self.assertIsInstance(model, ESDataSourceModel)

        model = self.factory.create_model()
        self.assertIsInstance(model, ESDataSourceModel)

    def test_create_data_source(self):
        ds = self.factory.create_data_source()
        self.assertIsInstance(ds, ESDataSource)
