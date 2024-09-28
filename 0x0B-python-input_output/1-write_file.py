#!/usr/bin/python3
'''Write a function that writes a string to a text file '''


def write_file(file_name="", text=""):
    '''returns the number of characters written:'''
    with open(file_name, "w+", encoding='utf-8') as f:
        return f.write(text)
