#!/usr/bin/python3
''' Write a function that prints My name is <first name> <last name> '''


def say_my_name(first_name, last_name=""):
    if (not first_name):
        raise TypeError("missing 1 required positional argument: 'first_name'")
    if (not (isinstance(first_name, str))):
        raise TypeError("first name must be a string")
    if not (first_name.strip()):
        raise TypeError("first name must be a string")
    if (not (isinstance(last_name, str))):
        raise TypeError("last name must be a string")
    else:
        print("My name is {:s} {:s}".format(first_name, last_name))
