#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np

plt.style.use("seaborn-v0_8-white")


def U(x):
    return np.exp(-50 * np.power(x - 0.3, 2))


c = 1
x = np.linspace(start=0, stop=1.15, num=400)

fig, ax = plt.subplots(layout="constrained")
ax.plot(x, U(x), color="red", linestyle="solid", linewidth=1)
ax.plot(x, U(x - c * 0.5), color="red", linestyle="solid", linewidth=1)
ax.arrow(
    x=0.45,
    y=0.6,
    dx=0.2,
    dy=0,
    length_includes_head=True,
    head_width=0.01,
    head_length=0.02,
)
ax.text(x=0.53, y=0.62, s=r"$ct$", fontdict=dict(size=18))
ax.text(x=0.36, y=0.9, s=r"$u\left(x,0\right)$", fontdict=dict(size=16))
ax.text(x=0.86, y=0.9, s=r"$u\left(x,t\right)$", fontdict=dict(size=16))
ax.set_xlim(left=x[0], right=x[-1])
ax.set_ylim(bottom=0, top=1)
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlabel(xlabel=r"$x$", loc="right", fontsize=18)
ax.set_ylabel(ylabel=r"$u\left(x,t\right)$", loc="top", rotation=0, fontsize=18)
ax.spines["left"].set_position("zero")
ax.spines["right"].set_color("none")
ax.spines["bottom"].set_position("zero")
ax.spines["top"].set_color("none")
plt.savefig("figure1.pdf", transparent=True, bbox_inches="tight")
