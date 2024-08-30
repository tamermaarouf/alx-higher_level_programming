#!/usr/bin/python3
for i in range(0,  100):
    if i == 99:
        print(f"{i}")
    elif i >= 10:
        print(f"{i}", end=', ')
    else:
        print(f"0{i}", end=', ')
