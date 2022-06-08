#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None

    if len(my_list) == 1:
        return my_list[0]

    if len(my_list) == 2:
        if my_list[0] > my_list[1]:
            return my_list[0]
        else:
            return my_list[1]

    i = len(my_list) - 1
    while i > 0:
        j = 0
        while j < i:
            if my_list[j] > my_list[j + 1]:
                temp = my_list[j]
                my_list[j + 1] = temp
            j += 1
        i -= 1
    return my_list[len(my_list) - 1]
