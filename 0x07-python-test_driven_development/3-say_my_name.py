#!/usr/bin/python3
''' Write a function that prints My name is <first name> <last name> '''


def say_my_name(first_name, last_name=""):
    ''' first_name and last_name must be strings otherwise,
    raise a TypeError exception with the message first name must be a string'''

    if (not first_name):
        raise TypeError("first name must be a string")
    if type(first_name) is not str:
        raise TypeError("first name must be a string")
    if type(last_name) not in [str]:
        raise TypeError("last name must be a string")
    print("My name is {} {}".format(first_name, last_name))
