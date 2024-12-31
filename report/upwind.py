import numpy as np
import matplotlib.pyplot as plt

x, Δx = np.linspace(start=0, stop=30, num=251, retstep=True)
t, Δt = np.linspace(start=0, stop=1, num=51, retstep=True)
c = 1
cfl = c * Δt / Δx


def U(x, U_left=2, U_right=1, x0=15):
    return U_left + (U_right - U_left) * np.heaviside(x - x0, 0)


fig, ax = plt.subplots(layout="constrained")
(ln,) = ax.plot(
    [],
    [],
    color="DarkBlue",
    label="Exacta",
    linestyle="dashed",
    linewidth=0.5,
)
ln1 = ax.scatter(
    x=[],
    y=[],
    c="blue",
    label=rf"$\operatorname{{Co}}={cfl:.1f}$, $\Delta x={Δx:.3f}$",
    s=0.4,
)
ax.set_xlabel(xlabel=r"$x$")
ax.set_xlim(left=x[0], right=x[-1])
ax.set_ylim(bottom=1 - 0.1, top=2 + 0.1)
ax.set_title(label="Método Upwind para un problema de Riemann", loc="center")

U1 = U(x=x)


def init():
    ln.set_data(x, U(x))
    ln1.set_offsets(offsets=np.column_stack([x, U1]))

    return (ln,)


def update(frame):
    ln1.set_offsets(offsets=np.column_stack([x, U1]))
    ln.set_data(x, U(x=x - c * frame * Δt))
    U1[1:] -= cfl * (U1 - np.roll(U1, 1))[1:]
    ax.set_ylabel(
        ylabel=rf"$U\left(x, t={frame * Δt:.2f}\right)$", loc="top", rotation=0
    )

    return (ln,)
