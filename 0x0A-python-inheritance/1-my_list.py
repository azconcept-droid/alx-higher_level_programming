#!/usr/bin/python3
"""Defines inherited list"""


class Mylist(list):
    """ Inherits from my list base class"""

    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)"""
        print(sorted(self))
