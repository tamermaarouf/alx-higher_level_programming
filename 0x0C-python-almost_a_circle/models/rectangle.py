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
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        '''Getter'''
        return self.__width

    @width.setter
    def width(self, valueWidth):
        '''Setter'''
        self.__width = valueWidth

    @property
    def height(self):
        '''Getter'''
        return self.__height

    @height.setter
    def height(self, valueH):
        '''Setter'''
        self.__height = valueH

    @property
    def x(self):
        '''Getter'''
        return self.__x

    @x.setter
    def x(self, valueX):
        '''Setter'''
        self.__x = valueX

    @property
    def y(self):
        '''Getter'''
        return self.__y

    @y.setter
    def y(self, valueY):
        '''Setter'''
        self.__y = valueY
