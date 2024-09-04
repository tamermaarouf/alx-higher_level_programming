#!/usr/bin/python3
import sys
if __main__ = "__name__":
    if len(sys.argv) < 2:
        print("0 arguments.")
    else:
        print("{} argument:".format(len(sys.argv) - 1))
        for i in range(1, len(sys.argv)):
            print("{}: {}".format(i, sys.argv[i]))
