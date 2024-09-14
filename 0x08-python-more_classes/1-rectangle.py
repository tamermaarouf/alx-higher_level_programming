#!/usr/bin/python3
'''class Rectangle that defines a rectangle by'''


class Rectangle():
    '''Instantiation with optional width and height: __init__'''
    def __init__(self, width=0, height=0):
        '''method is executed immediately after create an object'''
        self.__height = height
        self.__width = width

    '''property width to retrieve it'''
    @property
    def width(self):
        '''Getter'''
        return (self.__width)

    '''property setter width to set it: '''
    @width.setter
    def width(self, value):
        '''Setter'''
        if (isinstance(value, int)):
            if value >= 0:
                self.__width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    '''property height: to retrieve it'''
    @property
    def height(self):
        '''Getter'''
        return (self.__height)

    '''property setter height to set it: '''
    @height.setter
    def height(self, value):
        '''setter'''
        if(isinstance(value, int)):
            if value >= 0:
                self.__height = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")
