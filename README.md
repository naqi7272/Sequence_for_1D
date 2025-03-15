# Sequence Generation using QAOA, VQE, and GNN

## Overview
Presenting three distinct approaches for generating optimal sequences while enforcing unique symbols within a sliding window: 
- **QAOA (Quantum Approximate Optimization Algorithm)**
- **VQE (Variational Quantum Eigensolver)**
- **GNN (Graph Neural Networks)**

Each method optimizes sequences based on mathematical constraints and quantum computing or deep learning principles.

---

## Problem Statement
Given a 1D sequence of length n, we aim to generate an optimal sequence using a limited set of symbols {1,2,3} , ensuring that:
- Every sliding window of size w contains unique symbols.
- The sequence minimizes an associated cost function based on quantum principles or deep learning constraints.

Mathematically, the validity and uniqueness constraints are formulated as a Hamiltonian:

H_total = P_validity  + P_unique

where:
- H_validity enforces that each position in the sequence has a valid symbol.
- H_unique penalizes non-unique symbols within a sliding window.
- P_validity, P_unique are tunable penalty coefficients.

---

## Implementations
### 1. QAOA Approach 
QAOA is used to approximate the ground state of the problem Hamiltonian. The circuit consists of:
- A cost Hamiltonian encoding the constraints.
- A variational ansatz optimized via classical optimization algorithms (e.g., COBYLA, SPSA).
- An iterative search over hyperparameters.



---
### 2. VQE Approach 
VQE minimizes the eigenvalue of the Hamiltonian using:
- Parameterized quantum circuits (PQC) with entangling layers.
- Classical optimizers like SLSQP.
- The Estimator primitive from Qiskit to compute expectation values.

---
### 3. GNN Approach 
A Graph Neural Network (GNN) is trained to generate valid sequences by:
- Representing sequence positions as graph nodes.
- Using message passing to enforce local constraints.
- Defining a custom loss function to enforce window uniqueness.


#### **Installation & Running QAOA and VQE**
```bash
pip install qiskit==0.43 qiskit_aer qiskit_algorithms
python vqe.py
python qaoa.py

```

#### Installation & Running GNN 
```bash
pip install torch numpy
python gnn.py

```
---

## Conclusion
This project explores multiple approaches to combinatorial sequence optimization.


