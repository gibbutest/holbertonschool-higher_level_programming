#!/usr/bin/python3
""" The module """


def append_write(filename="", text=""):
    """ Append to a file, and return length of characters """
    with open(filename, 'a') as file:
        file.write(text)

        return len(text)
