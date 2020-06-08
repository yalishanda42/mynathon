#!python3

"""Mython tests."""

from mython import MythonParser
import unittest


class TestMythonParser(unittest.TestCase):
    """Class defining test cases for the mython parser."""

    def _test_script_from_file(self, testcase, expected_output):
        filepath = f"testscripts/{testcase}.my"
        output = MythonParser.execute_script_from_file(filepath, True)
        self.assertEqual(expected_output, output)

    def test_factorial(self):
        """Run the factorial.my test case."""
        expected_output = "Факториелът на 3 е 6, а на нула е 1\n"\
                          "Е не може с отрицателно число\n"\
                          "Готов си\n"

        self._test_script_from_file("factorial", expected_output)


if __name__ == '__main__':
    unittest.main()
