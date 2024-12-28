#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FFMpegWriter, FuncAnimation
from tqdm import tqdm

plt.style.use("seaborn-v0_8-white")


def U(x):
    return np.exp(-np.power(x - 15, 2))


x, Δx = np.linspace(start=0, stop=20, num=201, retstep=True)
t, Δt = np.linspace(start=0, stop=1, num=51, retstep=True)
c = -1.0

fig, ax = plt.subplots(layout="constrained")
ax.plot(x, U(x))
ax.plot(x, U(x - c * (t[0] + 10 * Δt)))
ax.plot(x, U(x - c * (t[0] + 20 * Δt)))
ax.plot(x, U(x - c * (t[0] + 30 * Δt)))
ax.plot(x, U(x - c * (t[0] + 40 * Δt)))
ax.plot(x, U(x - c * (t[0] + 50 * Δt)))
ax.set_xlim(left=x[0], right=x[-1])
ax.set_ylim(bottom=0, top=1)
plt.savefig("test1.pdf")
plt.close()

fig, ax = plt.subplots(layout="constrained")
(ln,) = ax.plot(
    [],
    [],
    color="red",
    label="Exacta",
    linestyle="dashed",
    linewidth=0.5,
)


def init():
    ln.set_data(x, U(x))

    return (ln,)


def update(frame):
    print(frame)
    ln.set_data(x, U(x=x - c * (t[0] + frame * Δt)))
    ax.set_ylabel(
        ylabel=rf"$U\left(x, t={frame * Δt:.2f}\right)$", loc="top", rotation=0
    )

    return (ln,)


anim = FuncAnimation(
    fig=fig,
    func=update,
    frames=tqdm(iterable=range(t.size), file=sys.stdout, colour="green"),
    interval=1,
    init_func=init,
    blit=True,
).save(
    filename="fou1d.gif",
    writer=FFMpegWriter(
        fps=90,
        codec="libx265",
        metadata={
            "subject": "Numerical Analysis",
            "title": "Exact solution",
            "author": "Gloria Almozara Sainz",
            "genre": "Mathematics",
            "copyright": "2025",
            "srcform": "Matplotlib 3.9.3",
            "comment": "Numerical Simulation for advection PDE",
        },
    ),
    dpi=300,
    savefig_kwargs={"transparent": True, "facecolor": "none"},
)
