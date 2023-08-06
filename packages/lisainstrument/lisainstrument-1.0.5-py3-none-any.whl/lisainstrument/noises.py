#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Noises module.

Implements basic random noise generators, and use them to implement instrumental noises.

Authors:
    Jean-Baptiste Bayle <j2b.bayle@gmail.com>
"""

import logging
import numpy
import pyplnoise

from numpy import pi, sqrt
from lisaconstants import c

logger = logging.getLogger(__name__)


def white(fs, size, asd):
    """Generate a white noise.

    Args:
        fs: sampling frequency [Hz]
        size: number of samples [samples]
        asd: amplitude spectral density [/sqrt(Hz)]
    """
    logger.debug("Generating white noise (fs=%s Hz, size=%s, asd=%s)", fs, size, asd)
    if not asd:
        logger.debug("Vanishing power spectral density, bypassing noise generation")
        return 0
    generator = pyplnoise.WhiteNoise(fs, asd**2 / 2)
    return generator.get_series(size)


def powerlaw(fs, size, asd, alpha):
    """Generate a f^(alpha) noise in amplitude, with alpha > -1.

    Pyplnoise natively accepts alpha values between -1 and 0 (in amplitude).

    We extend the domain of validity to positive alpha values by generating noise time series
    corresponding to the nth-order antiderivative of the desired noise (with exponent alpha + n
    valid for direct generation with pyplnoise), and then taking its nth-order numerical derivative.

    When alpha is -1 (resp. 0), we use internally call the optimized `red()` function (resp.
    the `white()` function).

    Args:
        fs: sampling frequency [Hz]
        size: number of samples [samples]
        asd: amplitude spectral density [/sqrt(Hz)]
        alpha: frequency exponent in amplitude [alpha > -1 and alpha != 0]
    """
    logger.debug("Generating power-law noise (fs=%s Hz, size=%s, asd=%s, alpha=%s)", fs, size, asd, alpha)
    if not asd:
        logger.debug("Vanishing power spectral density, bypassing noise generation")
        return 0

    if alpha < -1:
        raise ValueError(f"invalid value for alpha '{alpha}', must be > -1.")
    if alpha == -1:
        return red(fs, size, asd)
    if -1 < alpha < 0:
        generator = pyplnoise.AlphaNoise(fs, 1 / size, fs / 2, -2 * alpha)
        return asd / sqrt(2) * generator.get_series(size)
    if alpha == 0:
        return white(fs, size, asd)

    # Else, generate antiderivative and take numerical derivative
    antiderivative = powerlaw(fs, size, asd / (2 * numpy.pi), alpha - 1)
    return numpy.gradient(antiderivative, 1 / fs)


def violet(fs, size, asd):
    """Generate a violet noise in f in amplitude.

    Args:
        fs: sampling frequency [Hz]
        size: number of samples [samples]
        asd: amplitude spectral density [/sqrt(Hz)]"""
    logger.debug("Generating violet noise (fs=%s Hz, size=%s, asd=%s)", fs, size, asd)
    if not asd:
        logger.debug("Vanishing power spectral density, bypassing noise generation")
        return 0
    white_noise = white(fs, size, asd)
    return numpy.gradient(white_noise, 1 / fs) / (2 * pi)


def pink(fs, size, asd):
    """Generate a pink noise in f^(-1/2) in amplitude.

    Args:
        fs: sampling frequency [Hz]
        size: number of samples [samples]
        asd: amplitude spectral density [/sqrt(Hz)]"""
    logger.debug("Generating pink noise (fs=%s Hz, size=%s, asd=%s)", fs, size, asd)
    if not asd:
        logger.debug("Vanishing power spectral density, bypassing noise generation")
        return 0
    generator = pyplnoise.PinkNoise(fs, 1 / size, fs / 2)
    return asd / sqrt(2) * generator.get_series(size)


def red(fs, size, asd):
    """Generate a red noise (also Brownian or random walk) in f^(-1) in amplitude.

    Args:
        fs: sampling frequency [Hz]
        size: number of samples [samples]
        asd: amplitude spectral density [/sqrt(Hz)]"""
    logger.debug("Generating red noise (fs=%s Hz, size=%s, asd=%s)", fs, size, asd)
    if not asd:
        logger.debug("Vanishing power spectral density, bypassing noise generation")
        return 0
    generator = pyplnoise.RedNoise(fs, 1 / size)
    return asd / sqrt(2) * generator.get_series(size)


def infrared(fs, size, asd):
    """Generate an infrared noise in f^(-2) in amplitude.

    Args:
        fs: sampling frequency [Hz]
        size: number of samples [samples]
        asd: amplitude spectral density [/sqrt(Hz)]"""
    logger.debug("Generating infrared noise (fs=%s Hz, size=%s, asd=%s)", fs, size, asd)
    if not asd:
        logger.debug("Vanishing power spectral density, bypassing noise generation")
        return 0
    red_noise = red(fs, size, asd)
    return numpy.cumsum(red_noise) * (2 * pi / fs)


def laser(fs, size, asd=28.2):
    """Generate laser noise [Hz].

    This is a white noise,

        S_p(f) = asd^2.

    Args:
        asd: amplitude spectral density [Hz/sqrt(Hz)]
    """
    logger.debug("Generating laser noise (fs=%s Hz, size=%s, asd=%s Hz/sqrt(Hz))", fs, size, asd)
    return white(fs, size, asd)


def clock(fs, size, asd=6.32E-14):
    """Generate clock noise fluctuations [ffd].

    The power spectral density in fractional frequency deviations is a pink noise,

        S_q(f) [ffd] = (asd)^2 f^(-1)

    Args:
        asd: amplitude spectral density [/sqrt(Hz)]
    """
    logger.debug("Generating clock noise fluctuations (fs=%s Hz, size=%s, asd=%s /sqrt(Hz))", fs, size, asd)
    return pink(fs, size, asd)


def modulation(fs, size, asd=5.2E-14):
    """Generate modulation noise [ffd].

    The power spectral density as fractional frequency deviations reads

        S_M(f) [ffd] = (asd)^2 f^(2/3).

    It must be multiplied by the modulation frequency.

    Args:
        asd: amplitude spectral density [/sqrt(Hz)]
    """
    logger.debug("Generating modulation noise (fs=%s Hz, size=%s, asd=%s /sqrt(Hz))", fs, size, asd)
    return powerlaw(fs, size, asd, 1/3)


def backlink(fs, size, asd=3E-12, fknee=2E-3):
    """Generate backlink noise as fractional frequency deviation [ffd].

    The power spectral density in displacement is given by

        S_bl(f) [m] = asd^2 [ 1 + (fknee / f)^4 ].

    Multiplying by (2π f / c)^2 to express it as fractional frequency deviations,

        S_bl(f) [ffd] = (2π asd / c)^2 [ f^2 + (fknee^4 / f^2) ]
                      = (2π asd / c)^2 f^2 + (2π asd fknee^2 / c)^2 f^(-2)

    Because this is a optical pathlength noise expressed as fractional frequency deviation, it should
    be multiplied by the beam frequency to obtain the beam frequency fluctuations.

    Args:
        asd: amplitude spectral density [m/sqrt(Hz)]
        fknee: cutoff frequency [Hz]
    """
    logger.debug("Generating modulation noise (fs=%s Hz, size=%s, asd=%s m/sqrt(Hz), fknee=%s Hz)",
        fs, size, asd, fknee)
    return violet(fs, size, 2 * pi * asd / c) \
        + red(fs, size, 2 * pi * asd * fknee**2 / c)


def ranging(fs, size, asd=3E-9):
    """Generate stochastic ranging noise [s].

    This is a white noise as a timing jitter,

        S_R(f) [s] = asd.

    Args:
        asd: amplitude spectral density [s/sqrt(Hz)]
    """
    logger.debug("Generating ranging noise (fs=%s Hz, size=%s, asd=%s s/sqrt(Hz))", fs, size, asd)
    return white(fs, size, asd)


def testmass(fs, size, asd=2.4E-15, fknee=0.4E-3):
    """Generate test-mass acceleration noise [ffd].

    Expressed in acceleration, the noise power spectrum reads

        S_delta(f) [ms^(-2)] = (asd)^2 [ 1 + (fknee / f)^2 ].

    Multiplying by 1 / (2π f)^2 yields the noise as a velocity,

        S_delta(f) [ffd] = (asd / 2π)^2 [ f^(-2) + (fknee^2 / f^4) ]
                         = (asd / 2π)^2 f^(-2) + (2 asd fknee / 2π)^2 f^(-4) ].

    Args:
        asd: amplitude spectral density [ms^(-2)/sqrt(Hz)]
        fknee: cutoff frequency [Hz]
    """
    logger.debug("Generating test-mass noise (fs=%s Hz, size=%s, "
                 "asd=%s ms^(-2)/sqrt(Hz), fknee=%s Hz)", fs, size, asd, fknee)
    return red(fs, size, asd / (2 * pi)) \
        + infrared(fs, size, asd * fknee / (2 * pi))

def oms(fs, size, asd, fknee):
    """Generate optical metrology system (OMS) noise allocation [ffs].

    The power spectral density in displacement is given by

        S_oms(f) [m] = asd^2 [ 1 + (fknee / f)^4 ].

    Multiplying by (2π f / c)^2 to express it as fractional frequency deviations,

        S_oms(f) [ffd] = (2π asd / c)^2 [ f^2 + (fknee^4 / f^2) ]
                      = (2π asd / c)^2 f^2 + (2π asd fknee^2 / c)^2 f^(-2)

    Note that the level of this noise depends on the interferometer and the type of beatnote.

    Warning: this corresponds to the overall allocation for the OMS noise from the Performance
    Model. It is a collection of different noises, some of which are duplicates of standalone
    noises we already implement in the simulation (e.g., backlink noise).

    """
    logger.debug("Generating OMS noise (fs=%s Hz, size=%s, asd=%s m/sqrt(Hz), fknee=%s Hz)",
        fs, size, asd, fknee)
    return violet(fs, size, 2 * pi * asd / c) \
        + red(fs, size, 2 * pi * asd * fknee**2 / c)

def jitter(fs, size, asd):
    """Generate jitter for one angular degree of freedom.

    The power spectral density in angle is given by

        S_jitter(f) [rad] = asd^2,

    which is converted to angular velocity by mutliplying by (2π f)^2,

        S_jitter(f) [rad/s] = (2π asd)^2 f^2.

    Args:
        asd: amplitude spectral density [rad/sqrt(Hz)]
    """
    logger.debug("Generating jitter (fs=%s Hz, size=%s, asd=%s rad/sqrt(Hz))", fs, size, asd)
    return violet(fs, size, 2 * pi * asd)

def dws(fs, size, asd=7E-8/335):
    """Generate DWS measurement noise.

    The power spectral density in angle is given by

        S_dws(f) [rad] = asd^2,

    which is converted to angular velocity by mutliplying by (2π f)^2,

        S_dws(f) [rad/s] = (2π asd)^2 f^2.

    Args:
        asd: amplitude spectral density [rad/sqrt(Hz)]
    """
    logger.debug("Generating DWS measurement (fs=%s Hz, size=%s, asd=%s rad/sqrt(Hz))", fs, size, asd)
    return violet(fs, size, 2 * pi * asd)
