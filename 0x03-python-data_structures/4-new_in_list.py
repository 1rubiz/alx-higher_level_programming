#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    temp = my_list.copy()
    length = len(my_list)

    if idx < 0:
        return my_list
    if idx > (length - 1):
        return my_list
    else:
        temp[idx] = element
        return temp
