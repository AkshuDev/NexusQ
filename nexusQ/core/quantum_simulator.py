"""
Defines the QuantumSimulator class for simulating quantum circuits.
"""

import numpy as np
from .quantum_circuit import QuantumCircuit  # Import QuantumCircuit

class QuantumSimulator:
    """
    Simulates quantum circuits.
    """

    def run(self, circuit: QuantumCircuit) -> np.ndarray:
        """
        Simulates the given quantum circuit.

        Args:
            circuit (QuantumCircuit): The quantum circuit to simulate.

        Returns:
            np.ndarray: The final state vector of the qubits.
        """
        num_qubits: int = circuit.get_num_qubits()
        state: np.ndarray = np.zeros(2**num_qubits, dtype=complex)
        state[0] = 1  # Initialize to |00...0>

        for gate in circuit.get_gates():
            gate_type: str = gate[0]
            if gate_type in ("H", "X", "Y", "Z", "S", "T", "I", "Measure"):
                qubit: int = gate[1]
                params = None
            elif gate_type in ("CNOT", "CZ", "SWAP", "CY", "CH", "CS", "CSWAP"):
                control_qubit: int = gate[1]
                target_qubit: int = gate[2]
                params = None
            elif gate_type in ("RX", "RY", "RZ", "Rxx", "Ryy", "Rzz"):
                qubit: int = gate[1]
                theta = gate[2]
                if gate_type in ("Rxx", "Ryy", "Rzz"):
                    qubit2 = gate[1]
                    theta = gate[2]
                params = theta
            elif gate_type == "CCX":
                control_qubit1: int = gate[1]
                control_qubit2: int = gate[2]
                target_qubit: int = gate[3]
                params = None

            if gate_type == "I":
                self._apply_identity(state, qubit, num_qubits)
            elif gate_type == "H":
                self._apply_hadamard(state, qubit, num_qubits)
            elif gate_type == "X":
                self._apply_pauli_x(state, qubit, num_qubits)
            elif gate_type == "Y":
                self._apply_pauli_y(state, qubit, num_qubits)
            elif gate_type == "Z":
                self._apply_pauli_z(state, qubit, num_qubits)
            elif gate_type == "S":
                self._apply_s(state, qubit, num_qubits)
            elif gate_type == "T":
                self._apply_t(state, qubit, num_qubits)
            elif gate_type == "CNOT":
                self._apply_cnot(state, control_qubit, target_qubit, num_qubits)
            elif gate_type == "RX":
                self._apply_rx(state, qubit, num_qubits, params)
            elif gate_type == "RY":
                self._apply_ry(state, qubit, num_qubits, params)
            elif gate_type == "RZ":
                self._apply_rz(state, qubit, num_qubits, params)
            elif gate_type == "CZ":
                self._apply_cz(state, control_qubit, target_qubit, num_qubits)
            elif gate_type == "SWAP":
                self._apply_swap(state, qubit, target_qubit, num_qubits)
            elif gate_type == "CCX":
                self._apply_ccx(state, control_qubit1, control_qubit2, target_qubit, num_qubits)
            elif gate_type == "CY":
                self._apply_cy(state, control_qubit, target_qubit, num_qubits)
            elif gate_type == "CH":
                self._apply_ch(state, control_qubit, target_qubit, num_qubits)
            elif gate_type == "CS":
                self._apply_cs(state, control_qubit, target_qubit, num_qubits)
            elif gate_type == "CSWAP":
                self._apply_cswap(state, control_qubit, qubit, target_qubit, num_qubits)
            elif gate_type == "Rxx":
                self._apply_rxx(state, qubit, qubit2, num_qubits, params)
            elif gate_type == "Ryy":
                self._apply_ryy(state, qubit, qubit2, num_qubits, params)
            elif gate_type == "Rzz":
                self._apply_rzz(state, qubit, qubit2, num_qubits, params)
            elif gate_type == "Measure":
                self._apply_measure(state, qubit, num_qubits)
        return state

    def _apply_identity(self, state: np.ndarray, qubit: int, num_qubits: int) -> None:
        """Applies an Identity gate."""
        identity_matrix: np.ndarray = np.array([[1, 0], [0, 1]])
        self._apply_gate(state, identity_matrix, qubit, num_qubits)

    def _apply_hadamard(self, state: np.ndarray, qubit: int, num_qubits: int) -> None:
        """Applies a Hadamard gate."""
        hadamard_matrix: np.ndarray = np.array([[1 / np.sqrt(2), 1 / np.sqrt(2)], [1 / np.sqrt(2), -1 / np.sqrt(2)]])
        self._apply_gate(state, hadamard_matrix, qubit, num_qubits)

    def _apply_pauli_x(self, state: np.ndarray, qubit: int, num_qubits: int) -> None:
        """Applies a Pauli-X gate."""
        pauli_x_matrix: np.ndarray = np.array([[0, 1], [1, 0]])
        self._apply_gate(state, pauli_x_matrix, qubit, num_qubits)

    def _apply_pauli_y(self, state: np.ndarray, qubit: int, num_qubits: int) -> None:
        """Applies a Pauli-Y gate."""
        pauli_y_matrix: np.ndarray = np.array([[0, -1j], [1j, 0]])
        self._apply_gate(state, pauli_y_matrix, qubit, num_qubits)

    def _apply_pauli_z(self, state: np.ndarray, qubit: int, num_qubits: int) -> None:
        """Applies a Pauli-Z gate."""
        pauli_z_matrix: np.ndarray = np.array([[1, 0], [0, -1]])
        self._apply_gate(state, pauli_z_matrix, qubit, num_qubits)

    def _apply_s(self, state: np.ndarray, qubit: int, num_qubits: int) -> None:
        """Applies an S gate."""
        s_matrix: np.ndarray = np.array([[1, 0], [0, 1j]])
        self._apply_gate(state, s_matrix, qubit, num_qubits)

    def _apply_t(self, state: np.ndarray, qubit: int, num_qubits: int) -> None:
        """Applies a T gate."""
        t_matrix: np.ndarray = np.array([[1, 0], [0, np.exp(1j * np.pi / 4)]])
        self._apply_gate(state, t_matrix, qubit, num_qubits)

    def _apply_rx(self, state: np.ndarray, qubit: int, num_qubits: int, theta: float) -> None:
        """Applies an Rx gate."""
        rx_matrix: np.ndarray = np.array([[np.cos(theta/2), -1j * np.sin(theta/2)], [-1j * np.sin(theta/2), np.cos(theta/2)]])
        self._apply_gate(state, rx_matrix, qubit, num_qubits)

    def _apply_ry(self, state: np.ndarray, qubit: int, num_qubits: int, theta: float) -> None:
        """Applies an Ry gate."""
        ry_matrix: np.ndarray = np.array([[np.cos(theta/2), -np.sin(theta/2)], [np.sin(theta/2), np.cos(theta/2)]])
        self._apply_gate(state, ry_matrix, qubit, num_qubits)

    def _apply_rz(self, state: np.ndarray, qubit: int, num_qubits: int, theta: float) -> None:
        """Applies an Rz gate."""
        rz_matrix: np.ndarray = np.array([[np.exp(-1j * theta/2), 0], [0, np.exp(1j * theta/2)]])
        self._apply_gate(state, rz_matrix, qubit, num_qubits)

    def _apply_cnot(self, state: np.ndarray, control_qubit: int, target_qubit: int, num_qubits: int) -> None:
        """Applies a CNOT gate."""
        cnot_matrix: np.ndarray = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
        self._apply_controlled_gate(state, cnot_matrix, control_qubit, target_qubit, num_qubits)

    def _apply_cz(self, state: np.ndarray, control_qubit: int, target_qubit: int, num_qubits: int) -> None:
        """Applies a CZ gate."""
        cz_matrix: np.ndarray = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, -1]])
        self._apply_controlled_gate(state, cz_matrix, control_qubit, target_qubit, num_qubits)

    def _apply_swap(self, state: np.ndarray, qubit1: int, qubit2: int, num_qubits: int) -> None:
        """Applies a SWAP gate."""
        swap_matrix: np.ndarray = np.array([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])
        self._apply_two_qubit_gate(state, swap_matrix, qubit1, qubit2, num_qubits)

    def _apply_ccx(self, state: np.ndarray, control_qubit1: int, control_qubit2: int, target_qubit: int, num_qubits: int) -> None:
        """Applies a CCX (Toffoli) gate."""
        ccx_matrix: np.ndarray = np.array([[1, 0, 0, 0, 0, 0, 0, 0],
                                            [0, 1, 0, 0, 0, 0, 0, 0],
                                            [0, 0, 1, 0, 0, 0, 0, 0],
                                            [0, 0, 0, 1, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 1, 0, 0, 0],
                                            [0, 0, 0, 0, 0, 1, 0, 0],
                                            [0, 0, 0, 0, 0, 0, 0, 1],
                                            [0, 0, 0, 0, 0, 0, 1, 0]])
        self._apply_three_qubit_gate(state, ccx_matrix, control_qubit1, control_qubit2, target_qubit, num_qubits)

    def _apply_cy(self, state: np.ndarray, control_qubit: int, target_qubit: int, num_qubits: int) -> None:
        """Applies a CY gate."""
        cy_matrix: np.ndarray = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, -1j], [0, 0, 1j, 0]])
        self._apply_controlled_gate(state, cy_matrix, control_qubit, target_qubit, num_qubits)

    def _apply_ch(self, state: np.ndarray, control_qubit: int, target_qubit: int, num_qubits: int) -> None:
        """Applies a CH gate."""
        ch_matrix: np.ndarray = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1 / np.sqrt(2), 1 / np.sqrt(2)], [0, 0, 1 / np.sqrt(2), -1 / np.sqrt(2)]])
        self._apply_controlled_gate(state, ch_matrix, control_qubit, target_qubit, num_qubits)

    def _apply_cs(self, state: np.ndarray, control_qubit: int, target_qubit: int, num_qubits: int) -> None:
        """Applies a CS gate."""
        cs_matrix: np.ndarray = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1j]])
        self._apply_controlled_gate(state, cs_matrix, control_qubit, target_qubit, num_qubits)

    def _apply_cswap(self, state: np.ndarray, control_qubit: int, qubit1: int, qubit2: int, num_qubits: int) -> None:
        """Applies a CSWAP (Fredkin) gate."""
        cswap_matrix: np.ndarray = np.array([[1, 0, 0, 0, 0, 0, 0, 0],
                                               [0, 1, 0, 0, 0, 0, 0, 0],
                                               [0, 0, 1, 0, 0, 0, 0, 0],
                                               [0, 0, 0, 1, 0, 0, 0, 0],
                                               [0, 0, 0, 0, 1, 0, 0, 0],
                                               [0, 0, 0, 0, 0, 0, 1, 0],
                                               [0, 0, 0, 0, 0, 1, 0, 0],
                                               [0, 0, 0, 0, 0, 0, 0, 1]])
        self._apply_three_qubit_gate(state, cswap_matrix, control_qubit, qubit1, qubit2, num_qubits)

    def _apply_rxx(self, state: np.ndarray, qubit1: int, qubit2: int, num_qubits: int, theta: float) -> None:
        """Applies an Rxx gate."""
        rxx_matrix: np.ndarray = np.array([[np.cos(theta / 2), 0, 0, -1j * np.sin(theta / 2)],
                                            [0, np.cos(theta / 2), -1j * np.sin(theta / 2), 0],
                                            [0, -1j * np.sin(theta / 2), np.cos(theta / 2), 0],
                                            [-1j * np.sin(theta / 2), 0, 0, np.cos(theta / 2)]])
        self._apply_two_qubit_gate(state, rxx_matrix, qubit1, qubit2, num_qubits)

    def _apply_ryy(self, state: np.ndarray, qubit1: int, qubit2: int, num_qubits: int, theta: float) -> None:
        """Applies an Ryy gate."""
        ryy_matrix: np.ndarray = np.array([[np.cos(theta / 2), 0, 0, 1j * np.sin(theta / 2)],
                                            [0, np.cos(theta / 2), -1j * np.sin(theta / 2), 0],
                                            [0, -1j * np.sin(theta / 2), np.cos(theta / 2), 0],
                                            [1j * np.sin(theta / 2), 0, 0, np.cos(theta / 2)]])
        self._apply_two_qubit_gate(state, ryy_matrix, qubit1, qubit2, num_qubits)

    def _apply_rzz(self, state: np.ndarray, qubit1: int, qubit2: int, num_qubits: int, theta: float) -> None:
        """Applies an Rzz gate."""
        rzz_matrix: np.ndarray = np.array([[np.exp(-1j * theta / 2), 0, 0, 0],
                                            [0, np.exp(1j * theta / 2), 0, 0],
                                            [0, 0, np.exp(1j * theta / 2), 0],
                                            [0, 0, 0, np.exp(-1j * theta / 2)]])
        self._apply_two_qubit_gate(state, rzz_matrix, qubit1, qubit2, num_qubits)

    def _apply_measure(self, state: np.ndarray, qubit: int, num_qubits: int) -> None:
        """Applies a measurement gate."""
        # Basic measurement simulation, collapses state.
        # Real measurement is probabilistic.
        pass

    def _apply_gate(self, state: np.ndarray, gate_matrix: np.ndarray, qubit: int, num_qubits: int) -> None:
        """Applies a single-qubit gate to the state vector."""
        gate: np.ndarray = np.eye(2**num_qubits, dtype=complex)
        for i in range(2):
            for j in range(2):
                gate[i::2**(qubit+1), j::2**(qubit+1)] = gate_matrix[i, j]
        state[:] = gate @ state

    def _apply_controlled_gate(self, state: np.ndarray, gate_matrix: np.ndarray, control_qubit: int, target_qubit: int, num_qubits: int) -> None:
        """Applies a controlled gate to the state vector."""
        control_bit: int = 1 << (num_qubits - 1 - control_qubit)
        target_bit: int = 1 << (num_qubits - 1 - target_qubit)
        for i in range(2**num_qubits):
            if (i & control_bit) != 0:
                control_state: int = (i & target_bit) >> (num_qubits - 1 - target_qubit)
                target_state: int = (i & ~target_bit)
                target_state = (i & target_bit) >> (num_qubits - 1 - target_qubit)
                new_state: np.ndarray = np.zeros(4, dtype=complex)
                for j in range(4):
                    new_state[j] = gate_matrix[j, 2 * control_state + target_state]
                for j in range(4):
                    if (j & 1) == target_state:
                        state[i & ~target_bit | ((j & 1) << (num_qubits - 1 - target_qubit))] = new_state[j]

    def _apply_two_qubit_gate(self, state: np.ndarray, gate_matrix: np.ndarray, qubit1: int, qubit2: int, num_qubits: int) -> None:
        """Applies a two-qubit gate to the state vector."""
        gate: np.ndarray = np.eye(2**num_qubits, dtype=complex)
        for i in range(4):
            for j in range(4):
                gate[i::2**(min(qubit1, qubit2)+1), j::2**(min(qubit1, qubit2)+1)] = gate_matrix[i, j]
        state[:] = gate @ state

    def _apply_three_qubit_gate(self, state: np.ndarray, gate_matrix: np.ndarray, qubit1: int, qubit2: int, qubit3: int, num_qubits: int) -> None:
        """Applies a three-qubit gate to the state vector."""
        gate: np.ndarray = np.eye(2**num_qubits, dtype=complex)
        for i in range(8):
            for j in range(8):
                gate[i::2**(min(qubit1, qubit2, qubit3)+1), j::2**(min(qubit1, qubit2, qubit3)+1)] = gate_matrix[i, j]
        state[:] = gate @ state