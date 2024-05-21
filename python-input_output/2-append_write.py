#!/usr/bin/python3
"""
    This module contains a method which
    appends a string to the end of a text file.
"""
def append_write(filename="", text=""):
    """
        Parameters:
            filename (str): the name of the file to write to.
            text (str): the text to be written to the file.

        Returns:
            char_ct (int): the number of characters written.
    """
    char_ct = len(text)
    with open(filename, "a") as f:
        f.write(text)
    return char_ct