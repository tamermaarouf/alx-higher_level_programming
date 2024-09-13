#!/usr/bin/python3
'''Write a class Square that defines a square '''


class Square:
    ''' Instantiation with optional size: def __init__(self, size=0) '''
    def __init__(self, size=0):
        ''' Private instance attr: size '''
        if (isinstance(size, int)):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError('size must be >= 0')
        else:
            raise TypeError("size must be an integer")

    ''' Public instance method: def area(self): that returns the current square area'''
    @property
    def area(self):
        return (self.__size * self.__size)
