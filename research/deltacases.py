#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np

m = 3.702113166195264e-12
ε = 4 - 4e-2
θ0 = 1
q = -1e-2

θcrit = (ε - 2 * θ0) / (2 * (1 + q * ε))

θ = np.linspace(start=0, stop=20000, num=20000)
f = m * θ / (1 - q * θ) * np.exp(ε / (θ0 + θ))

fig, ax = plt.subplots(layout="constrained")
ax.plot(θ, f, label=r"$f$", linewidth=0.7)
ax.grid(c="gray", linewidth=0.1, linestyle="dashed")
ax.axhline(-m / q, color="red", linestyle="dashed", linewidth=0.7)
ax.set_xlim(θ[0], θ[-1])
ax.set_ylim(0, 4e-10)
ax.text(x=-1e3, y=-m / q, s=r"$-\frac{m}{q}$", fontdict=dict(size=12))
ax.set_xticks(ticks=np.linspace(start=θ[0], stop=θ[-1], num=5))
ax.set_yticks(ticks=np.linspace(start=0, stop=4e-10, num=5))
ax.set_xlabel(xlabel=r"$\theta$")
ax.set_ylabel(ylabel=r"$f\left(\theta\right)$")
ax.spines["bottom"].set_color("none")
ax.spines["top"].set_color("none")
ax.spines["left"].set_color("none")
ax.spines["right"].set_color("none")
plt.savefig("casedeltazeroa.pdf", transparent=True, bbox_inches="tight")
plt.clf()

θ = np.linspace(start=0, stop=4, num=1000)
f = m * θ / (1 - q * θ) * np.exp(ε / (θ0 + θ))
fprime = f * (1 / θ + q / (1 - q * θ) - ε / (θ0 + θ) ** 2)
fprimeprime = -f * (
    (2 * ε * q) / ((1 - q * θ) * (θ0 + θ) ** 2)
    - ε * (2 + ε / (θ0 + θ)) / (θ0 + θ) ** 3
    + 2 * ε / (θ * (θ0 + θ) ** 2)
    - 2 * q**2 / (1 - q * θ) ** 2
    - 2 * q / (θ * (1 - q * θ))
)
fig, ax = plt.subplots()
ax.plot(θ, f, label=r"$f\left(\theta\right)$", linewidth=0.7)
ax.plot(θ, fprime, label=r"$f^{\prime}\left(\theta\right)$", linewidth=0.7)
ax.plot(θ, fprimeprime, label=r"$f^{\prime\prime}\left(\theta\right)$", linewidth=0.5)
ax.legend()
ax.grid(c="gray", linewidth=0.1, linestyle="dashed")
# ax.axhline(y=0, color="black", linestyle="solid", linewidth=1)
ax.axvline(θcrit, ymin=0, ymax=1 / 4, color="red", linestyle="dashed", linewidth=0.5)
ax.text(x=θcrit, y=-1.15e-11, s=r"$\theta^{\text{crit}}$", fontdict=dict(size=12))
ax.set_xlim(θ[0], θ[-1])
ax.set_ylim(-1e-11, 3e-11)
ax.set_xlabel(xlabel=r"$\theta$")
ax.set_xticks(ticks=np.linspace(start=θ[0], stop=θ[-1], num=5))
ax.set_yticks(ticks=np.linspace(start=-1e-11, stop=3e-11, num=5))
ax.spines["bottom"].set_color("none")
ax.spines["top"].set_color("none")
ax.spines["left"].set_color("none")
ax.spines["right"].set_color("none")
plt.savefig("casedeltazerob.pdf", transparent=True, bbox_inches="tight")
plt.clf()

m = 3.702113166195264e-12
ε = 4 - 4e-2
θ0 = 1
q = -1e-2

θcrit = (ε - 2 * θ0) / (2 * (1 + q * ε))
