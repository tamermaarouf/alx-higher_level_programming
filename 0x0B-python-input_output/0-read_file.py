#!/usr/bin/python3
# Write a function that reads a text file (UTF8) and prints it to stdout:


def read_file(filename=""):
    with open(filename, mode="r", encoding="utf-8") as r_file:
        for line in r_file:
            print(line, end='')
