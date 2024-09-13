#!/usr/bin/pythoin3
'''Write a class Square that defines a square '''


class Square():
    ''' Instantiation with optional size: def __init__(self, size=0) '''
    def __init__(self, size=0):
        ''' Private instance attr: size '''
        if not (isinstance(size, int)):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >=0")
        else:
            self.__size = size
