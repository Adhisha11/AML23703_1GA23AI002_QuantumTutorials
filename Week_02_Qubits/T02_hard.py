import numpy as np
import matplotlib.pyplot as plt

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector

qc = QuantumCircuit(2)

qc.h(0)
qc.h(1)

state = Statevector.from_instruction(qc)

print("Statevector:")
print(state)

amps = state.data

print("\nAmplitudes:")
for i, amp in enumerate(amps):
    print(f"|{i:02b}> : {amp}")

probabilities = np.abs(amps) ** 2

print("\nProbabilities:")
print(probabilities)

print("Sum of probabilities:", probabilities.sum())
