import unittest

from unittest import mock

from traits.testing.api import UnittestTools
from force_bdss.api import DataValue, Slot, BaseDataSourceFactory

from es_example.es_data_source.es_data_source import (
    ESDataSource
)
from es_example.es_data_source.es_data_source_model import (
    ESDataSourceModel
)


class TestPowerEvaluatorDataSource(unittest.TestCase, UnittestTools):
    def setUp(self):
        print("TestPowerEvaluatorDataSource - setUp")
        super(TestPowerEvaluatorDataSource, self).setUp()
        self.factory = mock.Mock(spec=BaseDataSourceFactory)

    def test_initialization(self):
        ds = ESDataSource(self.factory)
        self.assertEqual(ds.factory, self.factory)

    def test_run(self):
        ds = ESDataSource(self.factory)
        model = ESDataSourceModel(self.factory)
        model.volume = 2
        mock_params = [DataValue(value=5, type="METER")]
        result = ds.run(model, mock_params)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0], DataValue)
        self.assertEqual(result[0].value, 25)

    def test_run_with_exception(self):
        ds = ESDataSource(self.factory)
        model = ESDataSourceModel(self.factory)
        mock_params = []
        model.volume = 3
        with self.assertRaises(IndexError):
            ds.run(model, mock_params)

    def test_slots(self):
        ds = ESDataSource(self.factory)
        model = ESDataSourceModel(self.factory)
        slots = ds.slots(model)
        self.assertEqual(len(slots), 2)
        self.assertEqual(len(slots[0]), 1)
        self.assertEqual(len(slots[1]), 1)
        self.assertIsInstance(slots[0][0], Slot)
        self.assertIsInstance(slots[1][0], Slot)

        with self.assertTraitChanges(model, 'changes_slots'):
            model.cuba_type_in = 'METER'
            model.cuba_type_out = 'METER'
        slots = ds.slots(model)
        self.assertEqual(slots[0][0].type, 'METER')
        self.assertEqual(slots[1][0].type, 'METER')
