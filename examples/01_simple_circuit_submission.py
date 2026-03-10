import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from qiskit import QuantumCircuit
from mqss.qiskit_adapter import MQSSQiskitAdapter
from qiskit import QuantumCircuit, compiler
from config import MQSS_BACKEND, MQSS_TOKEN, MQSS_URL, MQSS_PORT

adapter = MQSSQiskitAdapter(token=MQSS_TOKEN)
backend = adapter.get_backend(MQSS_BACKEND)

circuit = QuantumCircuit(2, 2)
circuit.h(0)
circuit.cx(0, 1)
circuit.measure([0, 1], [0, 1])


job = backend.run(
    circuit,
    shots=1000,
    no_modify=False,
    # Some additional options that can be passed to the run method:
    # no_modify (bool): do not modify/transpile the circuit
    # qasm3 (bool): use QASM3 format to send the circuit
    # queued (bool): enqueue (for limited time) the job while backend is offline
)

result = job.result()
counts = result.get_counts()
print("Measurement counts:", counts)
