#!/usr/bin/env python

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.use("pgf")

arr = np.zeros(shape=(3, 4))

fig, ax = plt.subplots()
ax.imshow(arr, cmap="Blues")
ax.set_xticklabels([])
ax.set_yticklabels([])

xticks, dxticks = np.linspace(
    start=ax.get_xticks()[0],
    stop=ax.get_xticks()[-1],
    num=arr.shape[0] + 2,
    retstep=True,
)
yticks, dyticks = np.linspace(
    start=ax.get_yticks()[0],
    stop=ax.get_yticks()[-1],
    num=arr.shape[1],
    retstep=True,
)

ax.set_xticks(xticks)
ax.set_yticks(yticks)
ax.set_axisbelow(True)
ax.set_frame_on(False)
ax.tick_params(tick1On=False)

ax.scatter(x=xticks[1], y=yticks[2], s=40, c="red")
ax.scatter(x=xticks[2], y=yticks[2], s=40, c="red")
ax.scatter(x=xticks[3], y=yticks[2], s=40, c="red")
ax.scatter(x=xticks[1], y=yticks[1], s=40, c="red")
ax.scatter(x=xticks[2], y=yticks[1], s=40, c="blue")
ax.scatter(x=xticks[3], y=yticks[1], s=40, c="red")

plt.axhline(
    y=yticks[1],
    xmin=1 / arr.shape[1] + 0.012,
    xmax=2 / arr.shape[1] - 0.012,
    color="black",
)
plt.axhline(
    y=yticks[1],
    xmin=2 / arr.shape[1] + 0.012,
    xmax=3 / arr.shape[1] - 0.012,
    color="black",
)
plt.axhline(
    y=yticks[2],
    xmin=1 / arr.shape[1] + 0.012,
    xmax=2 / arr.shape[1] - 0.012,
    color="black",
)
plt.axhline(
    y=yticks[2],
    xmin=2 / arr.shape[1] + 0.012,
    xmax=3 / arr.shape[1] - 0.012,
    color="black",
)
plt.axvline(
    x=xticks[2],
    ymin=1 / arr.shape[0] + 0.016,
    ymax=2 / arr.shape[0] - 0.016,
    color="black",
)

plt.text(
    x=xticks[-1] + dxticks / 40, y=yticks[-1] + dyticks / 5, s="Space", fontsize=15
)
plt.text(x=xticks[0] - dxticks / 2, y=yticks[0], s="Time", fontsize=15)

plt.text(
    x=xticks[1] + dxticks / 2.5, y=yticks[2] + dyticks / 6, s=r"$\Delta x$", fontsize=12
)
plt.text(
    x=xticks[1] - dxticks / 5, y=yticks[1] + dyticks / 2, s=r"$\Delta t$", fontsize=12
)

plt.text(
    x=xticks[1] + dxticks / 10,
    y=yticks[1] - dyticks / 10,
    s=r"$\symbf{f}^{n+1}_{j-1}$",
    fontsize=14,
)
plt.text(
    x=xticks[2] + dxticks / 10,
    y=yticks[1] - dyticks / 10,
    s=r"$\symbf{u}^{n+1}_{j}$",
    fontsize=14,
)
plt.text(
    x=xticks[3] + dxticks / 10,
    y=yticks[1] - dyticks / 10,
    s=r"$\symbf{f}^{n+1}_{j+1}$",
    fontsize=14,
)
plt.text(
    x=xticks[1] + dxticks / 10,
    y=yticks[2] - dyticks / 10,
    s=r"$\symbf{f}^{n}_{j-1}$",
    fontsize=14,
)
plt.text(
    x=xticks[2] + dxticks / 10,
    y=yticks[2] - dyticks / 10,
    s=r"$\symbf{u}^{n}_{j}$",
    fontsize=14,
)
plt.text(
    x=xticks[3] + dxticks / 10,
    y=yticks[2] - dyticks / 10,
    s=r"$\symbf{f}^{n}_{j+1}$",
    fontsize=14,
)

plt.text(
    x=xticks[1] - dxticks / 7.5, y=yticks[3] + dyticks / 5, s=r"$j-1$", fontsize=14
)
plt.text(x=xticks[2] - dxticks / 20, y=yticks[3] + dyticks / 5, s=r"$j$", fontsize=14)
plt.text(
    x=xticks[3] - dxticks / 7.5, y=yticks[3] + dyticks / 5, s=r"$j+1$", fontsize=14
)
plt.text(x=xticks[0] - dxticks / 4, y=yticks[2], s=r"$n$", fontsize=14)
plt.text(x=xticks[0] - dxticks / 2.5, y=yticks[1], s=r"$n+1$", fontsize=14)
plt.grid(c="gray", lw=0.25)
plt.tight_layout()
plt.savefig("stencilcranknicolson.pdf", transparent=True, bbox_inches="tight")
