#!/usr/bin/python3
''' Write a function that prints My name is <first name> <last name> '''


def say_my_name(first_name, last_name=""):
    error_message = "first_name must be a string or last_name must be a string"
    if (not first_name) or (not (isinstance(first_name, str))):
        raise TypeError("first name must be a string")
    if not (first_name.strip()):
        raise TypeError("first name must be a string")
    if (not (isinstance(last_name, str))):
        raise TypeError("last name must be a string")
    else:
        print("{} {}".format(first_name, last_name))
