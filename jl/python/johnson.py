import numpy as np
from scipy.spatial.distance import pdist


def jl_projection(X, k):
    """
    Implementa la proyección de Johnson-Lindenstrauss T_U.
    X: matriz de datos de tamaño (n, d) donde n es el número de puntos y d la
    la dimensión original.
    k: dimensión objetivo.
    Retorna la matriz proyectada de tamaño (n, k).
    """
    n, d = X.shape
    U = np.random.randn(d, k)
    return (X @ U) / np.sqrt(k)


X_test = np.random.randn(5, 10)
X_proj_test = jl_projection(X_test, 3)
print("Forma original:", X_test.shape)
print("Forma proyectada:", X_proj_test.shape)

n, d = 300, 1000
k_values = [19, 50, 108, 200, 300, 500, 800]
np.random.seed(42)
X = np.random.randn(n, d)
dist_original = pdist(X, metric="euclidean")
print(
    f"{'k':<10} | {'Error Empírico (ε)':<20} | {'Cota Teórica Johnson-Lindenstrauss':<20}"
)
print("-" * 70)
for k in k_values:
    X_proj = jl_projection(X, k)
    dist_projected = pdist(X_proj, metric="euclidean")
    ratios = dist_projected / dist_original
    min_ratio = np.min(ratios)
    max_ratio = np.max(ratios)
    epsilon_empirical = max(1 - min_ratio, max_ratio - 1)
    epsilon_theoretical = np.sqrt(48 * np.log(n) / k)
    print(f"{k:<10} | {epsilon_empirical:<20.4f} | {epsilon_theoretical:<20.4f}")
