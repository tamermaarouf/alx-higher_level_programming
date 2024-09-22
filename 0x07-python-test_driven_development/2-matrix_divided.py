#!/usr/bin/python3
''' Write a function that divides all elements of a matrix. '''


def matrix_divided(matrix, div):
    if not matrix:
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(matrix, list):
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if not isinstance(row, list) || len(row) == 0:
            raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats")
        for col in row:
            if type(col) not in [int, float]:
                raise TypeError(
                        "matrix must be a matrix (list of lists) of integers/floats")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    else:
        return [[round(col/div, 2) for col in row] for row in matrix]
