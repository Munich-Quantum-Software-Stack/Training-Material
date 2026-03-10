import qiskit.qasm3
import sys
import os
from qiskit import QuantumCircuit
from mqss.qiskit_adapter import MQSSQiskitAdapter
from qiskit import QuantumCircuit, compiler
import qiskit.qasm3

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from config import MQSS_BACKEND, MQSS_TOKEN, MQSS_URL, MQSS_PORT

adapter = MQSSQiskitAdapter(token=MQSS_TOKEN)
backend = adapter.get_backend(MQSS_BACKEND)

try:

    program = """
        OPENQASM 3;

        include "stdgates.inc";

        qubit[3] q;
        bit[3] c;

        // Create GHZ state
        h q[0];
        cx q[0], q[1];
        cx q[1], q[2];

        // Measure
        c = measure q;
    """
    circuit = qiskit.qasm3.loads(program)

    # Or, alternatively:

    # circuit = qiskit.qasm3.load("../ghz.qasm")

    job = backend.run(circuit, shots=1000, qasm3=True)

    result = job.result()
    counts = result.get_counts()
    print("Measurement counts:", counts)

except Exception as e:
    print("An error occurred while creating the circuit from QASM3:", str(e))
