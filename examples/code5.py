# UnitTesting

import unittest
from utils import multiply


# Example 1
# A simple test case in python unittest module
class SimpleTestCase(unittest.TestCase):

    def test_negative_numbers(self):
        expected = 3
        actual = multiply(-1, -3)

        self.assertEqual(expected, actual, msg='Result of multiplicity')


if __name__ == '__main__':
    unittest.main()
