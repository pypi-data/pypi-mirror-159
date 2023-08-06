#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Collections of methods for naming.
"""

import itertools

def split_indices(string):
    """Returns a tuple containing the variable name and both indices"""
    name, indices = string.split("_")
    return name, int(indices[0]), int(indices[1])

def join_indices(name, i, j):
    """Returns a tuple containing the variable name and both indices"""
    indices = "".join([str(i), str(j)])
    return "_".join([name, indices])

def lisa_indices():
    """Retutns an iterator over LISA double indices"""
    return itertools.permutations([1, 2, 3], 2)
