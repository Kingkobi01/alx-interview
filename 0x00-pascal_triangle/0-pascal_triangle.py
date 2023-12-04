#!/usr/bin/python3
"""A module for working with Pascal's triangle.
"""


def pascal_triangle(n):
    """Creates a list of lists of integers representing
    the Pascal's triangle of a given integer.
    """
    triangle = []
    if n <= 0:
        return triangle
    triangle.append([1])
    if n == 1:
        return triangle

    for _ in range(n - 1):
        padded_previous_row = [0] + triangle[-1] + [0]

        current_row = []
        for idx in range(len(triangle[-1]) + 1):
            new_value = padded_previous_row[idx] + padded_previous_row[idx + 1]
            current_row.append(new_value)
        triangle.append(current_row)

    return triangle
