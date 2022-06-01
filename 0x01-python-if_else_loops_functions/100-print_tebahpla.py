#!/usr/bin/python3
i = 122
while i > 96:
    if i % 2 == 0:
        print("{:s}".format(chr(i)), end="")
    elif i % 2 != 0:
        print("{:s}".format(chr(i - 32)), end="")
    i -= 1
