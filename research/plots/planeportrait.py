#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint


# def dx_dt(x, t):
#     return [x[1], x[0] * (1 - x[0] ** 2) + x[1]]


def dx_dt(So, θ):
    return [So[1], So[0] * (1 - So[0] ** 2) + x[1]]


fig, ax = plt.subplots()
# Trajectories in forward time.
ts = np.linspace(0, 10, 500)
ic = np.linspace(-3, 3, 6)
for r in ic:
    for s in ic:
        x0 = [r, s]
        xs = odeint(dx_dt, x0, ts)
        ax.plot(xs[:, 0], xs[:, 1], "r-")

# Trajectories in backward time.
ts = np.linspace(0, -10, 500)
ic = np.linspace(-3, 3, 6)
for r in ic:
    for s in ic:
        x0 = [r, s]
        xs = odeint(dx_dt, x0, ts)
        ax.plot(xs[:, 0], xs[:, 1], "r-")

ax.set_xlabel("x", fontsize=15)
ax.set_ylabel("y", fontsize=15)
# plt.tick_params(labelsize=15)
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)

# Plot the vectorfield.
X, Y = np.mgrid[-3:3:20j, -3:3:20j]
u = X
v = X * (1 - X**2) + Y
ax.quiver(X, Y, u, v, color="b")
fig.savefig("demophaseportrait.pdf", transparent=True, bbox_inches="tight")
