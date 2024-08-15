#!/usr/bin/python3
"""Python Interview question on solving 2D Matrix"""


def rotate_2d_matrix(matrix):
    """Rotates a 2D matrix 90 degrees clockwise."""
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for row in matrix:
        row.reverse()
