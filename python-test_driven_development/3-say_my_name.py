#!/usr/bin/python3
"""
Module for the say_my_name module
"""


def say_my_name(first_name, last_name=""):
    """
    concatenates str parameters into the string
    'My name is <first name> <last name>'

    Parameters:
        first_name(str): the first name to be concatenated
        last_name(str, optional): last name to be concatenated. Default "".

        Raises:
            TypeError: if either parameter is not of type str.
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if last_name:
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is {} ".format(first_name))
