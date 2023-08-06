#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Defines TDI first-and-second-generation Michelson variables.
"""

from . import core
from . import intervar


# X1, Y1, Z1 (first-generation Michelson) – reduce laser noise
X1_ETA = core.LISATDICombination({
    "eta_12": [
        (-1, []),
        (1, ['D_13', 'D_31'])],
    "eta_31": [
        (1, ['D_13']),
        (-1, ['D_12', 'D_21', 'D_13'])],
    "eta_13": [
        (1, []),
        (-1, ['D_12', 'D_21'])],
    "eta_21": [
        (-1, ['D_12']),
        (1, ['D_13', 'D_31', 'D_12'])],
})
Y1_ETA = X1_ETA.rotated()
Z1_ETA = Y1_ETA.rotated()

X1 = X1_ETA @ intervar.ETA_SET
Y1 = Y1_ETA @ intervar.ETA_SET
Z1 = Z1_ETA @ intervar.ETA_SET

# X2, Y2, Z2 (second-generation Michelson) – reduce laser noise
X2_ETA = core.LISATDICombination({
    "eta_12": [
        (-1, []),
        (1, ['D_13', 'D_31']),
        (1, ['D_13', 'D_31', 'D_12', 'D_21']),
        (-1, ['D_12', 'D_21', 'D_13', 'D_31', 'D_13', 'D_31'])],
    "eta_31": [
        (1, ['D_13']),
        (-1, ['D_12', 'D_21', 'D_13']),
        (-1, ['D_12', 'D_21', 'D_13', 'D_31', 'D_13']),
        (1, ['D_13', 'D_31', 'D_12', 'D_21', 'D_12', 'D_21', 'D_13'])],
    "eta_13": [
        (1, []),
        (-1, ['D_12', 'D_21']),
        (-1, ['D_12', 'D_21', 'D_13', 'D_31']),
        (1, ['D_13', 'D_31', 'D_12', 'D_21', 'D_12', 'D_21'])],
    "eta_21": [
        (-1, ['D_12']),
        (1, ['D_13', 'D_31', 'D_12']),
        (1, ['D_13', 'D_31', 'D_12', 'D_21', 'D_12']),
        (-1, ['D_12', 'D_21', 'D_13', 'D_31', 'D_13', 'D_31', 'D_12'])],
})
Y2_ETA = X2_ETA.rotated()
Z2_ETA = Y2_ETA.rotated()

X2 = X2_ETA @ intervar.ETA_SET
Y2 = Y2_ETA @ intervar.ETA_SET
Z2 = Z2_ETA @ intervar.ETA_SET
