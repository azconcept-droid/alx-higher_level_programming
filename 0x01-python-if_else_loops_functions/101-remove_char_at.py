#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = str
    if n < 0:
        return str
    elif n > 0 or n == 0:
        new_str = str[:n] + str[n + 1:]
        return new_str
