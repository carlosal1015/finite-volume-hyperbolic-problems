#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np

# Región de integración
x = np.linspace(0, 1, 100)
y = np.linspace(0, 1, 100)
X, Y = np.meshgrid(x, y)
Z = 1 - X**2

# Máscara para y <= x
mask = Y <= X
Z_masked = np.where(mask, Z, np.nan)
Z_base = np.zeros_like(X)
Z_base = np.where(mask, Z_base, np.nan)

# Gráfico 3D
fig = plt.figure()
ax = fig.add_subplot(projection="3d")
ax.plot_surface(X, Y, Z_base, color="orange", alpha=0.4, label="Base triangular")
# Superficie principal
ax.plot_surface(X, Y, Z_masked, cmap="viridis", alpha=0.8)
# Recta y = x en el plano xy (línea roja)
ax.plot(x, x, 0, color="red", linewidth=2, label=r"$y=x$")
# Parábola z = 1 - x² en el plano x-z (línea azul)
ax.plot(x, np.zeros_like(x), 1 - x**2, color="blue", linewidth=2, label=r"$z=1-x^{2}$")
ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$y$")
ax.set_xlim(left=x[0], right=x[-1])
ax.set_ylim(bottom=y[0], top=y[-1])
plt.title(r"Volumen bajo $f\left(x,y\right)=1-x^{2}$ en $0\leq y\leq x\leq 1$")
plt.savefig("2.pdf", transparent=True, bbox_inches="tight")
