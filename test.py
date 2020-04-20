import qiskit

from qiskit import IBMQ
from qiskit.providers.ibmq import least_busy

# Print the version of qiskit
print("Qiskit Version:", qiskit.__version__)

# Load local account information
provider = IBMQ.load_account()

# Get the least busy real quantum system
backend = least_busy(provider.backends(simulator=False))
print(backend, backend.status().pending_jobs)