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
Defines the core class `TDICombination`, used to build combinations.

Authors:
    Martin Staab <martin.staab@aei.mpg.de>
    Jean-Baptiste Bayle <jbayle@jpl.nasa.gov>
"""

import copy
import itertools
import logging
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

    @classmethod
    def from_string(cls, string, var_name="eta", half_way_shift=True):
        """Initialize TDI combination from a string.

        The string variable contains several groups of indices which represent individuals beams.

        These represent the path of different photons propagating along the constellation, with each
        index representing one visited spacecraft.

        Positive substrings represent a path that follows a photon from the event of emission
        from the spacecraft indicated by the leftmost index to the event of reception indicated
        by the rightmost index. This is a path forward in time, computed using advancements 'A_ij'.

        This order is reversed for negative substrings, which represent a path that follows a
        photon from the event of reception at the spacecraft indicated by the leftmost index
        to the event of emission indicated by the rightmost index. This is a path backwards in time,
        computed using delays 'D_ij'.

        Laser noise is cancelled if the overall path from the first index to the last index
        starts and ends at the same spacecraft, and the overall light travel time along this path
        is sufficiently small. See also [2] for the exact criteria in case of LISA.

        The full algorithm to construct a combination is based on [1], just updated to our notation.
        It can be summarized as follows:

            1. Extend substrings into lists of single links ij, for example, '12131 -12131'
               yields `[[12, 21, 13, 31], -[12, 21, 13, 31]]`.

            2. Initialize an empty combination `C` and an empty list of total time shits `T`.

            3. Iterate through all single links with indices ij.
                - If the link is an advancement, add `T A_ij eta_ji` to `C`
                  and append the advancement to the list of time shifts `T = T A[ij]`.
                - If the link is a delay, subtract `T eta_ij` from `C`
                  and append the delay to the list of time shifts `T = T D_ij`.

        This algorithm yields an increasingly long list of time shits in front of each eta.
        To reduce the number of total time shifts, the whole combination can be shifted by the
        inverse operators of the first half of the total list of time shifts. This yields expressions
        which are close to the 'traditional' TDI variables in the literature for e.g. Michelson X.
        This is the default option, to be toggled by the parameter `half_way_shift`.

            [1] M. Vallisneri, Geometric Time Delay Interferometry, Phys.Rev.D72:042003,2005
            [2] M. Muratore, D. Vetrugno, S. Vitale, Revisitation of time delay interferometry combinations
                that suppress laser noise in LISA, 2020 Class. Quantum Grav. 37 185019

        Args:
            string: string of beams, a minus sign signifies a delay, e.g. '12131 -12131'
            var_name: name of the variable that the combination is based on
            half_way_shift: whether to compensate for half of the shifts
        """
        # Vanishing combination for empty string
        if not string:
            return cls({})

        beams = string.split(' ')
        combination = cls({})
        total_shifts = []

        for beam in beams:
            if beam[0] == '-':
                is_delay = True
                beam = beam[1:]
            else:
                is_delay = False

            indices = [int(i) for i in beam]
            for i, j in zip(indices[:-1], indices[1:]):
                if is_delay:
                    combination -= total_shifts * cls({naming.join_indices(var_name, i, j): [(1, [])]})
                    total_shifts.append(naming.join_indices("D", i, j))
                else:
                    combination += total_shifts * cls({
                        naming.join_indices(var_name, j, i): [(1, [naming.join_indices("A", i, j)])]
                    })
                    total_shifts.append(naming.join_indices("A", i, j))

        if half_way_shift:
            half_shifts_inv = []
            for operator in reversed(total_shifts[:len(total_shifts)//2]):
                name, i, j = naming.split_indices(operator)
                name_inv = 'D' if name == 'A' else 'A'
                half_shifts_inv.append(naming.join_indices(name_inv, j, i))
            return half_shifts_inv * combination
        return combination

    @property
    def measurements(self):
        """Return the set of measurements in the combination."""
        return set(self.components.keys())

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

    def build(self, delays, fs, delay_derivatives=None, order=5, delta=1e-12, maxiter=10):
        """Prepare the combination for a set of delays.

        This function prepares the actual combination by pre-computing nested delays and Doppler factors.
        It returns a callable object that evaluates the combination for a given set of measurements, e.g.,

            >>> built = mytdi.build(
                {'d_12': t12_array, 'd_21': t21_array}, fs,
            )
            >>> tdi_data = built(
                {'y_12': y12_array,'y_21': y21_array},
            )

        If any advancement operators are used in the combination, they are computed iteratively.

        Args:
            delays (dict): dictionary of delays, in s
            fs (double): sampling frequency, in Hz
            delay_derivatives: dictionary of delay time derivatives, in s/s
            order (int): Lagrange interpolation orders for delay interpolations
            delta (float): allowed timing accuracy for advancements calculation
            maxiter (int): maximum iterations for advancements calculation
        """
        logger.info("Building combination '%s'", self)

        order = int(order)
        logger.debug("Using interpolation order '%d' for time shifts", order)

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
            logger.debug("Computing advancement '%s'", advancement)
            _, i, j = naming.split_indices(advancement)
            delay = naming.join_indices('d', j, i)
            shifts[advancement] = dsp.calculate_advancements(delays[delay], fs, order, delta, maxiter)
            if delay_derivatives:
                logger.debug("Computing advancement derivative '%s'", advancement)
                dotd_advanced = dsp.timeshift(delay_derivatives[delay], shifts[advancement] * fs)
                derivatives[advancement] = dotd_advanced / (1 - dotd_advanced)

        components_built = {}
        # Precompute polynomials of nested delays
        for measurement, polynomial in self.components.items():
            logger.debug("Computing nested delays for measurement '%s'", measurement)
            components_built[measurement] = []
            for factor, operators in polynomial:
                logger.debug("Computing term '%s %s' for measurement '%s'", factor, operators, measurement)
                # Compute the global time shift to apply
                shift = 0
                doppler = 1
                for operator in operators:
                    if delay_derivatives is not None:
                        doppler += dsp.timeshift(derivatives[operator], shift * fs, order)
                    shift += dsp.timeshift(shifts[operator], shift * fs)
                # Collect precomputed factors and time shifts
                components_built[measurement].append((factor * doppler, shift))

        def call(measurements, order=31):
            """Evaluate combination for a set of measurements.

            Args:
                measurements (dict): dictionary of measurements
                order (int): Lagrange interpolation orders for measurement interpolations
            """
            logger.info("Evaluate combination '%s'", self)

            order = int(order)
            logger.debug("Using interpolation order '%d' for measurements", order)

            result = 0
            for measurement, polynomial in components_built.items():
                logger.debug("Computing contributions from measurement '%s'", measurement)
                for factor, shift in polynomial:
                    # Shift the data, and add it to the result
                    result += factor * dsp.timeshift(measurements[measurement], shift * fs, order)
            return result
        return call

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
        """Return a simplified unique representation of the combination.

        We try to apply the following rules, for each time-shift operator polynomial:

            * drop polynomial if vanishing,
            * drop terms with a vanishing factor,
            * collect terms with identifical time-shift operators with a unique factor,
            * drop delay and advancement operator which cancel out.

        We then sort the components of the simplified combination to get a unique representative.

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
        # We sort components to return a unique representation
        for measurement in simplified.components:
            simplified.components[measurement].sort()
        return simplified

    def __eq__(self, other):
        simplified_self = self.simplified()
        simplified_other = other.simplified()
        return simplified_self.components == simplified_other.components

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
            TypeError(f"unsupported operand type(s) for *: '{type(other)}' and '{type(self)}'.")

        logger.info("Multiplying term '%s %s' and '%s'", factor_other, operators_other, self)
        product = copy.deepcopy(self)
        for measurement, polynomial in self.components.items():
            for factor, operators in polynomial:
                product.components[measurement].remove((factor, operators))
                product.components[measurement].append((factor_other * factor, operators_other + operators))

        return product.simplified()

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return (1 / other) * self
        raise TypeError(f"unsupported operand type(s) for /: '{type(self)}' and '{type(other)}'.")

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


class LISAClockCorrection:
    """Defines a quantity in which clock noise enters similarily to a LISA TDI combination.

    Clock-noise corrections are automatically built from a `LISATDICombination` instances,
    and use the algorithm described in [1] to suppress clock-noise from them.

    They are computed from inter-spacecraft (ISC) carrier and sideband beatnote frequencies.

    To compute a clock noise-free combination `TDIc` from a LISA TDI combination `TDI` and its
    associated clock correction `C`, compute: `TDIc = TDI - C`.

        [1] Olaf Hartwig, Jean-Baptiste Bayle, Clock-jitter reduction in LISA time-delay interferometry combinations,
            (2020), https://arxiv.org/abs/2005.02430
    """
    # pylint: disable=invalid-name

    def __init__(self, combination, modulation_freqs=None, modulation_reduction=True):
        """Build the clock-noise correction from a `LISATDICombination` instance.

        Args:
            combination: uncorrected `LISATDICombination` instance
            modulation_freqs: dictionary of constant modulation frequencies [Hz]
            modulation_reduction: removes right-sided modulation noise terms using reference sidebands
        """
        # Check that `combination` is a LISATDICombination
        if isinstance(combination, LISATDICombination):
            self.combination = combination
        else:
            raise TypeError(f"invalid combination type {type(combination)}, use LISATDICombination")

        logger.info("Initializing clock-noise correction from combination '%s'", self.combination)

        # Use default set of modulation frequencies, matching that of LISANode and Instrument
        if modulation_freqs is None:
            modulation_freqs = {
                '12': 2.4E9, '23': 2.4E9, '31': 2.4E9,
                '13': 2.401E9, '32': 2.401E9, '21': 2.401E9,
            }

        # Check that only a single measurement name (`var_name`) is found in `combination`
        var_name = None
        for measurement in combination.measurements:
            new_name, _, _ = naming.split_indices(measurement)
            if var_name is None:
                var_name = new_name
            elif var_name != new_name:
                raise ValueError(f"single measurement name allowed, found '{new_name}' and '{var_name}'")

        # Build `Delta_M_ij`
        if modulation_reduction:
            logger.debug("Building the differential modulation noise (ΔM) combinations")
            self.delta_M = {
                i: LISATDICombination({
                    f'ref_sb_{i}{k}': [(1/2, [])],
                    f'ref_{i}{k}': [(-1/2, [])],
                    f'ref_sb_{i}{j}': [(-1/2, [])],
                    f'ref_{i}{j}': [(1/2, [])],
                })
                for i, j, k in ['123', '231', '312']
            }
        else:
            self.delta_M = {i: LISATDICombination({}) for i in '123'}
        delta_M_set = {f'Delta_M_{i}': self.delta_M[i] for i in self.delta_M}

        # Build `r_ij`
        logger.debug("Building the modulation-corrected clock-correction variables (rc)")
        self.rc = {}
        for i, j, k in ['123', '231', '312']:
            self.rc[f'{i}{j}'] = LISATDICombination({
                f'isc_sb_{i}{j}': [(1 / modulation_freqs[f'{j}{i}'], [])],
                f'isc_{i}{j}': [(-1 / modulation_freqs[f'{j}{i}'], [])],
                f'Delta_M_{j}': [(1 / modulation_freqs[f'{j}{i}'], [f'D_{i}{j}'])],
            }) @ delta_M_set
            self.rc[f'{i}{k}'] = LISATDICombination({
                f'isc_sb_{i}{k}': [(1 / modulation_freqs[f'{k}{i}'], [])],
                f'isc_{i}{k}': [(-1 / modulation_freqs[f'{k}{i}'], [])],
                f'Delta_M_{i}': [(-1 / modulation_freqs[f'{k}{i}'], [])],
            }) @ delta_M_set
        rc_set = {f'rc_{mosa}': self.rc[mosa] for mosa in self.rc}

        # Build `P_ij`
        # Note that `P_component` here is denoted `P_ij` in the article, while
        # `P` in this code corresponds to `P_ij rc_ij` in the article
        logger.debug("Building the delay polynomials (P)")
        self.P = {}
        self.P_component = {}
        for i, j in naming.lisa_indices():
            self.P_component[f'{i}{j}'] = self.combination.components.get(f'{var_name}_{i}{j}', [])
            self.P[f'{i}{j}'] = LISATDICombination({f'rc_{i}{j}': self.P_component[f'{i}{j}']}) @ rc_set

        # Build `R_ij`
        logger.debug("Building the reconstructed photon path (R)")
        self.R_rc = {}
        self.R = {}
        for i, j in naming.lisa_indices():
            self.R_rc[f'{i}{j}'] = LISATDICombination({})
            for coeff, delays in self.P_component[f'{i}{j}']:
                self.R_rc[f'{i}{j}'] -= coeff * LISATDICombination.from_string(
                    self.to_string(delays), half_way_shift=False, var_name='rc')
            self.R[f'{i}{j}'] = self.R_rc[f'{i}{j}'] @ rc_set

    @staticmethod
    def to_string(delays):
        """Returns a string from a list of delay operators.

        Args:
            delays: list of delay operators
        """
        components = []
        for delay in delays:
            operator, i, j = naming.split_indices(delay)
            if operator == 'D':
                components.append(f'-{i}{j}')
            elif operator == 'A':
                components.append(f'{i}{j}')
            else:
                raise ValueError(f"unsupported time-shift operator '{operator}', use 'A' or 'D'")
        return ' '.join(components)

    def build(self, *args, **kwargs):
        """Prepare the clock-noise correction from delays.

        Refer to `TDICombination.build()`.
        """
        logger.info("Building clock-noise correction from combination")

        # Build the `P_ij`
        prepared_P = {
            mosa: self.P[mosa].build(*args, **kwargs)
            for mosa in self.P
        }

        # Build the `R_ij`
        prepared_R = {
            mosa: self.R[mosa].build(*args, **kwargs)
            for mosa in self.R
        }

        def call(measurements, beatnote_freqs, order=31, individual_rij=True):
            """Evaluate clock-noise correction for a set of measurements.

            The measurement dictionary must contain the inter-spacecraft (ISC) carrier and sideband
            beatnote frequencies.

            If `individual_rij=True`, the measurements are rescaled by the appropriate beatnote frequency for each term
            before the R_ij are computed. This reduces the impact of time-varying beatnote frequencies on the
            correction, at the expense of slightly longer computation time.

            Args:
                measurements: dictionary of measurements including sidebands [Hz]
                beatnote_freqs: dictionary of beatnote frequencies [Hz]
                order: Lagrange interpolation orders for measurement interpolations
                individual_rij: Compute R_ij for each term individually
            """
            result = 0
            if individual_rij:
                # prepare rescaled measurements
                rescaled_measurements = {}
                for i, j, k in ['123', '231', '312']:
                    rescaled_measurements[f'ref_{i}{j}'] = {key: beatnote_freqs[f'ref_{i}{j}'] * value \
                        for key, value in measurements.items()}
                    rescaled_measurements[f'isc_{i}{j}'] = {key: beatnote_freqs[f'isc_{i}{j}'] * value \
                        for key, value in measurements.items()}
                    rescaled_measurements[f'isc_{i}{k}'] = {key: beatnote_freqs[f'isc_{i}{k}'] * value \
                        for key, value in measurements.items()}
                # compute correction
                for i, j, k in ['123', '231', '312']:
                    result += prepared_R[f'{i}{j}'](rescaled_measurements[f'ref_{j}{k}'], order=order) \
                        - prepared_R[f'{i}{j}'](rescaled_measurements[f'isc_{i}{j}'], order=order) \
                        - prepared_R[f'{i}{k}'](rescaled_measurements[f'ref_{i}{j}'], order=order) \
                        - prepared_R[f'{i}{k}'](rescaled_measurements[f'isc_{i}{k}'], order=order) \
                        + prepared_P[f'{i}{j}'](rescaled_measurements[f'ref_{j}{k}'], order=order)
            else:
                # compute correction
                for i, j, k in ['123', '231', '312']:
                    result += (beatnote_freqs[f'ref_{j}{k}'] - beatnote_freqs[f'isc_{i}{j}']) \
                        * prepared_R[f'{i}{j}'](measurements, order=order) \
                        - (beatnote_freqs[f'ref_{i}{j}'] + beatnote_freqs[f'isc_{i}{k}']) \
                        * prepared_R[f'{i}{k}'](measurements, order=order) \
                        + beatnote_freqs[f'ref_{j}{k}'] * prepared_P[f'{i}{j}'](measurements, order=order)
            return result

        return call

    def is_valid(self):
        """Test whether clock-noise correction is valid.

        We check symbolically that P_ij q_i = R_ij, c.f. [1].

            [1] Olaf Hartwig, Jean-Baptiste Bayle, Clock-jitter reduction in LISA time-delay
                interferometry combinations, (2020), https://arxiv.org/abs/2005.02430

        Returns:
            Bool, whether the clock-noise correction is valid.
        """
        test_rc = {
            f'{i}{j}': LISATDICombination({f'q_{i}': [(-1, [])], f'q_{j}': [(1, [f'D_{i}{j}'])]})
            for i, j in naming.lisa_indices()
        }
        test_rc_set = {f'rc_{mosa}': test_rc[mosa] for mosa in test_rc}

        # Check that P_ij q_i = R_ij for all i, j
        for i, j in naming.lisa_indices():
            P_q = LISATDICombination({f'q_{i}': self.P_component[f'{i}{j}']}).simplified()
            if self.R_rc[f'{i}{j}'] @ test_rc_set != P_q:
                return False

        return True

    def __repr__(self):
        return f'<{self.__class__.__name__} based on {self.combination}>'
