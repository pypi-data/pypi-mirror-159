'''

This module provides ways to sort a python dictionary
Dictionary could be sorted by keys or by values

'''

def bykeys(x: dict) -> dict:
    val = {k:x[k] for k in sorted(x, key=lambda y:y)}
    return val


def byvalues(x: dict) -> dict:
    val = {k: x[k] for k in sorted(x, key=lambda y: x[y])}
    return val

