#!/usr/bin/python3
'''if the object is an instance of a class that inherited from'''


def inherits_from(obj, a_class):
    '''Determines if an object is exactly an instance of a class.'''
    return isinstance(obj, a_class) and type(obj) is not a_class
