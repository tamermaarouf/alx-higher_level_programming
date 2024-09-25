#!/usr/bin/python3
'''Write a class MyList that inherits from list:'''


class MyList(list):
    def __init__(self):
        self.__new_list = []
    
    def append(self, item):
        super().append(self._validate_number(item))

    def print_sorted(self):
        self.__new_list = self.copy()
        self.__new_list.sort()
        print(self.__new_list)

    def _validate_number(self, value):
        if isinstance(value, int):
            return value
        raise TypeError(
            f"numeric value expected, got {type(value).__name__}"
        )
