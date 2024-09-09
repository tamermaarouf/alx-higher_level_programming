#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for elem in range(x):
            if count == x:
                print('f'.format(my_list[elem]))
            else:
                print('{}'.format(my_list[elem]), end='')
                #raise IndexError
            count += 1
        print()
        return (count)
    except IndexError:
        print()
        return (count)
