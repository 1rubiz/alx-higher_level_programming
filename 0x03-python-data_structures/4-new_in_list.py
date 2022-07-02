#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    temp = my_list.copy()
    length = len(my_list)
    value = temp[idx]

    if idx < 0:
        return my_list
    if idx > length:
        return my_list
    else:
        temp[idx] = element
        return temp
