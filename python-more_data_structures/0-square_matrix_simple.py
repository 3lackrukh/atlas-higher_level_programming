#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    def square(x):
        return x ** 2
    new_matrix = [list(map(square, row)) for row in matrix]
    return new_matrix
