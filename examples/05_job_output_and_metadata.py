import sys
import os
from qiskit import QuantumCircuit
from mqss.qiskit_adapter import MQSSQiskitAdapter
from qiskit import QuantumCircuit, compiler

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from config import MQSS_BACKEND, MQSS_TOKEN, MQSS_URL, MQSS_PORT

adapter = MQSSQiskitAdapter(token=MQSS_TOKEN)
backend = adapter.get_backend(MQSS_BACKEND)

print(f"backend.instructions: {backend.instructions}")
print("*" * 100)
print(f"backend._coupling_map: {backend._coupling_map}")
