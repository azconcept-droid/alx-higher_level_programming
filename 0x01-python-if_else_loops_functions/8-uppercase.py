#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord(char) >= 97 and ord(char) < 123:
            new_str = chr(ord(char) - 32)
        else:
            new_str = char
        print('{:s}'.format(new_str), end="")
    print()
