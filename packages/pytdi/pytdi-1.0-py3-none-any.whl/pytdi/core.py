#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Defines the core class `TDICombination`, used to build combinations.

Authors:
    Martin Staab <martin.staab@aei.mpg.de>
    Jean-Baptiste Bayle <jbayle@jpl.nasa.gov>
"""

import copy
import itertools
import logging
import numpy as np
from . import dsp
from . import naming

logger = logging.getLogger(__name__)


class TDICombination():
    """Defines a time-delay interferometry (TDI) combination.

    A combination is defined as a sum of time-shift operator polynomials applied on measurements.
    Measurements are defined by their names and their time series, represented by arrays of sampled values.
    Time-shift operator polynomials are linear combinations of chained time-shift operators, e.g., the sum
    of terms containing a constant scalar factor (called "factor"), and the mathematical composition of
    time-shift operators (the "chaining" or "nesting" of time-shift operators).

    Time-shift operators come in two flavours:

        * delay operators `D_ij`, associated with delay `d_ij`, defined as: D_ij x(t) = x(t - d_ij(t))
        * advancement operators `A_ij`, associated with advancement `a_ij`, defined as:
          A_ij x(t) = x(t + a_ij(t)), and such that A_ij D_ji = D_ij A_ji = 1.

    Use the `build()` method to apply the combination to a given set of measurements and delays.
    Advancements are computed by solving iteratively the equation A_ij D_ji x(t) = x(t), i.e.,
    a_ij(t) = d_ji(t + a_ij(t)).

    TDI combinations support summation, subtraction, multiplication, and composition (`@` operator).
    """
    def __init__(self, components):
        """Initialize a time-delay interferometry combination.

        Pass a dictionary containing the measurement names as keys, and time-shift polynomials as values.
        Time-shift polynomials are defined as a list of couples `(factor, operators)`, where `factor` is
        the scalar factor, and `operators` is a list of nested time-shift operators, i.e.,

            >>> mytdi = TDICombination({
                'y_12': [(1, ['D_12', 'D_23']), (-1, ['A_12'])],
                'y_21': [(0.5, ['A_23', 'D_23'])],
            })

        Delay operators are represented by the string `D_ij`, where `i` and `j` are indices, and
        advancement operators by `A_ij`.

        Args:
            components (dict): dictionary defining the combination
        """
        logger.info("Initializing combination with components '%s'", components)
        self.components = dict(components)

    @property
    def delays(self):
        """Return the set of all delay operators in the combination."""
        delays = set()
        for polynomial in self.components.values():
            for _, operators in polynomial:
                for operator in operators:
                    name, _, _ = naming.split_indices(operator)
                    if name == "D":
                        delays.add(operator)
        return delays

    @property
    def advancements(self):
        """Return the set of all advancement operators in the combination."""
        advancements = set()
        for polynomial in self.components.values():
            for _, operators in polynomial:
                for operator in operators:
                    name, _, _ = naming.split_indices(operator)
                    if name == "A":
                        advancements.add(operator)
        return advancements

    def build(self, measurements, delays, fs, delay_derivatives=None, order=(31, 5), delta=1e-12, maxiter=10):
        """Apply the combination to a set of measurements and delays.

        This function computes the actual combination given a set of measurements and delays, e.g.,

            >>> mytdi.build(
                {'y_12': y12_array,'y_21': y21_array},
                {'d_12': t12_array, 'd_21': t21_array},
            )

        If any advancement operators are used in the combination, they are computed iteratively.
        Then measurements are time-shifted accordingly, and time-shift polynomials are formed.
        The sum of all terms is returned.

        Args:
            measurements (dict): dictionary of measurements
            delays (dict): dictionary of delays, in s
            fs (double): sampling frequency, in Hz
            delay_derivative: dictionary of delay time derivatives, in s/s
            order (int or tuple): Lagrange interpolation orders, either a tuple (meas, delay) for
                measurement and delay interpolations, or an integer for both interpolations
            delta (float): allowed timing accuracy for advancements calculation
            maxiter (int): maximum iterations for advancements calculation
        """
        # pylint: disable=R0914,R0912,R0915
        logger.info("Building combination '%s'", self)

        # Convert `order` to couple of integers
        if isinstance(order, (int, float)):
            order = (int(order), int(order))
        elif isinstance(order, tuple) and len(order) == 2:
            order = (int(order[0]), int(order[1]))
        else:
            raise ValueError(f"Invalid order '{order}', must be integer or couple of integers.")
        logger.debug("Using interpolation orders '%d' for measurement, '%d' for delays", order[0], order[1])

        # Check that all measurements have same length
        size = None
        for measurement in measurements.values():
            if size is None:
                size = measurement.size
            elif size != measurement.size:
                raise ValueError("Inconsistent data size, all must be of the same size.")
        logger.debug("Measurements have size '%d'", size)

        # Check the size of the delays
        for name, delay in delays.items():
            if isinstance(delay, np.ndarray) and delay.size != size:
                raise ValueError(f"Inconsistent size for delay '{name}': got {delay.size}, expected {size}.")
        logger.debug("Delays have size '%d'", size)

        # Check the size of the delay derivatives
        if delay_derivatives is not None:
            for name, delay_derivative in delay_derivatives.items():
                if isinstance(delay_derivative, np.ndarray) and delay_derivative.size != size:
                    raise ValueError(f"Inconsistent size for delay derivatives '{name}': "
                                     f"got {delay_derivative.size}, expected {size}.")
            logger.debug("Delay derivatives have size '%d'", size)

        shifts = {}
        derivatives = {}
        logger.debug("Computing delays")
        for delay in self.delays:
            logger.debug("Computing delay '%s'", delay)
            _, i, j = naming.split_indices(delay)
            shifts[delay] = -delays[naming.join_indices('d', i, j)]
            if delay_derivatives:
                logger.debug("Computing delay derivative '%s'", delay)
                derivatives[delay] = -delay_derivatives[naming.join_indices('d', i, j)]
        logger.debug("Computing advancements")
        for advancement in self.advancements:
            _, i, j = naming.split_indices(advancement)
            delay = naming.join_indices('d', j, i)
            if np.isscalar(delays[delay]):
                logger.debug("Computing constant advancement '%s'", advancement)
                shifts[advancement] = delays[delay]
            else:
                logger.debug("Computing time-varying advancement '%s'", advancement)
                shifts[advancement] = dsp.calculate_advancements(delays[delay], fs, order[1], delta, maxiter)
            if delay_derivatives is not None and np.isscalar(delay_derivatives[delay]):
                logger.debug("Computing constant advancement derivative '%s'", advancement)
                derivatives[advancement] = delay_derivatives[delay] / (1 - delay_derivatives[delay])
            elif delay_derivatives is not None:
                logger.debug("Computing time-varying advancement derivative '%s'", advancement)
                dotd_advanced = dsp.time_shift(delay_derivatives[delay], shifts[advancement], fs, order[1])
                derivatives[advancement] = dotd_advanced / (1 - dotd_advanced)

        result = np.zeros(size)
        for measurement, polynomial in self.components.items():
            logger.debug("Computing contributions from measurement '%s'", measurement)
            for factor, operators in polynomial:
                logger.debug("Computing term '%s %s' for measurement '%s'", factor, operators, measurement)
                # Compute the global time shift to apply
                shift = 0
                doppler = 1
                for operator in operators:
                    if delay_derivatives is not None and np.isscalar(derivatives[operator]):
                        doppler += derivatives[operator]
                    elif delay_derivatives is not None:
                        doppler += dsp.time_shift(derivatives[operator], shift, fs, order[1])
                    if np.isscalar(shifts[operator]):
                        shift += shifts[operator]
                    else:
                        shift += dsp.time_shift(shifts[operator], shift, fs, order[1])

                # Shift the data, and add it to the result
                result += factor * doppler * dsp.time_shift(measurements[measurement], shift, fs, order[0])
        return result

    def transformed(self, mapping):
        """Return a new combination by applying a transformation.

        A transformation is defined by a mapping of indices, e.g. `{1: 2, 2: 1}`.

        Args:
            mapping (dict): mapping of indices
        """
        def transform_string(string, mapping):
            name, i, j = naming.split_indices(string)
            if i not in mapping:
                raise ValueError(f"Incomplete mapping '{mapping}', should contain index '{i}'.")
            if j not in mapping:
                raise ValueError(f"Incomplete mapping '{mapping}', should contain index '{j}'.")
            i, j = mapping[i], mapping[j]
            return naming.join_indices(name, i, j)

        logger.info("Transforming combination '%s' with mapping '%s'", self, mapping)
        transformed = copy.deepcopy(self)
        transformed.components = {}
        for measurement, polynomial in self.components.items():
            transformed_meas = transform_string(measurement, mapping)
            logger.debug("Transforming measurement '%s' into '%s'", measurement, transformed_meas)
            if transformed_meas in transformed.components:
                raise ValueError(f"Invalid mapping '{mapping}', should be a bijection.")
            transformed.components[transformed_meas] = []
            for factor, operators in polynomial:
                transformed_term = (factor, [transform_string(operator, mapping) for operator in operators])
                logger.debug("Transforming term '%s' into '%s'", operators, transformed_term)
                transformed.components[transformed_meas].append(transformed_term)
        return transformed

    def simplified(self):
        """Return a simplified combination.

        We try to apply the following rules, for each time-shift operator polynomial:

            * drop polynomial if vanishing,
            * drop terms with a vanishing factor,
            * collect terms with identifical time-shift operators with a unique factor,
            * drop delay and advancement operator which cancel out.

        """
        logger.info("Simplifying combination '%s'", self)
        simplified = copy.deepcopy(self)
        for measurement, polynomial in simplified.components.items():
            # Drop variables that are not used
            if not polynomial:
                logger.debug("Empty polynomial for measurement '%s', removing", measurement)
                del simplified.components[measurement]
                return simplified.simplified()
            # Drop term with vanishing factor
            for factor, operators in list(polynomial):
                if not factor:
                    logger.debug("Vanishing factor for term '%s', removing", operators)
                    simplified.components[measurement].remove((factor, operators))
                    return simplified.simplified()
            # Collect terms with identical time-shift operator
            for (factor1, operators1), (factor2, operators2) in itertools.combinations(polynomial, 2):
                if operators1 == operators2:
                    logger.debug("Collecting factors '%s' and '%s' for term '%s'", factor1, factor2, operators1)
                    simplified.components[measurement].remove((factor1, operators1))
                    simplified.components[measurement].remove((factor2, operators2))
                    simplified.components[measurement].append((factor1 + factor2, operators1))
                    return simplified.simplified()
            # Simplify successive delay and advancement operation
            for factor, operators in list(polynomial):
                for i, (operator1, operator2) in enumerate(zip(operators, operators[1:])):
                    name1, i1, j1 = naming.split_indices(operator1)
                    name2, i2, j2 = naming.split_indices(operator2)
                    if (name1, name2) in [("A", "D"), ("D", "A")] and i1 == j2 and j1 == i2:
                        logger.debug("Cancelling operators '%s' and '%s', removing", operator1, operator2)
                        del operators[i + 1]
                        del operators[i]
                        return simplified.simplified()
        return simplified

    def __eq__(self, other):
        return self.components == other.components

    def __ne__(self, other):
        return not self.__eq__(other)

    def __add__(self, other):
        if not isinstance(other, TDICombination):
            TypeError(f"Unsupported operand type(s) for +: '{type(self)}' and '{type(other)}'.")

        logger.info("Adding combinations '%s' and '%s'", self, other)
        summation = copy.deepcopy(self)
        for other_measurement, other_polynomial in other.components.items():
            polynomial = summation.components.get(other_measurement, [])
            summation.components[other_measurement] = polynomial + other_polynomial
        return summation.simplified()

    def __sub__(self, other):
        return self + (-other)

    def __rmul__(self, other):
        if isinstance(other, tuple):
            factor_other, operators_other = other
        elif isinstance(other, list):
            factor_other, operators_other = 1, other
        elif isinstance(other, (int, float)):
            factor_other, operators_other = other, []
        else:
            TypeError(f"Unsupported operand type(s) for *: '{type(other)}' and '{type(self)}'.")

        logger.info("Multiplying term '%s %s' and '%s'", factor_other, operators_other, self)
        product = copy.deepcopy(self)
        for measurement, polynomial in self.components.items():
            for factor, operators in polynomial:
                product.components[measurement].remove((factor, operators))
                product.components[measurement].append((factor_other * factor, operators_other + operators))

        return product.simplified()

    def __neg__(self):
        return (-1) * self

    def __matmul__(self, other):
        logger.info("Composing combinations '%s' and '%s'", self, other)
        composition = copy.deepcopy(self)
        for measurement, polynomial in self.components.items():
            if measurement in other:
                del composition.components[measurement]
                for term in polynomial:
                    composition += term * other[measurement]
        return composition.simplified()

    def __repr__(self):
        return repr(self.components)


class LISATDICombination(TDICombination):
    """Defines a time-delay combination for a LISA-like system.

    A LISA-like system possesses the symmetry of the order-6 dihedral group (D3). This subclass
    implements the relevant transformations.
    """
    def __init__(self, components, allow_reflections=True):
        """Initialize a time-delay interferometry for a LISA-like system.

        Args:
            allow_reflections (bool): whether reflection transformations are allowed
            components (dict): dictionary defining the combination
        """
        super().__init__(components)
        self.allow_reflections = allow_reflections

    def rotated(self, nrot=1):
        """Returns a rotated combination.

        A rotation is a circular permutation of indices.

        Args:
            nrot (int): number of 120-degree rotations
        """
        nrot = nrot % 3
        logger.info("Rotating combination '%s' by %d degrees", self, 120 * nrot)
        if nrot == 0:
            mapping = {1: 1, 2: 2, 3: 3}
        elif nrot == 1:
            mapping = {1: 2, 2: 3, 3: 1}
        elif nrot == 2:
            mapping = {1: 3, 2: 1, 3: 2}

        return self.transformed(mapping)

    def reflected(self, axis=1):
        """Returns a reflected combination.

        A reflection leaves the axis unchanged, and swaps the others.

        Args:
            axis (int): index around which combination is reflected
        """
        logger.info("Reflecting combination '%s' around '%d'", self, axis)
        if not self.allow_reflections:
            raise UserWarning("Reflections are not allowed for this combination.")

        if axis == 1:
            mapping = {1: 1, 2: 3, 3: 2}
        elif axis == 2:
            mapping = {1: 3, 2: 2, 3: 1}
        elif axis == 3:
            mapping = {1: 2, 2: 1, 3: 3}
        else:
            raise ValueError(f"Invalid reflection axis '{axis}'.")

        return self.transformed(mapping)
