#!/usr/bin/python3


def replace_in_list(my_list, idx, element):
    length = len(my_list)
    value = my_list[idx]

    if idx < 0:
        return my_list
    elif idx > length:
        return my_list
    else:
        value = element
        return my_list
