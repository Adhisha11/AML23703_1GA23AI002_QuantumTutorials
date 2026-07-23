#Step 1: Import Libraries
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
import random

#Step 2: Quantum Random Bit Function
simulator = AerSimulator()

def quantum_random_bit():
    qc = QuantumCircuit(1, 1)
    qc.h(0)
    qc.measure(0, 0)

    compiled = transpile(qc, simulator)
    job = simulator.run(compiled, shots=1)
    result = job.result()
    counts = result.get_counts()

    return int(list(counts.keys())[0])


#Step 3: Generate Quantum Random Bits
quantum_bits = []

for _ in range(100):
    quantum_bits.append(quantum_random_bit())

print("Quantum Bits:")
print(quantum_bits)

#Step 4: Generate Python Random Bits
python_bits = []

for _ in range(100):
    python_bits.append(random.randint(0, 1))

print("Python Bits:")
print(python_bits)

#Step 5: Compare Statistics
print("\nQuantum")
print("Zeros:", quantum_bits.count(0))
print("Ones :", quantum_bits.count(1))

print("\nPython")
print("Zeros:", python_bits.count(0))
print("Ones :", python_bits.count(1))

#Step 6: (Optional) Plot Comparison
import matplotlib.pyplot as plt

labels = ["0", "1"]

quantum_counts = [
    quantum_bits.count(0),
    quantum_bits.count(1)
]

python_counts = [
    python_bits.count(0),
    python_bits.count(1)
]

x = range(len(labels))
width = 0.35

plt.bar([i - width/2 for i in x], quantum_counts, width, label="Quantum")
plt.bar([i + width/2 for i in x], python_counts, width, label="Python")

plt.xticks(x, labels)
plt.ylabel("Count")
plt.title("Quantum vs Python Random Bits")
plt.legend()

plt.show()