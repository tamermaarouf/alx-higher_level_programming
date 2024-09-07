#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    '''
    new_matrix = []
    for i in range(len(matrix)):
        mul_matrix = []
        for x in range(len(matrix[i])):
            mul_matrix.append(matrix[i][x] * matrix[i][x])
        new_matrix.append(mul_matrix)
    '''
    return ([[x**2 for x in i] for i in matrix])
