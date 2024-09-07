#!/usr/bin/python3
# Write a function that prints a dictionary by ordered keys.
def print_sorted_dictionary(a_dictionary):
    a_dic = dict(sorted(a_dictionary.items()))
    for k, v in a_dic.items():
        print('{}: {}'.format(k, v))
