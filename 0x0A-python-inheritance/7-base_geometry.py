#!/usr/bin/python3
'''Write an empty class BaseGeometry.'''


class BaseGeometry:
    '''A BaseGeometry class.'''
    def area(self):
        '''Exception with the message area() is not implemented'''
        raise Exception("area() is not implemented")

    '''Public instance method: that validates value: '''
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if (isinstance(value, int)) and (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))
