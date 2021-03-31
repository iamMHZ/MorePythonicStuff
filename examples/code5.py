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


# Example 3
# How to skip a test?
# You can use the same decorator to skip a class too
# There are other decorators too like unittest.skipIf
class SkipTestCase(unittest.TestCase):

    @unittest.skip('We are just skipping')
    def test_skip_me(self):
        print('lazy we are and we are skipping')

    def test_not_to_skip(self):
        print('We skipped the previous test hahaha')


if __name__ == '__main__':
    unittest.main()
