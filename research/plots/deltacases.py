#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np

"""Case Δ = 0, q < 0.
"""
m = 3.702113166195264e-12
ε = 4 - 4e-2
θ0 = 1
q = -1e-2
Δ = ε * (ε - 4 * θ0 - 4 * q * θ0**2)
assert np.isclose(a=Δ, b=0) and q < 0

θcrit = (ε - 2 * θ0) / (2 * (1 + q * ε))

θ = np.linspace(start=0, stop=20000, num=20000)
f = m * θ / (1 - q * θ) * np.exp(ε / (θ0 + θ))

fig, ax = plt.subplots(layout="constrained")
ax.plot(θ, f, label=r"$f\left(\theta\right)$", linewidth=0.7, color="blue")
ax.grid(c="gray", linewidth=0.1, linestyle="dashed")
ax.axhline(-m / q, color="red", linestyle="dashed", linewidth=0.7)
ax.set_xlim(θ[0], θ[-1])
ax.set_ylim(0, 4e-10)
ax.text(
    x=-1e3,
    y=-m / q,
    s=r"$-\frac{m}{q}$",
    fontdict=dict(size=12),
)
ax.set_xticks(ticks=np.linspace(start=θ[0], stop=θ[-1], num=5))
ax.set_yticks(ticks=np.linspace(start=0, stop=4e-10, num=5))
ax.set_xlabel(xlabel=r"$\theta$")
ax.legend(loc="lower right", shadow=True)
ax.spines["bottom"].set_color("none")
ax.spines["top"].set_color("none")
ax.spines["left"].set_color("none")
ax.spines["right"].set_color("none")
plt.savefig(
    "deltazeroa.pdf",
    transparent=True,
    bbox_inches="tight",
)
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
ax.plot(θ, f, label=r"$f\left(\theta\right)$", linewidth=0.7, color="blue")
ax.plot(
    θ, fprime, label=r"$f^{\prime}\left(\theta\right)$", linewidth=0.7, color="orange"
)
ax.plot(
    θ,
    fprimeprime,
    label=r"$f^{\prime\prime}\left(\theta\right)$",
    linewidth=0.5,
    color="green",
)
ax.legend(loc="best", shadow=True)
ax.grid(c="gray", linewidth=0.1, linestyle="dashed")
ax.axvline(
    θcrit,
    ymin=0,
    ymax=1 / 4,
    color="gray",
    linestyle="dashed",
    linewidth=0.5,
)
ax.text(
    x=θcrit,
    y=-1.15e-11,
    s=r"$\theta^{\text{crit}}$",
    fontdict=dict(size=12),
)
ax.set_xlim(θ[0], θ[-1])
ax.set_ylim(-1e-11, 3e-11)
ax.set_xlabel(xlabel=r"$\theta$")
ax.set_xticks(ticks=np.linspace(start=θ[0], stop=θ[-1], num=5))
ax.set_yticks(ticks=np.linspace(start=-1e-11, stop=3e-11, num=5))
ax.spines["bottom"].set_color("none")
ax.spines["top"].set_color("none")
ax.spines["left"].set_color("none")
ax.spines["right"].set_color("none")
plt.savefig(
    "deltazerob.pdf",
    transparent=True,
    bbox_inches="tight",
)
plt.clf()

θ = np.linspace(start=100, stop=4300, num=3000)
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
ax.plot(
    θ, fprime, label=r"$f^{\prime}\left(\theta\right)$", linewidth=0.7, color="orange"
)
ax.plot(
    θ,
    fprimeprime,
    label=r"$f^{\prime\prime}\left(\theta\right)$",
    linewidth=0.5,
    color="green",
)
ax.legend(loc="best", shadow=True)
ax.grid(c="gray", linewidth=0.1, linestyle="dashed")
ax.set_xlim(θ[0], θ[-1])
ax.set_ylim(-1e-13, 5e-13)
ax.set_xlabel(xlabel=r"$\theta$")
ax.set_xticks(ticks=np.linspace(start=θ[0], stop=θ[-1], num=7))
ax.set_yticks(ticks=np.linspace(start=-1e-13, stop=5e-13, num=7))
ax.spines["bottom"].set_color("none")
ax.spines["top"].set_color("none")
ax.spines["left"].set_color("none")
ax.spines["right"].set_color("none")
plt.savefig(
    "deltazeroc.pdf",
    transparent=True,
    bbox_inches="tight",
)
plt.clf()

q = 1
θ0 = 1
ε = 4 - 4e-2
m = 3.702113166195264e-12
θ = np.linspace(start=0, stop=2, num=30000)
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
ax.plot(θ, f, label=r"$f\left(\theta\right)$", linewidth=0.7, color="blue")
ax.plot(
    θ, fprime, label=r"$f^{\prime}\left(\theta\right)$", linewidth=0.7, color="orange"
)
ax.plot(
    θ,
    fprimeprime,
    label=r"$f^{\prime\prime}\left(\theta\right)$",
    linewidth=0.5,
    color="green",
)
ax.axhline(
    -m / q,
    color="black",
    linestyle="dashed",
    linewidth=0.7,
)
ax.legend(loc="best", shadow=True)
ax.grid(c="gray", linewidth=0.1, linestyle="dashed")
ax.set_xlim(θ[0], θ[-1])
ax.set_ylim(-1e-9, 1e-9)
ax.set_xlabel(xlabel=r"$\theta$")
ax.set_xticks(ticks=np.linspace(start=θ[0], stop=θ[-1], num=6))
ax.set_yticks(ticks=np.linspace(start=-1e-9, stop=1e-9, num=6))
ax.set_title(
    label=r"$q$"
    + f"= {q}, "
    + r"$\theta_0$"
    + f"= {θ0}, "
    + r"$\varepsilon$"
    + f" = {ε}, "
    + r"$m$"
    + f" ={m}",
    loc="center",
    wrap=True,
    fontsize=15,
)
ax.spines["bottom"].set_color("none")
ax.spines["top"].set_color("none")
ax.spines["left"].set_color("none")
ax.spines["right"].set_color("none")
plt.savefig(
    "epsilonmayorquedostheta.pdf",
    transparent=True,
    bbox_inches="tight",
)
plt.clf()

q = 1
θ0 = 1
ε = 2
m = 3.702113166195264e-12
θ = np.linspace(start=0, stop=2, num=30000)
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
ax.plot(θ, f, label=r"$f\left(\theta\right)$", linewidth=0.7, color="blue")
ax.plot(
    θ, fprime, label=r"$f^{\prime}\left(\theta\right)$", linewidth=0.7, color="orange"
)
ax.plot(
    θ,
    fprimeprime,
    label=r"$f^{\prime\prime}\left(\theta\right)$",
    linewidth=0.5,
    color="green",
)
ax.axhline(
    -m / q,
    color="black",
    linestyle="dashed",
    linewidth=0.7,
)
ax.legend(loc="best", shadow=True)
ax.grid(c="gray", linewidth=0.1, linestyle="dashed")
ax.set_xlim(θ[0], θ[-1])
ax.set_ylim(-1e-9, 1e-9)
ax.set_xlabel(xlabel=r"$\theta$")
ax.set_xticks(ticks=np.linspace(start=θ[0], stop=θ[-1], num=6))
ax.set_yticks(ticks=np.linspace(start=-1e-9, stop=1e-9, num=6))
ax.set_title(
    label=r"$q$"
    + f"= {q}, "
    + r"$\theta_0$"
    + f"= {θ0}, "
    + r"$\varepsilon$"
    + f" = {ε}, "
    + r"$m$"
    + f" ={m}",
    loc="center",
    wrap=True,
    fontsize=15,
)
ax.spines["bottom"].set_color("none")
ax.spines["top"].set_color("none")
ax.spines["left"].set_color("none")
ax.spines["right"].set_color("none")
plt.savefig(
    "epsilonigualadostheta.pdf",
    transparent=True,
    bbox_inches="tight",
)
plt.clf()

q = 1
θ0 = 1
ε = 1.5
m = 3.702113166195264e-12
θ = np.linspace(start=0, stop=2, num=30000)
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
ax.plot(θ, f, label=r"$f\left(\theta\right)$", linewidth=0.7, color="blue")
ax.plot(
    θ, fprime, label=r"$f^{\prime}\left(\theta\right)$", linewidth=0.7, color="orange"
)
ax.plot(
    θ,
    fprimeprime,
    label=r"$f^{\prime\prime}\left(\theta\right)$",
    linewidth=0.5,
    color="green",
)
ax.axhline(
    -m / q,
    color="black",
    linestyle="dashed",
    linewidth=0.7,
)
ax.legend(loc="best", shadow=True)
ax.grid(c="gray", linewidth=0.1, linestyle="dashed")
ax.set_xlim(θ[0], θ[-1])
ax.set_ylim(-1e-9, 1e-9)
ax.set_xlabel(xlabel=r"$\theta$")
ax.set_xticks(ticks=np.linspace(start=θ[0], stop=θ[-1], num=6))
ax.set_yticks(ticks=np.linspace(start=-1e-9, stop=1e-9, num=6))
ax.set_title(
    label=r"$q$"
    + f"= {q}, "
    + r"$\theta_0$"
    + f"= {θ0}, "
    + r"$\varepsilon$"
    + f" = {ε}, "
    + r"$m$"
    + f" ={m}",
    loc="center",
    wrap=True,
    fontsize=15,
)
ax.spines["bottom"].set_color("none")
ax.spines["top"].set_color("none")
ax.spines["left"].set_color("none")
ax.spines["right"].set_color("none")
plt.savefig(
    "epsilonmenorquedostheta.pdf",
    transparent=True,
    bbox_inches="tight",
)
plt.clf()

SoR = 1
So_ = np.linspace(start=-1, stop=1, num=2000)
θ_ = np.linspace(start=-1, stop=1, num=2000)
So, θ = np.meshgrid(So_, θ_)


def f(theta):
    return m * θ / (1 - q * θ) * np.exp(ε / (θ0 + θ))


fig, ax = plt.subplots()
ax.set_xlabel(r"$S_{0}$")
ax.set_ylabel(r"$\theta$")
ax.contour(So, θ, So * (SoR - So) - f(θ), [0], linewidths=0.5, colors=["red"])
ax.set_title(label="Case", loc="center", wrap=True, fontsize=15)
fig.savefig("phaseportraitdeltazeroa.pdf", transparent=True, bbox_inches="tight")

"""Case Δ > 0, q < 0, 1 + q * ε > 0.
"""

m = 3.702113166195264e-12
ε = 20.546467805308318
θ0 = 1
q = -1e-2

Δ = ε * (ε - 4 * θ0 - 4 * q * θ0**2)
assert Δ > 0 and q < 0 and (1 + q * ε) > 0
print(f"Case Δ > 0, q < 0, 1 + q * ε = {1 + q * ε}>0")

θcritplus = (ε - 2 * θ0 + np.sqrt(Δ)) / (2 * (1 + q * ε))
θcritminus = (ε - 2 * θ0 - np.sqrt(Δ)) / (2 * (1 + q * ε))

θ = np.linspace(start=0, stop=0.1, num=2000)
f = m * θ / (1 - q * θ) * np.exp(ε / (θ0 + θ))

fig, ax = plt.subplots(layout="constrained")
ax.plot(θ, f, label=r"$f\left(\theta\right)$", linewidth=0.7, color="blue")
ax.grid(c="gray", linewidth=0.1, linestyle="dashed")
ax.axhline(
    -m / q,
    color="red",
    linestyle="dashed",
    linewidth=0.7,
)
ax.set_xlim(θ[0], θ[-1])
ax.set_ylim(0, 6e-5)
ax.text(
    x=-1e-2,
    y=-m / q,
    s=r"$-\frac{m}{q}$",
    fontdict=dict(size=12),
)
ax.axvline(
    θcritminus,
    ymin=0,
    ymax=0.97,
    color="gray",
    linestyle="dashed",
    linewidth=0.5,
)
ax.text(
    x=θcritminus,
    y=-0.3e-5,
    s=r"$\theta^{\text{crit}}_{-}$",
    fontdict=dict(size=12),
)
ax.set_xticks(ticks=np.linspace(start=θ[0], stop=θ[-1], num=5))
ax.set_yticks(ticks=np.linspace(start=0, stop=6e-5, num=5))
ax.set_xlabel(xlabel=r"$\theta$")
ax.legend(loc="best", shadow=True)
ax.set_title(r"Case $1+q\varepsilon>0$")
ax.spines["bottom"].set_color("none")
ax.spines["top"].set_color("none")
ax.spines["left"].set_color("none")
ax.spines["right"].set_color("none")
plt.savefig(
    "deltapositivepositivea.pdf",
    transparent=True,
    bbox_inches="tight",
)
plt.clf()

θ = np.linspace(start=20, stop=30, num=2000)
f = m * θ / (1 - q * θ) * np.exp(ε / (θ0 + θ))

fig, ax = plt.subplots(layout="constrained")
ax.plot(θ, f, label=r"$f\left(\theta\right)$", linewidth=0.7, color="blue")
ax.grid(c="gray", linewidth=0.1, linestyle="dashed")
ax.axvline(
    θcritplus,
    ymin=0,
    ymax=0.24,
    color="gray",
    linestyle="dashed",
    linewidth=0.5,
)
ax.text(
    x=θcritplus,
    y=1.6185e-10,
    s=r"$\theta^{\text{crit}}_{+}$",
    fontdict=dict(size=12),
)
ax.set_xlim(θ[0], θ[-1])
ax.set_ylim(1.620e-10, 1.660e-10)
ax.set_xticks(ticks=np.linspace(start=θ[0], stop=θ[-1], num=5))
ax.set_yticks(ticks=np.linspace(start=1.620e-10, stop=1.660e-10, num=5))
ax.set_xlabel(xlabel=r"$\theta$")
ax.set_title(r"Case $1+q\varepsilon>0$")
ax.legend(loc="best", shadow=True)
ax.spines["bottom"].set_color("none")
ax.spines["top"].set_color("none")
ax.spines["left"].set_color("none")
ax.spines["right"].set_color("none")
plt.savefig(
    "deltapositivepositiveb.pdf",
    transparent=True,
    bbox_inches="tight",
)
plt.clf()

θ = np.linspace(start=5, stop=10, num=2000)
f = m * θ / (1 - q * θ) * np.exp(ε / (θ0 + θ))

fig, ax = plt.subplots(layout="constrained")
ax.plot(θ, f, label=r"$f\left(\theta\right)$", linewidth=0.7, color="blue")
ax.axhline(
    -m / q,
    color="red",
    linestyle="dashed",
    linewidth=0.7,
)
ax.text(
    x=4.75,
    y=-m / q,
    s=r"$-\frac{m}{q}$",
    fontdict=dict(size=12),
)
ax.grid(c="gray", linewidth=0.1, linestyle="dashed")
ax.set_xlim(θ[0], θ[-1])
ax.set_ylim(2e-10, 6e-10)
ax.set_xticks(ticks=np.linspace(start=θ[0], stop=θ[-1], num=5))
ax.set_yticks(ticks=np.linspace(start=2e-10, stop=6e-10, num=5))
ax.set_xlabel(xlabel=r"$\theta$")
ax.set_title(r"Case $1+q\varepsilon>0$")
ax.legend(loc="best", shadow=True)
ax.spines["bottom"].set_color("none")
ax.spines["top"].set_color("none")
ax.spines["left"].set_color("none")
ax.spines["right"].set_color("none")
plt.savefig(
    "deltapositivepositivec.pdf",
    transparent=True,
    bbox_inches="tight",
)
plt.clf()

θ = np.linspace(start=100, stop=8100, num=8000)
f = m * θ / (1 - q * θ) * np.exp(ε / (θ0 + θ))

fig, ax = plt.subplots(layout="constrained")
ax.plot(θ, f, label=r"$f\left(\theta\right)$", linewidth=0.7, color="blue")
ax.axhline(
    -m / q,
    color="red",
    linestyle="dashed",
    linewidth=0.7,
)
ax.grid(c="gray", linewidth=0.1, linestyle="dashed")
ax.set_xlim(θ[0], θ[-1])
ax.set_ylim(2e-10, 4e-10)
ax.set_xticks(ticks=np.linspace(start=θ[0], stop=θ[-1], num=5))
ax.set_yticks(ticks=np.linspace(start=2e-10, stop=4e-10, num=5))
ax.set_xlabel(xlabel=r"$\theta$")
ax.set_title(r"Case $1+q\varepsilon>0$")
ax.spines["bottom"].set_color("none")
ax.spines["top"].set_color("none")
ax.spines["left"].set_color("none")
ax.spines["right"].set_color("none")
plt.savefig(
    "deltapositivepositived.pdf",
    transparent=True,
    bbox_inches="tight",
)
plt.clf()

θ = np.linspace(start=0, stop=1, num=1000)
f = m * θ / (1 - q * θ) * np.exp(ε / (θ0 + θ))
fprime = f * (1 / θ + q / (1 - q * θ) - ε / (θ0 + θ) ** 2)
fprimeprime = -f * (
    (2 * ε * q) / ((1 - q * θ) * (θ0 + θ) ** 2)
    - ε * (2 + ε / (θ0 + θ)) / (θ0 + θ) ** 3
    + 2 * ε / (θ * (θ0 + θ) ** 2)
    - 2 * q**2 / (1 - q * θ) ** 2
    - 2 * q / (θ * (1 - q * θ))
)

fig, ax = plt.subplots(layout="constrained")
ax.plot(θ, f, label=r"$f\left(\theta\right)$", linewidth=0.7, color="blue")
ax.plot(
    θ, fprime, label=r"$f^{\prime}\left(\theta\right)$", linewidth=0.7, color="orange"
)
ax.plot(
    θ,
    fprimeprime,
    label=r"$f^{\prime\prime}\left(\theta\right)$",
    linewidth=0.5,
    color="green",
)
ax.grid(c="gray", linewidth=0.1, linestyle="dashed")
ax.set_xlim(θ[0], θ[-1])
ax.set_ylim(-2e-3, 2e-3)
ax.set_xticks(ticks=np.linspace(start=θ[0], stop=θ[-1], num=5))
ax.set_yticks(ticks=np.linspace(start=-2e-3, stop=2e-3, num=5))
ax.axvline(
    θcritminus,
    ymin=0.5,
    ymax=0.515,
    color="gray",
    linestyle="dashed",
    linewidth=0.5,
)
ax.text(
    x=θcritminus,
    y=-0.0001,
    s=r"$\theta^{\text{crit}}_{-}$",
    fontdict=dict(size=10),
)
ax.legend(loc="best", shadow=True)
ax.set_xlabel(xlabel=r"$\theta$")
ax.set_title(r"Case $1+q\varepsilon>0$")
ax.spines["bottom"].set_color("none")
ax.spines["top"].set_color("none")
ax.spines["left"].set_color("none")
ax.spines["right"].set_color("none")
plt.savefig(
    "deltapositivepositivee.pdf",
    transparent=True,
    bbox_inches="tight",
)
plt.clf()

θ = np.linspace(start=20, stop=30, num=1000)
f = m * θ / (1 - q * θ) * np.exp(ε / (θ0 + θ))
fprime = f * (1 / θ + q / (1 - q * θ) - ε / (θ0 + θ) ** 2)
fprimeprime = -f * (
    (2 * ε * q) / ((1 - q * θ) * (θ0 + θ) ** 2)
    - ε * (2 + ε / (θ0 + θ)) / (θ0 + θ) ** 3
    + 2 * ε / (θ * (θ0 + θ) ** 2)
    - 2 * q**2 / (1 - q * θ) ** 2
    - 2 * q / (θ * (1 - q * θ))
)

fig, ax = plt.subplots(layout="constrained")
# ax.plot(θ, f, label=r"$f$", linewidth=0.7, color="blue")
ax.plot(
    θ, fprime, label=r"$f^{\prime}\left(\theta\right)$", linewidth=0.7, color="orange"
)
ax.plot(
    θ,
    fprimeprime,
    label=r"$f^{\prime\prime}\left(\theta\right)$",
    linewidth=0.5,
    color="green",
)
ax.axvline(
    θcritplus,
    ymin=0.48,
    ymax=0.52,
    color="gray",
    linestyle="dashed",
    linewidth=0.5,
)
ax.text(
    x=θcritplus,
    y=-0.8e-13,
    s=r"$\theta^{\text{crit}}_{+}$",
    fontdict=dict(size=10),
)
ax.grid(c="gray", linewidth=0.1, linestyle="dashed")
ax.set_xlim(θ[0], θ[-1])
ax.set_ylim(-8e-13, 8e-13)
ax.set_xticks(ticks=np.linspace(start=θ[0], stop=θ[-1], num=5))
ax.set_yticks(ticks=np.linspace(start=-8e-13, stop=8e-13, num=5))
ax.legend(loc="best", shadow=True)
ax.set_xlabel(xlabel=r"$\theta$")
ax.set_title(r"Case $1+q\varepsilon>0$")
ax.spines["bottom"].set_color("none")
ax.spines["top"].set_color("none")
ax.spines["left"].set_color("none")
ax.spines["right"].set_color("none")
plt.savefig(
    "deltapositivepositivef.pdf",
    transparent=True,
    bbox_inches="tight",
)
plt.clf()

θ = np.linspace(start=20, stop=20000, num=30000)
f = m * θ / (1 - q * θ) * np.exp(ε / (θ0 + θ))
fig, ax = plt.subplots(layout="constrained")
ax.plot(θ, f, label=r"$f\left(\theta\right)$", linewidth=0.7, color="blue")
ax.axhline(-m / q, color="red", linestyle="dashed", linewidth=0.7)
ax.grid(c="gray", linewidth=0.1, linestyle="dashed")
ax.set_xlim(θ[0], θ[-1])
ax.set_ylim(1.5e-10, 4e-10)
ax.set_xticks(ticks=np.linspace(start=θ[0], stop=θ[-1], num=5))
ax.set_yticks(ticks=np.linspace(start=1.5e-10, stop=4e-10, num=5))
ax.legend(loc="best", shadow=True)
ax.set_xlabel(xlabel=r"$\theta$")
ax.set_title(r"Case $1+q\varepsilon>0$")
ax.spines["bottom"].set_color("none")
ax.spines["top"].set_color("none")
ax.spines["left"].set_color("none")
ax.spines["right"].set_color("none")
plt.savefig(
    "deltapositivepositiveg.pdf",
    transparent=True,
    bbox_inches="tight",
)
plt.clf()

θ = np.linspace(start=40, stop=2000, num=4000)
f = m * θ / (1 - q * θ) * np.exp(ε / (θ0 + θ))
fprime = f * (1 / θ + q / (1 - q * θ) - ε / (θ0 + θ) ** 2)
fprimeprime = -f * (
    (2 * ε * q) / ((1 - q * θ) * (θ0 + θ) ** 2)
    - ε * (2 + ε / (θ0 + θ)) / (θ0 + θ) ** 3
    + 2 * ε / (θ * (θ0 + θ) ** 2)
    - 2 * q**2 / (1 - q * θ) ** 2
    - 2 * q / (θ * (1 - q * θ))
)
fig, ax = plt.subplots(layout="constrained")
ax.plot(
    θ, fprime, label=r"$f^{\prime}\left(\theta\right)$", linewidth=0.7, color="orange"
)
ax.plot(
    θ,
    fprimeprime,
    label=r"$f^{\prime\prime}\left(\theta\right)$",
    linewidth=0.5,
    color="green",
)
ax.grid(c="gray", linewidth=0.1, linestyle="dashed")
ax.set_xlim(θ[0], θ[-1])
ax.set_ylim(-0.05e-12, 1.05e-12)
ax.set_xticks(ticks=np.linspace(start=θ[0], stop=θ[-1], num=5))
ax.set_yticks(ticks=np.linspace(start=-0.05e-12, stop=1.05e-12, num=5))
ax.axhline(0, color="gray", linestyle="dashed", linewidth=0.7)
ax.legend(loc="best", shadow=True)
ax.set_xlabel(xlabel=r"$\theta$")
ax.set_title(r"Case $1+q\varepsilon>0$")
ax.spines["bottom"].set_color("none")
ax.spines["top"].set_color("none")
ax.spines["left"].set_color("none")
ax.spines["right"].set_color("none")
plt.savefig(
    "deltapositivepositiveh.pdf",
    transparent=True,
    bbox_inches="tight",
)
plt.clf()

SoR = 1
So_ = np.linspace(start=-1, stop=1, num=2000)
θ_ = np.linspace(start=-1, stop=1, num=2000)
So, θ = np.meshgrid(So_, θ_)


def f(theta):
    return m * θ / (1 - q * θ) * np.exp(ε / (θ0 + θ))


fig, ax = plt.subplots()
ax.set_xlabel(r"$S_{0}$")
ax.set_ylabel(r"$\theta$")
ax.contour(So, θ, So * (SoR - So) - f(θ), [0], linewidths=0.5, colors=["red"])
ax.set_title(label="Case", loc="center", wrap=True, fontsize=15)
fig.savefig(
    "phaseportraitdeltapositivepositivea.pdf", transparent=True, bbox_inches="tight"
)

# """Case Δ > 0, q < 0, 1 + q * ε > 0.
# """

# m = 3.702113166195264e-2
# ε = 20.546467805308318
# θ0 = 1
# q = -1e-2

# Δ = ε * (ε - 4 * θ0 - 4 * q * θ0**2)
# assert Δ > 0 and q < 0 and (1 + q * ε) > 0
# print(f"Case Δ > 0, q < 0, 1 + q * ε = {1 + q * ε}>0")

# θcritplus = (ε - 2 * θ0 + np.sqrt(Δ)) / (2 * (1 + q * ε))
# θcritminus = (ε - 2 * θ0 - np.sqrt(Δ)) / (2 * (1 + q * ε))

# θ = np.linspace(start=0, stop=1, num=2000)
# f = m * θ / (1 - q * θ) * np.exp(ε / (θ0 + θ))

# fig, ax = plt.subplots(layout="constrained")
# ax.plot(θ, f, label=r"$f$", linewidth=0.7, color="blue")
# ax.grid(c="gray", linewidth=0.1, linestyle="dashed")
# ax.axhline(-m / q, color="red", linestyle="dashed", linewidth=0.7)
# # ax.set_xlim(θ[0], θ[-1])
# # ax.set_ylim(0, 6e-5)
# # ax.text(x=-1e-2, y=-m / q, s=r"$-\frac{m}{q}$", fontdict=dict(size=12))
# # ax.set_xticks(ticks=np.linspace(start=θ[0], stop=θ[-1], num=5))
# # ax.set_yticks(ticks=np.linspace(start=0, stop=6e-5, num=5))
# ax.set_xlabel(xlabel=r"$\theta$")
# ax.set_title(r"Case $1+q\varepsilon>0$")
# ax.legend(loc="best", shadow=True)
# ax.spines["bottom"].set_color("none")
# ax.spines["top"].set_color("none")
# ax.spines["left"].set_color("none")
# ax.spines["right"].set_color("none")
# plt.savefig(
#     "deltapositivepositiveaa.pdf",
#     transparent=True,
#     bbox_inches="tight",
# )
# plt.clf()

# θ = np.linspace(start=-10, stop=1, num=2000)
# f = m * θ / (1 - q * θ) * np.exp(ε / (θ0 + θ))

# fig, ax = plt.subplots(layout="constrained")
# ax.plot(θ, f, label=r"$f$", linewidth=0.7, color="blue")
# ax.grid(c="gray", linewidth=0.1, linestyle="dashed")
# ax.axhline(-m / q, color="red", linestyle="dashed", linewidth=0.7)
# # ax.set_xlim(θ[0], θ[-1])
# # ax.set_ylim(0, 6e-5)
# # ax.text(x=-1e-2, y=-m / q, s=r"$-\frac{m}{q}$", fontdict=dict(size=12))
# # ax.set_xticks(ticks=np.linspace(start=θ[0], stop=θ[-1], num=5))
# # ax.set_yticks(ticks=np.linspace(start=0, stop=6e-5, num=5))
# ax.set_xlabel(xlabel=r"$\theta$")
# ax.set_title(r"Case $1+q\varepsilon>0$")
# ax.legend(loc="best", shadow=True)
# ax.spines["bottom"].set_color("none")
# ax.spines["top"].set_color("none")
# ax.spines["left"].set_color("none")
# ax.spines["right"].set_color("none")
# plt.savefig(
#     "deltapositivepositivebb.pdf",
#     transparent=True,
#     bbox_inches="tight",
# )
# plt.clf()


# """Case Δ > 0, q < 0, 1 + q * ε < 0.
# """

# m = 3.702113166195264e-1
# ε = 20.546467805308318
# θ0 = 1
# q = -1.1

# Δ = ε * (ε - 4 * θ0 - 4 * q * θ0**2)
# assert Δ > 0 and q < 0 and (1 + q * ε) < 0
# print(f"Case Δ > 0, q < 0, 1 + q * ε = {1 + q * ε}<0")
# θcritplus = (ε - 2 * θ0 + np.sqrt(Δ)) / (2 * (1 + q * ε))
# θcritminus = (ε - 2 * θ0 - np.sqrt(Δ)) / (2 * (1 + q * ε))
# print(f"θcritplus: {θcritplus}")
# print(f"θcritminus: {θcritminus}")
# print(f"Horizontal asimptote: {-m / q}")
# print(f"Vertical asimptote: {1 / q}")

# θ = np.linspace(start=0, stop=0.12, num=2000)
# f = m * θ / (1 - q * θ) * np.exp(ε / (θ0 + θ))

# fig, ax = plt.subplots(layout="constrained")
# ax.plot(θ, f, label=r"$f\left(\theta\right)$", linewidth=0.7, color="blue")
# ax.grid(c="gray", linewidth=0.1, linestyle="dashed")
# ax.axhline(-m / q, color="red", linestyle="dashed", linewidth=0.7)
# ax.axvline(
#     θcritminus,
#     ymin=0,
#     ymax=0.92,
#     color="gray",
#     linestyle="dashed",
#     linewidth=0.5,
# )
# ax.text(
#     x=θcritminus,
#     y=-0.2e6,
#     s=r"$\theta^{\text{crit}}_{-}$",
#     fontdict=dict(size=10),
# )
# ax.set_xlim(θ[0], θ[-1])
# ax.set_ylim(0, 6e6)
# ax.text(x=-1e-2, y=-m / q, s=r"$-\frac{m}{q}$", fontdict=dict(size=12))
# ax.set_xticks(ticks=np.linspace(start=θ[0], stop=θ[-1], num=5))
# ax.set_yticks(ticks=np.linspace(start=0, stop=6e6, num=5))
# ax.set_xlabel(xlabel=r"$\theta$")
# ax.set_title(r"Case $1+q\varepsilon<0$")
# ax.legend(loc="best", shadow=True)
# ax.spines["bottom"].set_color("none")
# ax.spines["top"].set_color("none")
# ax.spines["left"].set_color("none")
# ax.spines["right"].set_color("none")
# plt.savefig(
#     "deltapositivenegativea.pdf",
#     transparent=True,
#     bbox_inches="tight",
# )
# plt.clf()

# θ = np.linspace(start=0, stop=0.2, num=2000)
# f = m * θ / (1 - q * θ) * np.exp(ε / (θ0 + θ))
# fprime = f * (1 / θ + q / (1 - q * θ) - ε / (θ0 + θ) ** 2)
# fprimeprime = -f * (
#     (2 * ε * q) / ((1 - q * θ) * (θ0 + θ) ** 2)
#     - ε * (2 + ε / (θ0 + θ)) / (θ0 + θ) ** 3
#     + 2 * ε / (θ * (θ0 + θ) ** 2)
#     - 2 * q**2 / (1 - q * θ) ** 2
#     - 2 * q / (θ * (1 - q * θ))
# )
# fig, ax = plt.subplots(layout="constrained")
# ax.plot(
#     θ, fprime, label=r"$f^{\prime}\left(\theta\right)$", linewidth=0.7, color="orange"
# )
# ax.plot(
#     θ,
#     fprimeprime,
#     label=r"$f^{\prime\prime}\left(\theta\right)$",
#     linewidth=0.5,
#     color="green",
# )
# ax.grid(c="gray", linewidth=0.1, linestyle="dashed")
# ax.legend(loc="best", shadow=True)
# ax.axhline(0, color="gray", linestyle="dashed", linewidth=0.7)
# ax.axvline(
#     θcritminus,
#     ymin=0.86,
#     ymax=0.89,
#     color="gray",
#     linestyle="dashed",
#     linewidth=0.5,
# )
# ax.text(
#     x=θcritminus,
#     y=-0.07e10,
#     s=r"$\theta^{\text{crit}}_{-}$",
#     fontdict=dict(size=10),
# )
# ax.set_xlim(θ[0], θ[-1])
# ax.set_ylim(-1.4e10, 0.2e10)
# ax.set_xticks(ticks=np.linspace(start=θ[0], stop=θ[-1], num=5))
# ax.set_yticks(ticks=np.linspace(start=-1.4e10, stop=0.2e10, num=5))
# ax.set_xlabel(xlabel=r"$\theta$")
# ax.set_title(r"Case $1+q\varepsilon<0$")
# ax.spines["bottom"].set_color("none")
# ax.spines["top"].set_color("none")
# ax.spines["left"].set_color("none")
# ax.spines["right"].set_color("none")
# plt.savefig(
#     "deltapositivenegativeb.pdf",
#     transparent=True,
#     bbox_inches="tight",
# )
# plt.clf()

# θ = np.linspace(start=10, stop=2010, num=2000)
# f = m * θ / (1 - q * θ) * np.exp(ε / (θ0 + θ))

# fig, ax = plt.subplots(layout="constrained")
# ax.plot(θ, f, label=r"$f\left(\theta\right)$", linewidth=0.7, color="blue")
# ax.grid(c="gray", linewidth=0.1, linestyle="dashed")
# ax.axhline(-m / q, color="red", linestyle="dashed", linewidth=0.7)
# # ax.axvline(θcritminus, color="red", linestyle="dashed", linewidth=0.5)
# ax.set_xlim(θ[0], θ[-1])
# ax.set_ylim(0, 2)
# # ax.text(x=-1e-2, y=-m / q, s=r"$-\frac{m}{q}$", fontdict=dict(size=12))
# ax.set_xticks(ticks=np.linspace(start=θ[0], stop=θ[-1], num=5))
# ax.set_yticks(ticks=np.linspace(start=0, stop=2, num=5))
# ax.set_xlabel(xlabel=r"$\theta$")
# ax.set_title(r"Case $1+q\varepsilon<0$")
# ax.legend(loc="best", shadow=True)
# ax.spines["bottom"].set_color("none")
# ax.spines["top"].set_color("none")
# ax.spines["left"].set_color("none")
# ax.spines["right"].set_color("none")
# plt.savefig(
#     "deltapositivenegativec.pdf",
#     transparent=True,
#     bbox_inches="tight",
# )
# plt.clf()
