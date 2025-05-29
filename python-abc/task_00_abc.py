#!/usr/bin/python3
""" The module """

from abc import ABC, abstractmethod


class Animal(ABC):
    """ Abstract animal class """

    @abstractmethod
    def sound():
        pass


class Dog(Animal):
    """ The dog class """

    def sound():
        return "Bark"
    

class Cat(Animal):
    """ The cat class """

    def sound():
        return "Meow"
