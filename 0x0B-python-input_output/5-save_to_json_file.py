#!/usr/bin/python3
'''Write a function that writes an Object to a text file'''
import json


def save_to_json_file(my_obj, filename):
    '''Object to a text file, using a JSON representation:'''
    with open(filename, mode="w", encoding="UTF-8") as wf:
        json.dump(my_obj, wf)
