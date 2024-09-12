#!/usr/bin/pythoin3
'''Write a class Square that defines a square '''


class Square():
    ''' Instantiation with optional size: def __init__(self, size=0) '''
    def __init__(self, size=0):
        ''' Private instance attr: size '''
        try:
            if size >= 0:
                self.__size = size
            elif size < 0:
                raise ValueError
            else:
                raise TypeError
        except ValueError:
            print("Size must be >= 0")
        except TypeError:
            print("size must be an integer")
