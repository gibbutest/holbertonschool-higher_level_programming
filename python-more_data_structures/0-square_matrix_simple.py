#!/usr/bin/python3

import copy

def square_matrix_simple(matrix=[]):
    new_matrix = copy.deepcopy(matrix)
    for aid, a in enumerate(matrix):
        for bid, b in enumerate(a):
            new_matrix[aid][bid] = new_matrix[aid][bid] ** 2
    return new_matrix
