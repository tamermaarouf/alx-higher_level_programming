#!/usr/bin/python3
''' class Rectangle '''


class Rectangle:
    ''' Instantiation with optional width and height '''
    def __init__(self, width=0, height=0):
        ''' method is executed immediately after create an object '''
        self.height = height
        self.width = width

    @property
    def width(self):
        ''' Getter '''
        return self.__width

    @width.setter
    def width(self, value):
        ''' Setter '''
        if (isinstance(value, int)):
            if value >= 0:
                self.__width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        ''' Getter '''
        return self.__height

    @height.setter
    def height(self, value):
        ''' Setter '''
        if(isinstance(value, int)):
            if value >= 0:
                self.__height = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")
