#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return (list(map(lambda mat: [x * x for x in mat], matrix)))
