#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) < 123:
            new_chr = ord(str[i]) - 32
            print('{:c}'.format(new_chr), end="")
        elif ord(str[i]) >= 65 and ord(str[i]) <= 90:
            print('{}'.format(str))
        else:
            print('{}'.format(str))
