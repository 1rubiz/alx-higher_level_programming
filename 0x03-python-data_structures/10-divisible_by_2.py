#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    new_list = []
    for x in my_list:
        y = True
        if x % 2 == 0:
            new_list.append(y)
        else:
            y = False
            new_list.append(y)

    return new_list
