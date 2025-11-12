#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from model import f, fprime, fprimeprime, q

plt.style.use("seaborn-v0_8-white")

mesh_quality = True
if mesh_quality:
    # fine grid
    θ = np.concatenate(
        (
            np.arange(0, 0.1, 0.001),
            np.arange(0.1, 1, 0.01),
            np.linspace(start=1, stop=580, num=3000),
            np.arange(580, 581, 0.000001),
            np.linspace(start=581, stop=900, num=3000),
        )
    )
    name = "Fine grid"
else:
    # coarse grid
    θ = np.linspace(start=0, stop=600)
    name = "Coarse grid"

fig, ax = plt.subplots(layout="constrained")
ax.plot(
    θ,
    f(θ),
    color="blue",
    label=r"$f\left(\theta\right)$",
    linewidth=0.7,
    linestyle="solid",
)
ax.grid(c="gray", linewidth=0.1, linestyle="dashed")
ax.legend(loc="best")
ax.set_title(f"Plot with {name}")
ax.set_xlim(θ.min(), 1)
ax.set_ylim(0, 35e-4)
ax.spines["bottom"].set_color("none")
ax.spines["top"].set_color("none")
ax.spines["left"].set_color("none")
ax.spines["right"].set_color("none")
plt.savefig("modelfa.pdf", transparent=True, bbox_inches="tight")
plt.clf()

fig, ax = plt.subplots(layout="constrained")
ax.plot(
    θ,
    f(θ),
    color="blue",
    label=r"$f\left(\theta\right)$",
    linewidth=0.7,
    linestyle="solid",
)
ax.grid(c="gray", linewidth=0.1, linestyle="dashed")
ax.legend(loc="best")
ax.set_title(f"Plot with {name}")
ax.set_xlim(θ.min(), 100)
ax.set_ylim(0, 1e-7)
ax.spines["bottom"].set_color("none")
ax.spines["top"].set_color("none")
ax.spines["left"].set_color("none")
ax.spines["right"].set_color("none")
plt.savefig("modelfb.pdf", transparent=True, bbox_inches="tight")
plt.clf()

fig, ax = plt.subplots(layout="constrained")
ax.plot(
    θ,
    f(θ),
    color="blue",
    label=r"$f\left(\theta\right)$",
    linewidth=0.7,
    linestyle="solid",
)
ax.grid(c="gray", linewidth=0.1, linestyle="dashed")
ax.axhline(
    y=1 / 4,
    color="r",
    linestyle="--",
    linewidth=0.5,
    label=r"$f\left(\theta_{M}\right)$",
)
ax.legend(loc="best")
ax.set_title(f"Plot with {name}")
ax.set_xlim(580.54360750766, 580.54360750768)  # 580.5436075076696
# 580.54360750848110229
ax.set_ylim(0.249999999, 0.250000001)
ax.spines["bottom"].set_color("none")
ax.spines["top"].set_color("none")
ax.spines["left"].set_color("none")
ax.spines["right"].set_color("none")
plt.savefig("modelfc.pdf", transparent=True, bbox_inches="tight")
plt.clf()

fig, ax = plt.subplots(layout="constrained")
ax.plot(
    θ,
    f(θ),
    color="blue",
    label=r"$f\left(\theta\right)$",
    linewidth=0.7,
    linestyle="solid",
)
ax.grid(c="gray", linewidth=0.1, linestyle="dashed")
ax.axhline(
    y=0.0034812091943386128,
    color="r",
    linestyle="--",
    linewidth=0.5,
    label=r"$f\left(\theta_{1}\right)$",
)
ax.legend(loc="best")
ax.set_title(f"Plot with {name}")
ax.set_xlim(580.5218, 580.52185)
ax.set_ylim(0.003475, 0.0035)
ax.spines["bottom"].set_color("none")
ax.spines["top"].set_color("none")
ax.spines["left"].set_color("none")
ax.spines["right"].set_color("none")
plt.savefig("modelfd.pdf", transparent=True, bbox_inches="tight")
plt.clf()

fig, ax = plt.subplots(layout="constrained")
ax.plot(
    θ,
    fprime(θ),
    color="red",
    label=r"$f^{\prime}\left(\theta\right)$",
    linewidth=0.7,
    linestyle="solid",
)
ax.grid(c="gray", linewidth=0.1, linestyle="dashed")
ax.legend(loc="best")
ax.set_title(f"Plot with {name}")
ax.set_xlim(θ.min(), 1)
ax.set_ylim(-21e-3, 16e-3)
ax.spines["bottom"].set_color("none")
ax.spines["top"].set_color("none")
ax.spines["left"].set_color("none")
ax.spines["right"].set_color("none")
plt.savefig("modelfprimea.pdf", transparent=True, bbox_inches="tight")
plt.clf()

fig, ax = plt.subplots(layout="constrained")
ax.plot(
    θ,
    fprime(θ),
    color="red",
    label=r"$f^{\prime}\left(\theta\right)$",
    linewidth=0.7,
    linestyle="solid",
)
ax.grid(c="gray", linewidth=0.1, linestyle="dashed")
ax.legend(loc="best")
ax.set_title(f"Plot with {name}")
ax.set_xlim(0, 100)
ax.set_ylim(-1e-9, 1e-9)
ax.spines["bottom"].set_color("none")
ax.spines["top"].set_color("none")
ax.spines["left"].set_color("none")
ax.spines["right"].set_color("none")
plt.savefig("modelfprimeb.pdf", transparent=True, bbox_inches="tight")
plt.clf()

fig, ax = plt.subplots(layout="constrained")
ax.plot(
    θ,
    fprimeprime(θ),
    color="green",
    label=r"$f^{\prime\prime}\left(\theta\right)$",
    linewidth=0.7,
    linestyle="solid",
)
ax.grid(c="gray", linewidth=0.1, linestyle="dashed")
ax.legend(loc="best")
ax.set_title(f"Plot with {name}")
ax.set_xlim(θ.min(), 1)
ax.set_ylim(-7, 1)
ax.spines["bottom"].set_color("none")
ax.spines["top"].set_color("none")
ax.spines["left"].set_color("none")
ax.spines["right"].set_color("none")
plt.savefig("modelfprimeprimea.pdf", transparent=True, bbox_inches="tight")
plt.clf()

fig, ax = plt.subplots(layout="constrained")
ax.plot(
    θ,
    fprimeprime(θ),
    color="green",
    label=r"$f^{\prime\prime}\left(\theta\right)$",
    linewidth=0.7,
    linestyle="solid",
)
ax.grid(c="gray", linewidth=0.1, linestyle="dashed")
ax.legend(loc="best")
ax.set_title(f"Plot with {name}")
ax.set_xlim(0, 100)
ax.set_ylim(-1e-9, 1e-9)
ax.spines["bottom"].set_color("none")
ax.spines["top"].set_color("none")
ax.spines["left"].set_color("none")
ax.spines["right"].set_color("none")
plt.savefig("modelfprimeprimeb.pdf", transparent=True, bbox_inches="tight")
plt.clf()

fig, ax = plt.subplots(layout="constrained")
ax.plot(
    θ,
    f(θ),
    color="blue",
    label=r"$f\left(\theta\right)$",
    linewidth=0.7,
    linestyle="solid",
)
ax.plot(
    θ,
    fprime(θ),
    color="red",
    label=r"$f^{\prime}\left(\theta\right)$",
    linewidth=0.7,
    linestyle="solid",
)
ax.plot(
    θ,
    fprimeprime(θ),
    color="green",
    label=r"$f^{\prime\prime}\left(\theta\right)$",
    linewidth=0.7,
    linestyle="solid",
)
ax.grid(c="gray", linewidth=0.1, linestyle="dashed")
ax.legend(loc="best")
ax.set_title(f"Plot with {name}")
ax.set_xlim(θ.min(), 100)
ax.spines["bottom"].set_color("none")
ax.spines["top"].set_color("none")
ax.spines["left"].set_color("none")
ax.spines["right"].set_color("none")
plt.savefig("modelall.pdf", transparent=True, bbox_inches="tight")
plt.clf()

fig, ax = plt.subplots(layout="constrained")
ax.plot(
    θ,
    fprime(θ),
    color="red",
    label=r"$f^{\prime}\left(\theta\right)$",
    linewidth=0.7,
    linestyle="solid",
)
ax.plot(
    θ,
    fprimeprime(θ),
    color="green",
    label=r"$f^{\prime\prime}\left(\theta\right)$",
    linewidth=0.7,
    linestyle="solid",
)
ax.grid(c="gray", linewidth=0.1, linestyle="dashed")
ax.legend(loc="best")
ax.set_title(f"Plot with {name}")
ax.set_xlim(θ.min(), 50)
ax.set_ylim(-1e-9, 1e-9)
ax.spines["bottom"].set_color("none")
ax.spines["top"].set_color("none")
ax.spines["left"].set_color("none")
ax.spines["right"].set_color("none")
plt.savefig("modelfprimeandfprimeprime.pdf", transparent=True, bbox_inches="tight")
plt.clf()

fig, ax = plt.subplots(layout="constrained")
ax.plot(
    θ,
    f(θ),
    color="blue",
    label=r"$f\left(\theta\right)$",
    linewidth=0.7,
    linestyle="solid",
)
ax.grid(c="gray", linewidth=0.1, linestyle="dashed")
ax.legend(loc="best")
ax.set_title(f"Plot with {name}")
ax.set_xlim(θ.min(), 100)
ax.set_ylim(-1e-7, 1e-7)
ax.spines["bottom"].set_color("none")
ax.spines["top"].set_color("none")
ax.spines["left"].set_color("none")
ax.spines["right"].set_color("none")
plt.savefig("modelfzoom.pdf", transparent=True, bbox_inches="tight")
plt.clf()
# θM = 1 / 4
