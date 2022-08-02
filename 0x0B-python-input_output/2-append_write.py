#!/usr/bin/python3
"""module with the appending function"""


def append_write(filename="", text=""):
    """function that append the text to the end of the file"""
    with open(filename, "a", encoding="utf-8"):
        return f.write(text)
