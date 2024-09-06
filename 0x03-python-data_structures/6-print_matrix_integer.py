#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 1 and len(matrix[0]) == 0:
        print('')
    if matrix:
        for x in range(len(matrix)):
            for j in range(len(matrix[x])):
                if j != (len(matrix[x]) - 1):
                    print('{:d}'.format(matrix[x][j]), end=' ')
                else:
                    print('{:d}'.format(matrix[x][j]))
