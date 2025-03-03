"""
Defines the QuantumSimulator class for simulating quantum circuits.
"""

import numpy as np

from . import *

class QuantumSimulator:
    """
    Simulates quantum circuits.
    """
    def run(self, circuit:QuantumCircuit) -> np.ndarray:
        """
        Simulates the given quantum circuit.

        Args:
            circuit (QuantumCircuit): The quantum circuit to simulate.

        Returns:
            numpy.ndarray: The final state vector of the qubits.
        """
        self.circuit = circuit
        num_qubits = circuit.get_num_qubits() # Get the number of Qbits
        state = np.zeros(2**num_qubits, dtype=complex)
        state[0] = 1 # Define 1 at the 0 index of state
        
        for gate in circuit.get_gates():
            gate_type = gate[0] # Get gate type
            if gate_type == "H":
                qubit = gate[1]
                self._apply_hadamard(state, qubit, num_qubits)
            elif gate_type == "X":
                qubit = gate[1]
                self._apply_pauli_x(state, qubit, num_qubits)
            elif gate_type == "Y":
                qubit = gate[1]
                self._apply_pauli_y(state, qubit, num_qubits)
            elif gate_type == "Z":
                qubit = gate[1]
                self._apply_pauli_z(state, qubit, num_qubits)
            elif gate_type == "CNOT":
                control_qubit, target_qubit = gate[1], gate[2]
                self._apply_cnot(state, control_qubit, target_qubit, num_qubits)
            elif gate_type == "Measure":
                qubit = gate[1]
                #Basic measurement simulation for now.
                self._apply_measure(state, qubit, num_qubits)
        return state
    
    def _apply_hadamard(self, state, qubit, num_qubits:int) -> None:
        """Applies a Hadamard gate."""
        hadamard_matrix = np.array([[1 / np.sqrt(2), 1 / np.sqrt(2)], [1 / np.sqrt(2), -1 / np.sqrt(2)]])
        self._apply_gate(state, hadamard_matrix, qubit, num_qubits)
        
    