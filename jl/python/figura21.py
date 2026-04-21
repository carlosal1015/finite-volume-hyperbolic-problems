import itertools

import matplotlib.pyplot as plt
import numpy as np

n, d, epsilon = 150, 100000, 0.1
X = np.random.uniform(0, 1, (n, d))
k = np.ceil(4 * np.log(n) / ((epsilon**2) / 2 - (epsilon**3) / 3))
phi = np.random.normal(0, 1 / np.sqrt(k), (k, d))
Z = X @ phi.T
del phi

sample_pairs = list(itertools.combinations(range(n), 2))
selected_indices = np.random.choice(len(sample_pairs), 500, replace=False)
d_original = []
d_proj = []
for idx in selected_indices:
    i, j = sample_pairs[idx]
    dist_orig = np.linalg.norm(X[i] - X[j])
    dist_proj = np.linalg.norm(Z[i] - Z[j])
    d_original.append(dist_orig)
    d_proj.append(dist_proj)

d_original = np.array(d_original)
d_proj = np.array(d_proj)
R = d_proj / d_original
cumplen = (R >= (1 - epsilon)) & (R <= (1 + epsilon))
porcentaje_cumple = np.mean(cumplen) * 100
plt.figure()
colors = ["darkgreen" if c else "red" for c in cumplen]
plt.scatter(range(len(R)), R, c=colors, s=20, alpha=0.7)
plt.axhline(
    y=1 - epsilon,
    color="blue",
    linestyle="--",
    linewidth=2,
    label=rf"Bound $\left(1-\varepsilon\right)={1 - epsilon:.2f}$",
)
plt.axhline(
    y=1 + epsilon,
    color="blue",
    linestyle="--",
    linewidth=2,
    label=rf"Bound $\left(1+\varepsilon\right)={1 + epsilon:.2f}$",
)
plt.axhline(
    y=1,
    color="black",
    linestyle="-",
    linewidth=1,
    label=r"Ideal $\left(R=1\right)$",
)
plt.title(rf"Distorsión de las distancias proyectadas $\left(k={k}\right)$")
plt.xlabel("Índice del par de puntos")
plt.ylabel(
    r"$R=\dfrac{\left\|T_{U\left(\omega\right)}\left(x_{i}\right)-T_{U\left(\omega\right)}\left(x_{j}\right)\right\|}{\left\|x_{i}-x_{j}\right\|}$"
)
plt.ylim(min(R.min(), 1 - epsilon) - 0.05, max(R.max(), 1 + epsilon) + 0.05)
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend()
plt.savefig("figura21_python.pdf", transparent=True, bbox_inches="tight")
