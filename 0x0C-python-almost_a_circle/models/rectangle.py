#!/usr/bin/python3
'''Write the class Rectangle that inherits from Base:'''
from models.base import Base


class Rectangle(Base):
    '''
    Class Rectangle inherits from Base
    Private instance attributes, each with its own public getter and setter:
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''constractor'''
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        '''Getter'''
        return self.__width

    @width.setter
    def width(self, valueWidth):
        '''Setter'''
        if (isinstance(valueWidth, int)):
            if (valueWidth > 0):
                self.__width = valueWidth
            else:
                raise ValueError('width must be > 0')
        else:
            raise TypeError('width must be an integer')

    @property
    def height(self):
        '''Getter'''
        return self.__height

    @height.setter
    def height(self, valueH):
        '''Setter'''
        if (isinstance(valueH, int)):
            if (valueH > 0):
                self.__height = valueH
            else:
                raise ValueError('height must be > 0')
        else:
            raise TypeError('height must be an integer')

    @property
    def x(self):
        '''Getter'''
        return self.__x

    @x.setter
    def x(self, valueX):
        '''Setter'''
        if (isinstance(valueX, int)):
            if (valueX >= 0):
                self.__x = valueX
            else:
                raise ValueError('x must be >= 0')
        else:
            raise TypeError('x must be an integer')

    @property
    def y(self):
        '''Getter'''
        return self.__y

    @y.setter
    def y(self, valueY):
        '''Setter'''
        if (isinstance(valueY, int)):
            if (valueY >= 0):
                self.__y = valueY
            else:
                raise ValueError('y must be >= 0')
        else:
            raise TypeError('y must be an integer')
