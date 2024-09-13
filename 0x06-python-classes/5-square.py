#!/usr/bin/python3
'''Write a class Square that defines a square '''


class Square:
    ''' Instantiation with optional size: def __init__(self, size=0) '''
    def __init__(self, size=0):
        ''' Private instance attr: size '''
        self.__size = size

    '''property def size(self): to retrieve it'''
    @property
    def size(self):
        return self.__size

    '''property setter def size(self, value): to set it: '''
    @size.setter
    def size(self, value=0):
        if (isinstance(value, int)):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError('size must be >= 0')
        else:
            raise TypeError('size must be an integer')
    ''' Public instance method: area that returns the current square area'''
    def area(self):
        return (self.__size ** 2)

    '''Public instance method: def my_print(self): that prints in stdout the square with the character #: '''
    def my_print(self):
        for row in range(self.__size):
            for col in range(self.__size):
                print('{}'.format('#'), end='')
            print('')
