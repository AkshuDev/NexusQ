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