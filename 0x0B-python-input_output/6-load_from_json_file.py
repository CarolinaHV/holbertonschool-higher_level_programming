#!/usr/bin/python3
"""
function creates an Object from a “JSON file”

"""
import json


def load_from_json_file(filename):
    """Create object from a JSON file"""
    with open(filename, encoding="utf-8") as holb_file:
        return (json.load(holb_file))
