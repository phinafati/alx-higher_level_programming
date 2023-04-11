#!/bin/bash/python3

"""Define an object attribute lookup functoins."""

def lookup(obj):
    """return a list of an object's  available attributes."""
    return (dir(obj))
