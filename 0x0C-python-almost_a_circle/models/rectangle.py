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
        super().integer_validator('width', width, False)
        self.width = width
        super().integer_validator('height', height, False)
        self.height = height
        super().integer_validator('x', x, True)
        self.x = x
        super().integer_validator('y', y, True)
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        '''Getter'''
        return self.__width

    @width.setter
    def width(self, valueWidth):
        '''Setter'''
        super().integer_validator('width', valueWidth, False)
        self.__width = valueWidth

    @property
    def height(self):
        '''Getter'''
        return self.__height

    @height.setter
    def height(self, valueH):
        '''Setter'''
        super().integer_validator('height', valueH, False)
        self.__height = valueH

    @property
    def x(self):
        '''Getter'''
        return self.__x

    @x.setter
    def x(self, valueX):
        '''Setter'''
        super().integer_validator('x', valueX, True)
        self.__x = valueX

    @property
    def y(self):
        '''Getter'''
        return self.__y

    @y.setter
    def y(self, valueY):
        '''Setter'''
        super().integer_validator('y', valueY, True)
        self.__y = valueY

    def area(self):
        return (self.__width * self.__height)

    def display(self):
        print(self.__width, self.__height)
