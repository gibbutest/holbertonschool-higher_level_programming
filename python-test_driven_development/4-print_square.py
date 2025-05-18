#!/usr/bin/python3
"""
    The module
"""


def print_square(size):
    """
        A function that prints a square of #
    """
    if not isinstance(size, int):
        raise TypeError("Size must be an integer")
    if size < 0:
        raise ValueError("Size must be >= 0")
    for i in range(size):
        print(f'#' * size)