#!/usr/bin/python3
"""This is the module"""
"""This function adds 2 integers."""


def add_integer(a, b=98):
    """This is the function"""
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    return int(a + b)
