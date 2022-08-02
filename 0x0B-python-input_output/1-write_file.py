#!/usr/bin/python3
"""a module that writes into a file and returns the num"""


def write_file(filename="", text=""):
    """function that writes into a file"""
    num = 0
    with open(filename, "r+", encoding="utf-8") as f:
        f.write(text)
        for i in f:
            num += 1
        return num
