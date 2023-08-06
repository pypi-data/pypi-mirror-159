#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2020, by the California Institute of Technology. ALL RIGHTS RESERVED.
# United States Government Sponsorship acknowledged. Any commercial use must be
# negotiated with the Office of Technology Transfer at the California Institute of Technology.
#
# This software may be subject to U.S. export control laws. By accepting this software,
# the user agrees to comply with all applicable U.S. export laws and regulations.
# User has the responsibility to obtain export licenses, or other export authority
# as may be required before exporting such information to foreign countries or
# providing access to foreign persons.
#
# Copyright 2021, by the Max Planck Institute for Gravitational Physics
# (Albert Einstein Institute). ALL RIGHTS RESERVED.
#
# The previous copyrights only apply to the respective contributions of the authors,
# as determined by the Git history of the project.
#
"""
Collections of methods for naming.
"""

import itertools

def split_indices(string):
    """Returns a tuple containing the variable name and both indices."""
    name, indices = string.rsplit('_', 1)
    return name, int(indices[0]), int(indices[1])

def join_indices(name, i, j):
    """Returns a tuple containing the variable name and both indices."""
    return f'{name}_{i}{j}'

def lisa_indices():
    """Returns an iterator over LISA double indices."""
    return itertools.permutations([1, 2, 3], 2)
