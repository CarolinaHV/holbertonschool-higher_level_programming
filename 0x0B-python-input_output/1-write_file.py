#!/usr/bin/python3
"""
This function writes a string to a text file (UTF8)
and returns the number of characters written

"""


def write_file(filename="", text=""):
    """Write file"""
    with open(filename, 'w') as holb_text:
        return holb_text.write(text)
