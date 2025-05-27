#!/usr/bin/python3
""" The module """


def inherits_from(obj, a_class):
    """ Checks if a instance of class that inherits from a specific class """
    return isinstance(obj, a_class) and type(obj) is not a_class
