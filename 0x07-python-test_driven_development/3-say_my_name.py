#!/usr/bin/python3
''' Write a function that prints My name is <first name> <last name> '''


def say_my_name(first_name, last_name=""):
    ''' first_name and last_name must be strings otherwise,
    raise a TypeError exception with the message
    first_name must be a string or last_name must be a string
    '''
    if (not isinstance(first_name, str)) or (not first_name):
        raise TypeError("first name must be a string")
    if (not isinstance(last_name, str)):
        raise TypeError("last name must be a string")
    print("My name is {} {}".format(first_name, last_name))
