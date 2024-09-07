#!/usr/bin/python3
# Write a function that returns a key with the biggest integer value.
def best_score(a_dictionary):
    if a_dictionary:
        return (max(a_dictionary, key=a_dictionary.get))
    else:
        return None
