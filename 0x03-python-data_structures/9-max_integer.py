#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) < 1:
        return None
    max_num = None
    if len(my_list) > 0:
        max_num = my_list[0]
        for num in my_list:
            if num > max_num:
                max_num = num
    return max_num
