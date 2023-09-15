# flake8: noqa: E402 (module level import not at top of file)
# flake8: noqa: E402 (module level import not at top of file)
# pylint: disable=unused-import
# pylint: disable=wrong-import-position
# pylint: disable=invalid-name
"""IPython startup-file, outside of PYTHONPATH.

Files in this startup-folder will be run in lexicographical order,
so you can control the execution order of files with a prefix, e.g.::

    00-foo.py
    10-baz.py
    20-bar.py

return-statements are not allowed.

"""
print(f"\nRunning {__file__}")
import os

import qiskit
import qiskit_ibm_provider

for key, val in qiskit.__qiskit_version__.items():
    print(f"{key}: {val}")

from qiskit import IBMQ

TOKEN = os.getenv("API_TOKEN_IBM")

try:
    qiskit_ibm_provider.IBMProvider.save_account(TOKEN)
# except AccountAlreadyExistsError:
except Exception as exc:
    pass

# qiskit_ibm_provider.IBMProvider.load_account()
qiskit_ibm_provider.IBMProvider()


# storage.read_config:DEBUG:2023-09-08 22:19:54,953: Read configuration data for 'None' from '/home/wouter/.qiskit/qiskit-ibm.json'
# storage._ensure_file_exists:DEBUG:2023-09-08 22:19:54,953: Create empty configuration file at /home/wouter/.qiskit/qiskit-ibm.json
# storage.save_config:DEBUG:2023-09-08 22:19:54,954: Save configuration data for 'default-ibm-qiskit' in '/home/wouter/.qiskit/qiskit-ibm.json'



# qiskit_ibm_provider.IBMProvider.saved_accounts()

from qiskit import QuantumCircuit
qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.measure([0,1], [0,1])


from qiskit import transpile
from qiskit.providers.basicaer import QasmSimulatorPy
backend_sim = QasmSimulatorPy()
transpiled_qc = transpile(qc, backend_sim)

result = backend_sim.run(transpiled_qc).result()
print(result.get_counts(qc))  # expected: {'00': 513, '11': 511}
