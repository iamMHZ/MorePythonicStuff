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


# Example 2
# setUp and tearDown methods
class SimpleTestCase2(unittest.TestCase):
    def setUp(self):
        """
        setUp method runs before each test method
        """
        print('Setting up a test')

    def setUpClass(cls):
        """
        Runs once before all the tests
        """
        pass

    def test_multiply_by_one(self):
        expected = 1
        actual = multiply(1, 1)

        self.assertEqual(expected, actual)

    def tearDown(self):
        """
        tearDown method runs after each test method
        """
        print('Tearing down')

    def tearDownClass(cls):
        """Runs once at the ends of the tests"""
        pass


if __name__ == '__main__':
    unittest.main()
