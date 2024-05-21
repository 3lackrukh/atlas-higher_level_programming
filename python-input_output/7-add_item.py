#!/usr/bin/python3
"""
    This module adds input arguments to a JSON file.

    Employs the following modules:
        - sys for reading command line arguments
        - save_to_json_file for writing to JSON files
        - load_from_json_file to read from JSON files
"""
import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


filename = "add_item.json"
arg_list = []
try:
    arg_list = load_from_json_file(filename)
except FileNotFoundError:
    pass
for i in range(1, len(sys.argv)):
    arg_list.append(sys.argv[i])
save_to_json_file(arg_list, filename)
