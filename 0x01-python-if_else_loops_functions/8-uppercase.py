#!/usr/bin/env python3
def uppercase(str):
    for i in range(len(str)):
        if i != (len(str) - 1):
            print("{0}".format((chr(ord(str[i])-32)) if 97 <= ord(str[i]) <= 122 else (str[i])), end='')
        else:
            print("{0}".format(chr(ord(str[i])-32)))
