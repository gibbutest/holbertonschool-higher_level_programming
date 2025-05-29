#!/usr/bin/python3
""" The module """


class Fish():
    """ The fish class """

    @staticmethod
    def swim():
        print("The fish is swimming")

    @staticmethod
    def habitat():
        print("The fish lives in water")


class Bird():
    """ The bird class """

    @staticmethod
    def fly():
        print("The bird is flying")

    @staticmethod
    def habitat():
        print("The bird lives in the sky")


class FlyingFish(Bird, Fish):
    """ The flying fish class """

    @staticmethod
    def fly():
        print("The flying fish is soaring!")

    @staticmethod
    def swim():
        print("The flying fish is swimming!")

    @staticmethod
    def habitat():
        print("The flying fish lives both in water and the sky!")
