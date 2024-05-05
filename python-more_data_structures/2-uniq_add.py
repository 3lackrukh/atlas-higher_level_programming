#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    seen = set()
    for i in my_list:
        if i not in seen:
            result += i
            seen.add(i)
    return result
