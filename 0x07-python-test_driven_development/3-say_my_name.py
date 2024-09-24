#!/usr/bin/python3
'''Write a function that prints My name is first name last name '''


def say_my_name(first_name, last_name=""):
    '''This function prints My name is first name last name
    TypeError: If either the first_name and last_name are not strings'''
    if not isinstance(first_name, str):
        raise TypeError("first name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
