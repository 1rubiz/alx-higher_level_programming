#!/usr/bin/python3


def no_c(my_string):
    sub = {67: 32, 99: 32}
    newStr = my_string.translate(sub)
    return newStr
