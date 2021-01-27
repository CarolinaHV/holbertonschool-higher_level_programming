#!/usr/bin/python3
""" Base class """
import json


class Base:
    """ Private class attribute """
    __nb_objects = 0
    """ Constructor """
    def __init__(self, id=None):
        #self.id = id

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects


    def save_to_file(cls, list_objs):
        if list_objs is None:
            empty = []
    #    else:
            

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return []
        else:
            return json.dumps(list_dictionaries)
