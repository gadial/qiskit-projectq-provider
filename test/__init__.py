# -*- coding: utf-8 -*-

# Copyright 2018, IBM.
#
# This source code is licensed under the Apache License, Version 2.0 found in
# the LICENSE.txt file in the root directory of this source tree.

"""
QISKit ProjectQ simulators unit tests.
Note: see Issue #4 - this file is temporary;
      common.py in qiskit-core will move to a location which is included in the pip package.
"""

import os


def load_tests(loader, standard_tests, pattern):
    """
    test suite for unittest discovery
    """
    this_dir = os.path.dirname(__file__)
    if pattern in ['test*.py', '*_test.py']:
        package_tests = loader.discover(start_dir=this_dir, pattern=pattern)
        standard_tests.addTests(package_tests)
    elif pattern in ['profile*.py', '*_profile.py']:
        loader.testMethodPrefix = 'profile'
        package_tests = loader.discover(start_dir=this_dir, pattern='test*.py')
        standard_tests.addTests(package_tests)
    return standard_tests
