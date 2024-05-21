#!/usr/bin/python3
"""
    This module contains a method which
    writes a string to a text file
    and returns the number of characters written.
"""


def write_file(filename="", text=""):
    """
        Parameters:
            filename (str): the name of the file to write to.
            text (str): the text to be written to the file.
    
        Returns:
            char_ct (int): the number of characters written.
    """
    char_ct = len(text)
    with open(filename, "w") as f:
        f.write(text)
    return char_ct
