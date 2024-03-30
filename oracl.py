from braket.circuits import Circuit
from simons_oracle import simons_oracle
from braket.devices import LocalSimulator

# Secret string
#s = '101011'
s='101'

n = len(s) 
circ = Circuit()
# Apply Hadamard gates to the first n qubits
circ.h(range(n))
# Apply the Oracle for f. See NBI / notebook for implementation
circ += simons_oracle(secret_s=s)
# Apply Hadamard gates to the first n qubits 
circ.h(range(n))

# Output the circuit
print(circ)

device = LocalSimulator()
task = device.run(circ, shots=4*n)
