#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < len(my_list) and idx >= 0:
        value = my_list[idx]
        my_list.remove(value)
    return my_list
