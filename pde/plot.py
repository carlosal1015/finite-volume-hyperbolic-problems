import matplotlib.pyplot as plt
import numpy as np

N = 4
x = np.linspace(start=N * 0, stop=N * 4, num=2000)
x_mod = np.mod(x, 4)
phi = np.piecewise(
    x=x,
    condlist=[
        (x_mod > 0) & (x_mod <= 1),
        (x_mod > 1) & (x_mod <= 2),
        (x_mod > 2) & (x_mod <= 3),
    ],
    funclist=[lambda t: 1, lambda t: 2, lambda t: 3, lambda t: 4],
)

plt.style.use("seaborn-v0_8-white")
fig, ax = plt.subplots(layout="constrained")
ax.set_xlabel(xlabel=r"$x$")
ax.set_ylabel(ylabel=r"$\phi\left(x\right)$")
ax.set_xlim(x.min(), x.max())
ax.set_ylim(phi.min(), phi.max())
phi[:: phi.size // N] = np.nan
ax.plot(
    x,
    phi,
    color="DarkRed",
    label=r"$f\left(t\right)$",
    linestyle="solid",
    linewidth=0.8,
)
ax.grid(c="gray", linewidth=0.1, linestyle="dashed")
ax.set_title(
    label=rf"Señal periódica en ${0 * N}\leq x\leq {4 * N}$",
    loc="center",
)
ax.set_aspect("equal", adjustable="box")
ax.spines["left"].set_alpha(alpha=0.8)
ax.spines["left"].set_edgecolor(color="gray")
ax.spines["left"].set_linewidth(w=0.5)
ax.spines["right"].set_alpha(alpha=0.8)
ax.spines["right"].set_edgecolor(color="gray")
ax.spines["right"].set_linewidth(w=0.5)
ax.spines["top"].set_color("none")
ax.spines["bottom"].set_alpha(alpha=0.8)
ax.spines["bottom"].set_edgecolor(color="gray")
ax.spines["bottom"].set_linewidth(w=0.5)
plt.savefig("2.pdf", transparent=True, bbox_inches="tight")
