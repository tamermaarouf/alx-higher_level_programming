#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0
        for elem in range(x):
            if count == x:
                print('{:d}'.format(my_list[elem]))
            else:
                if isinstance(my_list[elem], int):
                    print('{:d}'.format(my_list[elem]), end='')
            count += 1
        print()
        return (count)
    except ValueError:
        print()
        return (count)
