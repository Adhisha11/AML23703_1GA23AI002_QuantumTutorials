from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

qc = QuantumCircuit(3,3)

qc.h([0,1,2])

qc.measure([0,1,2],[0,1,2])

print(qc.draw())

sim = AerSimulator()

compiled = transpile(qc, sim)

job = sim.run(compiled, shots=1024)

result = job.result()

counts = result.get_counts()

print(counts)

shots = 1024

print("\nProbability Distribution")

for state in sorted(counts):
    print(state, counts[state]/shots)

plot_histogram(counts)

plt.show()