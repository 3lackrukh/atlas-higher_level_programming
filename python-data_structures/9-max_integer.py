#!/usr/bin/python3
def max_integer(my_list=[]):
    Mac = 0
    for i in my_list:
        if i > Mac:
            Mac = i
    return Mac
