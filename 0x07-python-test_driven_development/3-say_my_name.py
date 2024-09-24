#!/usr/bin/python3


def say_my_name(first_name, last_name=""):
    '''This function prints name (<first name> <last name>)
    Args:
    first_name (str): The fisrt name to be printed
    last_name (str): The last name to be printed
    Raises:
    TypeError: If either the first_name and last_name are not strings'''
    if not isinstance(first_name, str):
        raise TypeError("first name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last name must be a string")
    print("My name is {} {}".format(first_name, last_name))
