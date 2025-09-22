# Import the NumPy library and its linear algebra submodule.
import numpy as np
from numpy import linalg as la

# Set a small epsilon value for floating-point comparisons.
eps = 1e-8

# Define a sample 3x3 matrix A for demonstration.
A = np.array([[1, 2, 3], [4, 5, 6], [2, 8, 2]])

# Compute eigenvalues and eigenvectors.
# lamb1: array of eigenvalues.
# R: matrix whose columns are the right eigenvectors (A @ R = R @ diag(lamb1)).
lamb1, R = la.eig(A)

# The left eigenvectors of A are the transpose of the right eigenvectors of A.T.
# L: matrix whose rows are the left eigenvectors (L @ A = diag(lamb1) @ L).
# Note: lamb2 should be the same as lamb1.
lamb2, L_t = la.eig(A.T)
L = L_t.T

print("Right eigenvectors (columns of R): \n", R)
print("Left eigenvectors (rows of L): \n", L)

# Create a diagonal matrix from the eigenvalues.
LAM = np.diag(lamb1)
print("\nDiagonal matrix of eigenvalues [lambda]: \n", LAM)

# --- Verification ---

# 1. Verify the right eigenvector property: A @ R should be equal to R @ LAM.
# We compute C = A @ R - R @ LAM, which should be a zero matrix (within float precision).
print("\nVerifying A @ R - R @ LAM = 0:")
C1 = A @ R - R @ LAM
C1[abs(C1) < eps] = 0  # Set very small values to zero for clarity.
print(C1)

# 2. Verify the left eigenvector property: L @ A should be equal to LAM @ L.
# We compute C = L @ A - LAM @ L, which should be a zero matrix (within float precision).
print("\nVerifying L @ A - LAM @ L = 0:")
C2 = L @ A - LAM @ L
C2[abs(C2) < eps] = 0  # Set very small values to zero for clarity.
print(C2)

# 3. Verify the orthogonality of left and right eigenvectors.
# The product L @ R should be a diagonal matrix. This means that a left
# eigenvector v_i is orthogonal to a right eigenvector w_j for different
# eigenvalues (i != j).
print("\nVerifying L @ R is a diagonal matrix:")
lr = L @ R
lr[abs(lr) < eps] = 0  # Set very small values to zero for clarity.
print(lr)

# --- Individual Eigenvector Checks ---

# Extract individual eigenvectors for more detailed checks.
w1 = R[:, 0]  # First right eigenvector
w2 = R[:, 1]  # Second right eigenvector
w3 = R[:, 2]  # Third right eigenvector

v1 = L[0, :]  # First left eigenvector
v2 = L[1, :]  # Second left eigenvector
v3 = L[2, :]  # Third left eigenvector

# Check the defining property for the first left eigenvector: v1 @ A = lamb1[0] * v1
print("\nChecking v1 @ A - lamb1[0] * v1 = 0:")
result = v1 @ A - lamb1[0] * v1
result[abs(result) < eps] = 0
print(result)

# Check the dot product of left and right eigenvectors.
# The dot product v_i . w_j should be zero if i != j.
# The dot product v_i . w_i is non-zero and depends on normalization.
print("\nChecking dot products of left and right eigenvectors (v1 . w_j):")
vw11 = v1 @ w1
vw12 = v1 @ w2
vw13 = v1 @ w3
print(f"v1 . w1 = {vw11}")
print(f"v1 . w2 = {vw12}")
print(f"v1 . w3 = {vw13}")
