#!/usr/bin/python3
'''if the object is an instance of a class that inherited from'''


def is_kind_of_class(obj, a_class):
    '''Determines if an object is exactly an instance of a class.'''
    return issubclass(obj, a_class)
