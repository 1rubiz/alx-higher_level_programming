#!/usr/bin/python3
"""module for json conversion to obj"""
import json


def from_json_string(my_obj):
    """function returns the json rep of the object"""
    return json.dumps(my_obj)
