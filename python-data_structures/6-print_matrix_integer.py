#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for a in matrix:
        for index, b in enumerate(a):
            print("{:d}".format(b), end="" if index == len(a) - 1 else " ")
        print("".format())
