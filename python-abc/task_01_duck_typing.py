#!/usr/bin/python3
""" The module """

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """ Abstract shape class """

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """ The circle class """

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.area ** 2
    
    def perimeter(self):
        return pi * self.area * 2
    

class Rectangle(Shape):
    """ The rectangle class """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return self.width * 2 + self.height * 2


def shape_info(obj):
    print(f"Area: {obj.area()}")
    print(f"Perimeter: {obj.perimeter()}")
