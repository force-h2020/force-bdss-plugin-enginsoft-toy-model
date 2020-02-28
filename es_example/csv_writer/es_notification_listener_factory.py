from force_bdss.api import BaseNotificationListenerFactory

from .es_notification_listener import ESNotificationListener
from .es_notification_listener_model import ESNotificationListenerModel


class ESNotificationListenerFactory(BaseNotificationListenerFactory):
    """This is the factory of the notification listener.
    A notification listener listens to events provided by the MCO,
    and performs operations accordingly.
    """

    #: Return a unique string identifier within the scope of your plugin for
    #: this factory
    def get_identifier(self):
        return "es_notification_listener"

    #: Return a user-visible name for the factory
    def get_name(self):
        return "ES Notification Listener (stdout print)"

    #: Return the model class associated to this factory.
    def get_model_class(self):
        return ESNotificationListenerModel

    #: Return the class of the notification listener.
    def get_listener_class(self):
        return ESNotificationListener
