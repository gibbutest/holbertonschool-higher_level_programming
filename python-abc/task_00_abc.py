#!/usr/bin/python3
""" The module """

from abc import ABC, abstractmethod


class Animal(ABC):
    """ Abstract animal class """

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """ The dog class """

    def sound(self):
        return "Bark"
    

class Cat(Animal):
    """ The cat class """

    def sound(self):
        return "Meow"
