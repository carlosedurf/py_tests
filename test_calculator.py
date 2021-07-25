import unittest
from calculator import sum


class TestCalculator(unittest.TestCase):
    def test_sum_5_and_5_must_return_10(self):
        self.assertEqual(sum(5, 5), 10)

    def test_sum_5_negative_and_5_must_return_0(self):
        self.assertEqual(sum(-5, 5), 0)

    def test_sum_various_enters(self):
        x_y_outputs = (
            (10, 10, 20),
            (5, 5, 10),
            (1.5, 1.5, 3.0),
            (-5, 5, 0),
            (100, 100, 200),
        )

        for x_y_output in x_y_outputs:
            with self.subTest(x_y_output=x_y_output):
                x, y, output = x_y_output
                self.assertEqual(sum(x, y), output)

    def test_sum_param_x_not_int_or_float_must_return_assertionerror(self):
        with self.assertRaises(AssertionError):
            sum('11', 0)

    def test_sum_param_y_not_int_or_float_must_return_assertionerror(self):
        with self.assertRaises(AssertionError):
            sum(11, '0')


unittest.main(verbosity=2)
