#!/usr/bin/python3
"""
This function returns True if the object is an instance of a class
that inherited (directly or indirectly) from the specified class, otherwise
return False.

"""


def inherits_from(obj, a_class):
    """evaluate object inheritance vs class"""
    if type(obj) is not a_class:
        return issubclass(type(obj), a_class)
    else:
        return False
