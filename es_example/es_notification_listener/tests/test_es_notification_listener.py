import unittest
from es_example.tests.utils import captured_output

from unittest import mock

from force_bdss.api import (
    MCOStartEvent, MCOProgressEvent, MCOFinishEvent, DataValue)


from es_example.es_notification_listener\
    .es_notification_listener_model import (
        ESNotificationListenerModel)
from es_example.es_notification_listener\
    .es_notification_listener_factory import (
        ESNotificationListenerFactory)
from es_example.es_notification_listener\
    .es_notification_listener import (
        ESNotificationListener)


class TestESNotificationListener(unittest.TestCase):
    def test_initialization(self):
        print("PippoTESTES")
        listener = ESNotificationListener(
            mock.Mock(spec=ESNotificationListenerFactory))
        model = mock.Mock(spec=ESNotificationListenerModel)
        with captured_output() as (out, err):
            listener.initialize(model)
            listener.deliver(MCOStartEvent(
                parameter_names=["foo", "bar"],
                kpi_names=["baz", "quux"]))
            listener.deliver(MCOProgressEvent(
                optimal_point=[DataValue(value=1.0), DataValue(value=2.0)],
                optimal_kpis=[DataValue(value=3.0), DataValue(value=4.0)],
                weights=[0.5, 0.5]
            ))
            listener.deliver(MCOFinishEvent())
            listener.finalize()

        self.assertEqual(
            out.getvalue(),
            "Initializing\n"
            "MCOStartEvent ['foo', 'bar'] ['baz', 'quux']\n"
            "MCOProgressEvent [1.0, 2.0] [3.0, 4.0] [0.5, 0.5]\n"
            "MCOFinishEvent\n"
            "Finalizing\n"
        )
