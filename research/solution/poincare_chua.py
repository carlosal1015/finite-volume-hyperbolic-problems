#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from numpy import linspace
from matplotlib import rc
from numpy.typing import ArrayLike

# plt.style.use('ggplot')
# rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})
rc("text", usetex=True)

# plt.rcParams['text.usetex'] = True
# plt.rcParams['font.serif'] = ['Computer Modern']

α: float = 10.0
β: float = 16.4
R: float = -1.22
C_2: float = -0.728


def chua(t: float, u: ArrayLike) -> ArrayLike:
    """Chua system

    .. math::
        \frac{dx}{dt} = \frac{1}{R C_1}(V_2 - V_1 - g(V_1))
        \frac{dy}{dt} = \frac{1}{R C_2}(V_1 - V_2 + R i_L)
        \frac{dz}{dt} = -\frac{1}{L} V_{2}

    Args:
        t (float): temporal variable
        u (ArrayLike): position

    Returns:
        ArrayLike: vector solution
    """
    x, y, z = u
    f_x = C_2 * x + 0.5 * (R - C_2) * (abs(x + 1) - abs(x - 1))
    return [α * (y - x - f_x), x - y + z, -β * y]


x_section: int = 1


def poincare(t: ArrayLike, vector: ArrayLike) -> float:
    x: float = vector[0]
    return x - x_section


t_0: float = 0.0
t_final: float = 6e4
u0: list[float] = [0.1, 0.15, 0.01]

poincare.direction: float = -1
sol: ArrayLike = solve_ivp(
    chua,
    [t_0, t_final],
    u0,
    events=poincare,
    dense_output=True,
    vectorized=True,
)

sol.sol

t = sol.t_events[0]
vectors = sol.sol(t)
x, y, z = vectors

with plt.style.context("fivethirtyeight"):
    chua_attractor = plt.figure()
    ax = chua_attractor.add_subplot(111, projection="3d")
    ax.plot(sol.y[0], sol.y[1], sol.y[2], ",", alpha=0.12)
    x, y, z = vectors
    ax.plot(x, y, z, ".", alpha=0.4)
    ax.set_xlabel(r"$V_{C_{1}}$", fontsize=15)
    ax.set_ylabel(r"$V_{C_{2}}$", fontsize=15)
    ax.set_zlabel(r"$i_{L}$", fontsize=15)
    plt.tick_params(labelsize=15)
    plt.savefig("img/chua_double_atractor.pdf", transparent=True, bbox_inches="tight")
    plt.close()

with plt.style.context("fivethirtyeight"):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.view_init(30, -90)
    ax.plot(sol.y[0], sol.y[1], sol.y[2], ",")
    ax.plot(x, y, z, ".")
    ax.set_xlabel(r"$V_{C_{1}}$", fontsize=15)
    ax.set_ylabel(r"$V_{C_{2}}$", fontsize=15)
    ax.set_zlabel(r"$i_{L}$", fontsize=15)
    plt.savefig("img/chua_double_atractor30.pdf", transparent=True, bbox_inches="tight")
    plt.close()


with plt.style.context("fivethirtyeight"):
    y = vectors[1]
    plt.plot(y[:-1], y[1:], ",")
    plt.xlabel(r"$V_{C_{2}}\left(t_{n}\right)$", fontsize=15)
    plt.ylabel(r"$V_{C_{2}}\left(t_{n+1}\right)$", fontsize=15)
    plt.savefig(
        "img/V_C_2_t_n_versus_V_C_2_t_n_plus_1.pdf",
        transparent=True,
        bbox_inches="tight",
    )
    plt.close()
