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
Defines TDI first-and-second-generation Michelson variables.
"""

from . import core
from . import intervar


# X1, Y1, Z1 (first-generation Michelson) – reduce laser noise
X1_ETA = core.LISATDICombination.from_string('13121 -13121')
Y1_ETA = X1_ETA.rotated()
Z1_ETA = Y1_ETA.rotated()

X1 = X1_ETA @ intervar.ETA_SET
Y1 = Y1_ETA @ intervar.ETA_SET
Z1 = Z1_ETA @ intervar.ETA_SET

# X2, Y2, Z2 (second-generation Michelson) – reduce laser noise
X2_ETA = core.LISATDICombination.from_string('131212131 -121313121')
Y2_ETA = X2_ETA.rotated()
Z2_ETA = Y2_ETA.rotated()

X2 = X2_ETA @ intervar.ETA_SET
Y2 = Y2_ETA @ intervar.ETA_SET
Z2 = Z2_ETA @ intervar.ETA_SET
