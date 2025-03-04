import sys
sys.path.append("..")

from nexusQ.core import *

circuit = QuantumCircuit(10)
circuit.h(0)
circuit.rx(1, 5)
print(circuit.get_gates())
sim = QuantumSimulator()

print(sim.run(circuit))