import unittest

from unittest import mock

from es_example.es_notification_listener\
     .es_notification_listener_factory import (
            ESNotificationListenerFactory)

from es_example.es_notification_listener\
    .es_notification_listener_model import (
        ESNotificationListenerModel)


class TestESNotificationListenerModel(unittest.TestCase):
    def test_initialization(self):
        factory = mock.Mock(spec=ESNotificationListenerFactory)
        model = ESNotificationListenerModel(factory)
        self.assertEqual(model.factory, factory)
