#!/usr/bin/python3
""" The module """


def write_file(filename="", text=""):
    """ Write to a file, and return length of characters """
    file = open(filename, 'w')
    file.write(text)

    return len(text)
