#!/usr/bin/python3
"""Module that contain a functions reads from iles


def read_file(filename="""):
    """ Function that reds from a file

    Args:
    filename: filename

    Raises
    Exception: when the file can be opened

    """

    with open(filename, 'r', encording="uft-8") as f:
        read_data = f.read()
        print(read_data, end='')
