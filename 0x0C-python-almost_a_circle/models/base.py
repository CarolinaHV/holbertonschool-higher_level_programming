#!/usr/bin/python3
""" Base class """
import json


class Base:
    """ Private class attribute """
    __nb_objects = 0
    """ Constructor """
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def save_to_file(cls, list_objs):
        """ JSON string to a file """
        if list_objs is None:
            empty = []
        else:
            new_ld = []
            for obj in list_objs:
                obj = obj.to_dictionary()
                new_ld.append(obj)
            empty = (cls.to_json_string(new_ld))
        with open('{}.json'.format(cls.__name__), 'w') as file_J:
            file_J.write(empty)

    @classmethod
    def create(cls, **dictionary):
        """ Dictionary to Instance """
        if cls.__name__ == "Rectangle":
            dummy = Rectangle(1, 1, 3, 5)
        elif cls.__name__ == "Square":
            dummy = Square(1, 3, 5)
        dummy.update(**dictionary)
        return dummy

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Dictionary to JSON string """
        if list_dictionaries is None or list_dictionaries is []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """ JSON string to dictionary """
        if json_string is None or json_string is []:
            return "[]"
        else:
            return json.loads(json_string)
