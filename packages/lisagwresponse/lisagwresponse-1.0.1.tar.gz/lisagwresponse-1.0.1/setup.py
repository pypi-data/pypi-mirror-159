#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=line-too-long,missing-module-docstring

import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

meta = {}
with open("lisagwresponse/meta.py") as file:
    exec(file.read(), meta)

setuptools.setup(
    name="lisagwresponse",
    version=meta['__version__'],
    author=meta['__author__'],
    author_email=meta['__email__'],
    description="LISA GW Response generates the instrumental response to gravitational-waves, and produces a gravitational-wave file compatible with LISANode.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.in2p3.fr/lisa-simulation/gw-response",
    packages=setuptools.find_packages(),
    install_requires=[
        'h5py',
        'numpy',
        'scipy',
        'matplotlib',
        'healpy',
        'lisaconstants',
        'packaging',
    ],
    python_requires='>=3.7',
)
