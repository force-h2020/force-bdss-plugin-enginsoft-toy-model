import unittest

from es_example.es_plugin import ESPlugin


class TestESNotificationListenerFactory(unittest.TestCase):
    def setUp(self):
        self.plugin = ESPlugin()
        self.factory = self.plugin.notification_listener_factories[0]

    def test_create_methods(self):
        model = self.factory.create_model()
        self.assertEqual(model.factory, self.factory)

        model = self.factory.create_model({})
        self.assertEqual(model.factory, self.factory)

        listener = self.factory.create_listener()
        self.assertEqual(listener.factory, self.factory)
