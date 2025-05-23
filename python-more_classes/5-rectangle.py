#!/usr/bin/python3
"""
    The rectangle module
"""


def sizeError(value, field):
    if not isinstance(value, int):
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
        if self.width == 0 or self.height == 0:
            return 0
        return self.width * 2 + self.height * 2

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ''

        string = ''
        for _ in range(self.height):
            string += '#' * self.width + '\n'

        return string[:-1]

    def __repr__(self):
        return f"Rectangle({str(self.width)}, {str(self.height)})"

    def __del__(self):
        print('Bye rectangle...')
