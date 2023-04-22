#!/usr/bin/python3
"""
Defines a string-to-JSON functions
"""

import json


def save_to_json_file(my_obj):
    """Object to a text file, using a JSON representation"""
    with open(filename, 'w', encoding='utf=8') as f:
        return.dump(my_obj, f)
