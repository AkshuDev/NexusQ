"""
Defines the QuantumCircuit class for building and manipulating quantum circuits.
"""

class QuantumCircuit:
    """
    Represents a quantum circuit.
    """
    def __init__(self, num_qubits:int) -> None:
        """
        Initializes a quantum circuit with the given number of qubits.

        Args:
            num_qubits (int): The number of qubits in the circuit.
        """
        self.num_qubits = num_qubits
        self.gates = [] # Store the gates of the circuits

    def i(self, qubit:int) -> None:
        """Applies a Identitiy gate to the specified qubit.

        Args:
            qubit (int): The index of the qubit.
        """
        self.gates.append(("I", qubit))
        
    def h(self, qubit:int) -> None:
        """
        Applies a Hadamard gate to the specified qubit.

        Args:
            qubit (int): The index of the qubit.
        """
        self.gates.append(("H", qubit))
        
    def x(self, qubit:int) -> None:
        """
        Applies a Pauli-X gate to the specified qubit.

        Args:
            qubit (int): The index of the qubit.
        """
        self.gates.append(("X", qubit))

    def y(self, qubit:int) -> None:
        """
        Applies a Pauli-Y gate to the specified qubit.

        Args:
            qubit (int): The index of the qubit.
        """
        self.gates.append(("Y", qubit))

    def z(self, qubit:int) -> None:
        """
        Applies a Pauli-Z gate to the specified qubit.

        Args:
            qubit (int): The index of the qubit.
        """
        self.gates.append(("Z", qubit))

    def S(self, qubit:int) -> None:
        """Applies a Phase gate to the specified qubit.

        Args:
            qubit (int): The index of the qubit.
        """
        self.gates.append(("S", qubit))

    def T(self, qubit:int) -> None:
        """Applies a T (PI / 8) gate to the specified qubit.

        Args:
            qubit (int): The index of the qubit.
        """
        self.gates.append(("T", qubit))
        
    def cnot(self, control_qubit:int, target_qubit:int) -> None:
        """
        Applies a CNOT gate with the given control and target qubits.

        Args:
            control_qubit (int): The index of the control qubit.
            target_qubit (int): The index of the target qubit.
        """
        self.gates.append(("CNOT", control_qubit, target_qubit))

    def rx(self, qubit:int, theta:int) -> None:
        """Applies the Rotation-X gate using the theta to the specified qubit.

        Args:
            qubit (int): The index of the qubit.
            theta (int): The theta.
        """
        self.gates.append(("RX", qubit, theta))

    def ry(self, qubit:int, theta:int) -> None:
        """Applies the Rotation-Y gate using the theta to the specified qubit.

        Args:
            qubit (int): The index of the qubit.
            theta (int): The theta.
        """
        self.gates.append(("RY", qubit, theta))

    def rz(self, qubit:int, theta:int) -> None:
        """Applies the Rotation-Z gate using the theta to the specified qubit.

        Args:
            qubit (int): The index of the qubit.
            theta (int): The theta.
        """
        self.gates.append(("RZ", qubit, theta))


    def cz(self, control_qubit, target_qubit):
        """
        Applies a CZ gate to the specified control and target qubits.

        Args:
            control_qubit (int): The index of the control qubit.
            target_qubit (int): The index of the target qubit.
        """
        self.gates.append(("CZ", control_qubit, target_qubit))

    def swap(self, qubit1, qubit2):
        """
        Applies a SWAP gate to the specified qubits.

        Args:
            qubit1 (int): The index of the first qubit.
            qubit2 (int): The index of the second qubit.
        """
        self.gates.append(("SWAP", qubit1, qubit2))

    def ccx(self, control_qubit1, control_qubit2, target_qubit):
        """
        Applies a Toffoli (CCX) gate to the specified control and target qubits.

        Args:
            control_qubit1 (int): The index of the first control qubit.
            control_qubit2 (int): The index of the second control qubit.
            target_qubit (int): The index of the target qubit.
        """
        self.gates.append(("CCX", control_qubit1, control_qubit2, target_qubit))

    def cy(self, control_qubit, target_qubit):
        """
        Applies a Controlled-Y gate.

        Args:
            control_qubit(int): the control qubit.
            target_qubit(int): the target qubit.
        """
        self.gates.append(("CY", control_qubit, target_qubit))

    def ch(self, control_qubit, target_qubit):
        """
        Applies a Controlled-Hadamard gate.

        Args:
            control_qubit(int): the control qubit.
            target_qubit(int): the target qubit.
        """
        self.gates.append(("CH", control_qubit, target_qubit))

    def cs(self, control_qubit, target_qubit):
        """
        Applies a Controlled-Phase gate.

        Args:
            control_qubit(int): the control qubit.
            target_qubit(int): the target qubit.
        """
        self.gates.append(("CS", control_qubit, target_qubit))

    def cswap(self, control_qubit, qubit1, qubit2):
        """
        Applies a Fredkin(CSWAP) gate.

        Args:
            control_qubit(int): the control qubit.
            qubit1(int): the first target qubit.
            qubit2(int): the second target qubit.
        """
        self.gates.append(("CSWAP", control_qubit, qubit1, qubit2))

    def rxx(self, qubit1, qubit2, theta):
        """
        Applies a Rxx gate.

        Args:
            qubit1(int): the first qubit.
            qubit2(int): the second qubit.
            theta(float): the angle of rotation.
        """
        self.gates.append(("Rxx", qubit1, qubit2, theta))

    def ryy(self, qubit1, qubit2, theta):
        """
        Applies a Ryy gate.

        Args:
            qubit1(int): the first qubit.
            qubit2(int): the second qubit.
            theta(float): the angle of rotation.
        """
        self.gates.append(("Ryy", qubit1, qubit2, theta))

    def rzz(self, qubit1, qubit2, theta):
        """
        Applies a Rzz gate.

        Args:
            qubit1(int): the first qubit.
            qubit2(int): the second qubit.
            theta(float): the angle of rotation.
        """
        self.gates.append(("Rzz", qubit1, qubit2, theta))
        
    def measure(self, qubit:int) -> None:
        """
        Measures the specified qubit.

        Args:
            qubit (int): The index of the qubit.
        """
        self.gates.append(("Measure", qubit))

    def get_gates(self) -> list:
        """
        Returns the list of gates in the circuit.

        Returns:
            list: The list of gates.
        """
        return self.gates

    def get_num_qubits(self) -> int:
        """
        Returns the number of qubits in the circuit.

        Returns:
            int: The number of qubits.
        """
        return self.num_qubits