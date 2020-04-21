import numpy as np
import time
from qiskit import QuantumCircuit, execute, Aer

simulator = Aer.get_backend('qasm_simulator')

def Uf(circuit):
    circuit.cx(0, 1)
    circuit.x(1)

cur_time = time.time()

circuit = QuantumCircuit(2, 1)

circuit.x(1)

circuit.h(0)
circuit.h(1)

Uf(circuit)

circuit.h(0)

circuit.measure(0, 0)

print(circuit.draw())

job = execute(circuit, simulator, shots=1000000)
result = job.result()
counts = result.get_counts(circuit)

key = next(iter(counts))
print("f(0) == f(1) is", not bool(int(key)))
print("Counts:", counts[key])
print("Took", time.time() - cur_time, "seconds")