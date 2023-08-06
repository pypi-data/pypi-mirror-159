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
Defines TDI intermediary variables ξ (xi) and η (eta).
"""

from . import core


# ξ (xi) – reduce spacecraft jitter
XI_12 = core.LISATDICombination({
    "isc_12": [(1.0, [])],
    "ref_12": [(0.5, [])],
    "ref_21": [(0.5, ['D_12'])],
    "tm_12": [(-0.5, [])],
    "tm_21": [(-0.5, ['D_12'])],
})
XI_23 = XI_12.rotated()
XI_31 = XI_23.rotated()

XI_13 = XI_12.reflected(1)
XI_21 = XI_23.reflected(2)
XI_32 = XI_31.reflected(3)

XI_SET = {
    "xi_12": XI_12, "xi_23": XI_23, "xi_31": XI_31,
    "xi_13": XI_13, "xi_21": XI_21, "xi_32": XI_32,
}

# η (eta) – reduce to three lasers
ETA_12_XI = core.LISATDICombination({
    "xi_12": [(1.0, [])],
    "ref_23": [(-0.5, ['D_12'])],
    "ref_21": [(0.5, ['D_12'])],
}, allow_reflections=False)
ETA_23_XI = ETA_12_XI.rotated()
ETA_31_XI = ETA_23_XI.rotated()

ETA_13_XI = core.LISATDICombination({
    "xi_13": [(1.0, [])],
    "ref_12": [(0.5, [])],
    "ref_13": [(-0.5, [])],
}, allow_reflections=False)
ETA_21_XI = ETA_13_XI.rotated()
ETA_32_XI = ETA_21_XI.rotated()

ETA_XI_SET = {
    "eta_12": ETA_12_XI, "eta_23": ETA_23_XI, "eta_31": ETA_31_XI,
    "eta_13": ETA_13_XI, "eta_21": ETA_21_XI, "eta_32": ETA_32_XI,
}

ETA_SET = {
    "eta_12": ETA_12_XI @ XI_SET, "eta_23": ETA_23_XI @ XI_SET, "eta_31": ETA_31_XI @ XI_SET,
    "eta_13": ETA_13_XI @ XI_SET, "eta_21": ETA_21_XI @ XI_SET, "eta_32": ETA_32_XI @ XI_SET,
}
