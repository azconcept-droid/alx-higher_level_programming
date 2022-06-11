#!/usr/bin/python3
new_matrix = []
def square_matrix_simple(matrix=[]):
    for row in matrix:
        col = []
        for integers in row:
            col.append(integers ** 2)
        new_matrix.append(col)
    return new_matrix
