#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from calculations import f, m, varepsilon, theta0, q
SoR = 1 / 2
L = 1e-10
So = np.linspace(start=-L, stop=L, num=2000)
θ = np.linspace(start=-L, stop=L, num=2000)
So_, θ_ = np.meshgrid(So, θ)
LHS = So_ * (SoR - So_)
RHS = f(θ_)
# RHS = θ_ / (1 - θ_) * np.exp(1 / (θ_ + 1))
equation = LHS - RHS

So_detail = np.linspace(start=0, stop=0.5, num=200)
θ_detail = np.linspace(start=0, stop=0.01, num=200)

if __name__ == "__main__":
    fig, ax = plt.subplots()
    ax.set_xlabel(r"$S_{0}$")
    ax.set_ylabel(r"$\theta$")
    # ax.set_ylim(0, 4e-2)
    ax.set_title(
    label=rf"Case 3.1.2, $f\left(\theta\right)$ with parameters $m={{{m}}}$, $\varepsilon={{{varepsilon:.2f}}}$, $\theta_{0}={{{theta0:.2f}}}$, $q={{{q:.3f}}}$"
    + "\n"
    + rf"$1+q\varepsilon={{{(1 + q * varepsilon):.3f}}}>0$, "
    + rf"$2\theta_{0}-\varepsilon={{{(2 * theta0 - varepsilon):.3f}}}>0$",
    loc="center",
    wrap=True,
    fontsize=15,
)
    CS_1 = ax.contour(So_, θ_, equation, [0], linewidths=0.5, colors=["red"])
    fig.savefig("phaseportrait3.1.2.pdf", transparent=True, bbox_inches="tight")
