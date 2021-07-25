"""
class Peaple:
    __init__
        name str
        last_name str
        data_obtained bool
    
    API:
        get_all_data -> method
            OK
            404

            (data_obtained is True if data obtained with success)
"""
try:
    import sys
    import os

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../src'
            )
        )
    )
except:
    raise

import unittest
from unittest.mock import patch
from Peaple import Peaple


class TestPeaple(unittest.TestCase):
    def setUp(self):
        self.p1 = Peaple('Carlos', 'Eduardo')
        self.p2 = Peaple('Fulano', 'Tal')

    def test_peaple_attr_name_has_correct_value(self):
        self.assertEqual(self.p1.name, 'Carlos')
        self.assertEqual(self.p2.name, 'Fulano')

    def test_peaple_attr_name_is_str(self):
        self.assertIsInstance(self.p1.name, str)
        self.assertIsInstance(self.p2.name, str)

    def test_peaple_attr_last_name_has_correct_value(self):
        self.assertEqual(self.p1.last_name, 'Eduardo')
        self.assertEqual(self.p2.last_name, 'Tal')

    def test_peaple_attr_last_name_is_str(self):
        self.assertIsInstance(self.p1.last_name, str)
        self.assertIsInstance(self.p2.last_name, str)

    def test_peaple_attr_data_obtained_start_false(self):
        self.assertFalse(self.p1.data_obtained)
        self.assertFalse(self.p2.data_obtained)

    def test_get_all_data_success_OK(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True

            self.assertEqual(self.p1.get_all_data(), 'CONECTADO')
            self.assertTrue(self.p1.data_obtained)

            self.assertEqual(self.p2.get_all_data(), 'CONECTADO')
            self.assertTrue(self.p2.data_obtained)

    def test_get_all_data_failed_404(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = False

            self.assertEqual(self.p1.get_all_data(), 'ERROR 404')
            self.assertFalse(self.p1.data_obtained)

            self.assertEqual(self.p2.get_all_data(), 'ERROR 404')
            self.assertFalse(self.p2.data_obtained)

    def test_get_all_data_success_and_failed_sequence(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True

            self.assertEqual(self.p1.get_all_data(), 'CONECTADO')
            self.assertTrue(self.p1.data_obtained)

            self.assertEqual(self.p2.get_all_data(), 'CONECTADO')
            self.assertTrue(self.p2.data_obtained)

            fake_request.return_value.ok = False

            self.assertEqual(self.p1.get_all_data(), 'ERROR 404')
            self.assertFalse(self.p1.data_obtained)

            self.assertEqual(self.p2.get_all_data(), 'ERROR 404')
            self.assertFalse(self.p2.data_obtained)


if __name__ == '__main__':
    unittest.main(verbosity=2)
