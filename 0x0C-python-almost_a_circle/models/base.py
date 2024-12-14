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

    @staticmethod
    def to_json_string(list_dictionaries):
        '''returns the JSON string representation of list_dictionaries:
            '''
        if list_dictionaries is None or list_dictionaries == '[]':
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''
        Returns the list of the JSON string representation json_string.
        Args:
            json_string (str): _description_
        Returns:
            list: JSON string representation json_string
        '''
        file_name = f'{cls.__name__}.json'
        json_string = []
        if list_objs is None or list_objs == '[]':
            pass
        else:
            for arg in list_objs:
                json_string.append(arg.to_dictionary())

        dump_string = cls.to_json_string(json_string)
        with open(file_name, mode='w', encoding="UTF-8") as wf:
            wf.write(dump_string)

    @staticmethod
    def from_json_string(json_string):
        ''' returns the list of the JSON string representation'''
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)
