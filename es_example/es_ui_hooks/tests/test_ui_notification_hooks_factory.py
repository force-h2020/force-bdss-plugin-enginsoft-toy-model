import unittest

from es_example.es_plugin import ESPlugin
from es_example.es_ui_hooks.es_ui_hooks_manager import (
    ESUIHooksManager
)


class TestESUIHooksFactory(unittest.TestCase):
    def setUp(self):
        self.plugin = ESPlugin()
        self.ui_hooks_factory = self.plugin.ui_hooks_factories[0]

    def test_initialization(self):
        self.assertEqual(self.ui_hooks_factory.plugin, self.plugin)

    def test_create_ui_hooks_manager(self):
        self.assertIsInstance(
            self.ui_hooks_factory.create_ui_hooks_manager(),
            ESUIHooksManager)
