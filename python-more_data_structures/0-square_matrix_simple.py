#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = [row[:] for row in matrix]
    for aid, a in enumerate(matrix):
        for bid, b in enumerate(a):
            new_matrix[aid][bid] = new_matrix[aid][bid] ** 2
    return new_matrix
