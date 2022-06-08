#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix[:]
    for row in new_matrix:
        row_len = len(row)
        for idx in range(row_len):
            row[idx] = row[idx] ** 2
    return new_matrix
