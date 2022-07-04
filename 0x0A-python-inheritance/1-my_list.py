#!/usr/bin/python3
"""Defines Mylist Module inheritance"""


class Mylist(list):
    """ Inherits from list

    Args:
        list (object): base class to inherit from
    """
    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)"""
        print(sorted(self))
