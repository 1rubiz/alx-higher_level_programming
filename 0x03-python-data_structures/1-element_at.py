#!/usr/bin/python3


def element_at(my_list, idx):
    length = len(my_list)
    value = my_list[idx]

    for i in range(length):
        if idx < 0:
            return None
        elif idx > length:
            return None
        else:
            return value
