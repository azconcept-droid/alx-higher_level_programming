#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    i = 0
    k = 1
    for row in matrix:
        for col in row:
            i += 1
            if i == 3 * k:
                print("{:d}".format(col), end="")
                k += 1
            else:
                print("{:d}".format(col), end=" ")
        print()
