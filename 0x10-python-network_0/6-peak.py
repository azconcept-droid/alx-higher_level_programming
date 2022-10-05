#!/usr/bin/python3
"""
This module defines a function find_peak value of
an unsorted list of integers
"""


def find_peak_index(list_of_integers, Left=None, Right=None):
    """Finds the peak element index of a list using binary search algorithm
       list_of_integers (list) : list of integers
    """

    if Left is None and Right is None:
        Left = 0  # Left index boundary
        Right = len(list_of_integers) - 1  # Right index boundary

    mid = (Left + Right) // 2  # middle index

    # Check if the middle element is greater than its neighbors
    if ((mid == 0 or list_of_integers[mid - 1] <= list_of_integers[mid])
       and (mid == len(list_of_integers) - 1
       or list_of_integers[mid + 1] <= list_of_integers[mid])):
        return (mid)

    # If the left neighbor of `mid` is greater than the middle element,
    # find the peak recursively in the left sublist
    if mid - 1 >= 0 and list_of_integers[mid - 1] > list_of_integers[mid]:
        return find_peak_index(list_of_integers, Left, mid - 1)

    # If the right neighbor of `mid` is greater than the middle element,
    # find the peak recursively in the right sublist
    return find_peak_index(list_of_integers, mid + 1, Right)


def find_peak(list_of_integers):
    """Return peak element"""

    # If list is empty return none
    if list_of_integers == []:
        return None

    index = find_peak_index(list_of_integers)

    return list_of_integers[index]
