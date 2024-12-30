#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np

plt.style.use("seaborn-v0_8-white")

x = np.linspace(start=0, stop=1, num=2)

fig, ax = plt.subplots(layout="constrained")
ax.arrow(
    x=1, y=0, dx=-1, dy=1, length_includes_head=True, head_width=0.01, head_length=0.02
)
ax.text(x=0, y=-0.08, s=r"$x_{1}$", fontdict=dict(size=18))
ax.text(x=1 - 0.08, y=-0.08, s=r"$x_{1}+\Delta x$", fontdict=dict(size=18))
ax.text(x=-0.08, y=0, s=r"$t_{1}$", fontdict=dict(size=18))
ax.text(x=-0.18, y=1 - 0.04, s=r"$t_{1}+\Delta t$", fontdict=dict(size=18))
ax.text(x=0.3, y=0.3, s=r"$u=u_{l}$", fontdict=dict(size=18))
ax.text(x=0.6, y=0.6, s=r"$u=u_{r}$", fontdict=dict(size=18))
ax.text(x=-0.2, y=1 + 0.05, s="Discontinuidad", fontdict=dict(size=18))
ax.grid(c="gray", linewidth=0.1, linestyle="dashed")
ax.spines["bottom"].set_edgecolor(color="gray")
ax.spines["top"].set_edgecolor(color="gray")
ax.spines["left"].set_edgecolor(color="gray")
ax.spines["right"].set_edgecolor(color="gray")
ax.set_xlim(left=x[0], right=x[-1])
ax.set_ylim(bottom=x[0], top=x[-1])
ax.set_xticks([])
ax.set_yticks([])
plt.savefig("figure2.pdf", transparent=True, bbox_inches="tight")
