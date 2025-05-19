#!/usr/bin/python3
"""
    The square module
"""


def sizeErrors(size):
    """
        Function to raise errors for the size argument
    """
    if not (isinstance(size, int)):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')


def positionErrors(position):
    """
        Function to raise errors for the position argument
    """
    if (not isinstance(position, tuple) or
            not isinstance(position[0], int) or
            not isinstance(position[1], int) or
            position[0] < 0 or position[1] < 0):
        raise TypeError('position must be a tuple of 2 positive integers')


class Square:
    """
        A class to create a square
    """

    def __init__(self, size=0, position=(0, 0)):
        sizeErrors(size)
        positionErrors(position)
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        sizeErrors(value)
        self.__size = value

    @position.setter
    def position(self, value):
        positionErrors(value)
        self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(' ' * self.__position[0] + '#' * self.__size)
