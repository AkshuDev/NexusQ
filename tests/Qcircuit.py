import sys
import os

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

from nexusQ.core import *

circuit = QuantumCircuit(10)
circuit.h(0)
circuit.x(1)
circuit.y(2)
circuit.cnot(2, 1)
circuit.swap(2, 1)
circuit.cswap(0, 2, 1)
print(circuit.get_num_qubits())
print(circuit.get_gates())
sim = QuantumSimulator()

print(sim.run(circuit))