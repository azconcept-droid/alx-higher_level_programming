#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    list_len = len(my_list)
    new_list = my_list
    if idx < 0 and idx >= list_len:
        return my_list
    for i in range(list_len):
        if idx == i:
            new_list[i] = element
    return new_list
