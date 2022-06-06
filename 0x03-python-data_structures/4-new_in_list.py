#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = []
    i = 0
    list_len = len(my_list)

    if idx < 0 or idx > list_len:
        return my_list

    while i < list_len:
        new_list.append(my_list[i])
        i += 1

    for j in range(list_len):
        if idx == j:
            new_list[j] = element
            return new_list
