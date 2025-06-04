#!/usr/bin/python3
""" The module """


def class_to_json(obj):
    """ Converts a class to a json object """

    return obj.__dict__
