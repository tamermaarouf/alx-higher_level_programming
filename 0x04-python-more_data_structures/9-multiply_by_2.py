#!/usr/bin/python3
# a function that returns a new dictionary with all values multiplied by 2
def multiply_by_2(a_dictionary):
    '''
    a_dir = {}
    for x, y in a_dictionary.items():
        a_dir[x] = y * 2
    return (a_dir)
    '''
    return {x: y * 2 for x, y in a_dictionary.items()}
