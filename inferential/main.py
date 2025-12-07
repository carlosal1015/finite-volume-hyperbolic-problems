#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

plt.style.use("seaborn-v0_8-white")

mu = 0
sigma = 1

x = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 1000)
y = norm.pdf(x, mu, sigma)

fig, ax = plt.subplots(layout="constrained")
ax.plot(
    x,
    y,
    color="blue",
    label="Distribución normal",
    linestyle="solid",
    linewidth=0.8,
)
ax.fill_between(x, 0, y, where=x > 1.5, color="red", alpha=0.3)
ax.set_title("Distribución normal")
ax.set_xlim(x.min(), x.max())
ax.set_ylim(y.min() - 1e-3, y.max() + 2e-3)
ax.set_xlabel(r"$Z$")
ax.set_ylabel("Densidad de probabilidad")
# ax.set_aspect(aspect="equal", adjustable="box")
ax.grid(c="gray", linewidth=0.1, linestyle="dashed")
plt.savefig("normal.pdf", transparent=True, bbox_inches="tight")
