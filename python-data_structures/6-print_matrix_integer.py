#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for a in matrix:
        for index, b in enumerate(a):
            print(b, end="\n" if index == len(a) - 1 else " ")
