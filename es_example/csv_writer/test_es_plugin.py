import unittest

from es_example.es_plugin import ESPlugin


class TestESPlugin(unittest.TestCase):
    def test_basic_functionality(self):
        plugin = ESPlugin()
        self.assertEqual(len(plugin.data_source_factories), 1)
        self.assertEqual(len(plugin.mco_factories), 1)
        self.assertEqual(len(plugin.notification_listener_factories), 1)
        self.assertEqual(len(plugin.ui_hooks_factories), 1)
