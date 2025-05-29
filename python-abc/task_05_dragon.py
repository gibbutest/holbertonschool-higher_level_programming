#!/usr/bin/python3
""" The module """


class SwimMixin():
    """ The swim class """

    @staticmethod
    def swim():
        print("The creature swims!")


class FlyMixin():
    """ The fly class """

    @staticmethod
    def fly():
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """ the dragon class """

    @staticmethod
    def roar():
        print("The dragon roars!")
