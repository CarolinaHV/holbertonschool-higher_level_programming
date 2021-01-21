#!/usr/bin/python3
"""
This function appends a string at the end of a text file (UTF8)
and returns the number of characters added:

"""


def append_write(filename="", text=""):
    """append file"""
    with open(filename, 'a') as holb_text:
        return holb_text.write(text)
