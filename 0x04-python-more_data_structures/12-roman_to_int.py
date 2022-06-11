#!/usr/bin/python3
def roman_to_int(roman_string):
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    convert = 0
    prev_int = 0
    current_int = 0
    for letter in roman_string[::-1]:
        prev_int = current_int
        current_int = romans[letter]
        if current_int >= prev_int:
            convert += current_int
        else:
            convert -= current_int
    return convert
