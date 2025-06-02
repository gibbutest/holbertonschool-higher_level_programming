#!/usr/bin/python3
""" The module """


import json


def save_to_json_file(my_obj, filename):
    """ Save dict to json file """

    with open(filename, 'w') as file:
        obj = json.dumps(my_obj)

        file.write(obj)
