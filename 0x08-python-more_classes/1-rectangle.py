#!/usr/bin/python3
'''class Rectangle that defines a rectangle by'''


class Rectangle():
    '''Instantiation with optional width and height: __init__'''
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    '''property def width(self): to retrieve it'''
    @property
    def width(self):
        return (self.__width)

    '''property setter def width(self, value): to set it: '''
    @width.setter
    def width(self, value):
        if (isinstance(value, int)):
            if value >= 0:
                self.__width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    '''property def height(self): to retrieve it'''
    @property
    def height(self):
        return (self.__height)

    '''property setter def height(self, value): to set it: '''
    @height.setter
    def height(self, value):
        if(isinstance(value, int)):
            if value >= 0:
                self.__height = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")
