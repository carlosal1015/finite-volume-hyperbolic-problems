#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np

plt.style.use("seaborn-v0_8-white")

x = np.linspace(start=0, stop=4, num=5)

fig, ax = plt.subplots(layout="constrained")
ax.plot(x, np.zeros_like(x))
ax.scatter(x=x, y=np.zeros_like(x))
ax.text(x=0, y=-0.01, s=r"$x_{i-\frac{1}{2}}$", fontdict=dict(size=18))
ax.text(x=1 - 0.08, y=-0.01, s=r"$x_{i}$", fontdict=dict(size=18))
ax.text(x=2 - 0.08, y=-0.01, s=r"$x_{i+\frac{1}{2}}$", fontdict=dict(size=18))
ax.text(x=3 - 0.08, y=-0.01, s=r"$x_{i+1}$", fontdict=dict(size=18))
ax.text(x=4 - 0.08, y=-0.01, s=r"$x_{i+\frac{3}{2}}$", fontdict=dict(size=18))
ax.text(x=0.01, y=0.01, s=r"$\overbrace{\phantom{00000000000000000000000}}^{\text{celda }c_{i}}$", fontdict=dict(size=18))
ax.text(x=2.01, y=0.01, s=r"$\overbrace{\phantom{00000000000000000000000}}^{\text{celda }c_{i+1}}$", fontdict=dict(size=18))
ax.set_xlim(left=x[0] - 0.1, right=x[-1] + 0.1)
ax.set_ylim(bottom=-0.1, top=0.1)
ax.set_xticks([])
ax.set_yticks([])
ax.set_frame_on(False)
ax.tick_params(tick1On=False)
plt.savefig("figure3.pdf", transparent=True, bbox_inches="tight")
