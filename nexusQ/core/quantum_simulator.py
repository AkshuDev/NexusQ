"""
Defines the QuantumSimulator class for simulating quantum circuits.
"""

from . import *

import numpy as np

class QuantumSimulator:
    """
    Simulates quantum circuits.
    """

    def run(self, circuit) -> np.ndarray:
        """
        Simulates the given quantum circuit.

        Args:
            circuit (QuantumCircuit): The quantum circuit to simulate.

        Returns:
            numpy.ndarray: The final state vector of the qubits.
        """
        num_qubits = circuit.get_num_qubits()
        state = np.zeros(2**num_qubits, dtype=complex)
        state[0] = 1  # Initialize to |00...0>

        for gate in circuit.get_gates():
            gate_type = gate[0]
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

    def _apply_hadamard(self, state, qubit, num_qubits) -> None:
        """Applies a Hadamard gate."""
        hadamard_matrix = np.array([[1 / np.sqrt(2), 1 / np.sqrt(2)], [1 / np.sqrt(2), -1 / np.sqrt(2)]])
        self._apply_gate(state, hadamard_matrix, qubit, num_qubits)

    def _apply_pauli_x(self, state, qubit, num_qubits) -> None:
        """Applies a Pauli-X gate."""
        pauli_x_matrix = np.array([[0, 1], [1, 0]])
        self._apply_gate(state, pauli_x_matrix, qubit, num_qubits)

    def _apply_pauli_y(self, state, qubit, num_qubits) -> None:
        """Applies a Pauli-Y gate."""
        pauli_y_matrix = np.array([[0, -1j], [1j, 0]])
        self._apply_gate(state, pauli_y_matrix, qubit, num_qubits)

    def _apply_pauli_z(self, state, qubit, num_qubits) -> None:
        """Applies a Pauli-Z gate."""
        pauli_z_matrix = np.array([[1, 0], [0, -1]])
        self._apply_gate(state, pauli_z_matrix, qubit, num_qubits)

    def _apply_cnot(self, state, control_qubit, target_qubit, num_qubits) -> None:
        """Applies a CNOT gate."""
        cnot_matrix = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
        self._apply_controlled_gate(state, cnot_matrix, control_qubit, target_qubit, num_qubits)

    def _apply_measure(self, state, qubit, num_qubits) -> None:
        #Basic measurement simulation, collapses state.
        #Real measurement is probabilistic.
        pass

    def _apply_gate(self, state, gate_matrix, qubit, num_qubits) -> None:
        """Applies a single-qubit gate to the state vector."""
        gate = np.eye(2**num_qubits, dtype=complex)
        for i in range(2):
            for j in range(2):
                gate[i::2**(qubit+1), j::2**(qubit+1)] = gate_matrix[i, j]
        state[:] = gate @ state

    def _apply_controlled_gate(self, state, gate_matrix, control_qubit, target_qubit, num_qubits) -> None:
        """Applies a controlled gate to the state vector."""
        control_bit = 1 << (num_qubits - 1 - control_qubit)
        target_bit = 1 << (num_qubits - 1 - target_qubit)
        for i in range(2**num_qubits):
            if (i & control_bit) != 0:
                control_state = (i & target_bit) >> (num_qubits - 1 - target_qubit)
                target_state = (i & target_bit) >> (num_qubits - 1 - target_qubit)
                new_state = np.zeros(4, dtype=complex)
                for j in range(4):
                    new_state[j] = gate_matrix[j, 2 * control_state + target_state]
                for j in range(4):
                    if (j & 1) == target_state:
                        state[i & ~target_bit | ((j & 1) << (num_qubits - 1 - target_qubit))] = new_state[j]