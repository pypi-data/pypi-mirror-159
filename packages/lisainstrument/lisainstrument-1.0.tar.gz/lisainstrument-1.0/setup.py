#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=line-too-long,missing-module-docstring,exec-used

import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

meta = {}
with open("lisainstrument/meta.py") as file:
    exec(file.read(), meta)

setuptools.setup(
    name='lisainstrument',
    version=meta['__version__'],
    author=meta['__author__'],
    author_email=meta['__email__'],
    description='LISA Instrument simulates instrumental noises, propagates laser beams, generates measurements and the on-board processing to deliver simulated telemetry data.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.in2p3.fr/lisa-simulation/instrument",
    packages=setuptools.find_packages(),
    install_requires=[
        'h5py',
        'numpy',
        'scipy',
        'pyplnoise',
        'matplotlib',
        'lisaconstants',
    ],
    python_requires='>=3.7',
)
