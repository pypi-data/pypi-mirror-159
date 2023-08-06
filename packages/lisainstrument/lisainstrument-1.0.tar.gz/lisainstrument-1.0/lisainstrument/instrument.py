#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=too-many-lines
"""
LISA Instrument module.

Authors:
    Jean-Baptiste Bayle <j2b.bayle@gmail.com>
"""

import re
import logging
import h5py
import scipy.interpolate
import numpy
import matplotlib.pyplot

from lisaconstants import c

from .containers import ForEachSC
from .containers import ForEachMOSA

from . import meta
from . import dsp
from . import noises

logger = logging.getLogger(__name__)


class Instrument:
    """Represents an instrumental simulation."""
    # pylint: disable=attribute-defined-outside-init

    # Indexing conventions
    SCS = ForEachSC.indices()
    MOSAS = ForEachMOSA.indices()

    # Supported laser locking topology
    LOCK_TOPOLOGIES = {
        'N1': {'12': 'cavity', '23': 'adjacent', '31': 'distant', '13': 'adjacent', '32': 'adjacent', '21': 'distant'},
        'N2': {'12': 'cavity', '23': 'adjacent', '31': 'distant', '13': 'adjacent', '32': 'distant', '21': 'distant'},
        'N3': {'12': 'cavity', '23': 'adjacent', '31': 'adjacent', '13': 'adjacent', '32': 'distant', '21': 'distant'},
        'N4': {'12': 'cavity', '23': 'distant', '31': 'distant', '13': 'adjacent', '32': 'adjacent', '21': 'distant'},
        'N5': {'12': 'cavity', '23': 'distant', '31': 'distant', '13': 'adjacent', '32': 'adjacent', '21': 'adjacent'},
        'N6': {'12': 'cavity', '23': 'adjacent', '31': 'adjacent', '13': 'distant', '32': 'distant', '21': 'distant'},
    }

    INDEX_MAPS = {
        '12': {'12': '12', '23': '23', '31': '31', '13': '13', '32': '32', '21': '21'},
        '23': {'12': '31', '23': '12', '31': '23', '13': '32', '32': '21', '21': '13'},
        '31': {'12': '23', '23': '31', '31': '12', '13': '21', '32': '13', '21': '32'},
        '13': {'12': '13', '23': '21', '31': '32', '13': '12', '32': '31', '21': '23'},
        '32': {'12': '21', '23': '32', '31': '13', '13': '23', '32': '12', '21': '32'},
        '21': {'12': '32', '23': '13', '31': '21', '13': '31', '32': '23', '21': '12'},
    }

    def __init__(self,
                 # Sampling parameters
                 size=2592000, dt=1/4, t0='orbits',
                 # Physics simulation sampling and filtering
                 physics_upsampling=4, aafilter=('kaiser', 240, 1.1, 2.9),
                 # Inter-spacecraft propagation
                 orbits='static', gws=None, interpolation=('lagrange', 31),
                 # Artifacts
                 glitches=None,
                 # Laser locking and frequency plan
                 lock='N1-12', offsets_freqs='default',
                 # Laser sources
                 laser_asds=28.2, central_freq=2.816E14,
                 # Laser phase modulation
                 modulation_asds='default', modulation_freqs='default', tdir_tone=None,
                 # Clocks
                 clock_asds=6.32E-14, clock_offsets=0, clock_freqoffsets='default',
                 clock_freqlindrifts='default', clock_freqquaddrifts='default',
                 # Clock inversion
                 clockinv_tolerance=1E-10, clockinv_maxiter=5,
                 # Optical pathlength noises
                 backlink_asds=3E-12, backlink_fknees=2E-3, testmass_asds=2.4E-15, testmass_fknees=0.4E-3,
                 oms_asds=(6.35E-12, 1.25E-11, 1.42E-12, 3.38E-12, 3.32E-12, 7.90E-12), oms_fknees=2E-3,
                 # Tilt-to-length (TTL)
                 ttl_coeffs='default',
                 sc_jitter_asds=(1E-8, 1E-8, 1E-8), mosa_jitter_asds=1E-8, mosa_angles='default',
                 dws_asds=7E-8/335,
                 # Pseudo-ranging
                 ranging_biases=0, ranging_asds=3E-9):
        """Initialize an instrumental simulation.

        Args:
            size: number of samples to generate
            dt: sampling period [s]
            t0: initial time [s], or 'orbits' to match that of the orbits
            physics_upsampling: ratio of sampling frequencies for physics vs. measurement simulation
            aafilter: antialiasing filter function, list of coefficients, filter design method,
                or None for no filter; to design a filter from a Kaiser window, use a tuple
                ('kaiser', attenuation [dB], f1 [Hz], f2 [Hz]) with f1 < f2 the frequencies defining
                the transition band
            orbits: path to orbit file, dictionary of constant PPRs for static arms, or 'static'
                for a set of static PPRs corresponding to a fit of Keplerian orbits around t = 0
            gws: path to gravitational-wave file, or dictionary of gravitational-wave responses
            interpolation: interpolation function or interpolation method and parameters;
                use a tuple ('lagrange', order) with `order` the odd Lagrange interpolation order;
                an arbitrary function should take (x, shift [number of samples]) as parameter
            glitches: path to glitch file, or dictionary of glitch signals per injection point
            lock: pre-defined laser locking configuration ('N1-12' non-swap N1 with 12 primary laser),
                or 'six' for 6 lasers locked on cavities, or a dictionary of locking conditions
            offsets_freqs: dictionary of laser frequency offsets [Hz], or 'default'
            # fplan: path to frequency-plan file, or dictionary of locking beatnote frequencies [Hz],
            #     or None for a default set of constant locking beatnote frequencies
            laser_asds: dictionary of amplitude spectral densities for laser noise [Hz/sqrt(Hz)]
            central_freq: laser central frequency from which all offsets are computed [Hz]
            modulation_asds: dictionary of amplitude spectral densities for modulation noise
                on each MOSA [s/sqrt(Hz)], or 'default' for a default set of levels with a factor
                10 higher on right-sided MOSAs to account for the frequency distribution system
            modulation_freqs: dictionary of modulation frequencies [Hz], or 'default'
            tdir_tone: 3-tuple (amplitude [Hz], frequency [Hz], initial phase [rad]) of dictionaries
                for parameters of TDIR assistance tone, or None
            clock_asds: dictionary of clock noise amplitude spectral densities
            clock_offsets: dictionary of clock offsets
            clock_freqoffsets: dictionary of clock frequency offsets [s^-1], or 'default'
            clock_freqlindrifts: dictionary of clock frequency linear drifts [s^-2], or 'default'
            clock_freqquaddrifts: dictionary of clock frequency quadratic drifts [s^-2], or 'default'
            clockinv_tolerance: convergence tolerance for timer deviation inversion [s]
            clockinv_maxiter: maximum number of iterations for timer deviation inversion
            backlink_asds: dictionary of amplitude spectral densities for backlink noise [m/sqrt(Hz)]
            backlink_fknees: dictionary of cutoff frequencied for backlink noise [Hz]
            testmass_asds: dictionary of amplitude spectral densities for test-mass noise [ms^(-2)/sqrt(Hz)]
            testmass_fknees: dictionary of cutoff frequencies for test-mass noise [Hz]
            oms_asds: tuple of dictionaries of amplitude spectral densities for OMS noise [m/sqrt(Hz)],
                ordered as (isc_carrier, isc_usb, tm_carrier, tm_usb, ref_carrier, ref_usb)
            oms_fknees: dictionary of cutoff frequencies for OMS noise
            ttl_coeffs: tuple (local_phi, distant_phi, local_eta, distant_eta) of dictionaries of
                tilt-to-length coefficients on each MOSA [m/rad], 'default' for a default set of
                coefficients, or 'random' to randomly generate a set of coefficients in a uniform
                distribution [-1.6, 1.6] µm/rad (for local) and [-1.65, 1.65] µm/rad (for distant)
            sc_jitter_asds: tuple of dictionaries of angular jitter amplitude spectral densities
                for spacecraft, ordered as (yaw, pitch, roll) [rad/sqrt(Hz)]
            mosa_jitter_asds: dictionary of MOSA yaw jitter amplitude spectral densities [rad/sqrt(Hz)]
            mosa_angles: dictionary of oriented MOSA opening angles [deg], or 'default'
            dws_asds: dictionary of amplitude spectral densities for DWS measurement noise [rad/s/sqrt(Hz)]
            ranging_biases: dictionary of ranging noise bias [s]
            ranging_asds: dictionary of ranging noise amplitude spectral densities [s/sqrt(Hz)]
        """
        # pylint: disable=too-many-arguments,too-many-statements,too-many-locals,too-many-branches
        logger.info("Initializing instrumental simulation")
        self.git_url = 'https://gitlab.in2p3.fr/lisa-simulation/instrument'
        self.version = meta.__version__
        self.simulated = False

        # Measurement sampling
        self.size = int(size)
        self.dt = float(dt)
        if t0 == 'orbits':
            if isinstance(orbits, str) and orbits != 'static':
                logger.debug("Reading initial time from orbit file '%s'", orbits)
                with h5py.File(orbits, 'r') as orbitf:
                    self.t0 = float(orbitf.attrs['tau0'])
            else:
                self.t0 = 0.0
        else:
            self.t0 = float(t0)
        self.fs = 1 / self.dt
        self.duration = self.dt * self.size
        logger.info("Computing measurement time vector (size=%s, dt=%s)", self.size, self.dt)
        self.t = self.t0 + numpy.arange(self.size, dtype=numpy.float64) * self.dt

        # Physics sampling
        self.physics_upsampling = int(physics_upsampling)
        self.physics_size = self.size * self.physics_upsampling
        self.physics_dt = self.dt / self.physics_upsampling
        self.physics_fs = self.fs * self.physics_upsampling
        logger.info("Computing physics time vector (size=%s, dt=%s)", self.physics_size, self.physics_dt)
        self.physics_t = self.t0 + numpy.arange(self.physics_size, dtype=numpy.float64) * self.physics_dt

        # Instrument topology
        self.central_freq = float(central_freq)
        self.init_lock(lock)

        # Laser and modulation noise
        self.laser_asds = ForEachMOSA(laser_asds)
        if modulation_asds == 'default':
            # Default based on the performance model, with 10x amplification for right-sided
            # MOSAs, to account for errors in the frequency distribution system
            self.modulation_asds = ForEachMOSA({
                '12': 5.2E-14, '23': 5.2E-14, '31': 5.2E-14,
                '13': 5.2E-13, '32': 5.2E-13, '21': 5.2E-13,
            })
        elif modulation_asds is None:
            self.modulation_asds = ForEachMOSA(0)
        else:
            self.modulation_asds = ForEachMOSA(modulation_asds)

        if modulation_freqs == 'default':
            # Default based on mission baseline 2.4 MHz/2.401 MHz for left and right MOSAs
            self.modulation_freqs = ForEachMOSA({
                '12': 2.4E9, '23': 2.4E9, '31': 2.4E9,
                '13': 2.401E9, '32': 2.401E9, '21': 2.401E9,
            })
        else:
            self.modulation_freqs = ForEachMOSA(modulation_freqs)

        if tdir_tone is not None:
            self.tdir_tone_amplitudes = ForEachMOSA(tdir_tone[0])
            self.tdir_tone_frequencies = ForEachMOSA(tdir_tone[1])
            self.tdir_tone_initial_phases = ForEachMOSA(tdir_tone[2])
            logger.debug("Using assistance tone for TDIR (amplitude=%s, frequency=%s, initial phase=%s)",
                self.tdir_tone_amplitudes, self.tdir_tone_frequencies, self.tdir_tone_initial_phases)
        else:
            self.tdir_tone_amplitudes = ForEachMOSA(0)
            self.tdir_tone_frequencies = ForEachMOSA(0)
            self.tdir_tone_initial_phases = ForEachMOSA(0)

        # Clocks
        self.clock_asds = ForEachSC(clock_asds)
        self.clock_offsets = ForEachSC(clock_offsets)
        if clock_freqoffsets == 'default':
            # Default based on LISANode
            self.clock_freqoffsets = ForEachSC({'1': 5E-8, '2': 6.25E-7, '3': -3.75E-7})
        else:
            self.clock_freqoffsets = ForEachSC(clock_freqoffsets)
        if clock_freqlindrifts == 'default':
            # Default based on LISANode
            self.clock_freqlindrifts = ForEachSC({'1': 1.6E-15, '2': 2E-14, '3': -1.2E-14})
        else:
            self.clock_freqlindrifts = ForEachSC(clock_freqlindrifts)
        if clock_freqquaddrifts == 'default':
            # Default based on LISANode
            self.clock_freqquaddrifts = ForEachSC({'1': 9E-24, '2': 6.75E-23, '3': -1.125e-22})
        else:
            self.clock_freqquaddrifts = ForEachSC(clock_freqquaddrifts)

        # Clock-noise inversion
        self.clockinv_tolerance = float(clockinv_tolerance)
        self.clockinv_maxiter = int(clockinv_maxiter)

        # Ranging noise
        self.ranging_biases = ForEachMOSA(ranging_biases)
        self.ranging_asds = ForEachMOSA(ranging_asds)

        # Backlink, OMS and test-mass acceleration noise
        self.backlink_asds = ForEachMOSA(backlink_asds)
        self.backlink_fknees = ForEachMOSA(backlink_fknees)
        self.testmass_asds = ForEachMOSA(testmass_asds)
        self.testmass_fknees = ForEachMOSA(testmass_fknees)
        self.oms_isc_carrier_asds = ForEachMOSA(oms_asds[0])
        self.oms_isc_usb_asds = ForEachMOSA(oms_asds[1])
        self.oms_tm_carrier_asds = ForEachMOSA(oms_asds[2])
        self.oms_tm_usb_asds = ForEachMOSA(oms_asds[3])
        self.oms_ref_carrier_asds = ForEachMOSA(oms_asds[4])
        self.oms_ref_usb_asds = ForEachMOSA(oms_asds[5])
        self.oms_fknees = ForEachMOSA(oms_fknees)

        # Tilt-to-length
        if ttl_coeffs == 'default':
            # Default values drawn from uniform distribution [-1.6, 1.6] µm/rad
            # for local coeffs and [-1.65, 1.65] µm/rad for distant coeffs
            # using `numpy.random.uniform()``
            self.ttl_coeffs_local_phis = ForEachMOSA({
                '12': -8.13811247e-07, '23': 1.08128266e-06, '31': -7.77853952e-07,
                '13': -3.41618871e-07, '32': -6.07855849e-07, '21': -1.34899774e-06,
            })
            self.ttl_coeffs_distant_phis = ForEachMOSA({
                '12': -4.85714829e-07, '23': 1.59761007e-06, '31': 1.33568044e-07,
                '13': 1.48472066e-06, '32': -1.27955015e-06, '21': 7.90851921e-07,
            })
            self.ttl_coeffs_local_etas = ForEachMOSA({
                '12': -1.09550223e-06, '23': 5.29135813e-07, '31': 1.38781495e-06,
                '13': -1.42392125e-06, '32': -7.91375904e-07, '21': -1.57000487e-06,
            })
            self.ttl_coeffs_distant_etas = ForEachMOSA({
                '12': -7.66056679e-08, '23': 1.09993663e-06, '31': 2.06975290e-07,
                '13': -1.10208832e-06, '32': 8.93975974e-07, '21': 1.39319993e-06,
            })
        elif ttl_coeffs == 'random':
            self.ttl_coeffs_local_phis = ForEachMOSA(lambda _: numpy.random.uniform(-1.6E-6, 1.6E-6))
            self.ttl_coeffs_distant_phis = ForEachMOSA(lambda _: numpy.random.uniform(-1.65E-6, 1.65E-6))
            self.ttl_coeffs_local_etas = ForEachMOSA(lambda _: numpy.random.uniform(-1.6E-6, 1.6E-6))
            self.ttl_coeffs_distant_etas = ForEachMOSA(lambda _: numpy.random.uniform(-1.65E-6, 1.65E-6))
        else:
            self.ttl_coeffs_local_phis = ForEachMOSA(ttl_coeffs[0])
            self.ttl_coeffs_distant_phis = ForEachMOSA(ttl_coeffs[1])
            self.ttl_coeffs_local_etas = ForEachMOSA(ttl_coeffs[2])
            self.ttl_coeffs_distant_etas = ForEachMOSA(ttl_coeffs[3])
        self.sc_jitter_phi_asds = ForEachSC(sc_jitter_asds[0])
        self.sc_jitter_eta_asds = ForEachSC(sc_jitter_asds[1])
        self.sc_jitter_theta_asds = ForEachSC(sc_jitter_asds[2])
        self.mosa_jitter_phi_asds = ForEachMOSA(mosa_jitter_asds)
        self.dws_asds = ForEachMOSA(dws_asds)

        # MOSA opening angles
        if mosa_angles == 'default':
            # Default MOSA at +/- 30 deg
            self.mosa_angles = ForEachMOSA({
                '12': 30, '23': 30, '31': 30,
                '13': -30, '32': -30, '21': -30,
            })
        else:
            self.mosa_angles = ForEachMOSA(mosa_angles)

        # Frequency plan
        if offsets_freqs == 'default':
            # Default based on default for LISANode
            self.offsets_freqs = ForEachMOSA({
                '12': 8.1E6, '23': 9.2E6, '31': 10.3E6,
                '13': 1.4E6, '32': -11.6E6, '21': -9.5E6,
            })
        else:
            self.offsets_freqs = ForEachMOSA(offsets_freqs)

        # Orbits, gravitational waves, glitches
        self.init_orbits(orbits)
        self.init_gws(gws)
        self.init_glitches(glitches)

        # Interpolation and antialiasing filter
        self.init_interpolation(interpolation)
        self.init_aafilter(aafilter)

    def init_interpolation(self, interpolation):
        """Initialize or design the interpolation function.

        We support no interpolation, a custom interpolation function, or Lagrange interpolation.

        Args:
            parameters: see `interpolation` docstring in `__init__()`
        """
        if interpolation is None:
            logger.info("Disabling interpolation")
            self.interpolation_order = None
            self.interpolate = lambda x, _: x
        elif callable(interpolation):
            logger.info("Using user-provided interpolation function")
            self.interpolation_order = None
            self.interpolate = lambda x, shift: x if numpy.isscalar(x) else \
                interpolation(x, shift * self.physics_fs)
        else:
            method = str(interpolation[0])
            if method == 'lagrange':
                self.interpolation_order = int(interpolation[1])
                logger.debug("Using Lagrange interpolation of order %s", self.interpolation_order)
                self.interpolate = lambda x, shift: x if numpy.isscalar(x) else \
                    dsp.timeshift(x, shift * self.physics_fs, self.interpolation_order)
            else:
                raise ValueError(f"invalid interpolation parameters '{interpolation}'")

    def init_aafilter(self, aafilter):
        """Initialize antialiasing filter and downsampling."""
        self.downsampled = lambda _, x: x if numpy.isscalar(x) else x[::self.physics_upsampling]

        if aafilter is None:
            logger.info("Disabling antialiasing filter")
            self.aafilter_coeffs = None
            self.aafilter = lambda _, x: x
        elif isinstance(aafilter, (list, numpy.ndarray)):
            logger.info("Using user-provided antialiasing filter coefficients")
            self.aafilter_coeffs = aafilter
            self.aafilter = lambda _, x: x if numpy.isscalar(x) else \
                scipy.signal.lfilter(self.aafilter_coeffs, 1, x)
        elif callable(aafilter):
            logger.info("Using user-provided antialiasing filter function")
            self.aafilter_coeffs = None
            self.aafilter = lambda _, x: x if numpy.isscalar(x) else aafilter(x)
        else:
            logger.info("Designing antialiasing filter %s", aafilter)
            self.aafilter_coeffs = self.design_aafilter(aafilter)
            self.aafilter = lambda _, x: x if numpy.isscalar(x) else \
                scipy.signal.lfilter(self.aafilter_coeffs, 1, x)

    def design_aafilter(self, parameters):
        """Design the antialiasing filter.

        We currently support finite-impulse response filter designed from a Kaiser window.
        The order and beta parameters of the Kaiser window are deduced from the desired attenuation
        and transition bandwidth of the filter.

        Args:
            parameters: see `aafilter` docstring in `__init__()`

        Returns:
            A function that filters data.
        """
        method = parameters[0]
        nyquist = self.physics_fs / 2

        if method == 'kaiser':
            logger.debug("Designing finite-impulse response filter from Kaiser window")
            attenuation, freq1, freq2 = parameters[1], parameters[2], parameters[3]
            if attenuation == 0:
                logger.debug("Vanishing filter attenuation, disabling filtering")
                return lambda x: x
            logger.debug("Filter attenuation is %s dB", attenuation)
            logger.debug("Filter transition band is [%s Hz, %s Hz]", freq1, freq2)
            numtaps, beta = scipy.signal.kaiserord(attenuation, (freq2 - freq1) / nyquist)
            logger.debug("Kaiser window has %s taps and beta is %s", numtaps, beta)
            taps = scipy.signal.firwin(numtaps, (freq1 + freq2) / (2 * nyquist), window=('kaiser', beta))
            logger.debug("Filter taps are %s", taps)
            return taps

        raise ValueError(f"invalid filter parameters '{parameters}'")

    def init_lock(self, lock):
        """Initialize laser locking configuration."""
        if lock == 'six':
            logger.info("Using pre-defined locking configuration 'six'")
            self.lock_config = 'six'
            self.lock = {'12': 'cavity', '23': 'cavity', '31': 'cavity', '13': 'cavity', '32': 'cavity', '21': 'cavity'}
        elif isinstance(lock, str):
            logger.info("Using pre-defined locking configuration '%s'", lock)
            match = re.match(r'^(N[1-6])-(12|23|31|13|32|21)$', lock)
            if match:
                self.lock_config = (match.group(1), match.group(2))
                lock_12 = self.LOCK_TOPOLOGIES[self.lock_config[0]] # with 12 as primary
                index_map = self.INDEX_MAPS[self.lock_config[1]] # correspondance to lock_12
                self.lock = {mosa: lock_12[index_map[mosa]] for mosa in self.MOSAS}
            else:
                raise ValueError(f"unsupported pre-defined locking configuration '{lock}'")
        elif isinstance(lock, dict):
            logger.info("Using explicit locking configuration '%s'", lock)
            if (set(lock.keys()) != set(self.MOSAS) or
                set(lock.values()) != set(['cavity', 'distant', 'adjacent'])):
                raise ValueError(f"invalid locking dictionary '{lock}'")
            self.lock = lock
        else:
            raise ValueError(f"invalid locking configuration '{lock}'")

    def init_orbits(self, orbits):
        """Initialize orbits."""
        if orbits == 'static':
            logger.info("Using default set of static proper pseudo-ranges")
            self.orbit_file = None
            self.pprs = ForEachMOSA({
                # Default PPRs based on first samples of Keplerian orbits (v1.0)
                '12': 8.3324, '23': 8.3028, '31': 8.3324,
                '13': 8.3315, '32': 8.3044, '21': 8.3315,
            })
            self.d_pprs = ForEachMOSA(0)
        elif isinstance(orbits, str):
            logger.info("Using orbit file '%s'", orbits)
            self.orbit_file = orbits
            orbitf = h5py.File(self.orbit_file, 'r')
            if 'version' not in orbitf.attrs:
                raise ValueError(f"cannot read version of orbit file '{self.orbit_file}'")
            orbits_version = orbitf.attrs['version']
            logger.debug("Using orbit file version %s", orbits_version)
            if orbits_version in ['1.0', '1.0.1']:
                try:
                    logger.debug("Interpolating proper pseudo-ranges")
                    self.pprs = ForEachMOSA(lambda mosa: scipy.interpolate.InterpolatedUnivariateSpline(
                        orbitf['tps']['tau'][:], orbitf[f'tps/l_{mosa}']['ppr'], k=5, ext='raise')(self.physics_t)
                    )
                    logger.debug("Interpolating proper pseudo-range derivatives")
                    self.d_pprs = ForEachMOSA(lambda mosa: scipy.interpolate.InterpolatedUnivariateSpline(
                        orbitf['tps']['tau'][:], orbitf[f'tps/l_{mosa}']['d_ppr'], k=5, ext='raise')(self.physics_t)
                    )
                except ValueError as error:
                    logger.error("Missing orbit information at \n%s", self.physics_t)
                    raise ValueError("missing orbit information, use longer orbit file or adjust sampling") from error
            else:
                raise ValueError(f"unsupported orbit file version '{orbits_version}'")
            orbitf.close()
        else:
            logger.info("Using user-provided proper pseudo-ranges and derivatives thereof")
            self.orbit_file = None
            self.pprs = ForEachMOSA(orbits)
            self.d_pprs = self.pprs.transformed(lambda sc, x:
                0 if numpy.isscalar(x) else numpy.gradient(x, self.physics_fs)
            )

    def init_gws(self, gws):
        """Initialize gravitational-wave responses."""
        if isinstance(gws, str):
            self.gw_file = gws
            logger.info("Interpolating gravitational-wave responses from GW file '%s'", self.gw_file)
            gwf = h5py.File(self.gw_file, 'r')
            self.gws = ForEachMOSA(lambda mosa: scipy.interpolate.InterpolatedUnivariateSpline(
                gwf['t'][:], gwf[f'l_{mosa}'][:], k=5, ext='zeros')(self.physics_t)
            )
            gwf.close()
        elif gws is None:
            logger.debug("No gravitational-wave responses")
            self.gw_file = None
            self.gws = ForEachMOSA(0)
        else:
            logger.info("Using user-provided gravitational-wave responses")
            self.gw_file = None
            self.gws = ForEachMOSA(gws)

    def init_glitches(self, glitches):
        """Initialize glitches.

        According to https://gitlab.in2p3.fr/lisa-simulation/glitch, we have

            * test-mass glitches `tm_ij` [m/s]
            * laser glitches `laser_ij` [Hz]

        """
        if isinstance(glitches, str):
            self.glitch_file = glitches
            logger.info("Interpolating glitch signals from glitch file '%s'", self.glitch_file)
            glitchf = h5py.File(self.glitch_file, 'r')
            self.glitch_tms = ForEachMOSA(lambda mosa:
                0 if f'tm_{mosa}' not in glitchf else \
                scipy.interpolate.InterpolatedUnivariateSpline(
                    glitchf['t'][:], glitchf[f'tm_{mosa}'][:], k=5, ext='const')(self.physics_t)
            )
            self.glitch_lasers = ForEachMOSA(lambda mosa:
                0 if f'laser_{mosa}' not in glitchf else \
                scipy.interpolate.InterpolatedUnivariateSpline(
                    glitchf['t'][:], glitchf[f'laser_{mosa}'][:], k=5, ext='const')(self.physics_t)
            )
            glitchf.close()
        elif glitches is None:
            logger.debug("No glitches")
            self.glitch_file = None
            self.glitch_tms = ForEachMOSA(0)
            self.glitch_lasers = ForEachMOSA(0)
        else:
            raise ValueError(f"invalid value '{glitches}' for glitches")

    def disable_all_noises(self, but=None):
        """Turn off all instrumental noises.

        Args:
            but: optional category of noises to keep on ['laser', 'modulation',
                'clock', 'pathlength', 'ranging', 'jitters']
        """
        valid_noises = ['laser', 'modulation', 'clock', 'pathlength', 'ranging', 'jitters']
        if but is not None and but not in valid_noises:
            raise ValueError(f"unknown noise '{but}'")

        if but != 'laser':
            self.laser_asds = ForEachMOSA(0)
        if but != 'modulation':
            self.modulation_asds = ForEachMOSA(0)
        if but != 'clock':
            self.disable_clock_noises()
        if but != 'pathlength':
            self.disable_pathlength_noises()
        if but != 'ranging':
            self.disable_ranging_noises()
        if but != 'jitters':
            self.disable_jitters()

    def disable_clock_noises(self):
        """Turn off all imperfections on clocks.

        This includes offsets, and frequency offsets and deviations.
        """
        self.clock_asds = ForEachSC(0)
        self.clock_offsets = ForEachSC(0)
        self.clock_freqoffsets = ForEachSC(0)
        self.clock_freqlindrifts = ForEachSC(0)
        self.clock_freqquaddrifts = ForEachSC(0)

    def disable_pathlength_noises(self):
        """Turn off all optical pathlength noises."""
        self.backlink_asds = ForEachMOSA(0)
        self.testmass_asds = ForEachMOSA(0)
        self.oms_isc_carrier_asds = ForEachMOSA(0)
        self.oms_isc_usb_asds = ForEachMOSA(0)
        self.oms_tm_carrier_asds = ForEachMOSA(0)
        self.oms_tm_usb_asds = ForEachMOSA(0)
        self.oms_ref_carrier_asds = ForEachMOSA(0)
        self.oms_ref_usb_asds = ForEachMOSA(0)

    def disable_ranging_noises(self):
        """Turn off all pseudo-ranging noises."""
        self.ranging_biases = ForEachMOSA(0)
        self.ranging_asds = ForEachMOSA(0)

    def disable_jitters(self):
        """Turn off all angular jitters."""
        self.sc_jitter_phi_asds = ForEachSC(0)
        self.sc_jitter_eta_asds = ForEachSC(0)
        self.sc_jitter_theta_asds = ForEachSC(0)
        self.mosa_jitter_phi_asds = ForEachMOSA(0)

    def disable_dopplers(self):
        """Set proper pseudo-range derivatives to zero to turn off Doppler effects."""
        self.d_pprs = ForEachMOSA(0)

    def simulate(self, keep_all=False):
        """Run a simulation, and generate all intermediary signals.

        Args:
            keep_all: whether to keep all quantities in memory
        """
        # pylint: disable=too-many-locals,too-many-statements,too-many-branches

        logger.info("Starting simulation")
        self.keep_all = keep_all
        self.simulated = True

        self.simulate_noises()

        ## TDIR tone

        logger.debug("Computing local timer deviations")
        self.local_timer_deviations = \
            self.clock_offsets + ForEachSC(lambda sc:
                numpy.cumsum(numpy.broadcast_to(
                    self.clock_noise_offsets[sc] + self.clock_noise_fluctuations[sc],
                    self.physics_size)
                * self.physics_dt)
            )

        self.tdir_tones = ForEachMOSA(lambda mosa:
            0 if self.tdir_tone_amplitudes[mosa] == 0 \
            else self.tdir_tone_amplitudes[mosa] * numpy.sin(
                2 * numpy.pi * self.tdir_tone_frequencies[mosa]
                * (self.physics_t + self.local_timer_deviations[mosa[0]])
                + self.tdir_tone_initial_phases[mosa]
            )
        )

        ## Local beams

        logger.info("Simulating local beams")
        self.simulate_locking()

        ## Propagation to distant MOSA

        logger.info("Propagating local beams to distant MOSAs")

        logger.debug("Propagating carrier offsets to distant MOSAs")
        self.distant_carrier_offsets = \
            -self.d_pprs * self.central_freq \
            + (1 - self.d_pprs) * self.local_carrier_offsets.distant() \
            .transformed(lambda mosa, x: self.interpolate(x, -self.pprs[mosa]))

        logger.debug("Propagating carrier fluctuations to distant MOSAs")
        carrier_fluctuations = \
            self.local_carrier_fluctuations \
            + (self.central_freq + self.local_carrier_offsets) * self.distant_ttls / c
        propagated_carrier_fluctuations = \
            (1 - self.d_pprs) * carrier_fluctuations.distant() \
            .transformed(lambda mosa, x: self.interpolate(x, -self.pprs[mosa]))
        self.distant_carrier_fluctuations = \
            propagated_carrier_fluctuations \
            + self.central_freq * self.gws \
            + (self.central_freq + self.local_carrier_offsets) * self.local_ttls / c

        logger.debug("Propagating upper sideband offsets to distant MOSAs")
        self.distant_usb_offsets = \
            -self.d_pprs * self.central_freq \
            + (1 - self.d_pprs) * self.local_usb_offsets.distant() \
            .transformed(lambda mosa, x: self.interpolate(x, -self.pprs[mosa]))

        logger.debug("Propagating upper sideband fluctuations to distant MOSAs")
        usb_fluctuations = \
            self.local_usb_fluctuations \
            + (self.central_freq + self.local_usb_offsets) * self.distant_ttls / c
        propagated_usb_fluctuations = \
            (1 - self.d_pprs) * usb_fluctuations.distant() \
            .transformed(lambda mosa, x: self.interpolate(x, -self.pprs[mosa]))
        self.distant_usb_fluctuations = \
            propagated_usb_fluctuations \
            + self.central_freq * self.gws \
            + (self.central_freq + self.local_usb_offsets) * self.local_ttls / c

        logger.debug("Propagating timer deviations to distant MOSAs")
        self.distant_timer_deviations = \
            self.local_timer_deviations.for_each_mosa().distant() \
            .transformed(lambda mosa, x: self.interpolate(x, -self.pprs[mosa])
            - self.pprs[mosa]
        )

        ## Propagation to adjacent MOSA

        logger.info("Propagating local beams to adjacent MOSAs")

        logger.debug("Propagating carrier offsets to adjacent MOSAs")
        self.adjacent_carrier_offsets = self.local_carrier_offsets.adjacent()

        logger.debug("Propagating carrier fluctuations to adjacent MOSAs")
        self.adjacent_carrier_fluctuations = \
            self.local_carrier_fluctuations.adjacent() \
            + self.central_freq * self.backlink_noises

        logger.debug("Propagating upper sideband offsets to adjacent MOSAs")
        self.adjacent_usb_offsets = self.local_usb_offsets.adjacent()

        logger.debug("Propagating upper sideband fluctuations to adjacent MOSAs")
        self.adjacent_usb_fluctuations = \
            self.local_usb_fluctuations.adjacent() \
            + self.central_freq * self.backlink_noises

        ## Inter-spacecraft interferometer local beams

        logger.info("Propagating local beams to inter-spacecraft interferometers")

        logger.debug("Propagating local carrier offsets to inter-spacecraft interferometer")
        self.local_isc_carrier_offsets = self.local_carrier_offsets

        logger.debug("Propagating local carrier fluctuations to inter-spacecraft interferometer")
        self.local_isc_carrier_fluctuations = self.local_carrier_fluctuations

        logger.debug("Propagating local upper sideband offsets to inter-spacecraft interferometer")
        self.local_isc_usb_offsets = self.local_usb_offsets

        logger.debug("Propagating local upper sideband fluctuations to inter-spacecraft interferometer")
        self.local_isc_usb_fluctuations = self.local_usb_fluctuations

        ## Inter-spacecraft interferometer distant beams

        logger.info("Propagating distant beams to inter-spacecraft interferometers")

        logger.debug("Propagating distant carrier offsets to inter-spacecraft interferometer")
        self.distant_isc_carrier_offsets = self.distant_carrier_offsets

        logger.debug("Propagating distant carrier fluctuations to inter-spacecraft interferometer")
        self.distant_isc_carrier_fluctuations = self.distant_carrier_fluctuations

        logger.debug("Propagating distant upper sideband offsets to inter-spacecraft interferometer")
        self.distant_isc_usb_offsets = self.distant_usb_offsets

        logger.debug("Propagating distant upper sideband fluctuations to inter-spacecraft interferometer")
        self.distant_isc_usb_fluctuations = self.distant_usb_fluctuations

        ## Inter-spacecraft interferometer beatnotes on TPS (high-frequency)

        logger.info("Computing inter-spacecraft beatnotes on TPS")

        logger.debug("Computing inter-spacecraft carrier beatnote offsets on TPS")
        self.tps_isc_carrier_offsets = \
            self.distant_isc_carrier_offsets - self.local_isc_carrier_offsets

        logger.debug("Computing inter-spacecraft carrier beatnote fluctuations on TPS")
        self.tps_isc_carrier_fluctuations = \
            self.distant_isc_carrier_fluctuations - self.local_isc_carrier_fluctuations \
            + self.central_freq * self.oms_isc_carrier_noises

        logger.debug("Computing inter-spacecraft upper sideband beatnote offsets on TPS")
        self.tps_isc_usb_offsets = \
            self.distant_isc_usb_offsets - self.local_isc_usb_offsets

        logger.debug("Computing inter-spacecraft upper sideband beatnote fluctuations on TPS")
        self.tps_isc_usb_fluctuations = \
            self.distant_isc_usb_fluctuations - self.local_isc_usb_fluctuations \
            + self.central_freq * self.oms_isc_usb_noises

        ## Inter-spacecraft DWS measurements on TPS (high-frequency)

        logger.info("Computing inter-spacecraft DWS measurements on TPS")
        self.tps_isc_dws_phis = self.mosa_total_jitter_phis + self.dws_phi_noises
        self.tps_isc_dws_etas = self.mosa_total_jitter_etas + self.dws_eta_noises

        ## Measured pseudo-ranging on TPS grid (high-frequency)

        logger.info("Computing measured pseudo-ranges on TPS")
        self.tps_mprs = \
            self.local_timer_deviations \
            - self.distant_timer_deviations + self.ranging_noises

        ## Test-mass interferometer local beams

        logger.info("Propagating local beams to test-mass interferometers")

        logger.debug("Propagating local carrier offsets to test-mass interferometer")
        self.local_tm_carrier_offsets = self.local_carrier_offsets

        logger.debug("Propagating local carrier fluctuations to test-mass interferometer")
        self.local_tm_carrier_fluctuations = \
            self.local_carrier_fluctuations \
            + 2 * (self.testmass_noises + self.glitch_tms) / c \
            * (self.central_freq + self.local_tm_carrier_offsets)

        logger.debug("Propagating local upper sideband offsets to test-mass interferometer")
        self.local_tm_usb_offsets = self.local_usb_offsets

        logger.debug("Propagating local upper sideband fluctuations to test-mass interferometer")
        self.local_tm_usb_fluctuations = \
            self.local_usb_fluctuations \
            + 2 * (self.testmass_noises + self.glitch_tms) / c \
            * (self.central_freq + self.local_tm_usb_offsets)

        ## Test-mass interferometer adjacent beams

        logger.info("Propagating adjacent beams to test-mass interferometers")

        logger.debug("Propagating adjacent carrier offsets to test-mass interferometer")
        self.adjacent_tm_carrier_offsets = self.adjacent_carrier_offsets

        logger.debug("Propagating adjacent carrier fluctuations to test-mass interferometer")
        self.adjacent_tm_carrier_fluctuations = self.adjacent_carrier_fluctuations

        logger.debug("Propagating adjacent upper sideband offsets to test-mass interferometer")
        self.adjacent_tm_usb_offsets = self.adjacent_usb_offsets

        logger.debug("Propagating adjacent upper sideband fluctuations to test-mass interferometer")
        self.adjacent_tm_usb_fluctuations = self.adjacent_usb_fluctuations

        ## Test-mass interferometer beatnotes on TPS (high-frequency)

        logger.info("Computing test-mass beatnotes on TPS")

        logger.debug("Computing test-mass carrier beatnote offsets on TPS")
        self.tps_tm_carrier_offsets = \
            self.adjacent_tm_carrier_offsets - self.local_tm_carrier_offsets

        logger.debug("Computing test-mass carrier beatnote fluctuations on TPS")
        self.tps_tm_carrier_fluctuations = \
            self.adjacent_tm_carrier_fluctuations - self.local_tm_carrier_fluctuations \
            + self.central_freq * self.oms_tm_carrier_noises

        logger.debug("Computing test-mass upper sideband beatnote offsets on TPS")
        self.tps_tm_usb_offsets = \
            self.adjacent_tm_usb_offsets - self.local_tm_usb_offsets

        logger.debug("Computing test-mass upper sideband beatnote fluctuations on TPS")
        self.tps_tm_usb_fluctuations = \
            self.adjacent_tm_usb_fluctuations - self.local_tm_usb_fluctuations \
            + self.central_freq * self.oms_tm_usb_noises

        ## Reference interferometer local beams

        logger.info("Propagating local beams to reference interferometers")

        logger.debug("Propagating local carrier offsets to reference interferometer")
        self.local_ref_carrier_offsets = self.local_carrier_offsets

        logger.debug("Propagating local carrier fluctuations to reference interferometer")
        self.local_ref_carrier_fluctuations = self.local_carrier_fluctuations

        logger.debug("Propagating local upper sideband offsets to reference interferometer")
        self.local_ref_usb_offsets = self.local_usb_offsets

        logger.debug("Propagating local upper sideband fluctuations to reference interferometer")
        self.local_ref_usb_fluctuations = self.local_usb_fluctuations

        ## Reference interferometer adjacent beams

        logger.info("Propagating adjacent beams to reference interferometers")

        logger.debug("Propagating adjacent carrier offsets to reference interferometer")
        self.adjacent_ref_carrier_offsets = self.adjacent_carrier_offsets

        logger.debug("Propagating adjacent carrier fluctuations to reference interferometer")
        self.adjacent_ref_carrier_fluctuations = self.adjacent_carrier_fluctuations

        logger.debug("Propagating adjacent upper sideband offsets to reference interferometer")
        self.adjacent_ref_usb_offsets = self.adjacent_usb_offsets

        logger.debug("Propagating adjacent upper sideband fluctuations to reference interferometer")
        self.adjacent_ref_usb_fluctuations = self.adjacent_usb_fluctuations

        ## Reference interferometer beatnotes on TPS (high-frequency)

        logger.info("Computing reference beatnotes on TPS")

        logger.debug("Computing reference carrier beatnote offsets on TPS")
        self.tps_ref_carrier_offsets = \
            self.adjacent_ref_carrier_offsets - self.local_ref_carrier_offsets

        logger.debug("Computing reference carrier beatnote fluctuations on TPS")
        self.tps_ref_carrier_fluctuations = \
            self.adjacent_ref_carrier_fluctuations - self.local_ref_carrier_fluctuations \
            + self.central_freq * self.oms_ref_carrier_noises

        logger.debug("Computing reference upper sideband beatnote offsets on TPS")
        self.tps_ref_usb_offsets = \
            self.adjacent_ref_usb_offsets - self.local_ref_usb_offsets

        logger.debug("Computing reference upper sideband beatnote fluctuations on TPS")
        self.tps_ref_usb_fluctuations = \
            self.adjacent_ref_usb_fluctuations - self.local_ref_usb_fluctuations \
            + self.central_freq * self.oms_ref_usb_noises

        ## Sampling beatnotes, DWS measurements, and measured pseudo-ranges to THE grid

        logger.info("Inverting timer deviations")
        self.inverse_timer_deviations = self.local_timer_deviations \
            .transformed(lambda sc, x: self.invert_timer_deviations(x, sc))

        self.timestamped = \
            lambda mosa, x: self.interpolate(x, -self.inverse_timer_deviations.for_each_mosa()[mosa])

        logger.info("Sampling inter-spacecraft beatnotes to THE grid")

        logger.debug("Sampling inter-spacecraft carrier beatnote fluctuations to THE grid")
        self.the_isc_carrier_offsets = (
            self.tps_isc_carrier_offsets / (1 + self.clock_noise_offsets)
        ).transformed(self.timestamped)

        logger.debug("Sampling inter-spacecraft carrier beatnote fluctuations to THE grid")
        self.the_isc_carrier_fluctuations = (
            self.tps_isc_carrier_fluctuations / (1 + self.clock_noise_offsets)
                - self.tps_isc_carrier_offsets * self.clock_noise_fluctuations
                / (1 + self.clock_noise_offsets)**2
        ).transformed(self.timestamped)

        logger.debug("Sampling inter-spacecraft upper sideband beatnote offsets to THE grid")
        self.the_isc_usb_offsets = (
            self.tps_isc_usb_offsets / (1 + self.clock_noise_offsets)
        ).transformed(self.timestamped)

        logger.debug("Sampling inter-spacecraft upper sideband beatnote fluctuations to THE grid")
        self.the_isc_usb_fluctuations = (
            self.tps_isc_usb_fluctuations / (1 + self.clock_noise_offsets)
                - self.tps_isc_usb_offsets * self.clock_noise_fluctuations
                / (1 + self.clock_noise_offsets)**2
        ).transformed(self.timestamped)

        logger.debug("Sampling inter-spacecraft DWS measurements to THE grid")
        self.the_isc_dws_phis = self.tps_isc_dws_phis.transformed(self.timestamped)
        self.the_isc_dws_etas = self.tps_isc_dws_etas.transformed(self.timestamped)

        logger.info("Sampling measured pseudo-ranges to THE grid")
        self.the_mprs = self.tps_mprs.transformed(self.timestamped)

        logger.info("Sampling test-mass beatnotes to THE grid")

        logger.debug("Sampling test-mass carrier beatnote offsets to THE grid")
        self.the_tm_carrier_offsets = (
            self.tps_tm_carrier_offsets / (1 + self.clock_noise_offsets)
        ).transformed(self.timestamped)

        logger.debug("Sampling test-mass carrier beatnote fluctuations to THE grid")
        self.the_tm_carrier_fluctuations = (
            self.tps_tm_carrier_fluctuations / (1 + self.clock_noise_offsets)
                - self.tps_tm_carrier_offsets * self.clock_noise_fluctuations
                / (1 + self.clock_noise_offsets)**2
        ).transformed(self.timestamped)

        logger.debug("Sampling test-mass upper sideband beatnote offsets to THE grid")
        self.the_tm_usb_offsets = (
            self.tps_tm_usb_offsets / (1 + self.clock_noise_offsets)
        ).transformed(self.timestamped)

        logger.debug("Sampling test-mass upper sideband beatnote fluctuations to THE grid")
        self.the_tm_usb_fluctuations = (
            self.tps_tm_usb_fluctuations / (1 + self.clock_noise_offsets)
                - self.tps_tm_usb_offsets * self.clock_noise_fluctuations
                / (1 + self.clock_noise_offsets)**2
        ).transformed(self.timestamped)

        logger.info("Sampling reference beatnotes to THE grid")

        logger.debug("Sampling reference carrier beatnote offsets to THE grid")
        self.the_ref_carrier_offsets = (
            self.tps_ref_carrier_offsets / (1 + self.clock_noise_offsets)
        ).transformed(self.timestamped)

        logger.debug("Sampling reference carrier beatnote fluctuations to THE grid")
        self.the_ref_carrier_fluctuations = (
            self.tps_ref_carrier_fluctuations / (1 + self.clock_noise_offsets)
                - self.tps_ref_carrier_offsets * self.clock_noise_fluctuations
                / (1 + self.clock_noise_offsets)**2
        ).transformed(self.timestamped)

        logger.debug("Sampling reference upper sideband beatnote offsets to THE grid")
        self.the_ref_usb_offsets = (
            self.tps_ref_usb_offsets / (1 + self.clock_noise_offsets)
        ).transformed(self.timestamped)

        logger.debug("Sampling reference upper sideband beatnote fluctuations to THE grid")
        self.the_ref_usb_fluctuations = (
            self.tps_ref_usb_fluctuations / (1 + self.clock_noise_offsets)
                - self.tps_ref_usb_offsets * self.clock_noise_fluctuations
                / (1 + self.clock_noise_offsets)**2
        ).transformed(self.timestamped)

        ## Total frequencies

        logger.info("Computing total beatnote frequencies")

        logger.debug("Computing total inter-spacecraft carrier beatnotes")
        self.the_isc_carriers = \
            self.the_isc_carrier_offsets + self.the_isc_carrier_fluctuations

        logger.debug("Computing total inter-spacecraft upper sideband beatnotes")
        self.the_isc_usbs = \
            self.the_isc_usb_offsets + self.the_isc_usb_fluctuations

        logger.debug("Computing total test-mass carrier beatnotes")
        self.the_tm_carriers = \
            self.the_tm_carrier_offsets + self.the_tm_carrier_fluctuations

        logger.debug("Computing total test-mass upper sideband beatnotes")
        self.the_tm_usbs = \
            self.the_tm_usb_offsets + self.the_tm_usb_fluctuations

        logger.debug("Computing total reference carrier beatnotes")
        self.the_ref_carriers = \
            self.the_ref_carrier_offsets + self.the_ref_carrier_fluctuations

        logger.debug("Computing total reference upper sideband beatnotes")
        self.the_ref_usbs = \
            self.the_ref_usb_offsets + self.the_ref_usb_fluctuations

        ## Antialiasing filtering

        logger.info("Filtering beatnotes")

        logger.debug("Filtering inter-spacecraft beatnotes")
        self.filtered_isc_carrier_offsets = self.the_isc_carrier_offsets.transformed(self.aafilter)
        self.filtered_isc_carrier_fluctuations = self.the_isc_carrier_fluctuations.transformed(self.aafilter)
        self.filtered_isc_carriers = self.the_isc_carriers.transformed(self.aafilter)
        self.filtered_isc_usb_offsets = self.the_isc_usb_offsets.transformed(self.aafilter)
        self.filtered_isc_usb_fluctuations = self.the_isc_usb_fluctuations.transformed(self.aafilter)
        self.filtered_isc_usbs = self.the_isc_usbs.transformed(self.aafilter)

        logger.debug("Filtering inter-spacecraft DWS measurements")
        self.filtered_isc_dws_phis = self.the_isc_dws_phis.transformed(self.aafilter)
        self.filtered_isc_dws_etas = self.the_isc_dws_etas.transformed(self.aafilter)

        logger.debug("Filtering measured pseudo-ranges")
        self.filtered_mprs = self.the_mprs.transformed(self.aafilter)

        logger.debug("Filtering test-mass beatnotes")
        self.filtered_tm_carrier_offsets = self.the_tm_carrier_offsets.transformed(self.aafilter)
        self.filtered_tm_carrier_fluctuations = self.the_tm_carrier_fluctuations.transformed(self.aafilter)
        self.filtered_tm_carriers = self.the_tm_carriers.transformed(self.aafilter)
        self.filtered_tm_usb_offsets = self.the_tm_usb_offsets.transformed(self.aafilter)
        self.filtered_tm_usb_fluctuations = self.the_tm_usb_fluctuations.transformed(self.aafilter)
        self.filtered_tm_usbs = self.the_tm_usbs.transformed(self.aafilter)

        logger.debug("Filtering reference beatnotes")
        self.filtered_ref_carrier_offsets = self.the_ref_carrier_offsets.transformed(self.aafilter)
        self.filtered_ref_carrier_fluctuations = self.the_ref_carrier_fluctuations.transformed(self.aafilter)
        self.filtered_ref_carriers = self.the_ref_carriers.transformed(self.aafilter)
        self.filtered_ref_usb_offsets = self.the_ref_usb_offsets.transformed(self.aafilter)
        self.filtered_ref_usb_fluctuations = self.the_ref_usb_fluctuations.transformed(self.aafilter)
        self.filtered_ref_usbs = self.the_ref_usbs.transformed(self.aafilter)

        ## Downsampling filtering

        logger.info("Downsampling beatnotes")

        logger.debug("Downsampling inter-spacecraft beatnotes")
        self.isc_carrier_offsets = self.filtered_isc_carrier_offsets.transformed(self.downsampled)
        self.isc_carrier_fluctuations = self.filtered_isc_carrier_fluctuations.transformed(self.downsampled)
        self.isc_carriers = self.filtered_isc_carriers.transformed(self.downsampled)
        self.isc_usb_offsets = self.filtered_isc_usb_offsets.transformed(self.downsampled)
        self.isc_usb_fluctuations = self.filtered_isc_usb_fluctuations.transformed(self.downsampled)
        self.isc_usbs = self.filtered_isc_usbs.transformed(self.downsampled)

        logger.debug("Downsampling inter-spacecraft DWS measurements")
        self.isc_dws_phis = self.filtered_isc_dws_phis.transformed(self.downsampled)
        self.isc_dws_etas = self.filtered_isc_dws_etas.transformed(self.downsampled)

        logger.debug("Downsampling measured pseudo-ranges")
        self.mprs = self.filtered_mprs.transformed(self.downsampled)

        logger.debug("Downsampling test-mass beatnotes")
        self.tm_carrier_offsets = self.filtered_tm_carrier_offsets.transformed(self.downsampled)
        self.tm_carrier_fluctuations = self.filtered_tm_carrier_fluctuations.transformed(self.downsampled)
        self.tm_carriers = self.filtered_tm_carriers.transformed(self.downsampled)
        self.tm_usb_offsets = self.filtered_tm_usb_offsets.transformed(self.downsampled)
        self.tm_usb_fluctuations = self.filtered_tm_usb_fluctuations.transformed(self.downsampled)
        self.tm_usbs = self.filtered_tm_usbs.transformed(self.downsampled)

        logger.debug("Downsampling reference beatnotes")
        self.ref_carrier_offsets = self.filtered_ref_carrier_offsets.transformed(self.downsampled)
        self.ref_carrier_fluctuations = self.filtered_ref_carrier_fluctuations.transformed(self.downsampled)
        self.ref_carriers = self.filtered_ref_carriers.transformed(self.downsampled)
        self.ref_usb_offsets = self.filtered_ref_usb_offsets.transformed(self.downsampled)
        self.ref_usb_fluctuations = self.filtered_ref_usb_fluctuations.transformed(self.downsampled)
        self.ref_usbs = self.filtered_ref_usbs.transformed(self.downsampled)

        ## Closing simulation
        logger.info("Simulation complete")

    def simulate_noises(self):
        """Generate noise time series."""

        ## Laser noise
        # Laser noise are only generated for lasers locked on cavities,
        # in `simulate_locking.lock_on_cavity()`

        self.laser_noises = ForEachMOSA(None)

        ## Clock noise

        logger.info("Generating clock noise")

        if self.clock_freqlindrifts == self.clock_freqquaddrifts == 0:
            # Optimize to use a scalar if we only have a constant frequency offset
            logger.debug("Generating clock noise offsets as constant frequency offsets")
            self.clock_noise_offsets = self.clock_freqoffsets
        else:
            logger.debug("Generating clock noise offsets")
            t = self.physics_t
            self.clock_noise_offsets = \
                self.clock_freqoffsets \
                + self.clock_freqlindrifts * t \
                + self.clock_freqquaddrifts * t**2

        logger.debug("Generating clock noise fluctuations")
        self.clock_noise_fluctuations = ForEachSC(lambda sc:
            noises.clock(self.physics_fs, self.physics_size, self.clock_asds[sc])
        )

        ## Modulation noise

        logger.info("Generating modulation noise")
        self.modulation_noises = ForEachMOSA(lambda mosa:
            noises.modulation(self.physics_fs, self.physics_size, self.modulation_asds[mosa])
        )

        ## Backlink noise

        logger.info("Generating backlink noise")
        self.backlink_noises = ForEachMOSA(lambda mosa:
            noises.backlink(self.physics_fs, self.physics_size,
                self.backlink_asds[mosa], self.backlink_fknees[mosa])
        )

        ## Test-mass acceleration noise

        logger.info("Generating test-mass acceleration noise")
        self.testmass_noises = ForEachMOSA(lambda mosa:
            noises.testmass(self.physics_fs, self.physics_size,
                self.testmass_asds[mosa], self.testmass_fknees[mosa])
        )

        ## Ranging noise

        logger.info("Generating ranging noise")
        self.ranging_noises = ForEachMOSA(lambda mosa:
            self.ranging_biases[mosa] + noises.ranging(self.physics_fs,
                self.physics_size, self.ranging_asds[mosa])
        )

        ## OMS noise

        logger.info("Generating OMS noise")

        self.oms_isc_carrier_noises = ForEachMOSA(lambda mosa:
            noises.oms(self.physics_fs, self.physics_size,
                self.oms_isc_carrier_asds[mosa], self.oms_fknees[mosa])
        )

        self.oms_isc_usb_noises = ForEachMOSA(lambda mosa:
            noises.oms(self.physics_fs, self.physics_size,
                self.oms_isc_usb_asds[mosa], self.oms_fknees[mosa])
        )

        self.oms_tm_carrier_noises = ForEachMOSA(lambda mosa:
            noises.oms(self.physics_fs, self.physics_size,
                self.oms_tm_carrier_asds[mosa], self.oms_fknees[mosa])
        )

        self.oms_tm_usb_noises = ForEachMOSA(lambda mosa:
            noises.oms(self.physics_fs, self.physics_size,
                self.oms_tm_usb_asds[mosa], self.oms_fknees[mosa])
        )

        self.oms_ref_carrier_noises = ForEachMOSA(lambda mosa:
            noises.oms(self.physics_fs, self.physics_size,
                self.oms_ref_carrier_asds[mosa], self.oms_fknees[mosa])
        )

        self.oms_ref_usb_noises = ForEachMOSA(lambda mosa:
            noises.oms(self.physics_fs, self.physics_size,
                self.oms_ref_usb_asds[mosa], self.oms_fknees[mosa])
        )

        ## DWS measurement noise

        logger.info("Generating DWS measurement noise")

        self.dws_phi_noises = ForEachMOSA(lambda mosa:
            noises.dws(self.physics_fs, self.physics_size, self.dws_asds[mosa])
        )
        self.dws_eta_noises = ForEachMOSA(lambda mosa:
            noises.dws(self.physics_fs, self.physics_size, self.dws_asds[mosa])
        )

        ## Angular jitters

        logger.info("Generating spacecraft angular jitters")

        self.sc_jitter_phis = ForEachSC(lambda sc:
            noises.jitter(self.physics_fs, self.physics_size, self.sc_jitter_phi_asds[sc])
        )
        self.sc_jitter_etas = ForEachSC(lambda sc:
            noises.jitter(self.physics_fs, self.physics_size, self.sc_jitter_eta_asds[sc])
        )
        self.sc_jitter_thetas = ForEachSC(lambda sc:
            noises.jitter(self.physics_fs, self.physics_size, self.sc_jitter_theta_asds[sc])
        )

        logger.info("Generating MOSA angular jitters")

        self.mosa_jitter_phis = ForEachMOSA(lambda mosa:
            noises.jitter(self.physics_fs, self.physics_size, self.mosa_jitter_phi_asds[mosa])
        )

        logger.info("Computing MOSA total angular jitters")

        self.mosa_total_jitter_phis = self.sc_jitter_phis.for_each_mosa() + self.mosa_jitter_phis
        cos_mosa_angles = (self.mosa_angles * numpy.pi / 180).transformed(lambda _, x: numpy.cos(x))
        sin_mosa_angles = (self.mosa_angles * numpy.pi / 180).transformed(lambda _, x: numpy.sin(x))
        self.mosa_total_jitter_etas = \
             cos_mosa_angles * self.sc_jitter_etas.for_each_mosa() \
             + sin_mosa_angles * self.sc_jitter_thetas.for_each_mosa()

        ## Tilt-to-length coupling
        ## TTL couplings are defined as velocities [m/s]

        logger.info("Computing tilt-to-length couplings")

        logger.debug("Computing local tilt-to-length couplings")
        self.local_ttls = \
         self.ttl_coeffs_local_phis * self.mosa_total_jitter_phis \
         + self.ttl_coeffs_local_etas * self.mosa_total_jitter_etas

        logger.debug("Computing unpropagated distant tilt-to-length couplings")
        self.distant_ttls = \
         self.ttl_coeffs_distant_phis * self.mosa_total_jitter_phis \
         + self.ttl_coeffs_distant_etas * self.mosa_total_jitter_etas

    def lock_on_cavity(self, mosa):
        """Compute carrier and upper sideband offsets and fluctuations for laser locked on cavity.

        We generate laser noises for lasers locked on cavities here.

        Args:
            mosa: laser index
        """
        sc = ForEachMOSA.sc

        logger.info("Generating laser noise for laser %s", mosa)
        self.laser_noises[mosa] = noises.laser(self.physics_fs, self.physics_size, self.laser_asds[mosa])

        logger.debug("Computing carrier offsets for primary local beam %s", mosa)
        self.local_carrier_offsets[mosa] = self.offsets_freqs[mosa]

        logger.debug("Computing carrier fluctuations for primary local beam %s", mosa)
        self.local_carrier_fluctuations[mosa] = \
            self.laser_noises[mosa] + self.glitch_lasers[mosa] + self.tdir_tones[mosa]

        logger.debug("Computing upper sideband offsets for primary local beam %s", mosa)
        self.local_usb_offsets[mosa] = self.offsets_freqs[mosa] \
            + self.modulation_freqs[mosa] * (1 + self.clock_noise_offsets[sc(mosa)])

        logger.debug("Computing upper sideband fluctuations for primary local beam %s", mosa)
        self.local_usb_fluctuations[mosa] = \
            self.laser_noises[mosa] + self.glitch_lasers[mosa] + self.tdir_tones[mosa] \
            + self.modulation_freqs[mosa] * (self.clock_noise_fluctuations[sc(mosa)] + self.modulation_noises[mosa])

    def lock_on_adjacent(self, mosa):
        """Compute carrier and upper sideband offsets and fluctuations for laser locked to adjacent beam.

        Args:
            mosa: laser index
        """
        sc = ForEachMOSA.sc
        adjacent = ForEachMOSA.adjacent_mosa

        logger.debug("Computing carrier offsets for local beam %s "
                     "locked on adjacent beam %s", mosa, adjacent(mosa))
        self.local_carrier_offsets[mosa] = \
            self.local_carrier_offsets[adjacent(mosa)] \
            + self.offsets_freqs[mosa] * (1 + self.clock_noise_offsets[sc(mosa)])

        logger.debug("Computing carrier fluctuations for local beam %s "
                     "locked on adjacent beam %s", mosa, adjacent(mosa))
        adjacent_carrier_fluctuations = self.local_carrier_fluctuations[adjacent(mosa)] \
            + self.central_freq * self.backlink_noises[mosa]
        self.local_carrier_fluctuations[mosa] = adjacent_carrier_fluctuations \
            + self.offsets_freqs[mosa] * self.clock_noise_fluctuations[sc(mosa)] \
            + self.central_freq * self.oms_ref_carrier_noises[mosa] \
            + self.tdir_tones[mosa]

        logger.debug("Computing upper sideband offsets for local beam %s "
                     "locked on adjacent beam %s", mosa, adjacent(mosa))
        self.local_usb_offsets[mosa] = \
            self.local_usb_offsets[adjacent(mosa)] \
            + self.offsets_freqs[mosa] * (1 + self.clock_noise_offsets[sc(mosa)])

        logger.debug("Computing upper sideband fluctuations for local beam %s "
                     "locked on adjacent beam %s", mosa, adjacent(mosa))
        adjacent_usb_fluctuations = self.local_usb_fluctuations[adjacent(mosa)] \
            + self.central_freq * self.backlink_noises[mosa]
        self.local_usb_fluctuations[mosa] = adjacent_usb_fluctuations \
            + self.offsets_freqs[mosa] * self.clock_noise_fluctuations[sc(mosa)] \
            + self.central_freq * self.oms_ref_usb_noises[mosa] \
            + self.tdir_tones[mosa]

    def lock_on_distant(self, mosa):
        """Compute carrier and upper sideband offsets and fluctuations for locked laser to distant beam.

        Args:
            mosa: laser index
        """
        sc = ForEachMOSA.sc
        distant = ForEachMOSA.distant_mosa

        logger.debug("Computing carrier offsets for local beam %s "
                     "locked on distant beam %s", mosa, distant(mosa))
        carrier_offsets = self.local_carrier_offsets[distant(mosa)]
        distant_carrier_offsets = \
            -self.d_pprs[mosa] * self.central_freq \
            + (1 - self.d_pprs[mosa]) * self.interpolate(carrier_offsets, -self.pprs[mosa])
        self.local_carrier_offsets[mosa] = distant_carrier_offsets \
            + self.offsets_freqs[mosa] * (1 + self.clock_noise_offsets[sc(mosa)])

        logger.debug("Computing carrier fluctuations for local beam %s "
                     "locked on distant beam %s", mosa, distant(mosa))
        carrier_fluctuations = \
            self.local_carrier_fluctuations[distant(mosa)] \
            - (self.central_freq + self.local_carrier_offsets[distant(mosa)]) \
                * self.distant_ttls[distant(mosa)] / c
        distant_carrier_fluctuations = \
            (1 - self.d_pprs[mosa]) * self.interpolate(carrier_fluctuations, -self.pprs[mosa]) \
            + self.central_freq * self.gws[mosa] \
            - (self.central_freq + self.local_carrier_offsets[mosa]) * self.local_ttls[mosa] / c
        self.local_carrier_fluctuations[mosa] = distant_carrier_fluctuations \
            + self.offsets_freqs[mosa] * self.clock_noise_fluctuations[sc(mosa)] \
            + self.central_freq * self.oms_isc_carrier_noises[mosa] \
            + self.tdir_tones[mosa]

        logger.debug("Computing upper sideband offsets for local beam %s "
                     "locked on distant beam %s", mosa, distant(mosa))
        usb_offsets = self.local_usb_offsets[distant(mosa)]
        distant_usb_offsets = \
            -self.d_pprs[mosa] * self.central_freq \
            + (1 - self.d_pprs[mosa]) * self.interpolate(usb_offsets, -self.pprs[mosa])
        self.local_usb_offsets[mosa] = distant_usb_offsets \
            + self.offsets_freqs[mosa] * (1 + self.clock_noise_offsets[sc(mosa)])

        logger.debug("Computing upper sideband fluctuations for local beam %s "
                     "locked on distant beam %s", mosa, distant(mosa))
        usb_fluctuations = \
            self.local_usb_fluctuations[distant(mosa)] \
            - (self.central_freq + self.local_usb_offsets[distant(mosa)]) \
                * self.distant_ttls[distant(mosa)] / c
        distant_usb_fluctuations = \
            + (1 - self.d_pprs[mosa]) * self.interpolate(usb_fluctuations, -self.pprs[mosa]) \
            + self.central_freq * self.gws[mosa] \
            - (self.central_freq + self.local_usb_offsets[mosa]) * self.local_ttls[mosa] / c
        self.local_usb_fluctuations[mosa] = distant_usb_fluctuations \
            + self.offsets_freqs[mosa] * self.clock_noise_fluctuations[sc(mosa)] \
            + self.central_freq * self.oms_isc_usb_noises[mosa] \
            + self.tdir_tones[mosa]

    def simulate_locking(self):
        """Simulate local beams from the locking configuration."""
        # pylint: disable=too-many-statements
        adjacent = ForEachMOSA.adjacent_mosa
        distant = ForEachMOSA.distant_mosa

        self.local_carrier_offsets = ForEachMOSA(None)
        self.local_carrier_fluctuations = ForEachMOSA(None)
        self.local_usb_offsets = ForEachMOSA(None)
        self.local_usb_fluctuations = ForEachMOSA(None)

        # Transform the lock dictionary into a dependency dictionary
        dependencies = {}
        logger.debug("Computing laser locking dependencies")
        for mosa, lock_type in self.lock.items():
            if lock_type == 'cavity':
                dependencies[mosa] = None
            elif lock_type == 'adjacent':
                dependencies[mosa] = adjacent(mosa)
            elif lock_type == 'distant':
                dependencies[mosa] = distant(mosa)
            else:
                raise ValueError(f"invalid locking type '{self.lock[mosa]}' for laser '{mosa}'")
        logger.debug("Laser locking dependencies read: %s", dependencies)

        # Apply locking conditions in order
        logger.debug("Applying locking conditions")
        just_locked = [None]
        while dependencies:
            being_locked = []
            for mosa in [mosa for mosa in dependencies if dependencies[mosa] in just_locked]:
                if self.lock[mosa] == 'cavity':
                    logger.debug("Locking laser %s on cavity", mosa)
                    self.lock_on_cavity(mosa)
                elif self.lock[mosa] == 'adjacent':
                    logger.debug("Locking laser %s on adjacent laser %s", mosa, adjacent(mosa))
                    self.lock_on_adjacent(mosa)
                elif self.lock[mosa] == 'distant':
                    logger.debug("Locking laser %s on distant laser %s", mosa, distant(mosa))
                    self.lock_on_distant(mosa)
                else:
                    raise ValueError(f"invalid locking type '{self.lock[mosa]}' for laser '{mosa}'")
                being_locked.append(mosa)
                del dependencies[mosa]
            just_locked = being_locked
            if not just_locked:
                raise RuntimeError(f"cannot apply locking conditions to remaining lasers '{list(dependencies.keys())}'")

    def invert_timer_deviations(self, timer_deviations, sc):
        """Invert timer deviations of a given spacecraft.

        We recursively solve the implicit equation dtau(tau) = dtau_hat(tau - dtau(tau)) until the
        convergence criteria (tolerance) is met, or we exceed the maximum number of iterations.

        Args:
            timer_deviations: array of timer deviations
            sc: spacecraft index
        """
        logger.debug("Inverting timer deviations for spacecraft %s", sc)
        logger.debug("Solving iteratively (tolerance=%s s, maxiter=%s)",
            self.clockinv_tolerance, self.clockinv_maxiter)

        niter = 0
        error = 0
        edge = 100 # drop samples at the edges to check convergence
        next_inverse = timer_deviations
        while not niter or error > self.clockinv_tolerance:
            if niter >= self.clockinv_maxiter:
                logger.warning("Maximum number of iterations '%s' reached for SC %s (error=%.2E)", niter, sc, error)
                break
            logger.debug("Starting iteration #%s", niter)
            inverse = next_inverse
            next_inverse = self.interpolate(timer_deviations, -inverse)
            error = numpy.max(numpy.abs((inverse - next_inverse)[edge:-edge]))
            logger.debug("End of iteration %s, with an error of %.2E s", niter, error)
            niter += 1
        logger.debug("End of timer deviation inversion after %s iterations with an error of %.2E s", niter, error)
        return inverse

    def write_metadata(self, hdf5):
        """Set all properties as HDF5 attributes on `object`.

        Args:
            hdf5: an HDF5 file, or a dataset
        """
        for key, value in self.__dict__.items():
            try:
                hdf5.attrs[key] = value
            except (TypeError, RuntimeError):
                try:
                    hdf5.attrs[key] = str(value)
                except RuntimeError:
                    logger.warning("Cannot write metadata '%s' on '%s'", key, hdf5)

    def write(self, output='measurements.h5', mode='w-', write_all=False):
        """Run a simulation.

        Args:
            output: path to measurement file
            mode: measurement file opening mode
            write_all: whether to write all quantities to file
        """
        # pylint: disable=too-many-statements
        hdf5 = h5py.File(output, mode)
        if not self.simulated:
            self.simulate(keep_all=write_all)

        logger.info("Writing simulation to '%s'", output)
        logger.debug("Writing metadata and physics time dataset to '%s'", output)

        self.write_metadata(hdf5)
        hdf5['physics_t'] = self.physics_t

        if write_all:

            logger.debug("Writing proper pseudo-ranges to '%s'", output)
            self.pprs.write(hdf5, 'pprs')
            self.d_pprs.write(hdf5, 'd_pprs')

            logger.debug("Writing gravitational-wave responses to '%s'", output)
            self.gws.write(hdf5, 'gws')

            logger.debug("Writing glitch signals to '%s'", output)
            self.glitch_tms.write(hdf5, 'glitch_tms')
            self.glitch_lasers.write(hdf5, 'glitch_lasers')

            logger.debug("Writing TDIR assistance tone to %s", output)
            self.tdir_tones.write(hdf5, 'tdir_tones')

            logger.debug("Writing laser noise to '%s'", output)
            self.laser_noises.write(hdf5, 'laser_noises')

            logger.debug("Writing clock noise to '%s'", output)
            self.clock_noise_offsets.write(hdf5, 'clock_noise_offsets')
            self.clock_noise_fluctuations.write(hdf5, 'clock_noise_fluctuations')

            logger.debug("Writing modulation noise to '%s'", output)
            self.modulation_noises.write(hdf5, 'modulation_noises')

            logger.debug("Writing backlink noise to '%s'", output)
            self.backlink_noises.write(hdf5, 'backlink_noises')

            logger.debug("Writing test-mass acceleration noise to '%s'", output)
            self.testmass_noises.write(hdf5, 'testmass_noises')

            logger.debug("Writing ranging noise to '%s'", output)
            self.ranging_noises.write(hdf5, 'ranging_noises')

            logger.debug("Writing OMS noise to '%s'", output)
            self.oms_isc_carrier_noises.write(hdf5, 'oms_isc_carrier_noises')
            self.oms_isc_usb_noises.write(hdf5, 'oms_isc_usb_noises')
            self.oms_tm_carrier_noises.write(hdf5, 'oms_tm_carrier_noises')
            self.oms_tm_usb_noises.write(hdf5, 'oms_tm_usb_noises')
            self.oms_ref_carrier_noises.write(hdf5, 'oms_ref_carrier_noises')
            self.oms_ref_usb_noises.write(hdf5, 'oms_ref_usb_noises')

            logger.debug("Writing spacecraft angular jitter to '%s'", output)
            self.sc_jitter_phis.write(hdf5, 'sc_jitter_phis')
            self.sc_jitter_etas.write(hdf5, 'sc_jitter_etas')
            self.sc_jitter_thetas.write(hdf5, 'sc_jitter_thetas')

            logger.debug("Writing MOSA angular jitter to '%s'", output)
            self.mosa_jitter_phis.write(hdf5, 'mosa_jitter_phis')

            logger.debug("Writing MOSA total angular jitter to '%s'", output)
            self.mosa_total_jitter_phis.write(hdf5, 'mosa_total_jitter_phis')
            self.mosa_total_jitter_etas.write(hdf5, 'mosa_total_jitter_etas')

            logger.debug("Writing local beams to '%s'", output)
            self.local_carrier_offsets.write(hdf5, 'local_carrier_offsets')
            self.local_carrier_fluctuations.write(hdf5, 'local_carrier_fluctuations')
            self.local_usb_offsets.write(hdf5, 'local_usb_offsets')
            self.local_usb_fluctuations.write(hdf5, 'local_usb_fluctuations')

            logger.debug("Writing local timer deviations to '%s'", output)
            self.local_timer_deviations.write(hdf5, 'local_timer_deviations')

            logger.debug("Writing tilt-to-length couplings to '%s'", output)
            self.local_ttls.write(hdf5, 'local_ttls')
            self.distant_ttls.write(hdf5, 'distant_ttls')

            logger.debug("Writing propagated distant beams to '%s'", output)
            self.distant_carrier_offsets.write(hdf5, 'distant_carrier_offsets')
            self.distant_carrier_fluctuations.write(hdf5, 'distant_carrier_fluctuations')
            self.distant_usb_offsets.write(hdf5, 'distant_usb_offsets')
            self.distant_usb_fluctuations.write(hdf5, 'distant_usb_fluctuations')

            logger.debug("Writing propagated timer deviations to '%s'", output)
            self.distant_timer_deviations.write(hdf5, 'distant_timer_deviations')

            logger.debug("Writing propagated adjacent beams to '%s'", output)
            self.adjacent_carrier_offsets.write(hdf5, 'adjacent_carrier_offsets')
            self.adjacent_carrier_fluctuations.write(hdf5, 'adjacent_carrier_fluctuations')
            self.adjacent_usb_offsets.write(hdf5, 'adjacent_usb_offsets')
            self.adjacent_usb_fluctuations.write(hdf5, 'adjacent_usb_fluctuations')

            logger.debug("Writing local beams at inter-spacecraft interferometer to '%s'", output)
            self.local_isc_carrier_offsets.write(hdf5, 'local_isc_carrier_offsets')
            self.local_isc_carrier_fluctuations.write(hdf5, 'local_isc_carrier_fluctuations')
            self.local_isc_usb_offsets.write(hdf5, 'local_isc_usb_offsets')
            self.local_isc_usb_fluctuations.write(hdf5, 'local_isc_usb_fluctuations')

            logger.debug("Writing distant beams at inter-spacecraft interferometer to '%s'", output)
            self.distant_isc_carrier_offsets.write(hdf5, 'distant_isc_carrier_offsets')
            self.distant_isc_carrier_fluctuations.write(hdf5, 'distant_isc_carrier_fluctuations')
            self.distant_isc_usb_offsets.write(hdf5, 'distant_isc_usb_offsets')
            self.distant_isc_usb_fluctuations.write(hdf5, 'distant_isc_usb_fluctuations')

            logger.debug("Writing inter-spacecraft beatnotes on TPS to '%s'", output)
            self.tps_isc_carrier_offsets.write(hdf5, 'tps_isc_carrier_offsets')
            self.tps_isc_carrier_fluctuations.write(hdf5, 'tps_isc_carrier_fluctuations')
            self.tps_isc_usb_offsets.write(hdf5, 'tps_isc_usb_offsets')
            self.tps_isc_usb_fluctuations.write(hdf5, 'tps_isc_usb_fluctuations')

            logger.debug("Writing inter-spacecraft DWS measurements on TPS to '%s'", output)
            self.tps_isc_dws_phis.write(hdf5, 'tps_isc_dws_phis')
            self.tps_isc_dws_etas.write(hdf5, 'tps_isc_dws_etas')

            logger.debug("Writing measured pseudo-ranges on TPS to '%s'", output)
            self.tps_mprs.write(hdf5, 'tps_mprs')

            logger.debug("Writing local beams at test-mass interferometer to '%s'", output)
            self.local_tm_carrier_offsets.write(hdf5, 'local_tm_carrier_offsets')
            self.local_tm_carrier_fluctuations.write(hdf5, 'local_tm_carrier_fluctuations')
            self.local_tm_usb_offsets.write(hdf5, 'local_tm_usb_offsets')
            self.local_tm_usb_fluctuations.write(hdf5, 'local_tm_usb_fluctuations')

            logger.debug("Writing adjacent beams at test-mass interferometer to '%s'", output)
            self.adjacent_tm_carrier_offsets.write(hdf5, 'adjacent_tm_carrier_offsets')
            self.adjacent_tm_carrier_fluctuations.write(hdf5, 'adjacent_tm_carrier_fluctuations')
            self.adjacent_tm_usb_offsets.write(hdf5, 'adjacent_tm_usb_offsets')
            self.adjacent_tm_usb_fluctuations.write(hdf5, 'adjacent_tm_usb_fluctuations')

            logger.debug("Writing test-mass beatnotes on TPS to '%s'", output)
            self.tps_tm_carrier_offsets.write(hdf5, 'tps_tm_carrier_offsets')
            self.tps_tm_carrier_fluctuations.write(hdf5, 'tps_tm_carrier_fluctuations')
            self.tps_tm_usb_offsets.write(hdf5, 'tps_tm_usb_offsets')
            self.tps_tm_usb_fluctuations.write(hdf5, 'tps_tm_usb_fluctuations')

            logger.debug("Writing local beams at reference interferometer to '%s'", output)
            self.local_ref_carrier_offsets.write(hdf5, 'local_ref_carrier_offsets')
            self.local_ref_carrier_fluctuations.write(hdf5, 'local_ref_carrier_fluctuations')
            self.local_ref_usb_offsets.write(hdf5, 'local_ref_usb_offsets')
            self.local_ref_usb_fluctuations.write(hdf5, 'local_ref_usb_fluctuations')

            logger.debug("Writing adjacent beams at reference interferometer to '%s'", output)
            self.adjacent_ref_carrier_offsets.write(hdf5, 'adjacent_ref_carrier_offsets')
            self.adjacent_ref_carrier_fluctuations.write(hdf5, 'adjacent_ref_carrier_fluctuations')
            self.adjacent_ref_usb_offsets.write(hdf5, 'adjacent_ref_usb_offsets')
            self.adjacent_ref_usb_fluctuations.write(hdf5, 'adjacent_ref_usb_fluctuations')

            logger.debug("Writing reference beatnotes on TPS to '%s'", output)
            self.tps_ref_carrier_offsets.write(hdf5, 'tps_ref_carrier_offsets')
            self.tps_ref_carrier_fluctuations.write(hdf5, 'tps_ref_carrier_fluctuations')
            self.tps_ref_usb_offsets.write(hdf5, 'tps_ref_usb_offsets')
            self.tps_ref_usb_fluctuations.write(hdf5, 'tps_ref_usb_fluctuations')

            logger.debug("Writing inverted timer deviations to '%s'", output)
            self.inverse_timer_deviations.write(hdf5, 'inverse_timer_deviations')

            logger.debug("Writing inter-spacecraft beatnotes sampled to THE grid to '%s'", output)
            self.the_isc_carrier_offsets.write(hdf5, 'the_isc_carrier_offsets')
            self.the_isc_carrier_fluctuations.write(hdf5, 'the_isc_carrier_fluctuations')
            self.the_isc_usb_offsets.write(hdf5, 'the_isc_usb_offsets')
            self.the_isc_usb_fluctuations.write(hdf5, 'the_isc_usb_fluctuations')

            logger.debug("Writing inter-spacecraft DWS measurements sampled to THE grid to '%s'", output)
            self.the_isc_dws_phis.write(hdf5, 'the_isc_dws_phis')
            self.the_isc_dws_etas.write(hdf5, 'the_isc_dws_etas')

            logger.debug("Writing measured pseudo-ranges sampled to THE grid to '%s'", output)
            self.the_mprs.write(hdf5, 'the_mprs')

            logger.debug("Writing test-mass beatnotes sampled to THE grid to '%s'", output)
            self.the_tm_carrier_offsets.write(hdf5, 'the_tm_carrier_offsets')
            self.the_tm_carrier_fluctuations.write(hdf5, 'the_tm_carrier_fluctuations')
            self.the_tm_usb_offsets.write(hdf5, 'the_tm_usb_offsets')
            self.the_tm_usb_fluctuations.write(hdf5, 'the_tm_usb_fluctuations')

            logger.debug("Writing reference beatnotes sampled to THE grid to '%s'", output)
            self.the_ref_carrier_offsets.write(hdf5, 'the_ref_carrier_offsets')
            self.the_ref_carrier_fluctuations.write(hdf5, 'the_ref_carrier_fluctuations')
            self.the_ref_usb_offsets.write(hdf5, 'the_ref_usb_offsets')
            self.the_ref_usb_fluctuations.write(hdf5, 'the_ref_usb_fluctuations')

            logger.debug("Writing total beatnote frequencies to '%s'", output)
            self.the_isc_carriers.write(hdf5, 'the_isc_carriers')
            self.the_isc_usbs.write(hdf5, 'the_isc_usbs')
            self.the_tm_carriers.write(hdf5, 'the_tm_carriers')
            self.the_tm_usbs.write(hdf5, 'the_tm_usbs')
            self.the_ref_carriers.write(hdf5, 'the_ref_carriers')
            self.the_ref_usbs.write(hdf5, 'the_ref_usbs')

            logger.debug("Writing filtered inter-spacecraft beatnotes to '%s'", output)
            self.filtered_isc_carrier_offsets.write(hdf5, 'filtered_isc_carrier_offsets')
            self.filtered_isc_carrier_fluctuations.write(hdf5, 'filtered_isc_carrier_fluctuations')
            self.filtered_isc_carriers.write(hdf5, 'filtered_isc_carriers')
            self.filtered_isc_usb_offsets.write(hdf5, 'filtered_isc_usb_offsets')
            self.filtered_isc_usb_fluctuations.write(hdf5, 'filtered_isc_usb_fluctuations')
            self.filtered_isc_usbs.write(hdf5, 'filtered_isc_usbs')

            logger.debug("Writing filtered inter-spacecraft DWS measurements to '%s'", output)
            self.filtered_isc_dws_phis.write(hdf5, 'filtered_isc_dws_phis')
            self.filtered_isc_dws_etas.write(hdf5, 'filtered_isc_dws_etas')

            logger.debug("Writing filtered measured pseudo-ranges to '%s'", output)
            self.filtered_mprs.write(hdf5, 'filtered_mprs')

            logger.debug("Writing filtered test-mass beatnotes to '%s'", output)
            self.filtered_tm_carrier_offsets.write(hdf5, 'filtered_tm_carrier_offsets')
            self.filtered_tm_carrier_fluctuations.write(hdf5, 'filtered_tm_carrier_fluctuations')
            self.filtered_tm_carriers.write(hdf5, 'filtered_tm_carriers')
            self.filtered_tm_usb_offsets.write(hdf5, 'filtered_tm_usb_offsets')
            self.filtered_tm_usb_fluctuations.write(hdf5, 'filtered_tm_usb_fluctuations')
            self.filtered_tm_usbs.write(hdf5, 'filtered_tm_usbs')

            logger.debug("Writing filtered reference beatnotes to '%s'", output)
            self.filtered_ref_carrier_offsets.write(hdf5, 'filtered_ref_carrier_offsets')
            self.filtered_ref_carrier_fluctuations.write(hdf5, 'filtered_ref_carrier_fluctuations')
            self.filtered_ref_carriers.write(hdf5, 'filtered_ref_carriers')
            self.filtered_ref_usb_offsets.write(hdf5, 'filtered_ref_usb_offsets')
            self.filtered_ref_usb_fluctuations.write(hdf5, 'filtered_ref_usb_fluctuations')
            self.filtered_ref_usbs.write(hdf5, 'filtered_ref_usbs')

        logger.debug("Writing downsampled inter-spacecraft beatnotes to '%s'", output)
        self.isc_carrier_offsets.write(hdf5, 'isc_carrier_offsets')
        self.isc_carrier_fluctuations.write(hdf5, 'isc_carrier_fluctuations')
        self.isc_carriers.write(hdf5, 'isc_carriers')
        self.isc_usb_offsets.write(hdf5, 'isc_usb_offsets')
        self.isc_usb_fluctuations.write(hdf5, 'isc_usb_fluctuations')
        self.isc_usbs.write(hdf5, 'isc_usbs')

        logger.debug("Writing downsampled inter-spacecraft DWS measurements to '%s'", output)
        self.isc_dws_phis.write(hdf5, 'isc_dws_phis')
        self.isc_dws_etas.write(hdf5, 'isc_dws_etas')

        logger.debug("Writing downsampled measured pseudo-ranges to '%s'", output)
        self.mprs.write(hdf5, 'mprs')

        logger.debug("Writing downsampled test-mass beatnotes to '%s'", output)
        self.tm_carrier_offsets.write(hdf5, 'tm_carrier_offsets')
        self.tm_carrier_fluctuations.write(hdf5, 'tm_carrier_fluctuations')
        self.tm_carriers.write(hdf5, 'tm_carriers')
        self.tm_usb_offsets.write(hdf5, 'tm_usb_offsets')
        self.tm_usb_fluctuations.write(hdf5, 'tm_usb_fluctuations')
        self.tm_usbs.write(hdf5, 'tm_usbs')

        logger.debug("Writing downsampled reference beatnotes to '%s'", output)
        self.ref_carrier_offsets.write(hdf5, 'ref_carrier_offsets')
        self.ref_carrier_fluctuations.write(hdf5, 'ref_carrier_fluctuations')
        self.ref_carriers.write(hdf5, 'ref_carriers')
        self.ref_usb_offsets.write(hdf5, 'ref_usb_offsets')
        self.ref_usb_fluctuations.write(hdf5, 'ref_usb_fluctuations')
        self.ref_usbs.write(hdf5, 'ref_usbs')

        logger.info("Closing measurement file '%s'", output)
        hdf5.close()

    def plot_fluctuations(self, output=None, skip=0):
        """Plot beatnote frequency fluctuations generated by the simulation.

        Args:
            output: output file, None to show the plots
            skip: number of initial samples to skip [samples]
        """
        # Run simulation if needed
        if not self.simulated:
            self.simulate()
        # Plot signals
        logger.info("Plotting beatnote frequency fluctuations")
        _, axes = matplotlib.pyplot.subplots(3, 1, figsize=(16, 18))
        plot = lambda axis, x, label: axis.plot(self.t[skip:], numpy.broadcast_to(x, self.size)[skip:], label=label)
        for mosa in self.MOSAS:
            plot(axes[0], self.isc_carrier_fluctuations[mosa], mosa)
            plot(axes[1], self.tm_carrier_fluctuations[mosa], mosa)
            plot(axes[2], self.ref_carrier_fluctuations[mosa], mosa)
        # Format plot
        axes[0].set_title("Beatnote frequency fluctuations")
        axes[2].set_xlabel("Time [s]")
        axes[0].set_ylabel("Inter-spacecraft frequency [Hz]")
        axes[1].set_ylabel("Test-mass frequency [Hz]")
        axes[2].set_ylabel("Reference frequency [Hz]")
        for axis in axes:
            axis.grid()
            axis.legend()
        # Save or show glitch
        if output is not None:
            logger.info("Saving plot to %s", output)
            matplotlib.pyplot.savefig(output, bbox_inches='tight')
        else:
            matplotlib.pyplot.show()

    def plot_offsets(self, output=None, skip=0):
        """Plot beatnote frequency offsets generated by the simulation.

        Args:
            output: output file, None to show the plots
            skip: number of initial samples to skip [samples]
        """
        # Run simulation if needed
        if not self.simulated:
            self.simulate()
        # Plot signals
        logger.info("Plotting beatnote frequency offsets")
        _, axes = matplotlib.pyplot.subplots(3, 1, figsize=(16, 18))
        plot = lambda axis, x, label: axis.plot(self.t[skip:], numpy.broadcast_to(x, self.size)[skip:], label=label)
        for mosa in self.MOSAS:
            plot(axes[0], self.isc_carrier_offsets[mosa], mosa)
            plot(axes[1], self.tm_carrier_offsets[mosa], mosa)
            plot(axes[2], self.ref_carrier_offsets[mosa], mosa)
        # Format plot
        axes[0].set_title("Beatnote frequency offsets")
        axes[2].set_xlabel("Time [s]")
        axes[0].set_ylabel("Inter-spacecraft frequency [Hz]")
        axes[1].set_ylabel("Test-mass frequency [Hz]")
        axes[2].set_ylabel("Reference frequency [Hz]")
        for axis in axes:
            axis.grid()
            axis.legend()
        # Save or show glitch
        if output is not None:
            logger.info("Saving plot to %s", output)
            matplotlib.pyplot.savefig(output, bbox_inches='tight')
        else:
            matplotlib.pyplot.show()

    def plot_totals(self, output=None, skip=0):
        """Plot beatnote total frequencies generated by the simulation.

        Args:
            output: output file, None to show the plots
            skip: number of initial samples to skip [samples]
        """
        # Run simulation if needed
        if not self.simulated:
            self.simulate()
        # Plot signals
        logger.info("Plotting beatnote total frequencies")
        _, axes = matplotlib.pyplot.subplots(3, 1, figsize=(16, 18))
        plot = lambda axis, x, label: axis.plot(self.t[skip:], numpy.broadcast_to(x, self.size)[skip:], label=label)
        for mosa in self.MOSAS:
            plot(axes[0], self.isc_carriers[mosa], mosa)
            plot(axes[1], self.tm_carriers[mosa], mosa)
            plot(axes[2], self.ref_carriers[mosa], mosa)
        # Format plot
        axes[0].set_title("Beatnote total frequencies")
        axes[2].set_xlabel("Time [s]")
        axes[0].set_ylabel("Inter-spacecraft frequency [Hz]")
        axes[1].set_ylabel("Test-mass frequency [Hz]")
        axes[2].set_ylabel("Reference frequency [Hz]")
        for axis in axes:
            axis.grid()
            axis.legend()
        # Save or show glitch
        if output is not None:
            logger.info("Saving plot to %s", output)
            matplotlib.pyplot.savefig(output, bbox_inches='tight')
        else:
            matplotlib.pyplot.show()

    def plot_mprs(self, output=None, skip=0):
        """Plot measured pseudo-ranges (MPRs) generated by the simulation.

        Args:
            output: output file, None to show the plots
            skip: number of initial samples to skip [samples]
        """
        # Run simulation if needed
        if not self.simulated:
            self.simulate()
        # Plot signals
        logger.info("Plotting measured pseudo-ranges")
        _, axes = matplotlib.pyplot.subplots(2, 1, figsize=(16, 12))
        plot = lambda axis, x, label: axis.plot(self.t[skip:], numpy.broadcast_to(x, self.size)[skip:], label=label)
        for mosa in self.MOSAS:
            plot(axes[0], self.mprs[mosa], mosa)
            plot(axes[1], numpy.gradient(self.mprs[mosa], self.dt), mosa)
        # Format plot
        axes[0].set_title("Measured pseudo-ranges")
        axes[1].set_xlabel("Time [s]")
        axes[0].set_ylabel("Pseudo-range [s]")
        axes[1].set_ylabel("Pseudo-range derivative [s/s]")
        for axis in axes:
            axis.grid()
            axis.legend()
        # Save or show glitch
        if output is not None:
            logger.info("Saving plot to %s", output)
            matplotlib.pyplot.savefig(output, bbox_inches='tight')
        else:
            matplotlib.pyplot.show()

    def plot_dws(self, output=None, skip=0):
        """Plot DWS measurements generated by the simulation.

        Args:
            output: output file, None to show the plots
            skip: number of initial samples to skip [samples]
        """
        # Run simulation if needed
        if not self.simulated:
            self.simulate()
        # Plot signals
        logger.info("Plotting DWS measurements")
        _, axes = matplotlib.pyplot.subplots(2, 1, figsize=(16, 12))
        plot = lambda axis, x, label: axis.plot(self.t[skip:], numpy.broadcast_to(x, self.size)[skip:], label=label)
        for mosa in self.MOSAS:
            plot(axes[0], self.isc_dws_phis[mosa], mosa)
            plot(axes[1], self.isc_dws_etas[mosa], mosa)
        # Format plot
        axes[0].set_title("DWS measurements")
        axes[1].set_xlabel("Time [s]")
        axes[0].set_ylabel("ISC Yaw (phi) [rad/s]")
        axes[1].set_ylabel("ISC Pitch (eta) [rad/s]")
        for axis in axes:
            axis.grid()
            axis.legend()
        # Save or show glitch
        if output is not None:
            logger.info("Saving plot to %s", output)
            matplotlib.pyplot.savefig(output, bbox_inches='tight')
        else:
            matplotlib.pyplot.show()
