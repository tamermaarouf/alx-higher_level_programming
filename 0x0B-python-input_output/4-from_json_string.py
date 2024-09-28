#!/usr/bin/python3
import json
'''a function that returns an object Python data structure'''


def from_json_string(my_str):
    '''returns (Python data structure) represented by a JSON string'''
    return (json.loads(my_str))
