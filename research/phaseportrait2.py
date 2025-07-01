#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from calculations import f

SoR = 1 / 2
L = 5
So = np.linspace(start=0, stop=0.5, num=200)
θ = np.linspace(start=0, stop=0.025, num=200)
So_, θ_ = np.meshgrid(So, θ)
LHS = So_ * (SoR - So_)
# RHS = f(θ_)
RHS = θ_ / (1 - θ_) * np.exp(1 / (θ_ + 1))
equation = LHS - RHS

if __name__ == "__main__":
    fig, ax = plt.subplots()
    ax.set_xlabel(r"$S_{0}$")
    ax.set_ylabel(r"$\theta$")
    ax.set_title(r"$f\left(\theta\right)$ with parameters $m=n=p=q=1$")
    # ax.grid()
    # ax.set_xlim(So[0], So[-1])
    # ax.set_ylim(-4e-6, 4e-6)
    # ax.plot(So, So * (SoR - So), "b", lw=0.5)
    # ax.plot(θ, f(θ), "r", lw=0.5)
    # https://matplotlib.org/stable/gallery/subplots_axes_and_figures/axis_equal_demo.html
    # https://stackoverflow.com/a/39500357/9302545
    # ax.axis("equal")
    CS_1 = ax.contour(So_, θ_, equation, [0], linewidths=0.5, colors=["red"])
    # h, _ = CS.legend_elements()
    # label=r"$x + y = 24$"
    #     black_patch = mpatches.Patch(
    #         color="red", label=r"$x^{2} + xy = 77$", linewidth=0.1, linestyle="-"
    #     )
    #     ax.legend(
    #         handles=[black_patch], shadow=True, title="Leyenda", fancybox=True
    #     )
    fig.savefig("phaseportrait2.pdf", transparent=True, bbox_inches="tight")
