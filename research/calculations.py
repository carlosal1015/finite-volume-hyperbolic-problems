#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

plt.style.use("seaborn-v0_8-white")
np.set_printoptions(precision=2, suppress=True, threshold=5)


# tast = 1e8 / kp
# beta = alpha * tast / Cm
# m = (beta * Sor) / (Sly * tast * kp * b1)
def f(theta):
    alpha = 0.2
    Sly = 1 / 2  # np.linspace(start=0, stop=1, num=10)
    Sor = 1 - Sly
    kp = 1  # 24556
    Cm = 2e6
    a1 = 0.00189
    a2 = 27.6
    a3 = 0.00252
    b1 = 1.1
    b2 = 30.4
    b3 = 1
    Er = 51247
    R = 8.314
    Tres = 300
    p = 1  # Tres / tast
    c = (a2 * b3 * Sly + a3 * b2 * Sor) / (b2 * Sor + b3 * Sly)
    q = (a1 * b3) / (b1 * (c - a3))
    m = alpha * Sor / (Sly * b1) * 1 / (kp * Cm)
    n = Er / (R * Tres)  # Tres= Tast
    return m * theta * np.exp(n / (theta + p)) / (1 - q * theta)


# if __name__ == "__main__":
#     print(f"Valor de c: {c}")
#     print(f"Valor de 1/q: {1 / q} cuando S^L_y = {Sly} y S^R_o = {Sor}")
#     theta = np.linspace(start=0, stop=1000, num=3000)
#     plt.scatter(x=theta, y=f(theta=theta), s=0.5)
#     # plt.axhline(y=1 / 16, linewidth=0.5, color="g", linestyle="dashed")
#     plt.axhline(linewidth=0.5, color="r")
#     plt.axhline(y=2.5e-7, linewidth=0.5, color="g", linestyle="dashed")
#     plt.axvline(x=511.5294712364778, linewidth=0.5, color="b", linestyle="dashed")
#     plt.title(r"$f\left(\theta\right)$ over $\theta\in\left[0,1000\right]$")
#     plt.xlim(0, 1000)
#     plt.ylim(-5e-7, 5e-7)
#     # plt.ylim(-5e-6, 5e-6)
#     plt.tight_layout()
#     plt.savefig("fthetaplot.pdf", transparent=True, bbox_inches="tight")

#     print(f"Valor de m: {m}")
#     print(f"Valor de n: {n}")
#     print(f"Valor de p: {p}")
#     print(f"Valor de q: {q}")
