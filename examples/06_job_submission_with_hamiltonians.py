import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from config import MQSS_BACKEND, MQSS_TOKEN, MQSS_URL, MQSS_PORT

import pennylane as qml
from pennylane import numpy as np
from mqss.pennylane_adapter.device import MQSSPennylaneDevice

dev_hamiltonian = MQSSPennylaneDevice(wires=2, token=MQSS_TOKEN, backends=MQSS_BACKEND)


def arbitrary_quantum_circuit(x: float, y: float) -> None:
    """
    Defines an arbitrary mock quantum circuit for testing purposes, without a measurement operation

    :param x: The parameter `x` in the `quantum_function_expval` represents the angle for the rotation gate
    `RZ` applied on the qubit at wire 0
    :param y: The parameter `y` in the `quantum_function_expval` function is used as the angle parameter for
    the rotation gate `RY(y, wires=1)`. This gate applies a rotation around the y-axis of the Bloch
    sphere by an angle `y` to the qubit on wire
    """
    qml.RZ(x, wires=0)
    qml.CNOT(wires=[0, 1])
    qml.RY(y, wires=1)
    qml.CNOT(wires=[1, 0])
    qml.RX(x, wires=1)


@qml.qnode(dev_hamiltonian)
def quantum_function_hamiltonian_expval(
    x: float, y: float, H: qml.Hamiltonian
) -> float:
    """
    The function `quantum_function_expval` applies quantum operations RZ, CNOT, and RY to qubits and returns
    the expectation value of PauliZ on the second qubit.

    :param x: The parameter `x` in the `quantum_function_expval` represents the angle for the rotation gate
    `RZ` applied on the qubit at wire 0
    :param y: The parameter `y` in the `quantum_function_expval` function is used as the angle parameter for
    the rotation gate `RY(y, wires=1)`. This gate applies a rotation around the y-axis of the Bloch
    sphere by an angle `y` to the qubit on wire
    :return: The function `quantum_function_expval` returns the expected value of a given operator
    :H: Pennylane Hamiltonian object
    """
    arbitrary_quantum_circuit(x, y)

    return qml.expval(H)


J = 0.5  # Interaction strength
h = 0.2  # Transverse field strength
coeffs = [-J, -h, -h]  # TFIM with 2 sites
obs = [
    qml.PauliZ(0) @ qml.PauliZ(1),  # Ising interaction between sites 0 and 1
    qml.PauliX(0) @ qml.Identity(1),  # Transverse field on site 0
    qml.Identity(0) @ qml.PauliX(1),  # Transverse field on site 1
]

hamiltonian = qml.Hamiltonian(coeffs, obs)
params = [np.pi / 2, np.pi / 4]  # Example parameters for the quantum circuit
result = quantum_function_hamiltonian_expval(*params, hamiltonian)
print(f"Expectation value of the Hamiltonian: {result}")
