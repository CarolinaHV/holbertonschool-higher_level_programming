#!/usr/bin/python3
"""
This function returns True
if the object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class, otherwise return False.

"""


def is_kind_of_class(obj, a_class):
    """Return object and class"""
    return isinstance(obj, a_class)
