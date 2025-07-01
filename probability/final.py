#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

print(norm.cdf(1))
P72 = 1 - norm.cdf(-1)
P84 = 1 - norm.cdf(1)
print(P84 / P72)


# Región de integración
x = np.linspace(start=0, stop=1, num=100)
y = np.linspace(start=0, stop=1, num=100)
X, Y = np.meshgrid(x, y)
Z = 2 * np.ones_like(X)

# Máscara para y < x
mask = Y < X
Z_masked = np.where(mask, Z, np.nan)
Z_base = np.zeros_like(X)
Z_base = np.where(mask, Z_base, np.nan)

# Gráfico 3D
plt.style.use("seaborn-v0_8-white")
fig, ax = plt.subplots(layout="constrained", subplot_kw=dict(projection="3d"))
ax.plot_surface(X, Y, Z_base, color="orange", alpha=0.4, label="Base triangular")
# Superficie principal
ax.plot_surface(X, Y, Z_masked, cmap="viridis", alpha=0.8)
# Recta y = x en el plano xy (línea roja)
ax.plot(x, x, 0, color="red", linewidth=2, label=r"$y=x$")
ax.set_xticks(ticks=np.linspace(start=x[0], stop=x[-1], num=2))
ax.set_yticks(ticks=np.linspace(start=y[0], stop=y[-1], num=2))
ax.set_zticks(ticks=np.linspace(start=0, stop=2, num=3))
ax.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.set_aspect(aspect="equal", adjustable="box")
ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$y$")
ax.set_xlim(left=x[0], right=x[-1])
ax.set_ylim(bottom=y[0], top=y[-1])
plt.title(r"Volumen bajo $f\left(x,y\right)=2\cdot\mathbf{1}_{A}\left(x,y\right)$")
plt.savefig("2final.pdf", transparent=True, bbox_inches="tight")
