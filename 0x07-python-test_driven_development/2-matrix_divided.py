#!/usr/bin/python3
''' Write a function that divides all elements of a matrix. '''

def matrix_divided(matrix, div):
    for row in matrix:
        if len(row) == len(matrix[0]):
            pass
        else:
            raise TypeError("Each row of the matrix must have the same size")
    if not(all([isinstance(col, int) for col in row] for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    elif not(isinstance(div, int)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    else:
        return [[round(col/div, 2) for col in row] for row in matrix]
