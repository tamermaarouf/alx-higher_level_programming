#!/usr/bin/python3
''' Write a function that divides all elements of a matrix. '''


def matrix_divided(matrix=None, div=0):
    """Divides all elements of a matrix.

    Args:
        matrix: The matrix whoses elements are to be divided by div.
        div: The dividing number.

    Raises:
        TypeError: if matrix is not a list of lists of int or float.
        TypeError: if each row of matrix is not of same size.
        TypeError: if div is neither an int nor float
        ZeroDivisionError: if div is zero

    Returns:
        a new matrix with elements rounded to 2 decimal places.
    """

    message = "matrix must be a matrix (list of lists) of integers/floats"
    if (not isinstance(matrix, list)) | (not matrix):
        raise TypeError(message)
    if not matrix:
        raise TypeError(message)
    for row in matrix:
        if len(row) == 0:
            raise TypeError(message)
        if not isinstance(row, list):
            raise TypeError(message)
        for col in row:
            if type(col) not in [int, float]:
                raise TypeError(message)
    len_rows = []
    for ele in matrix:
        len_rows.append(len(ele))
    if not all(lists == len_rows[0] for lists in len_rows):
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    else:
        return ([[round(col/div, 2) for col in row] for row in matrix])
