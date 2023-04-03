#!/usr/bin/python3
"""
This is a function that finds a peak in a list of unsorted integers.
"""
def find_peak(list_of_integers):
    """ Searches for and returns a peak value in a list"""
    if len(list_of_integers) == 0:
        return
    if type(list_of_integers).__name__ != "list":
        return

    peak = list_of_integers[0]
    a = 0
    b = -1

    while a < len(list_of_integers) / 2:
        if list_of_integers[b] <= list_of_integers[a]:
            tmp = list_of_integers[a]
        else:
            tmp = list_of_integers[b]

        if tmp >= peak:
            peak = tmp
        a += 1
        b -= 1
    list_of_integers.sort()
    return list_of_integers[-1]
