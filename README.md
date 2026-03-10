# Training Material

Examples for submitting quantum circuits to MQSS backends via Qiskit and PennyLane adapters.

## Setup

```bash
pip install uv
uv sync
source .venv/bin/activate
```

Copy `.env.example` to `.env` and fill in your credentials:

```
MQSS_TOKEN=your_token
MQSS_BACKEND=EQE1
MQSS_URL=https://portal.quantum.lrz.de
MQSS_PORT=4000
```

## Examples

| File | Description |
|------|-------------|
| `01_simple_circuit_submission.py` | Build a Bell circuit with Qiskit and submit it as a job |
| `02_batch_job_submission.py` | Submit multiple circuits in a single batch job |
| `03_transpiled_circuit_submission.py` | Transpile a circuit locally with a specific qubit layout, then submit with `no_modify=True` |
| `04_reading_from_qasm.py` | Load a circuit from a QASM3 string or file and submit it |
| `05_job_output_and_metadata.py` | Inspect backend metadata: available instructions, coupling map, job results |
| `06_job_submission_with_hamiltonians.py` | Use PennyLane to compute expectation values of Hamiltonians on the backend |

Run any example from the `Training-Material` directory:

```bash
python examples/01_simple_circuit_submission.py
```
