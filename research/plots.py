#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

plt.style.use("seaborn-v0_8-white")

# r"""Case 3: $f\left(\theta\right)$ posses two crital points
# """

m = 1
varepsilon = 1.5
theta0 = 0.15
q = -2
theta = np.linspace(start=0, stop=50, num=1000)
f = m * (theta / (1 - q * theta)) * np.exp(varepsilon / (theta + theta0))

fig, ax = plt.subplots(layout="constrained")
ax.plot(
    theta,
    f,
    label=r"$f\left(\theta\right)$",
    linewidth=0.7,
)
ax.axhline(y=1 / 4, color="r", linestyle="--", label=r"$-\frac{m}{q}$")
ax.set_xlabel(xlabel=r"$\theta$")
ax.set_ylabel(ylabel=r"$f\left(\theta\right)$")
# ax.set_xlim(0, 10)
# ax.set_ylim(0, 5)
ax.set_xticks([])
ax.set_yticks([])
ax.legend(loc="best")
plt.savefig("picture0.pdf", transparent=True, bbox_inches="tight")
plt.clf()

m = 2
varepsilon = 3
theta0 = 1
q = -1
theta = np.linspace(start=0, stop=50, num=1000)
f = m * (theta / (1 - q * theta)) * np.exp(varepsilon / (theta + theta0))

fig, ax = plt.subplots(layout="constrained")
ax.plot(
    theta,
    f,
    label=r"$f\left(\theta\right)$",
    linewidth=0.7,
)
ax.axhline(y=-m / q, color="r", linestyle="--", label=r"Asíntota $-\frac{m}{q}$")
ax.set_xlabel(xlabel=r"$\theta$")
ax.set_ylabel(ylabel=r"$f\left(\theta\right)$")
ax.set_xlim(0, 10)
ax.set_ylim(0, 5)
ax.set_xticks([])
ax.set_yticks([])
ax.legend(loc="best")
plt.savefig("picture1.pdf", transparent=True, bbox_inches="tight")
plt.clf()


m = 2
varepsilon = 5
theta0 = 1
q = -0.5
theta = np.linspace(start=0, stop=50, num=1000)
f = m * (theta / (1 - q * theta)) * np.exp(varepsilon / (theta + theta0))

fig, ax = plt.subplots(layout="constrained")
ax.plot(
    theta,
    f,
    label=r"$f\left(\theta\right)$",
    linewidth=0.7,
)
ax.axhline(y=-m / q, color="r", linestyle="--", label=r"Asíntota $-\frac{m}{q}$")
ax.set_xlabel(xlabel=r"$\theta$")
ax.set_ylabel(ylabel=r"$f\left(\theta\right)$")
# ax.set_xlim(0, 10)
# ax.set_ylim(0, 5)
ax.set_xticks([])
ax.set_yticks([])
ax.legend(loc="best")
plt.savefig("picture2.pdf", transparent=True, bbox_inches="tight")
plt.clf()

# def f(theta):
#     return m * (theta / (1 - q * theta)) * np.exp(varepsilon / (theta + theta0))

# fig, axs = plt.subplots(2, 2, layout="constrained")

# r"""
# Subcase 3.1: $1+q\varepsilon>0$
# Subsubcase 3.1.1: $2\theta_0-\varepsilon>0$
# """
# m = 1
# varepsilon = -1
# theta0 = 1
# q = -1
# assert 1 + q * varepsilon > 0
# assert 2 * theta0 - varepsilon > 0

# theta = np.linspace(start=-0.9, stop=5, num=200)
# axs[0, 0].plot(
#     theta,
#     f(theta),
#     label=rf"${{{m}}}\cdot\left(\frac{{\theta}}{{1-{q}\theta}}\right)\cdot\exp\left(\frac{{{varepsilon}}}{{\theta+{theta0}}}\right)$",
#     linewidth=0.7,
# )
# axs[0, 0].set_xlabel(xlabel=r"$\theta$")
# axs[0, 0].set_ylabel(ylabel=r"$f\left(\theta\right)$")
# axs[0, 0].legend(loc="best")
# axs[0, 0].set_title(
#     label=rf"$m={{{m}}}$, $\varepsilon={{{varepsilon}}}$, $\theta_0={{{theta0}}}$, $q={{{q}}}$."
#     + "\nSubcase 3.1:\t"
#     + r"$1+q\varepsilon>0$."
#     + "\nSubsubcase 3.1.1:\t"
#     + r"$2\theta_0-\varepsilon>0$.",
#     loc="center",
#     wrap=True,
# )

# r"""
# Subcase 3.1: $1+q\varepsilon>0$
# Subsubcase 3.1.2: $2\theta_0-\varepsilon<0$
# """

# m = 1
# varepsilon = -1
# theta0 = -1
# q = -1
# assert 1 + q * varepsilon > 0
# assert 2 * theta0 - varepsilon < 0

# theta = np.linspace(start=0.99, stop=5, num=200)
# axs[0, 1].plot(
#     theta,
#     f(theta),
#     label=rf"${{{m}}}\cdot\left(\frac{{\theta}}{{1-{q}\theta}}\right)\cdot\exp\left(\frac{{{varepsilon}}}{{\theta+{theta0}}}\right)$",
#     linewidth=0.7,
# )
# axs[0, 1].set_xlabel(xlabel=r"$\theta$")
# axs[0, 1].set_ylabel(ylabel=r"$f\left(\theta\right)$")
# axs[0, 1].legend(loc="best")
# axs[0, 1].set_title(
#     label=rf"$m={{{m}}}$, $\varepsilon={{{varepsilon}}}$, $\theta_0={{{theta0}}}$, $q={{{q}}}$."
#     + "\nSubcase 3.1:\t"
#     + r"$1+q\varepsilon>0$."
#     + "\nSubsubcase 3.1.2:\t"
#     + r"$2\theta_0-\varepsilon<0$.",
#     loc="center",
#     wrap=True,
# )
# r"""
# Subcase 3.2: $1+q\varepsilon<0$
# Subsubcase 3.2.1: $2\theta_0-\varepsilon>0$
# """

# m = 1
# varepsilon = -1
# theta0 = 1
# q = -1
# assert 1 + q * varepsilon > 0
# assert 2 * theta0 - varepsilon > 0

# axs[1, 0].plot(
#     theta,
#     f(theta),
#     label=r"$m\left(\frac{\theta}{1-q\theta}\right)\exp\left(\frac{\varepsilon}{\theta+\theta_0}\right)$",
#     linewidth=0.7,
# )
# axs[1, 0].set_xlabel(xlabel=r"$\theta$")
# axs[1, 0].set_ylabel(ylabel=r"$f\left(\theta\right)$")
# axs[1, 0].legend(loc="best")
# axs[1, 0].set_title(
#     label="Parameters: "
#     + rf"$m={{{m}}}$, $\varepsilon={{{varepsilon}}}$, $\theta_0={{{theta0}}}$, $q={{{q}}}$."
#     + "\nSubcase 3.2:\t"
#     + r"$1+q\varepsilon<0$."
#     + "\nSubsubcase 3.2.1:\t"
#     + r"$2\theta_0-\varepsilon>0$.",
#     loc="center",
#     wrap=True,
# )

# r"""
# Subcase 3.2: $1+q\varepsilon<0$
# Subsubcase 3.2.2: $2\theta_0-\varepsilon<0$
# """

# m = 1
# varepsilon = -1
# theta0 = 1
# q = -1
# assert 1 + q * varepsilon > 0
# assert 2 * theta0 - varepsilon > 0

# axs[1, 1].plot(
#     theta,
#     f(theta),
#     label=r"$m\left(\frac{\theta}{1-q\theta}\right)\exp\left(\frac{\varepsilon}{\theta+\theta_0}\right)$",
#     linewidth=0.7,
# )
# axs[1, 1].set_xlabel(xlabel=r"$\theta$")
# axs[1, 1].set_ylabel(ylabel=r"$f\left(\theta\right)$")
# axs[1, 1].legend(loc="best")
# axs[1, 1].set_title(
#     label="Parameters: "
#     + rf"$m={{{m}}}$, $\varepsilon={{{varepsilon}}}$, $\theta_0={{{theta0}}}$, $q={{{q}}}$."
#     + "\nSubcase 3.2:\t"
#     + r"$1+q\varepsilon<0$."
#     + "\nSubsubcase 3.2.2:\t"
#     + r"$2\theta_0-\varepsilon<0$.",
#     loc="center",
#     wrap=True,
# )
# fig.suptitle(
#     r"$f\left(\theta\right)=m\left(\frac{\theta}{1-q\theta}\right)\exp\left(\frac{\varepsilon}{\theta+\theta_0}\right)$."
# )
# plt.savefig("plots.pdf", transparent=True, bbox_inches="tight")
