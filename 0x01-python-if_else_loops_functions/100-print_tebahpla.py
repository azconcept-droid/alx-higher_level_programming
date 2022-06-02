#!/usr/bin/python3
i = 122
while i >= 97:
    if i % 2 == 0:
        print('{:s}'.format(chr(i)), end="")
    else:
        print('{:s}'.format(chr(i - 32)), end="")
    i -= 1
