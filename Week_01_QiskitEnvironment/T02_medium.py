from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

qc = QuantumCircuit(1,1)

qc.h(0)

qc.measure(0,0)

print(qc.draw())

simulator = AerSimulator()

compiled = transpile(qc, simulator)

job = simulator.run(compiled, shots=1024)

result = job.result()

counts = result.get_counts()

print("Counts:", counts)

plot_histogram(counts)

plt.show()
