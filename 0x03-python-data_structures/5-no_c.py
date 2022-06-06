#!/usr/bin/python3
def no_c(my_string):
    for i in range(len(my_string)):
        if my_string[i] == "C":
            C_idx = i
            print(C_idx)
        if my_string[i] == "c":
            c_idx = i
            print(c_idx)
            my_string = my_string[:c_idx] + my_string[c_idx + 1:]
    return my_string
