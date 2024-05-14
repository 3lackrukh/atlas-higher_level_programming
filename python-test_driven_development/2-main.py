#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
    [0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0]
]
print(matrix_divided(matrix, (float('inf'))))
print(matrix)
