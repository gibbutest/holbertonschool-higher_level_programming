#!/usr/bin/python3
"""
    The square module
"""


def raiseErrors(size):
    """
        Simple function to raise errors
    """
    if not (isinstance(size, int)):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')


class Square:
    """
        A class to create a square
    """

    def __init__(self, size=0):
        raiseErrors(size)
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        raiseErrors(value)
        self.__size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        for i in range(self.__size):
            print(f'#' * self.__size, end=" " if self.__size == 0 else "\n")
