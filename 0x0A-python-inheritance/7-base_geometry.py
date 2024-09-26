#!/usr/bin/python3
'''Write an empty class BaseGeometry.'''


class BaseGeometry:
    '''A BaseGeometry class.'''
    def area(self):
        '''Exception with the message area() is not implemented'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''Method for validating the value.'''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

    '''def integer_validator(self, name, value):
        Public instance method: that validates value:
        if (type(value) != int):
            raise TypeError("{} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))
    '''
