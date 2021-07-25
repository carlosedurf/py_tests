"""
TDD - Test Driven Development (Desenvolvimento dirigido a testes)

Red
Part 1 -> Create the see test fail

Green
Part 2 -> Create the see test sucess

Refactor
Part 3 -> Improve the code
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
from baconwithegges import bacon_with_egges


class TestBaconWithEgges(unittest.TestCase):
    def test_bacon_with_egges_must_return_assertion_erro_if_not_receive_int(self):
        with self.assertRaises(AssertionError):
            bacon_with_egges('')

    def test_bacon_with_egges_must_return_bacon_with_egges_if_enter_is_multiple_3_and_5(self):
        enters = (15, 30, 45, 60)
        output = 'bacon with egges'

        for enter in enters:
            with self.subTest(enter=enter, output=output):
                self.assertEqual(
                    bacon_with_egges(enter),
                    output,
                    msg=f'"{enter}" not returns "{output}"'
                )

    def test_bacon_with_egges_must_return_starves_if_enter_not_is_multiple_3_and_5(self):
        enters = (1, 2, 4, 7)
        output = 'starves'

        for enter in enters:
            with self.subTest(enter=enter, output=output):
                self.assertEqual(
                    bacon_with_egges(enter),
                    output,
                    msg=f'"{enter}" not returns "{output}"'
                )

    def test_bacon_with_egges_must_return_bacon_if_enter_is_multiple_3(self):
        enters = (3, 6, 9, 12, 18, 21)
        output = 'bacon'

        for enter in enters:
            with self.subTest(enter=enter, output=output):
                self.assertEqual(
                    bacon_with_egges(enter),
                    output,
                    msg=f'"{enter}" not returns "{output}"'
                )

    def test_bacon_with_egges_must_return_egges_if_enter_is_multiple_5(self):
        enters = (5, 10, 20, 25, 35)
        output = 'egges'

        for enter in enters:
            with self.subTest(enter=enter, output=output):
                self.assertEqual(
                    bacon_with_egges(enter),
                    output,
                    msg=f'"{enter}" not returns "{output}"'
                )


if __name__ == '__main__':
    unittest.main(verbosity=2)
