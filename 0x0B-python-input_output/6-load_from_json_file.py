#!/usr/bin/python3
'''Write a function that creates an Object from a “JSON file”:'''
import json


def load_from_json_file(filename):
    '''
    Prototype: def load_from_json_file(filename):
    You must use the with statement
    You don’t need to manage file permissions / exceptions.
    '''
    with open(filename, "r", encoding="UTF-8") as rf:
        return json.load(rf)
