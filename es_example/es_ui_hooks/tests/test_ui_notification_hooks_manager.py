import unittest

from unittest import mock

from es_example.tests.utils import captured_output
from es_example.es_ui_hooks.es_ui_hooks_factory import (
    ESUIHooksFactory
)
from es_example.es_ui_hooks.es_ui_hooks_manager import (
    ESUIHooksManager
)


class TestESUIHooksManager(unittest.TestCase):
    def test_initialization(self):
        mock_factory = mock.Mock(spec=ESUIHooksFactory)
        manager = ESUIHooksManager(factory=mock_factory)
        self.assertEqual(manager.factory, mock_factory)

    def test_before_and_after_execution(self):
        mock_factory = mock.Mock(spec=ESUIHooksFactory)
        manager = ESUIHooksManager(factory=mock_factory)

        mock_task = mock.Mock()
        with captured_output() as (stdout, stderr):
            manager.before_execution(mock_task)
            manager.after_execution(mock_task)
            manager.before_save(mock_task)

        self.assertEqual(
            stdout.getvalue(),
            ("This is the ES UI hook. The execution is about to begin.\n"
             "This is the ES UI hook. The execution is done.\n"
             "This is the ES UI hook. The save is about to begin.\n"))
