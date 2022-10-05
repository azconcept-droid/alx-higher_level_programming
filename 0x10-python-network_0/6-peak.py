#!/usr/bin/python3
"""
This module defines a function find_peak
"""


def find_peak_index(list_of_integers, Left=None, Right=None):
    """Finds the peak element index of a list
       list_of_integers (list) : list of integers
    """

    if Left is None and Right is None:
        Left = 0  # Left index boundary
        Right = len(list_of_integers) - 1  # Right index boundary

    mid = (Left + Right) // 2  # middle index

    if ((mid == 0 or list_of_integers[mid - 1] <= list_of_integers[mid])
       and (mid == len(list_of_integers) - 1
       or list_of_integers[mid + 1] <= list_of_integers[mid])):
        return (mid)

    if mid - 1 >= 0 and list_of_integers[mid - 1] > list_of_integers[mid]:
        return find_peak_index(list_of_integers, Left, mid - 1)

    return find_peak_index(list_of_integers, mid + 1, Right)


def find_peak(list_of_integers):
    """Return peak element"""

    if list_of_integers == []:
        return None

    index = find_peak_index(list_of_integers)

    return list_of_integers[index]
