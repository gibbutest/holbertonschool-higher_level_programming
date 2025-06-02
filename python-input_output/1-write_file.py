#!/usr/bin/python3
""" The module """


def write_file(filename="", text=""):
    """ Write to a file, and return length of characters """
    with open(filename, 'w') as file:
        file.write(text)

        return len(text)
