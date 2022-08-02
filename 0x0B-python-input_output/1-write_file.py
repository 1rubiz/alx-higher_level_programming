#!/usr/bin/python3
"""a module that writes into a file and returns the num"""


def write_file(filename="", text=""):
    """function that writes into a file"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
