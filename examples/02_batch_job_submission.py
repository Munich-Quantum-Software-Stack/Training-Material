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

circuit_2 = QuantumCircuit(10, 10)
circuit_2.h(0)
for i in range(1, 10):
    circuit_2.cx(0, i)
circuit_2.measure([0, 1], [0, 1])

job = backend.run(
    [circuit, circuit_2],  # Submitting a list of circuits as a batch job
    shots=1000,
    no_modify=False,
)

result = job.result()
counts = result.get_counts()
print("Measurement counts:", counts)
