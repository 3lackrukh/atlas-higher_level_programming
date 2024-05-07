#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    ln = 0
    try:
        for i in range(x):
            print(my_list[i], end='')
            ln += 1
    except IndexError:
        pass
    print()
    return ln
