#!/usr/bin/python3
""" The module """


def read_file(filename=""):
    """ Opens the file and prints its contents """
    with open(filename) as file:
        for line in file:
            print(line, end='')
