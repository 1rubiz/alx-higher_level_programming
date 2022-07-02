#!/usr/bin/python3


def max_integer(my_list=[]):
    if (len(my_list) - 1) < 0:
        return None
    x = sorted(my_list)
    length = len(x) - 1
    return x[length]
