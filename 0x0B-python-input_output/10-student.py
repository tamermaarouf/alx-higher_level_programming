#!/usr/bin/python3
'''Write a class Student that defines a student by:'''


class Student:
    '''Instantiation with first_name, last_name and age'''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    '''If attrs is a list of strings,
    only attribute names contained in this list must be retrieved.
    Otherwise, all attributes must be retrieved
    '''

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            my_dict = {}
            for key, value in self.__dict__.items():
                if key in attrs:
                    my_dict[key] = value
            return my_dict
