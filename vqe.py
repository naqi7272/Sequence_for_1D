# -*- coding: utf-8 -*-
"""VQE.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1cs8Cu3KGaObStZBfkM5GdKXX8Hk0B4EG
"""

!pip install qiskit==0.43
!pip install qiskit_aer
!pip install qiskit_algorithms
from qiskit_aer import Aer

import numpy as np
from qiskit.circuit.library import TwoLocal
from qiskit_algorithms.optimizers import COBYLA, SLSQP
from qiskit_algorithms import VQE
from qiskit.quantum_info import SparsePauliOp

# Define problem parameters
num_positions = 12  # 1D Sequence length
num_symbols = 3  # Available Symbols {1,2,3}
window_size = 3  # Sliding Window
P_validity = 10  # Penalty Coefficient for validity
P_unique = 80  # **Increased penalty coefficient for uniqueness**


# Define Hamiltonian for validity constraint
H_validity = SparsePauliOp.from_list([
    ("I" * i + "Z" + "I" * (num_positions - i - 1), P_validity) for i in range(num_positions)
])

# Define uniqueness constraint for sliding window
H_unique = SparsePauliOp.from_list([
    ("I" * i + "Z" + "I" * (j - i - 1) + "Z" + "I" * (num_positions - j - 1), P_unique)
    for i in range(num_positions - window_size + 1) for j in range(i + 1, i + window_size)
])

# Total hamiltonian
H_total= H_unique+H_validity
# Print results
print("H_validity:\n", H_validity)
print("H_unique:\n", H_unique)
print("H_total:\n", H_total)

#Define Quantum Ansatz
ansatz=TwoLocal(num_qubits=num_positions, rotation_blocks='ry', entanglement_blocks='cz', reps=10)

#Define VQE solver
optimizer=SLSQP()
backend=Aer.get_backend('qasm_simulator')
print(ansatz)
from qiskit.primitives import Estimator

estimator = Estimator()
vqe = VQE(estimator, ansatz, optimizer=optimizer)

#Solve the problem
result=vqe.compute_minimum_eigenvalue(H_total)
optimal_params=result.optimal_point

print(result)
#Decode solution
def decode_solution(params):
  sequence=[]
  for i in range(num_positions):
    symbol=(int(params[i])%num_symbols)+1
    sequence.append(symbol)
  return sequence

final_sequence=decode_solution(optimal_params)
print("Generated Sequence :", final_sequence)