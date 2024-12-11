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
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height
        self.integer_validator('x', x)
        self.__x = x
        self.integer_validator('y', y)
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        '''Getter'''
        return self.__width

    @width.setter
    def width(self, valueWidth):
        '''Setter'''
        if not isinstance(valueWidth, int):
            raise TypeError('width must be an integer')
        if valueWidth < 0:
            raise ValueError('width must be > 0')
        self.__width = valueWidth

    @property
    def height(self):
        '''Getter'''
        return self.__height

    @height.setter
    def height(self, valueH):
        '''Setter'''
        if not isinstance(valueH, int):
            raise TypeError('height must be an integer')
        if valueH < 0:
            raise ValueError('height must be > 0')
        self.__height = valueH

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
