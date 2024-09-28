#!/usr/bin/python3
'''Write a script that adds all arguments to a Python list'''
import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if os.path.isfile("add_item.json"):
    load_list = load_from_json_file("add_item.json")
    for arg in sys.argv[1:]:
        load_list.append(arg)
    '''and then save them to a file:'''
    save_to_json_file(load_list, "add_item.json")
else:
    load_list = sys.argv[1:]
    save_to_json_file(load_list, "add_item.json")
