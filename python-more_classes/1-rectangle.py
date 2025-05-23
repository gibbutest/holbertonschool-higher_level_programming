#!/usr/bin/python3
"""
    The rectangle module
"""


def sizeError(size):
    if not (isinstance(size, int)):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')


class Rectangle():
    """
        Start of the rectangle class
    """

    __width = 0
    __height = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        sizeError(value)
        self.__width = value

    @height.setter
    def height(self, value):
        sizeError(value)
        self.__height = value
