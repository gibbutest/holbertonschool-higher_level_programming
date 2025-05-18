#!/usr/bin/python3
"""
    The module
"""


def text_indentation(text):
    """
        A function that prints 2 new lines after these characters:
        `.`, `?`, `:`
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    string = ""
    for char in text:
        string += char
        if char in ".?:":
            print(string)
            print()
            string = ""

    if string:
        print(string)
