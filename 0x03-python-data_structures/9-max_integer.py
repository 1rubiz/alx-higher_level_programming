#!/usr/bin/python3


def max_integer(my_list=[]):
    x = sorted(my_list)
    length = len(x) - 1
    return x[length]
