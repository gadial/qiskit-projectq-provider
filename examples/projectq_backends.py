# -*- coding: utf-8 -*-

# Copyright 2018, IBM.
#
# This source code is licensed under the Apache License, Version 2.0 found in
# the LICENSE.txt file in the root directory of this source tree.
"""
Example use of the ProjectQ based simulators
"""

import os
from qiskit import execute, load_qasm_file, register
from qiskit.backends.projectq import ProjectQProvider


def use_projectq_backends():

    register(provider_class=ProjectQProvider)
   
    # ProjectQ simulator
    q_circuit = load_qasm_file('ghz.qasm')
    result = execute(q_circuit, backend='projectq_qasm_simulator', shots=100).result()
    print("counts: ")
    print(result.get_counts(q_circuit))

    # ProjectQ statevector simulator
    q_circuit = load_qasm_file('simple.qasm')
    result = execute(q_circuit, backend='projectq_statevector_simulator').result()
    print("final quantum amplitude vector: ")
    print(result.get_statevector(q_circuit))


if __name__ == "__main__":
    use_projectq_backends()
