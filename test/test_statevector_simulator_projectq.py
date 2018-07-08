# -*- coding: utf-8 -*-

# Copyright 2018, IBM.
#
# This source code is licensed under the Apache License, Version 2.0 found in
# the LICENSE.txt file in the root directory of this source tree.

# pylint: disable=invalid-name,missing-docstring,broad-except

from test.common import QiskitProjectQTestCase

import unittest
from qiskit import execute, load_qasm_file, register
from qiskit_addon_projectq import ProjectQProvider


class StatevectorSimulatorProjectQTest(QiskitProjectQTestCase):
    """Test ProjectQ C++ statevector simulator."""

    def setUp(self):
        register(provider_class=ProjectQProvider)
        self.qasm_filename = self._get_resource_path('simple.qasm')
        self.q_circuit = load_qasm_file(self.qasm_filename, name='example')

    def test_sv_simulator_projectq(self):
        """Test final state vector for single circuit run."""
        result = execute(self.q_circuit, backend='projectq_statevector_simulator').result()
        self.assertEqual(result.get_status(), 'COMPLETED')
        actual = result.get_statevector(self.q_circuit)

        # state is 1/sqrt(2)|00> + 1/sqrt(2)|11>, up to a global phase
        self.assertAlmostEqual((abs(actual[0]))**2, 1/2)
        self.assertEqual(actual[1], 0)
        self.assertEqual(actual[2], 0)
        self.assertAlmostEqual((abs(actual[3]))**2, 1/2)


if __name__ == '__main__':
    unittest.main()
