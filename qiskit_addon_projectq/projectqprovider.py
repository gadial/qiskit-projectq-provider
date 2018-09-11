# -*- coding: utf-8 -*-

# Copyright 2018, IBM.
#
# This source code is licensed under the Apache License, Version 2.0 found in
# the LICENSE.txt file in the root directory of this source tree.

"""Provider for local ProjectQ backends."""

from qiskit.backends import BaseProvider
from .statevector_simulator_projectq import StatevectorSimulatorProjectQ
from .qasm_simulator_projectq import QasmSimulatorProjectQ


class ProjectQProvider(BaseProvider):
    """Provider for ProjectQ backends."""
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)

        # Populate the list of local ProjectQ backends.
        statevector_simulator = StatevectorSimulatorProjectQ()
        qasm_simulator = QasmSimulatorProjectQ()
        self.backends = {statevector_simulator.name(): statevector_simulator,
                         qasm_simulator.name(): qasm_simulator}

    def get_backend(self, name):
        return self.backends[name]

    def available_backends(self):
        # pylint: disable=arguments-differ
        return list(self.backends.values())
