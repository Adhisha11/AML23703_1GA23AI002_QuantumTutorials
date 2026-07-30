import numpy as np
import matplotlib.pyplot as plt

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector

qc = QuantumCircuit(1)
qc.x(0)

state = Statevector.from_instruction(qc)

print("Statevector:")
print(state)

# Draw Bloch sphere
plot_bloch_multivector(state)
plt.show()
