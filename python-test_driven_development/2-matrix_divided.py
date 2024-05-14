#!/usr/bin/python3
"""
Module for the matrix_divided method.
"""


def matrix_divided(matrix, div):
    """
    divides a matrix of integers by a specified divisor
    
    Parameters:
        matrix: a matrix of type int or float
        div: a divisor of type int or float

    Raises:
        TypeError: if any element of matrix is not of type int or float
        TypeError: if the rows of the matrix are not the same size
        TypeError: if div is not of type int or float
        ZeroDivisionError: if divisor is 0

    Returns:
        a new matrix containing the results of division

    """
    if (not isinstance(matrix, list) or
        not all(isinstance(row, list) for row in matrix) or 
        not all(len(row) > 0 for row in matrix) or
        not all(isinstance(i, (int, float))for row in matrix for i in row)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    lengths = []
    for row in matrix:
        lengths.append(len(row))
    if not all(value == lengths[0] for value in lengths):
        raise TypeError("Each row of the matrix must have the same size")
    
    matrix_d = [[round(i / div, 2)for i in row] for row in matrix]

    return matrix_d
