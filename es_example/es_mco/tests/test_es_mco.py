import unittest

from unittest import mock
from traits.api import TraitError

from force_bdss.api import BaseMCOFactory

from es_example.es_mco.parameters import (
    RangedMCOParameter,
    RangedMCOParameterFactory
)

from es_example.es_mco.es_mco_model import ESMCOModel
from es_example.es_mco.es_mco import ESMCO


class TestESMCO(unittest.TestCase):
    def setUp(self):
        self.factory = mock.Mock(spec=BaseMCOFactory)
        self.factory.plugin = mock.Mock()
        self.factory.plugin.application = mock.Mock()
        self.factory.plugin.application.workflow_filepath = "whatever"

    def test_initialization(self):
        opt = ESMCO(self.factory)
        self.assertEqual(opt.factory, self.factory)

    def test_run(self):
        opt = ESMCO(self.factory)
        model = ESMCOModel(self.factory)
        model.parameters = [
            RangedMCOParameter(
                mock.Mock(spec=RangedMCOParameterFactory),
                lower_bound=1,
                upper_bound=3,
                initial_value=2)
        ]

        mock_process = mock.Mock()
        mock_process.communicate = mock.Mock(return_value=(b"1 2 3", b""))

        with mock.patch("subprocess.Popen") as mock_popen:
            mock_popen.return_value = mock_process
            opt.run(model)

        self.assertEqual(mock_popen.call_count, 2)

        # test whether arugment order matters on object creation
        model.parameters = [
            RangedMCOParameter(
                mock.Mock(spec=RangedMCOParameterFactory),
                initial_value=2,
                upper_bound=3,
                lower_bound=1,
            )
        ]

        mock_process = mock.Mock()
        mock_process.communicate = mock.Mock(return_value=(b"1 2 3", b""))

        with mock.patch("subprocess.Popen") as mock_popen:
            mock_popen.return_value = mock_process
            opt.run(model)

        self.assertEqual(mock_popen.call_count, 2)

        # test whether arugment order matters on object creation
        model_data = {"initial_value": 2, "upper_bound": 3, "lower_bound": 1}
        model.parameters = [
            RangedMCOParameter(mock.Mock(spec=RangedMCOParameterFactory),
                               **model_data)
        ]

        mock_process = mock.Mock()
        mock_process.communicate = mock.Mock(return_value=(b"1 2 3", b""))

        with mock.patch("subprocess.Popen") as mock_popen:
            mock_popen.return_value = mock_process
            opt.run(model)

        self.assertEqual(mock_popen.call_count, 2)

    def test_failure(self):
        model = ESMCOModel(self.factory)
        with self.assertRaises(TraitError):
            model.parameters = [
                RangedMCOParameter(
                    mock.Mock(spec=RangedMCOParameterFactory),
                    lower_bound=1,
                    upper_bound=3,
                    initial_value=5,
                )
            ]
