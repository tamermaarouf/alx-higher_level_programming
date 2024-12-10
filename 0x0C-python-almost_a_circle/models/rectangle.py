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
    def width(self, value):
        '''Setter'''
        self.__width = value

    @property
    def height(self):
        '''Getter'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Setter'''
        self.__height = value

    @property
    def x(self):
        '''Getter'''
        return self.__x

    @x.setter
    def x(self, value):
        '''Setter'''
        self.__x = value

    @property
    def y(self):
        '''Getter'''
        return self.__y

    @y.setter
    def y(self, value):
        '''Setter'''
        self.__y = value
