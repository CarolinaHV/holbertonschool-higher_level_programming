#!/usr/bin/python3
import json
"""
This function writes an Object to a text file,
using a JSON representation

"""


def save_to_json_file(my_obj, filename):
    with open(filename, 'w') as f_json:
        return (json.dump(my_obj, f_json))
