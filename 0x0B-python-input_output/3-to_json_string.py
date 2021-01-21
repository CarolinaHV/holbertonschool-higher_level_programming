#!/usr/bin/python3
"""
This function returns the JSON representation
of an object (string)

"""
import json


def to_json_string(my_obj):
    """to JSON from string"""
    return (json.dumps(my_obj))
