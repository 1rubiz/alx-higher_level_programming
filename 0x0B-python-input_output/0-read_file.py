#!/usr/bin/python3
"""File reading program"""


def read_file(filename=""):
    """Function that reads a file to stdout"""
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
