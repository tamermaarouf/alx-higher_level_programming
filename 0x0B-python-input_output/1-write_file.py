#!/usr/bin/python3
'''0x0B. Python - Input/Output'''


def write_file(file_name="", text=""):
    with open(file_name, "w", encoding='utf-8') as f:
        return f.write(text)
