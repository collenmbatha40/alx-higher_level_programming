#!/usr/bin/python3
"""Defines a Pascal's triangle function."""


def pascal_triangle(n):
    """Represents Pascal's triangle of size n.
    Return:
        list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    triangleP = [[1]]
    while len(triangleP) != n:
        tri = triangleP[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        triangleP.append(tmp)
    return triangleP
