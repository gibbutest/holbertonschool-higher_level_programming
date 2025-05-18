#!/usr/bin/python3
"""
    The module
"""


def matrix_divided(matrix, div):
    """
        Divides all elements of a matrix by a number,
        rounding to 2 decimal places. Then returning a new matrix.
    """
    if not isinstance(div, int):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if (not isinstance(matrix, list) or
        not all(isinstance(row, list) for row in matrix) or
            not all(isinstance(x, (int, float)) for row in matrix for x in row)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError(
            "Each row of the matrix must have the same size"
        )

    return [[round(val / div, 2) for val in row] for row in matrix]
