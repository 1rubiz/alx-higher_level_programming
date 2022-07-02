#!/usr/bin/python3


def element_at(my_list, idx):
    length = len(my_list)
    value = my_list[idx]

    if idx < 0:
        return None
    elif idx > length:
        return None
    else:
        return value
