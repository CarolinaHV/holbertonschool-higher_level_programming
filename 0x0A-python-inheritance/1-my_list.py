#!/usr/bin/python3
"""
Class inheritance from list

"""


class MyList(list):
    """Mylist class inherits from list"""
    def print_sorted(self):
        """Print the list sorted"""
        print(sorted(self))
