import unittest

from unittest import mock

from force_bdss.api import BaseMCOFactory

from es_example.es_mco.es_mco_model import ESMCOModel
from es_example.es_mco.es_mco import (
    SubprocessWorkflow
)


class TestSubprocessWorkflow(unittest.TestCase):

    def setUp(self):
        self.evaluator = SubprocessWorkflow(
            workflow_filepath="test_probe.json")
        self.mock_process = mock.Mock()
        self.mock_process.communicate = mock.Mock(return_value=(b"2", b"1 0"))

    def test___call_subprocess(self):

        # Test simple bash command
        stdout = self.evaluator._call_subprocess(["uniq"], ["Hello", "World"])
        self.assertEqual("Hello World", stdout.decode("utf-8").strip())

    def test__subprocess_solve(self):
        factory = mock.Mock(spec=BaseMCOFactory)
        self.evaluator.mco_model = ESMCOModel(factory)

        with mock.patch("subprocess.Popen") as mock_popen:
            mock_popen.return_value = self.mock_process
            kpi_results = self.evaluator._subprocess_evaluate([
                1.0], 'dummy_filename')

        self.assertEqual(1, len(kpi_results))

    def test_solve_error_mco_communicator(self):
        def mock_subprocess_evaluate(self, *args):
            raise Exception

        factory = mock.Mock(spec=BaseMCOFactory)
        self.evaluator.mco_model = ESMCOModel(factory)

        with mock.patch('es_example.es_mco.es_mco'
                        '.SubprocessWorkflow._subprocess_evaluate',
                        side_effect=mock_subprocess_evaluate):
            with self.assertRaisesRegex(
                    RuntimeError,
                    'SubprocessWorkflow failed '
                    'to run. This is likely due to an error in the '
                    'BaseMCOCommunicator assigned to '
                    "<class 'force_bdss.mco.base_mco_factory."
                    "BaseMCOFactory'>."):
                self.evaluator.evaluate([1.0])
