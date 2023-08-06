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
Defines convenienve functions to interface with other softwares.

Authors:
    Jean-Baptiste Bayle <jbayle@jpl.nasa.gov>
"""

import logging
import numpy
import h5py

from scipy.interpolate import InterpolatedUnivariateSpline

logger = logging.getLogger(__name__)


class Data():
    """Holds arguments to `build()` function.

    Can be loaded from various sources, including HDF5 files and objects, e.g.,

        >>> data = Data.from_lisanode('my-file.h5')
        >>> data = Data.from_instrument(i)

    and be used to build TDI combinations, either explicitely or using the double-star syntax,

        >>> my_combination.build(data.measurements, data.delays, data.fs)
        >>> my_combination.build(**data.args, order=31)

    """
    MOSAS = ['12', '23', '31', '13', '32', '21']

    LISANODE_FLUCTUATIONS = {
        **{f'isc_{mosa}': f'isc_c_fluctuations_{mosa}' for mosa in MOSAS},
        **{f'tm_{mosa}': f'tm_c_fluctuations_{mosa}' for mosa in MOSAS},
        **{f'ref_{mosa}': f'ref_c_fluctuations_{mosa}' for mosa in MOSAS},
        **{f'isc_sb_{mosa}': f'isc_sb_fluctuations_{mosa}' for mosa in MOSAS},
    }

    LISANODE_OFFSETS = {
        **{f'isc_{mosa}': f'isc_c_frequency_{mosa}' for mosa in MOSAS},
        **{f'tm_{mosa}': f'tm_c_frequency_{mosa}' for mosa in MOSAS},
        **{f'ref_{mosa}': f'ref_c_frequency_{mosa}' for mosa in MOSAS},
        **{f'isc_sb_{mosa}': f'isc_sb_frequency_{mosa}' for mosa in MOSAS},
    }

    LISANODE_TOTALFREQS = {
        **{f'isc_{mosa}': f'isc_c_{mosa}' for mosa in MOSAS},
        **{f'tm_{mosa}': f'tm_c_{mosa}' for mosa in MOSAS},
        **{f'ref_{mosa}': f'ref_c_{mosa}' for mosa in MOSAS},
        **{f'isc_sb_{mosa}': f'isc_sb_{mosa}' for mosa in MOSAS},
    }

    LISANODE_MPRS = {f'd_{mosa}': f'mpr_{mosa}' for mosa in MOSAS}


    def __init__(self, measurements, delays, fs, delay_derivatives=None):
        """Initialize a data object explicitely.

        Args:
            measurements: dictionary of measurements
            delays: dictionary of delays [s]
            fs: sampling frequency [Hz]
            delay_derivatives: dictionary of delay time derivatives [s/s]
        """
        logger.info("Initializing data object")
        self.measurements = measurements
        self.delays = delays
        self.fs = fs
        self.delay_derivatives = delay_derivatives

    @property
    def args(self):
        """Return a dictionary of data that can be used as argument of `TDICombination.build()`.

        Use the double-star syntax,

            >>> my_combination.build(**data.args, delta)

        This includes the delay derivatives. To exclude them, use `data.args_nodoppler`.
        """
        if self.delay_derivatives is None:
            self.compute_delay_derivatives()

        return {
            'delays': self.delays,
            'fs': self.fs,
            'delay_derivatives': self.delay_derivatives,
        }

    @property
    def args_nodoppler(self):
        """Return a dictionary of data that can be used as argument of `TDICombination.build()`.

        Use the double-star syntax,

            >>> my_combination.build(**data.args, delta)

        This excludes the delay derivatives.
        """
        return {
            'delays': self.delays,
            'fs': self.fs,
            'delay_derivatives': None,
        }

    def compute_delay_derivatives(self):
        """Compute delay derivatives from delays.

        We use a simple two-point numerical derivative, using `numpy.gradient()`.
        """
        self.delay_derivatives = {}
        logger.info("Computing delay derivatives")
        for key, delay in self.delays.items():
            self.delay_derivatives[key] = numpy.gradient(delay, 1 / self.fs)

    @classmethod
    def from_lisanode(cls, path, signals='fluctuations', skipped=0):
        """Load LISANode [1] output file.

            [1] https://gitlab.in2p3.fr/j2b.bayle/LISANode

        Args:
            path: path to LISANode output file
            signals: signal to use, one of 'fluctuations', 'offsets', 'total'
            skipped: samples to skip the beginning
        """
        delays = {}
        measurements = {}
        logger.info("Opening LISANode output file '%s'", path)
        with h5py.File(path, 'r') as hdf5:
            # Read sampling rate
            any_value = next(iter(cls.LISANODE_FLUCTUATIONS.values()))
            fs = hdf5[any_value].attrs['sampling_frequency'][0]
            # Load measurements
            if signals == 'fluctuations':
                for key in cls.LISANODE_FLUCTUATIONS:
                    key_fluctuations = cls.LISANODE_FLUCTUATIONS[key]
                    key_offsets = cls.LISANODE_OFFSETS[key]
                    measurements[key] = hdf5[key_fluctuations][skipped:, 1] * numpy.sign(hdf5[key_offsets][skipped:, 1])
            elif signals == 'offsets':
                for key, key_offsets in cls.LISANODE_OFFSETS.items():
                    measurements[key] = hdf5[key_offsets][skipped:, 1]
            elif signals == 'total':
                for key, key_totals in cls.LISANODE_TOTALFREQS.items():
                    measurements[key] = hdf5[key_totals][skipped:, 1]
            else:
                raise ValueError(f"invalid signals parameter '{signals}'")
            # Load MPRs
            for key, key_mprs in cls.LISANODE_MPRS.items():
                delays[key] = hdf5[key_mprs][skipped:, 1]
        logger.debug("Closing LISANode output file '%s'", path)
        # Create instance
        data = cls(measurements, delays, fs)
        data.compute_delay_derivatives()
        return data

    @classmethod
    def from_instrument(cls, instrument_or_path, signals='fluctuations', skipped=0):
        """Load instrument object or measurement file from lisainstrument [1].

            [1] https://gitlab.in2p3.fr/lisa-simulation/instrument

        Args:
            instrument_or_path: instrument instance or path to measurement file
            signals: signal to use, one of 'fluctuations', 'offsets', 'total'
            skipped: samples to skip the beginning [samples]
        """
        if isinstance(instrument_or_path, str):
            return cls.from_instrument_file(instrument_or_path, signals, skipped)
        if isinstance(instrument_or_path, object):
            return cls.from_instrument_object(instrument_or_path, signals, skipped)
        raise TypeError(f"unsupported object type '{type(instrument_or_path)}'")

    @classmethod
    def from_instrument_object(cls, instrument, signals='fluctuations', skipped=0):
        """Load instrument object from lisainstrument [1].

            [1] https://gitlab.in2p3.fr/lisa-simulation/instrument

        Args:
            instrument: instrument instance
            signals: signal to use, one of 'fluctuations', 'offsets', 'total'
            skipped: samples to skip the beginning
        """
        delays = {}
        measurements = {}
        logger.info("Loading instrument object '%s'", instrument)
        # Check that simulation has been run
        if not instrument.simulated:
            raise ValueError("simulation must be run before loading data")
        # Check version and load data
        if instrument.version in ['0.1', '1.0', '1.0.1', '1.0.2']:
            logger.debug("Using specifications for lisainstrument v%s", instrument.version)
            fs = instrument.fs
            for mosa in cls.MOSAS:
                # Load measurements
                if signals == 'fluctuations':
                    measurements[f'isc_{mosa}'] = Data.slice(instrument.isc_carrier_fluctuations[mosa], skipped)
                    measurements[f'ref_{mosa}'] = Data.slice(instrument.ref_carrier_fluctuations[mosa], skipped)
                    measurements[f'tm_{mosa}'] = Data.slice(instrument.tm_carrier_fluctuations[mosa], skipped)
                    measurements[f'isc_sb_{mosa}'] = Data.slice(instrument.isc_usb_fluctuations[mosa], skipped)
                    measurements[f'ref_sb_{mosa}'] = Data.slice(instrument.ref_usb_fluctuations[mosa], skipped)
                elif signals == 'offsets':
                    measurements[f'isc_{mosa}'] = Data.slice(instrument.isc_carrier_offsets[mosa], skipped)
                    measurements[f'ref_{mosa}'] = Data.slice(instrument.ref_carrier_offsets[mosa], skipped)
                    measurements[f'tm_{mosa}'] = Data.slice(instrument.tm_carrier_offsets[mosa], skipped)
                    measurements[f'isc_sb_{mosa}'] = Data.slice(instrument.isc_usb_offsets[mosa], skipped)
                    measurements[f'ref_sb_{mosa}'] = Data.slice(instrument.ref_usb_offsets[mosa], skipped)
                elif signals == 'total':
                    measurements[f'isc_{mosa}'] = Data.slice(instrument.isc_carriers[mosa], skipped)
                    measurements[f'ref_{mosa}'] = Data.slice(instrument.ref_carriers[mosa], skipped)
                    measurements[f'tm_{mosa}'] = Data.slice(instrument.tm_carriers[mosa], skipped)
                    measurements[f'isc_sb_{mosa}'] = Data.slice(instrument.isc_usbs[mosa], skipped)
                    measurements[f'ref_sb_{mosa}'] = Data.slice(instrument.ref_usbs[mosa], skipped)
                # Load MPRs
                delays[f'd_{mosa}'] = Data.slice(instrument.mprs[mosa], skipped)
        else:
            raise ValueError(f"unsupported lisainstrument version '{instrument.version}'")
        # Create instance
        data = cls(measurements, delays, fs)
        data.compute_delay_derivatives()
        return data

    @classmethod
    def from_instrument_file(cls, path, signals='fluctuations', skipped=0):
        """Load measurement file from lisainstrument [1].

            [1] https://gitlab.in2p3.fr/lisa-simulation/instrument

        Args:
            path: path to measurement file
            signals: signal to use, one of 'fluctuations', 'offsets', 'total'
            skipped: samples to skip the beginning [samples]
        """
        delays = {}
        measurements = {}
        logger.info("Loading measurement file '%s'", path)
        with h5py.File(path, 'r') as hdf5:
            # Check version and load data
            if hdf5.attrs['version'] in ['0.1', '1.0', '1.0.1', '1.0.2']:
                logger.debug("Using specifications for lisainstrument v%s", hdf5.attrs['version'])
                fs = hdf5.attrs['fs']
                for mosa in cls.MOSAS:
                    # Load measurements
                    if signals == 'fluctuations':
                        measurements[f'isc_{mosa}'] = Data.slice(hdf5['isc_carrier_fluctuations'][mosa], skipped)
                        measurements[f'ref_{mosa}'] = Data.slice(hdf5['ref_carrier_fluctuations'][mosa], skipped)
                        measurements[f'tm_{mosa}'] = Data.slice(hdf5['tm_carrier_fluctuations'][mosa], skipped)
                        measurements[f'isc_sb_{mosa}'] = Data.slice(hdf5['isc_usb_fluctuations'][mosa], skipped)
                        measurements[f'ref_sb_{mosa}'] = Data.slice(hdf5['ref_usb_fluctuations'][mosa], skipped)
                    elif signals == 'offsets':
                        measurements[f'isc_{mosa}'] = Data.slice(hdf5['isc_carrier_offsets'][mosa], skipped)
                        measurements[f'ref_{mosa}'] = Data.slice(hdf5['ref_carrier_offsets'][mosa], skipped)
                        measurements[f'tm_{mosa}'] = Data.slice(hdf5['tm_carrier_offsets'][mosa], skipped)
                        measurements[f'isc_sb_{mosa}'] = Data.slice(hdf5['isc_usb_offsets'][mosa], skipped)
                        measurements[f'ref_sb_{mosa}'] = Data.slice(hdf5['ref_usb_offsets'][mosa], skipped)
                    elif signals == 'total':
                        measurements[f'isc_{mosa}'] = Data.slice(hdf5['isc_carriers'][mosa], skipped)
                        measurements[f'ref_{mosa}'] = Data.slice(hdf5['ref_carriers'][mosa], skipped)
                        measurements[f'tm_{mosa}'] = Data.slice(hdf5['tm_carriers'][mosa], skipped)
                        measurements[f'isc_sb_{mosa}'] = Data.slice(hdf5['isc_usbs'][mosa], skipped)
                        measurements[f'ref_sb_{mosa}'] = Data.slice(hdf5['ref_usbs'][mosa], skipped)
                    # Load MPRs
                    delays[f'd_{mosa}'] = Data.slice(hdf5['mprs'][mosa], skipped)
            else:
                raise ValueError(f"unsupported lisainstrument version '{hdf5.attrs['version']}'")
        # Create instance
        data = cls(measurements, delays, fs)
        data.compute_delay_derivatives()
        return data

    @classmethod
    def from_gws(cls, path, orbits, skipped=0):
        """Load gravitational-wave (GW) file from lisagwresponse [1].

        This method reads the link responses to GWs and assume that they correspond
        exactly to the noise-free inter-spacecraft (ISC) interferometric measurements.
        All other measurements are assumed to be zero.

        Delays are computed as interpolated proper pseudo-ranges (PPRs) expressed
        in spacecraft proper time (TPS), read from the orbit file [2] passed as arguments.

            [1] https://gitlab.in2p3.fr/lisa-simulation/gw-response
            [2] https://gitlab.in2p3.fr/lisa-simulation/orbits

        Args:
            path: path to gravitational-wave file
            orbits: path to orbit file
            skipped: samples to skip the beginning [samples]
        """
        delays = {}
        measurements = {}
        logger.info("Loading gravitational-wave file '%s'", path)
        # Load measurements
        with h5py.File(path, 'r') as gws:
            # Check version and load data
            if gws.attrs['version'] in ['0.1', '1.0']:
                logger.debug("Using specifications for lisagwresponse v%s", gws.attrs['version'])
                fs = gws.attrs['fs']
                dt = gws.attrs['dt']
                t0 = gws.attrs['t0']
                size = gws.attrs['size']
                t = t0 + numpy.arange(size) * dt
                for mosa in cls.MOSAS:
                    measurements[f'isc_{mosa}'] = Data.slice(gws[f'l_{mosa}'], skipped)
                    measurements[f'isc_sb_{mosa}'] = Data.slice(gws[f'l_{mosa}'], skipped)
                    measurements[f'tm_{mosa}'] = 0
                    measurements[f'ref_{mosa}'] = 0
                    measurements[f'ref_sb_{mosa}'] = 0
            else:
                raise ValueError(f"unsupported lisagwresponse version '{gws.attrs['version']}'")
        # Load MPRs as PPRs from orbit file
        with h5py.File(orbits, 'r') as orbitf:
            # Check version and load data
            if orbitf.attrs['version'] in ['1.0', '1.0.1', '1.0.2']:
                logger.debug("Using specifications for lisaorbits v%s", orbitf.attrs['version'])
                for mosa in cls.MOSAS:
                    delays[f'd_{mosa}'] = InterpolatedUnivariateSpline(
                        orbitf['tps']['tau'][:], orbitf[f'tps/l_{mosa}']['ppr'], k=5, ext='raise',
                    )(t)
            else:
                raise ValueError(f"unsupported lisaorbits version '{orbitf.attrs['version']}'")
        # Create instance
        data = cls(measurements, delays, fs)
        data.compute_delay_derivatives()
        return data

    @staticmethod
    def slice(data, skipped):
        """Slice data if it is an array with more than one element.

        * If `data` is a scalar, return the scalar
        * If `data` is is one-element array, extract and return it
        * If `data` is any other array, slice it according to `skipped` and return it

        Args:
            data: input array
            skipped: number of samples to skip [samples]
        """
        if numpy.isscalar(data):
            return data
        if data.size == 1:
            return data[0]
        return data[skipped:]
