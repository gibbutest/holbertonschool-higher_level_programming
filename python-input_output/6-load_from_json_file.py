#!/usr/bin/python3
""" The module """


import json


def load_from_json_file(filename):
    """ Load json file """

    with open(filename) as file:
        return json.load(file)
