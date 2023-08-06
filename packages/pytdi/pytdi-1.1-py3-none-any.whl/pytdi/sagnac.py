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
Defines TDI first-and-second-generation Sagnac variables.
"""

from . import core
from . import intervar


# ɑ1, β1, ɣ1 (first-generation Sagnac) – reduce laser noise
ALPHA1_ETA = core.LISATDICombination.from_string('1321 -1321')
BETA1_ETA = ALPHA1_ETA.rotated()
GAMMA1_ETA = BETA1_ETA.rotated()

ALPHA1 = ALPHA1_ETA @ intervar.ETA_SET
BETA1 = BETA1_ETA @ intervar.ETA_SET
GAMMA1 = GAMMA1_ETA @ intervar.ETA_SET

# ζ1 (first-generation symmetric Sagnac) – reduce laser noise
ZETA1_ETA = core.LISATDICombination({
    'eta_12': [(1, ['D_23'])],
    'eta_23': [(1, ['D_31'])],
    'eta_31': [(1, ['D_12'])],
    'eta_13': [(-1, ['D_32'])],
    'eta_32': [(-1, ['D_21'])],
    'eta_21': [(-1, ['D_13'])],
})

ZETA1 = ZETA1_ETA @ intervar.ETA_SET

# ɑ2, β2, ɣ2 (second-generation Sagnac) – reduce laser noise
ALPHA2_ETA = core.LISATDICombination.from_string('1231321 -1321231')
BETA2_ETA = ALPHA2_ETA.rotated()
GAMMA2_ETA = BETA2_ETA.rotated()

ALPHA2 = ALPHA2_ETA @ intervar.ETA_SET
BETA2 = BETA2_ETA @ intervar.ETA_SET
GAMMA2 = GAMMA2_ETA @ intervar.ETA_SET

# ζ21, ζ22, ζ23 (second-generation symmetric Sagnac) – reduce laser noise
ZETA21_ETA = core.LISATDICombination({
    'eta_12': [(1, ['D_23', 'D_32']), (-1, ['D_13', 'D_21', 'D_32'])],
    'eta_23': [(1, ['D_32', 'D_13']), (-1, ['D_12', 'D_31', 'D_13'])],
    'eta_31': [(1, ['D_23', 'D_12']), (-1, ['D_13', 'D_21', 'D_12'])],
    'eta_13': [(1, ['D_12', 'D_31', 'D_23']), (-1, ['D_32', 'D_23'])],
    'eta_32': [(1, ['D_13', 'D_21', 'D_12']), (-1, ['D_23', 'D_12'])],
    'eta_21': [(1, ['D_12', 'D_31', 'D_13']), (-1, ['D_32', 'D_13'])],
})
ZETA22_ETA = ZETA21_ETA.rotated()
ZETA23_ETA = ZETA22_ETA.rotated()

ZETA21 = ZETA21_ETA @ intervar.ETA_SET
ZETA22 = ZETA22_ETA @ intervar.ETA_SET
ZETA23 = ZETA23_ETA @ intervar.ETA_SET
