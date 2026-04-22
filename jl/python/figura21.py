import itertools

import matplotlib.pyplot as plt
import numpy as np

plt.style.use("seaborn-v0_8-white")

n, d, epsilon = 150, 100000, 0.1
X = np.random.uniform(low=0, high=1, size=(n, d))
k = int(np.ceil(4 * np.log(n) / ((epsilon**2) / 2 - (epsilon**3) / 3)))
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

fig, ax = plt.subplots(layout="constrained")
ax.scatter(
    range(len(R)), R, c=["darkgreen" if c else "red" for c in cumplen], s=10, alpha=0.7
)
ax.axhline(
    y=1 - epsilon,
    color="blue",
    linestyle="--",
    linewidth=0.8,
    label=rf"Cota $\left(1-\varepsilon\right)={1 - epsilon:.2f}$",
)
ax.axhline(
    y=1 + epsilon,
    color="blue",
    linestyle="--",
    linewidth=1,
    label=rf"Cota $\left(1+\varepsilon\right)={1 + epsilon:.2f}$",
)
ax.axhline(
    y=1,
    color="black",
    linestyle="-",
    linewidth=0.8,
    label=r"Ideal $\left(R=1\right)$",
)
ax.set_xlim(0 - 1, 500 + 1)
ax.set_ylim(min(R.min(), 1 - epsilon) - 0.005, max(R.max(), 1 + epsilon) + 0.005)
ax.set_title(
    label=rf"Distorsión de las distancias proyectadas $\left(k={k}\right)$",
    loc="center",
    wrap=True,
    fontsize=13,
)
ax.set_xlabel(
    xlabel="Índice del par de puntos",
    fontsize=13,
)
ax.set_ylabel(
    ylabel=r"$R=\frac{\left\|T_{U\left(\omega\right)}\left(x_{i}\right)-T_{U\left(\omega\right)}\left(x_{j}\right)\right\|}{\left\|x_{i}-x_{j}\right\|}$",
    fontsize=13,
)
ax.grid(c="gray", linewidth=0.1, linestyle="dashed")
ax.legend(
    loc="best",
    shadow=True,
    fontsize=13,
)
ax.set_xticks(ticks=np.linspace(start=0, stop=500, num=6))
ax.set_yticks(ticks=np.linspace(start=0.9, stop=1.1, num=6))
ax.spines["bottom"].set_color("none")
ax.spines["top"].set_color("none")
ax.spines["left"].set_color("none")
ax.spines["right"].set_color("none")
fig.savefig("figura21_python.pdf", transparent=True, bbox_inches="tight")
