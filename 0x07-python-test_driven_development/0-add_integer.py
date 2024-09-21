#!/usr/bin/python3
''' Write a function that adds 2 integers. 
Prototype: def add_integer(a, b=98):
'''


def add_integer(a, b=98):
    ''' a and b must be integers or floats, otherwise raise a '''
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    ''' a and b must be first casted to integers if they are float '''
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    ''' Returns an integer: the addition of a and b '''
    else:
        return a + b
