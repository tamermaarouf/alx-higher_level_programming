#!/usr/bin/python3
'''a class Rectangle that inherits from BaseGeometry'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Instantiation with width and heigh'''
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return "[Square] {}/{}".format(self.__width, self.__height)
