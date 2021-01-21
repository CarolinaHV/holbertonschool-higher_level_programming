#!/usr/bin/python3
"""
script that adds all arguments to a Python list
and then save them to a file

"""

import sys

save_to_json_f = __import__('5-save_to_json_file').save_to_json_file
load_from_json_f = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    obj = load_from_json_f(filename)
except:
    obj = []

for x in sys.argv[1:]:
    obj.append(x)
save_to_json_f(obj, filename)
