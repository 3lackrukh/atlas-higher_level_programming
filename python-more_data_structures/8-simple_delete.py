#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    keys = sorted(a_dictionary.keys())
    for i in keys:
        if i == key:
            del a_dictionary[key]
    return a_dictionary
