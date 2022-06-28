#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test max integer"""

    def test_type(self):
        l =  ["a", 1, 5, "z", 29]
        self.assertRaises(TypeError, max_integer, (1, 4, 6, 8, 9))
        self.assertRaises(ValueError, max_integer, l)
        
    def test_list(self):
        self.assertEqual(max_integer([1, 4, 7, 8]), 8)
        
        
    # def test_value(self):
    #     self.assertRaises(ValueError, max_integer, ["a", 1, 5, "z", 29])