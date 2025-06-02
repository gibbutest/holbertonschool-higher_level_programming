#!/usr/bin/python3
""" The module """


def load_from_json_file(filename):
    """ Load json file """

    with open(filename) as file:
        return file.read()
