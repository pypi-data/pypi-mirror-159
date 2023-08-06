#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=E0401
"""
Collections of methods for digital signal processing.
"""

import logging
import numpy as np
import scipy.sparse as sp

logger = logging.getLogger(__name__)


def time_shift(data, tau, fs, order=31):
    """Shift data in time by tau

    Args:
        data (np.ndarray): data to be shited
        tau (np.ndarray): amount of time each data point is to be shifted
                            (must be of same dimension as data)
        fs (double): sampling frequency in (Hz)
        order (int): interpolation order
    """
    logger.debug("Time shifting data '%s' by '%s' (fs=%f, order=%d)", data, tau, fs, order)

    data = np.asarray(data)
    mode = "timeseries" if isinstance(tau, np.ndarray) else "constant"
    logger.debug("Using mode '%s'", mode)

    if mode == "timeseries" and data.size != tau.size:
        raise ValueError(f"`data` and `tau` must be of the same size (got {data.size}, {tau.size})")

    num_tabs = order + 1
    p = num_tabs // 2 # pylint: disable=invalid-name
    size = data.size

    def lagrange_coeffs(eps):
        """Calculate coefficients for lagrange interpolation"""
        coeffs = np.zeros([num_tabs, eps.size])

        if p > 1:
            factor = np.ones(eps.size, dtype=np.float64)
            factor *= eps * (1 - eps)

            for j in range(1, p):
                factor *= (-1) * (1 - j / p) / (1 + j / p)
                coeffs[p - 1 - j] = factor / (j + eps)
                coeffs[p + j] = factor / (j + 1 - eps)

            coeffs[p - 1] = 1 - eps
            coeffs[p] = eps

            for j in range(2, p):
                coeffs *= 1 - (eps / j)**2

            coeffs *= (1 + eps) * (1 - eps / p)
        else:
            coeffs[p - 1] = 1 - eps
            coeffs[p] = eps

        return coeffs.T

    k = np.floor(tau * fs).astype(int)
    eps = tau * fs - k
    coeffs = lagrange_coeffs(eps)
    logger.debug("Using Lagrange coefficiens '%s'", coeffs)

    if mode == "timeseries":
        logger.debug("Computing Lagrange matrix")
        indices = np.arange(size)
        i_min = np.min(k - (p - 1) + indices)
        i_max = np.max(k + p + indices + 1)
        csr_ind = np.tile(np.arange(num_tabs), size) + np.repeat(k + indices, num_tabs) - (p - 1)
        csr_ptr = num_tabs * np.arange(size + 1)
        mat = sp.csr_matrix((np.ravel(coeffs), csr_ind - i_min, csr_ptr), shape=(size, i_max - i_min))
        logger.debug("Padding data (left=%d, right=%d)", max(0, -i_min), max(0, i_max - size))
        data_padded = np.pad(data[max(0, i_min):min(size, i_max)], (max(0, -i_min), max(0, i_max - size)))
        logger.debug("Computing matrix-vector product")
        shifted = mat.dot(data_padded)
    elif mode == "constant":
        i_min = k - (p - 1)
        i_max = k + p + size
        logger.debug("Padding data (left=%d, right=%d)", max(0, -i_min), max(0, i_max - size))
        data_padded = np.pad(data[max(0, i_min):min(size, i_max)], (max(0, -i_min), max(0, i_max - size)))
        logger.debug("Computing correlation product")
        shifted = np.correlate(data_padded, coeffs[0], mode="valid")

    return shifted

def calculate_advancements(delays, fs, order=5, delta=1e-12, maxiter=10):
    """Calculates advancements from delays.

    This is done by iteratively solving the following expression for a_ij(t).

        a_ij(t) = d_ji(t + a_ij(t)),

    with d_ji(t) being the associated delay.

    Args:
        delays (np.ndarray): time series of delays
        fs (double): sampling frequency
        order (int): order of interpolation
        delta (float): allowed root mean-square (RMS) error between two successive iterations
        max_iter (int): maximum number of iterations
    """
    logger.info("Computing advancements from delays, solving for implicit equation")
    logger.debug("Computing advancements for delays '%s' (fs=%f, order=%d, delta=%f, maxiter=%d)",
        delays, fs, order, delta, maxiter)

    advancements = delays.copy()
    delta2 = delta**2
    mean_squared_error = delta2


    count = 0
    while mean_squared_error >= delta2:
        logger.debug("Computing iteration %d", count + 1)
        if count >= maxiter:
            logger.warning("Maximum number of iterations %d reached, returning current advancement", maxiter)
            break
        advancements_prev = advancements
        advancements = time_shift(delays, advancements_prev, fs, order=order)
        advancement_max = np.max(advancements_prev)
        num_tabs = order + 1
        k_max = int(advancement_max * fs)
        cut_start = max(-(k_max + 1) + num_tabs // 2, 0)
        cut_end = k_max + num_tabs // 2
        difference = (advancements - advancements_prev)[cut_start:-cut_end]
        mean_squared_error = np.mean(difference**2)
        logger.debug("Mean squared error of iteration %d: '%f' (aim at %f)", count + 1, mean_squared_error, delta2)
        count += 1

    return advancements
