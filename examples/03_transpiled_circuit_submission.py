import sys
import os
from qiskit import QuantumCircuit
from mqss.qiskit_adapter import MQSSQiskitAdapter
from qiskit import QuantumCircuit, compiler

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from config import MQSS_BACKEND, MQSS_TOKEN, MQSS_URL, MQSS_PORT

adapter = MQSSQiskitAdapter(token=MQSS_TOKEN)
backend = adapter.get_backend(MQSS_BACKEND)

circuit = QuantumCircuit(2, 2)
circuit.h(0)
circuit.cx(0, 1)
circuit.measure([0, 1], [0, 1])

job = backend.run(circuit, shots=1000)

transpiled_circuit = compiler.transpile(
    circuit, backend, initial_layout=[0, 5], optimization_level=3
)  # Initial_layout parameter is used to specify the initial mapping of virtual qubits in the circuit to physical qubits on the backend. In this example, we are mapping virtual qubit 0 to physical qubit 0 and virtual qubit 1 to physical qubit 5. This can help optimize the transpilation process by starting with a specific qubit layout that may be more efficient for the given circuit and backend topology.

job = backend.run(
    transpiled_circuit,
    shots=1000,
    no_modify=True,
    # We could skip the transpilation step and just set no_modify=True, but this way we can be sure that the circuit is transpiled locally.
)
result = job.result()
counts = result.get_counts()
print("Measurement counts:", counts)
