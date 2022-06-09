#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    j = 0
    for i in my_list:
        if i == search:
            new_list.append(replace)
        else:
            new_list.append(my_list[j])
        j += 1
    return new_list
