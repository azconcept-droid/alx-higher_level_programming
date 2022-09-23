#!/usr/bin/python3
"""
This module defines a function find_peak
"""

def find_peak(list_of_integers):
    """Finds the the peak"""
    list_of_integers.reverse()
    return list_of_integers[0]
