#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        char = ord(str[i])
        if 97 <= char <= 122:
            char = char - 32
        print("{0}".format(chr(char)), end='')
    print()
