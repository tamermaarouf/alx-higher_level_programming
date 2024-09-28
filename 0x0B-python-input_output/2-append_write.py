#!/usr/bin/python3
'''Write a function that appends a string at the end of a text file'''


def append_write(file_name="", text=""):
    '''returns the number of characters add:'''
    with open(file_name, "a", encoding='utf-8') as f:
        return f.write(text)
