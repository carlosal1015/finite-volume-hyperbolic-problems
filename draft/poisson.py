#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
from scipy.sparse import csr_array, diags_array
from scipy.sparse.linalg import spsolve


def fvm_poisson1d(N: int):
    """Computes the finite volume matrix for the Poisson problem in 1D

    Parameters:
    N (int): Number of grid points :math:`\\{x_i\\}_{i=0}^N` counting from 0.

    Returns:
    A (scipy.sparse._csr.csr_array): Finite difference sparse matrix

    """

    Δx = 1 / N
    diag = np.concatenate(
        (
            np.ones(shape=1),
            np.full(shape=N - 1, fill_value=2 / Δx**2),
            np.ones(shape=1),
        )
    )
    diag_sup = np.concatenate(
        (np.zeros(shape=1), np.full(shape=N - 1, fill_value=-1 / Δx**2))
    )
    diag_inf = np.flipud(m=diag_sup)

    return diags_array(
        [diag, diag_sup, diag_inf],
        offsets=[0, 1, -1],
        shape=(N + 1, N + 1),
        format="csr",
    )


N = 10
x, Δx = np.linspace(start=-1, stop=1, num=N + 1, retstep=True)
A = fvm_poisson1d(N)
f = np.power(np.pi / 2, 2) * np.cos(np.pi / 2 * x)
u = np.cos(np.pi * x / 2)

plt.style.use("seaborn-v0_8-white")

fig, ax = plt.subplots(layout="constrained")
ax.spy(Z=A, precision=0.1, markersize=1, color="blue")
ax.set_title(rf"Sparsity pattern of matrix $A^{h}$, $h={{{x}}}$")
plt.savefig("sparsitypattern.pdf", transparent=True, bbox_inches="tight")
plt.close()

# fig, ax = plt.subplots(layout="constrained")
# ax.plot(
#     x,
#     u,
#     color="DarkBlue",
#     label=r"$u\left(x\right)$",
#     linestyle="solid",
#     linewidth=0.5,
# )
# ax.set_xlabel(xlabel=r"$x$")
# ax.set_ylabel(ylabel=r"$y$")
# ax.set_xlim(x.min(), x.max())
# ax.set_ylim(u.min(), u.max())
# ax.legend(loc="best")
# ax.set_title(r"Gráfica de $\cos\left(\frac{\pi x}{2}\right)$")
# ax.grid(c="gray", linewidth=0.1, linestyle="dashed")
# ax.set_aspect("equal", adjustable="box")
# plt.savefig("poisson.pdf", transparent=True, bbox_inches="tight")
# plt.close()
