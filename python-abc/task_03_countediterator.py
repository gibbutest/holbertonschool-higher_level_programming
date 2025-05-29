#!/usr/bin/python3
""" The module """


class CountedIterator():
    """ Wack iteration class """

    def __init__(self, data):
        self.__counter = 0
        self.data = data

    def __next__(self):
        if self.__counter >= len(self.data):
            raise StopIteration()
        item = self.data[self.__counter]
        self.__counter += 1
        return item

    def get_count(self):
        return self.__counter
