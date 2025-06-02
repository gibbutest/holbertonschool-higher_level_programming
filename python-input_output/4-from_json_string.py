#!/usr/bin/python3
""" The module """


import json


def from_json_string(my_str):
    """ Returns a json object/dict """
    return json.loads(my_str)
