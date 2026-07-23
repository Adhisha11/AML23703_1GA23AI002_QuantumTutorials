import qiskit
from qiskit_aer import Aer

print("Qiskit Version:")
print(qiskit.__version__)

print("\nAvailable Backends:")

simulator = Aer.backends()

for backend in simulator:
    print(backend.name)


