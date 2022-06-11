#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = list(a_dictionary)
    sort_keys = sorted(keys)
    for key in sort_keys:
        value = a_dictionary.get(key)
        print("{}: {}".format(key, value))
