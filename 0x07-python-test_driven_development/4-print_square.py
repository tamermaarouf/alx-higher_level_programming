#!/usr/bin/python3
'''Write a function that prints a square with the character #.'''


def print_square(size):
    '''Prototype: def print_square(size):
    size is the size length of the square
    size must be an integer, raise a TypeError(size must be an integer)
    if size is less than 0, raise a ValueError(size must be >= 0)
    if size is a float and is less than 0, TypeError(size must be an integer)
    '''
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    print((("#" * size + "\n") * size), end="")
