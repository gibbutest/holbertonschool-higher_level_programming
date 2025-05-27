#!/usr/bin/python3
""" The module """


class BaseGeometry:
    """ The geometry class """

    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        if not type(value) is int:
            raise TypeError(f'{name} must be an integer')
        elif value <= 0:
            raise ValueError(f'{name} must be greater than 0')
