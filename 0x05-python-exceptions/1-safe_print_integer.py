<<<<<<< HEAD
#!/bin/bash/python3

def safe_print_integer(value);
try:
print("{:d}".format(value))
return (True)
except(TypeError, ValueError);
return (False)
=======
#!/usr/bin/python3


def safe_print_integer(value):
    """Print an integer with "{:d}".format().

    Args:
        value (int): The integer to print.

    Returns:
        If a TypeError or ValueError occurs - False.
        Otherwise - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)

>>>>>>> b0203d7989c3251a49a6f434a773a08a5675cf8b
