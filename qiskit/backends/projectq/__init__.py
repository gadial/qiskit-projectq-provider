# -*- coding: utf-8 -*-

# Copyright 2018, IBM.
#
# This source code is licensed under the Apache License, Version 2.0 found in
# the LICENSE.txt file in the root directory of this source tree.

"""Local ProjectQ Backends."""

from .qasm_simulator_projectq import QasmSimulatorProjectQ
from .statevector_simulator_projectq import StatevectorSimulatorProjectQ
from .projectqprovider import ProjectQProvider

__version__ = '0.1.0'
