#!/usr/bin/python3
'''Write a function that reads a text file (UTF8) and prints it to stdout:'''


def read_file(filename=""):
    '''You must use the with statement'''
    with open(filename, encoding="utf-8") as r_file:
        for line in r_file:
            print(line, end='')
