#!/usr/bin/python3


def element_at(my_list, idx):
    length = len(my_list)
    value = my_list[idx]

    for i in range(length):
        if idx < 0 or idx > length:
            return None
        elif idx == i:
            return value
