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
Defines first and second-generation quasi-orthogonal combinations (A, E, and T).

We follow the LISA Data Challenge (LDC) conventions given in [1].

[1] LISA Data Challenge Manual (LISA-LCST-SGS-MAN-001),
    https://atrium.in2p3.fr/19ea417c-dd9e-4e2b-a0b1-9c887ed01a42

"""

from numpy import sqrt
from .michelson import X1, Y1, Z1, X2, Y2, Z2


# A1, E1, T1 (first-generation orthogonal combinations)
A1_RAW = (Z1 - X1) / sqrt(2)
E1_RAW = (X1 - 2 * Y1 + Z1) / sqrt(6)
T1_RAW = (X1 + Y1 + Z1) / sqrt(3)

# A2, E2, T2 (second-generation orthogonal combinations)
A2_RAW = (Z2 - X2) / sqrt(2)
E2_RAW = (X2 - 2 * Y2 + Z2) / sqrt(6)
T2_RAW = (X2 + Y2 + Z2) / sqrt(3)

# Simplified versions
A1, A2 = A1_RAW.simplified(), A2_RAW.simplified()
E1, E2 = E1_RAW.simplified(), E2_RAW.simplified()
T1, T2 = T1_RAW.simplified(), T2_RAW.simplified()
