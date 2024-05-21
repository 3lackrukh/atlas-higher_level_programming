#!/usr/bin/python3
"""
    This module reads and prints the contents of a file.
"""


def read_file(filename=""):
    """
        This method reads a file line-by-line,
        prints each line, and closes the file.
    """
    with open(filename, "r") as f:
        f_cont = f.read()
        print(f_cont, end="")
