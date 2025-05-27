#!/usr/bin/python3
""" MyList module """


class MyList(list):
    """ My class??? """

    def print_sorted(self):
        new_list = sorted(self)
        print(new_list)
        return new_list
