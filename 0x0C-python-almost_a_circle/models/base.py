#!/usr/bin/python3
'''
Write the first class Base:
'''
import json


class Base():
    '''Class Base'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''
        if id is not None, assign the public instance attribute id with
        this argument value - you can assume id is an integer and
        you don’t need to test the type of it
        otherwise, increment __nb_objects and assign
        the new value to the public instance attribute id
        '''
        if id is not None and (isinstance(id, int)):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        '''returns the JSON string representation of list_dictionaries:'''
        if (list_dictionaries is None) or list_dictionaries == '[]':
            return []
        else:
            return json.dumps(list_dictionaries)
