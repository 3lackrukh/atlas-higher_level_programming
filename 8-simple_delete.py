#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    for ky, val in a_dictionary.items():
        if val == key:
            del a_dictionary[ky]
    return a_dictionary
