#!/usr/bin/env python

from matplotlib import pyplot as plt
from numpy.typing import ArrayLike
import numpy as np
from scipy.integrate import odeint


def system(
    ξ: float,
    X: ArrayLike,
    a1: float,
    a3: float,
    b1: float,
    b3: float,
    c: float,
    β: float,
    SLy: float,
    SRo: float,
):
    So = X[0]
    θ = X[1]
    Sy = (SRo - So) * (SLy / SRo)
    Φ = 1e8 * np.exp(-51247 / (8.314 * 300 * (X[1] + 1)))
    dX = np.empty_like(X)
    dX[0] = -b3 * Sy * So / (a3 - c) * Φ
    dX[1] = (β * θ * (c - a3) + (a1 * b3 * θ - b1 * (c - a3) * Sy * So * Φ)) / (
        (c - a1 * So) * (c - a3)
    )
    return dX


SLy = 1 / 2
SRo = 1 - SLy
a1 = 0.00189
a2 = 27.6
a3 = 0.00252
b1 = 1.1
b2 = 30.4
b3 = 1
c = (a2 * b3 * SLy + a3 * b2 * SRo) / (b2 * SRo + b3 * SLy)
β = 10

time = np.linspace(start=0, stop=0.25, num=10000)
X0 = [0.05, 0.05]
X_s = odeint(
    func=system, y0=X0, t=time, args=(a1, a3, b1, b3, c, β, SLy, SRo), tfirst=True
)
fig, ax = plt.subplots(constrained_layout=True)
ax.set_title(
    r"$a_1=$"
    + f"{a1}, "
    + r"$a_2=$"
    + f"{a2}, "
    + r"$a_3=$"
    + f"{a3}, "
    + r"$b_1=$"
    + f"{b1}, "
    + r"$b_2=$"
    + f"{b2}, "
    + r"$b_3=$"
    + f"{b3}\n"
    + r"$c=$"
    + f"{c}, "
    + r"$\beta=$"
    + f"{β} ",
    fontsize=12,
    wrap=True,
)  # y=0.5
ax.plot(time, X_s[:, 0], "r", label=r"$S_{\text{o}}$")
ax.plot(time, X_s[:, 1], "g", label=r"$\theta$")
ax.set_xlim([time[0], time[-1]])
ax.set_ylim([0, 0.5])
ax.set_xticks(ticks=np.linspace(start=time[0], stop=time[-1], num=3))
ax.set_yticks(ticks=np.linspace(start=0, stop=0.5, num=6))
ax.set_aspect("equal", adjustable="box")
ax.grid(c="gray", linewidth=0.1, linestyle="dashed")
ax.legend(
    # [ax0.get_ylabel(), ax1.get_ylabel()],
    loc="best",
    shadow=True,
    # title="Leyenda",
    fancybox=True,
    # ncol=2,
    # bbox_to_anchor=(0.5, 1.12),
)
plt.savefig("odesolution4.pdf", transparent=True, bbox_inches="tight")

time = np.linspace(start=0, stop=0.5, num=10000)
X0 = [0.05, 0.05]
X_s = odeint(
    func=system, y0=X0, t=time, args=(a1, a3, b1, b3, c, β, SLy, SRo), tfirst=True
)
fig, (ax0, ax1) = plt.subplots(nrows=2, constrained_layout=True)
fig.suptitle(
    r"$a_1=$"
    + f"{a1}, "
    + r"$a_2=$"
    + f"{a2}, "
    + r"$a_3=$"
    + f"{a3}, "
    + r"$b_1=$"
    + f"{b1}, "
    + r"$b_2=$"
    + f"{b2}, "
    + r"$b_3=$"
    + f"{b3}\n"
    + r"$c=$"
    + f"{c}, "
    + r"$\beta=$"
    + f"{β} ",
    fontsize=12,
    wrap=True,
)  # y=0.5
ax0.plot(time, X_s[:, 0], "r")
ax0.set_ylabel(r"$S_{\text{o}}$", fontsize=15)
ax0.set_xlim([time[0], time[-1]])
ax0.grid(c="gray", linewidth=0.1, linestyle="dashed")
ax1.plot(time, X_s[:, 1], "g")
ax1.set_ylabel(r"$\theta$", fontsize=15)
ax1.set_xlim([time[0], time[-1]])
ax1.grid(c="gray", linewidth=0.1, linestyle="dashed")
fig.legend(
    [ax0.get_ylabel(), ax1.get_ylabel()],
    loc="lower center",
    shadow=True,
    title="Leyenda",
    fancybox=True,
    ncol=2,
    bbox_to_anchor=(0.5, 1.12),
)
plt.savefig("odesolution10.pdf", transparent=True, bbox_inches="tight")

time = np.linspace(start=0.5, stop=2, num=10000)
X0 = [0.05, 0.05]
X_s = odeint(
    func=system, y0=X0, t=time, args=(a1, a3, b1, b3, c, β, SLy, SRo), tfirst=True
)
fig, (ax0, ax1) = plt.subplots(nrows=2, constrained_layout=True)
fig.suptitle(
    r"$a_1=$"
    + f"{a1}, "
    + r"$a_2=$"
    + f"{a2}, "
    + r"$a_3=$"
    + f"{a3}, "
    + r"$b_1=$"
    + f"{b1}, "
    + r"$b_2=$"
    + f"{b2}, "
    + r"$b_3=$"
    + f"{b3}\n"
    + r"$c=$"
    + f"{c}, "
    + r"$\beta=$"
    + f"{β} ",
    fontsize=12,
    wrap=True,
)  # y=0.5
ax0.plot(time, X_s[:, 0], "r")
ax0.set_ylabel(r"$S_{\text{o}}$", fontsize=15)
ax0.set_xlim([time[0], time[-1]])
ax0.grid(c="gray", linewidth=0.1, linestyle="dashed")
ax1.plot(time, X_s[:, 1], "g")
ax1.set_ylabel(r"$\theta$", fontsize=15)
ax1.set_xlim([time[0], time[-1]])
ax1.grid(c="gray", linewidth=0.1, linestyle="dashed")
fig.legend(
    [ax0.get_ylabel(), ax1.get_ylabel()],
    loc="lower center",
    shadow=True,
    title="Leyenda",
    fancybox=True,
    ncol=2,
    bbox_to_anchor=(0.5, 1.12),
)
plt.savefig("odesolution30.pdf", transparent=True, bbox_inches="tight")

# Segundo grupo de ejemplos
SLy = 1 / 2
SRo = 1 - SLy
a1 = 0.00189
a2 = 0.00252
a3 = 10
b1 = 1.1
b2 = 30.4
b3 = 1
c = (a2 * b3 * SLy + a3 * b2 * SRo) / (b2 * SRo + b3 * SLy)
β = 10

time = np.linspace(start=0, stop=2, num=10000)
X0 = [0.05, 0.05]
X_s = odeint(
    func=system, y0=X0, t=time, args=(a1, a3, b1, b3, c, β, SLy, SRo), tfirst=True
)
fig, ax = plt.subplots(constrained_layout=True)
ax.set_title(
    r"$a_1=$"
    + f"{a1}, "
    + r"$a_2=$"
    + f"{a2}, "
    + r"$a_3=$"
    + f"{a3}, "
    + r"$b_1=$"
    + f"{b1}, "
    + r"$b_2=$"
    + f"{b2}, "
    + r"$b_3=$"
    + f"{b3}\n"
    + r"$c=$"
    + f"{c}, "
    + r"$\beta=$"
    + f"{β} ",
    fontsize=12,
    wrap=True,
)  # y=0.5
ax.plot(time, X_s[:, 0], "r", label=r"$S_{\text{o}}$", linewidth=0.75)
ax.plot(time, X_s[:, 1], "g", label=r"$\theta$", linewidth=0.75)
ax.grid(c="gray", linewidth=0.1, linestyle="dashed")
ax.set_xlim([time[0], time[-1]])
ax.set_ylim([0, 0.4])
ax.set_xticks(ticks=np.linspace(start=time[0], stop=time[-1], num=11))
ax.set_yticks(ticks=np.linspace(start=0, stop=0.4, num=9))
ax.legend(
    # [ax0.get_ylabel(), ax1.get_ylabel()],
    loc="best",
    shadow=True,
    # title="Legend",
    fancybox=True,
    # ncol=2,
    # bbox_to_anchor=(0.5, 1.12),
)
plt.savefig("odesolutionI.pdf", transparent=True, bbox_inches="tight")

SLy = 1 / 2
SRo = 1 - SLy
a1 = 0.00189
a2 = 0.00252
a3 = 20
b1 = 1.1
b2 = 30.4
b3 = 1
c = (a2 * b3 * SLy + a3 * b2 * SRo) / (b2 * SRo + b3 * SLy)
β = 10

time = np.linspace(start=0, stop=0.35, num=10000)
X0 = [0.05, 0.05]
X_s = odeint(
    func=system, y0=X0, t=time, args=(a1, a3, b1, b3, c, β, SLy, SRo), tfirst=True
)
fig, ax = plt.subplots(constrained_layout=True)
ax.set_title(
    r"$a_1=$"
    + f"{a1}, "
    + r"$a_2=$"
    + f"{a2}, "
    + r"$a_3=$"
    + f"{a3}, "
    + r"$b_1=$"
    + f"{b1}, "
    + r"$b_2=$"
    + f"{b2}, "
    + r"$b_3=$"
    + f"{b3}\n"
    + r"$c=$"
    + f"{c}, "
    + r"$\beta=$"
    + f"{β} ",
    fontsize=12,
    wrap=True,
)  # y=0.5
ax.plot(time, X_s[:, 0], "r", label=r"$S_{\text{o}}$", linewidth=0.75)
ax.plot(time, X_s[:, 1], "g", label=r"$\theta$", linewidth=0.75)
ax.set_xlim([time[0], time[-1]])
ax.grid(c="gray", linewidth=0.1, linestyle="dashed")
ax.legend(
    # [ax0.get_ylabel(), ax1.get_ylabel()],
    loc="best",
    shadow=True,
    title="Leyenda",
    fancybox=True,
    # ncol=2,
    # bbox_to_anchor=(0.5, 1.12),
)
plt.savefig("odesolutionII.pdf", transparent=True, bbox_inches="tight")

SLy = 1 / 2
SRo = 1 - SLy
a1 = 0.00189
a2 = 0.00252
a3 = 27.6
b1 = 1.1
b2 = 30.4
b3 = 1
c = (a2 * b3 * SLy + a3 * b2 * SRo) / (b2 * SRo + b3 * SLy)
β = 10

time = np.linspace(start=0, stop=0.35, num=10000)
X0 = [0.05, 0.05]
X_s = odeint(
    func=system, y0=X0, t=time, args=(a1, a3, b1, b3, c, β, SLy, SRo), tfirst=True
)
fig, ax = plt.subplots(constrained_layout=True)
ax.set_title(
    r"$a_1=$"
    + f"{a1}, "
    + r"$a_2=$"
    + f"{a2}, "
    + r"$a_3=$"
    + f"{a3}, "
    + r"$b_1=$"
    + f"{b1}, "
    + r"$b_2=$"
    + f"{b2}, "
    + r"$b_3=$"
    + f"{b3}\n"
    + r"$c=$"
    + f"{c}, "
    + r"$\beta=$"
    + f"{β} ",
    fontsize=12,
    wrap=True,
)  # y=0.5
ax.plot(time, X_s[:, 0], "r", label=r"$S_{\text{o}}$", linewidth=0.75)
ax.plot(time, X_s[:, 1], "g",label=r"$\theta$", linewidth=0.75)
ax.set_xlim([time[0], time[-1]])
ax.grid(c="gray", linewidth=0.1, linestyle="dashed")
ax.legend(
    # [ax0.get_ylabel(), ax1.get_ylabel()],
    loc="best",
    shadow=True,
    # title="Leyenda",
    fancybox=True,
    # ncol=2,
    # bbox_to_anchor=(0.5, 1.12),
)
plt.savefig("odesolutionIII.pdf", transparent=True, bbox_inches="tight")

# Tercer grupo de ejemplos
SLy = 1 / 2
SRo = 1 - SLy
a1 = 0.00189
a2 = 1
a3 = 10
b1 = 1.1
b2 = 30.4
b3 = 1
c = (a2 * b3 * SLy + a3 * b2 * SRo) / (b2 * SRo + b3 * SLy)
β = 10

time = np.linspace(start=0, stop=3, num=10000)
X0 = [0.05, 0.05]
X_s = odeint(
    func=system, y0=X0, t=time, args=(a1, a3, b1, b3, c, β, SLy, SRo), tfirst=True
)
fig, ax = plt.subplots(constrained_layout=True)
ax.set_title(
    r"$a_1=$"
    + f"{a1}, "
    + r"$a_2=$"
    + f"{a2}, "
    + r"$a_3=$"
    + f"{a3}, "
    + r"$b_1=$"
    + f"{b1}, "
    + r"$b_2=$"
    + f"{b2}, "
    + r"$b_3=$"
    + f"{b3}\n"
    + r"$c=$"
    + f"{c}, "
    + r"$\beta=$"
    + f"{β} ",
    fontsize=12,
    wrap=True,
)  # y=0.5
ax.plot(time, X_s[:, 0], "r", label=r"$S_{\text{o}}$", linewidth=0.75)
ax.plot(time, X_s[:, 1], "g", label=r"$\theta$", linewidth=0.75)
ax.set_xlim([time[0], time[-1]])
ax.grid(c="gray", linewidth=0.1, linestyle="dashed")
ax.legend(
    # [ax0.get_ylabel(), ax1.get_ylabel()],
    loc="best",
    shadow=True,
    # title="Leyenda",
    fancybox=True,
    # ncol=2,
    # bbox_to_anchor=(0.5, 1.12),
)
plt.savefig("odesolutionIV.pdf", transparent=True, bbox_inches="tight")

SLy = 1 / 2
SRo = 1 - SLy
a1 = 0.00189
a2 = 5
a3 = 10
b1 = 1.1
b2 = 30.4
b3 = 1
c = (a2 * b3 * SLy + a3 * b2 * SRo) / (b2 * SRo + b3 * SLy)
β = 10

time = np.linspace(start=0, stop=0.35, num=10000)
X0 = [0.05, 0.05]
X_s = odeint(
    func=system, y0=X0, t=time, args=(a1, a3, b1, b3, c, β, SLy, SRo), tfirst=True
)
fig, ax = plt.subplots(constrained_layout=True)
ax.set_title(
    r"$a_1=$"
    + f"{a1}, "
    + r"$a_2=$"
    + f"{a2}, "
    + r"$a_3=$"
    + f"{a3}, "
    + r"$b_1=$"
    + f"{b1}, "
    + r"$b_2=$"
    + f"{b2}, "
    + r"$b_3=$"
    + f"{b3}\n"
    + r"$c=$"
    + f"{c}, "
    + r"$\beta=$"
    + f"{β} ",
    fontsize=12,
    wrap=True,
)  # y=0.5
ax.plot(time, X_s[:, 0], "r", label=r"$S_{\text{o}}$", linewidth=0.75)
ax.set_xlim([time[0], time[-1]])
ax.grid(c="gray", linewidth=0.1, linestyle="dashed")
ax.plot(time, X_s[:, 1], "g", label=r"$\theta$", linewidth=0.75)
ax.legend(
    # [ax0.get_ylabel(), ax1.get_ylabel()],
    loc="best",
    shadow=True,
    # title="Leyenda",
    fancybox=True,
    # ncol=2,
    # bbox_to_anchor=(0.5, 1.12),
)
plt.savefig("odesolutionV.pdf", transparent=True, bbox_inches="tight")

SLy = 1 / 2
SRo = 1 - SLy
a1 = 0.00189
a2 = 10
a3 = 25
b1 = 1.1
b2 = 30.4
b3 = 1
c = (a2 * b3 * SLy + a3 * b2 * SRo) / (b2 * SRo + b3 * SLy)
β = 10

time = np.linspace(start=0, stop=50, num=10000)
X0 = [0.05, 0.05]
X_s = odeint(
    func=system, y0=X0, t=time, args=(a1, a3, b1, b3, c, β, SLy, SRo), tfirst=True
)
fig, ax = plt.subplots(constrained_layout=True)
ax.set_title(
    r"$a_1=$"
    + f"{a1}, "
    + r"$a_2=$"
    + f"{a2}, "
    + r"$a_3=$"
    + f"{a3}, "
    + r"$b_1=$"
    + f"{b1}, "
    + r"$b_2=$"
    + f"{b2}, "
    + r"$b_3=$"
    + f"{b3}\n"
    + r"$c=$"
    + f"{c}, "
    + r"$\beta=$"
    + f"{β} ",
    fontsize=12,
    wrap=True,
)  # y=0.5
ax.plot(time, X_s[:, 0], "r", label=r"$S_{\text{o}}$", linewidth=0.75)
ax.set_xlim([time[0], time[-1]])
ax.grid(c="gray", linewidth=0.1, linestyle="dashed")
ax.plot(time, X_s[:, 1], "g", label=r"$\theta$", linewidth=0.75)
ax.legend(
    # [ax0.get_ylabel(), ax1.get_ylabel()],
    loc="best",
    shadow=True,
    # title="Leyenda",
    fancybox=True,
    # ncol=2,
    # bbox_to_anchor=(0.5, 1.12),
)
plt.savefig("odesolutionVI.pdf", transparent=True, bbox_inches="tight")
