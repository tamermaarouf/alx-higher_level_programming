#!/usr/bin/python3
'''Write a class Student that defines a student by:'''


class Student:
    def __init__(self, first_name, last_name, age):
        '''Instantiation with first_name, last_name and age'''
        self.first_name = first_name
        self.last = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
