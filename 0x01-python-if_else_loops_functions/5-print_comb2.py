#!/usr/bin/python3
for i in range(0,  100):
    if i == 99:
        print("{0}".format(i))
    else:
        print('{}{}'.format("0" if i < 10 else "", i), end=', ')
