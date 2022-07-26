#!/usr/bin/python3
"""
Class locking procedure
"""


class LockedClass:
    """ Prevents user to create new attributes except firstname"""
    __slots__ = ['first_name']

    def __init__(self, name=""):
        self.first_name = name
