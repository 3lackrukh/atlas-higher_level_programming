#!/usr/bin/python3

"""
Module for the text_indentation method
"""


def text_indentation(text):

    """
    Prints a text with 2 new lines after each of the following chars
    '.' '?' ':'

    Parameters:
        Text (str): A string of chars to be formatted and printed.

    Raises:
        TypeError: if text is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    skip = False

    for i in text:
        if i in (".", "?", ":"):
            print(i + "\n\n", end="")
            skip = True
        elif skip:
            continue
        else: 
            print(i, end="")
        skip = False