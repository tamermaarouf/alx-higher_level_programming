#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    ta = reset(tuple_a)
    tb = reset(tuple_b)
    
    return (ta[0] + tb[0], ta[1] + tb[1])

def reset(tple=()):
    if len(tple) == 0:
        tple = 0, 0
    elif len(tple) == 1:
        tple = tple[0], 0
    else:
        tple = tple[0], tple[1]
    return (tple)
