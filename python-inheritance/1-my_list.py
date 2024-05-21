#!/usr/bin/python3
"""
    Module extends utility of the list class.
    Adds sorted print method.
"""

class MyList(list):
    """
        sub-class of list

        Attributes:
            Inherits attributes and methods from list class.

        Returns: None
    """
    def print_sorted(self):
        """
            prints the list in ascending sort order.
            Utilizes the sorted() function.

            Pure method does not change the list

        """
        print(sorted(self))