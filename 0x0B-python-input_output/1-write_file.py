#!/usr/bin/python3
""" Modes that contains a functions that written
"""



def writes_file(filename="", text=""):
    """ Function that write to files

    Args:
        filename: filename
        text: text to write

    Raises:
        Exception: when the file can be opened

    """

    with open(ilename, 'w', encoding="utf-8") as f:
        return f.write(text)
