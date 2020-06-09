#!python3

"""Mynathon tests."""

from mynathon import MynathonParser
import unittest


class TestMynathonParser(unittest.TestCase):
    """Class defining test cases for the mynathon parser."""

    def _test_script_from_file(self, testcase, expected_output):
        filepath = "testscripts/{0}.my".format(testcase)
        output = MynathonParser.execute_script_from_file(filepath, True)
        self.assertEqual(expected_output, output)

    def test_factorial(self):
        """Run the factorial.my test case."""
        expected_output = "Факториелът на 3 е 6, а на нула е 1\n"\
                          "Е не може с отрицателно число\n"\
                          "Готов си\n"

        self._test_script_from_file("factorial", expected_output)

    def test_keywords_are_valid(self):
        """Test that the mynathon keywords are not ambiguous."""
        keywords = MynathonParser.KEYWORDS.keys()

        for keyword in keywords:
            for keyword2 in filter(lambda k: k != keyword, keywords):
                if keyword in keyword2.split():
                    self.fail("Keyword '{0}' is contained in '{1}'; "
                              "this may cause unpredictable behaviour."
                              .format(keyword, keyword2))

        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
