#!/usr/bin/python3
"""
    The rectangle module
"""


def sizeError(value, field):
    if not (isinstance(value, int)):
        raise TypeError(f'{field} must be an integer')
    if value < 0:
        raise ValueError(f'{field} must be >= 0')


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
        sizeError(value, 'width')
        self.__width = value

    @height.setter
    def height(self, value):
        sizeError(value, 'height')
        self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (
            self.height * 2 + self.width * 2
            if self.height != 0 or self.width != 0
            else
            0)
