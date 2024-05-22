#!/usr/bin/python3
"""
    This module defines the method pascal_triangle which
    returns a matrix of integers
    representing a pascal's triangle of n
"""


def pascal_triangle(n):
    """
        Parameters:
            - n (int) the height of matrix to return.
        Returns:
            - matrix (list of lists) of integers representing
            pascal's triangle.
    """
    matrix = []

    for i in range(n):
        lvl = []
        matrix.append(lvl)
        for k in range(i + 1):
            if k == 0 or k == i:
                lvl.append(1)
            else:
                lvl.append(matrix[i - 1][k] + matrix[i - 1][k - 1])
    return matrix
