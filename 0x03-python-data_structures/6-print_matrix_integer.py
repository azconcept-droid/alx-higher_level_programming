#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for col in row:
            for i in range(len(row)):
                print("{:d}".format(col[i]))
