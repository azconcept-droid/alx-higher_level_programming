#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test max integer"""

    def test_interger_arg(self):
        with self.assertRaises((TypeError)):
            max_integer(10)
            max_integer(-1)
        
    def test_correct_return(self):
        self.assertEqual(max_integer([1, 4, 7, 8]), 8)
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)

    def test_one_list_arg(self):
        self.assertEqual(max_integer([10]), 10)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)
        self.assertNotEqual(max_integer([]), 0)

    def test_negative_list(self):
        self.assertEqual(max_integer([-10, -2, -1, -3]), -1)

    def test_tuple_arg(self):
        self.assertEqual(max_integer((3, 9, 7, 89)), 89)

    def test_tuple_in_list(self):
        with self.assertRaises(TypeError):
            max_integer([0, (0, )])

    def test_list_of_string(self):
        self.assertEqual(max_integer(['Python', 'is', 'fun']), 'is')

    def test_string_arg(self):
        self.assertEqual(max_integer('Cisfun'), 'u')

    def test_empty_string_arg(self):
        self.assertEqual(max_integer(''), None)

    def test_list_mixed(self):
        with self.assertRaises(TypeError):
            max_integer([-10, 'c', 90, 'python'])

    def test_large_list(self):
        self.assertEqual(max_integer([
            3245, 323232, 2132323, 3233, 221,
            21323, 32323, 3323, 54545, 323, 23,
            3233, 7566, 43434, 42434, 45, 324, 3]), 2132323)

    def test_very_large_values(self):
        self.assertEqual(max_integer([
            float("inf"), 8903283926, 89892382683283
            ]), float("inf"))

    def test_very_small_values(self):
        self.assertEqual(max_integer([
            float("-inf"), 0, -1
            ]), 0)