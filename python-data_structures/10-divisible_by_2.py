#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    i = 0
    new_list = []
    while i < len(my_list):
        if my_list[i] % 2 == 0:
            new_list.append(1)
        else:
            new_list.append(0)
        i += 1
    return new_list
