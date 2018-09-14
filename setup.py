# -*- coding: utf-8 -*-

# Copyright 2018, IBM.
#
# This source code is licensed under the Apache License, Version 2.0 found in
# the LICENSE.txt file in the root directory of this source tree.

from setuptools import setup, find_packages

setup(
    name="qiskit-addon-projectq",
    version="0.1.0",
    author="Qiskit Development Team",
    author_email="qiskit@us.ibm.com",
    description="Qiskit simulators with ProjectQ backends",
    long_description = "This module contains [Qiskit](https://www.qiskit.org/) simulators with ProjectQ backends. The simulators simulate a quantum circuit on a classical computer.",
    url="https://github.com/Qiskit/qiskit-addon-projectq",
    license="Apache 2.0",
    classifiers=[
        "Environment :: Console",
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Scientific/Engineering",
    ],
    install_requires=['qiskit>=0.6,<0.7', 'projectq>=0.3.6'],
    keywords="qiskit quantum projectq simulator",
    packages=['qiskit.backends.projectq'],
    include_package_data=True,
    python_requires=">=3.5"
)
