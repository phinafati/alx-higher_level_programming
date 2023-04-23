#!/usr/bin/python3
"""
Python Module created by Phina
"""
import json


def save_to_json_file(my_obj, filename):
    """
    function to save file to objects
    Arguments:
    my_obj (obj): The inputed object to convert in json format
        filename (str): The name of the output file
        return:
        A file with a text in json format
        """
        with open(filename, 'w', encoding='utf=8') as my_file:
            return my_file.write(json.dumps(my_obj))
