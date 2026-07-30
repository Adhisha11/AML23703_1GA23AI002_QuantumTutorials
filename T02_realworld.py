
import numpy as np
import matplotlib.pyplot as plt

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector
qc = QuantumCircuit(1)

# Prepare |+>
qc.h(0)

state = Statevector.from_instruction(qc)

# Small random phase error
phi = np.random.normal(loc=0.0, scale=0.15)

phase_matrix = np.array([
    [1, 0],
    [0, np.exp(1j * phi)]
])

noisy_state = Statevector(phase_matrix @ state.data)

print("Random phase error (radians):", phi)
print(noisy_state)

plot_bloch_multivector(noisy_state)
plt.show()
