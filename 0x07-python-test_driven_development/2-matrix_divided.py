#!/usr/bin/python3
''' Write a function that divides all elements of a matrix. '''


def matrix_divided(matrix, div):
    message = "matrix must be a matrix (list of lists) of integers/floats"
    if not matrix:
        raise TypeError(message)
    if not isinstance(matrix, list):
        raise TypeError(message)
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(message)
        for col in row:
            if type(col) not in [int, float]:
                raise TypeError(message)
    for ele in matrix:
        if len(ele) == 0:
            raise TypeError(message)
    if not all(len(lists) == len(matrix[0]) for lists in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(col/div, 2) for col in row] for row in matrix]
