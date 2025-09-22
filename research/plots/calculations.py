#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

plt.style.use("seaborn-v0_8-white")
np.set_printoptions(precision=2, suppress=True, threshold=5)

Sly = 1 / 2  # np.linspace(start=0, stop=1, num=10)
Sor = 1 - Sly
a1 = 0.00189
a2 = 27.6
a3 = 0.00252
b1 = 1.1
b2 = 30.4
b3 = 1
alpha = 0.2
kp = 1  # 24556
Cm = 2e6
Er = 51247
R = 8.314
Tres = 300
tast = 1e8 / kp
beta = alpha * tast / Cm
print(f"Valor de beta es {beta}")
theta0 = 1  # Tres / tast
c = (a2 * b3 * Sly + a3 * b2 * Sor) / (b2 * Sor + b3 * Sly)
q = (a1 * b3) / (b1 * (c - a3))
m = beta * Sor / (b1 * Sly * tast * kp)
m = 1
varepsilon = Er / (R * Tres)  # Tres= Tast

# varepsilon = 0.5
# theta0 = 1
# q = -1
theta0 = 1.5
q = 1
varepsilon = 2

theta0 = 0.5
delta = varepsilon * (varepsilon - 4 * theta0 - 4 * theta0**2 * q)
print(f"Delta: {delta}")


# m = (beta * Sor) / (Sly * tast * kp * b1)
def f(theta):
    return m * (theta / (1 - q * theta)) * np.exp(varepsilon / (theta + theta0))


def Phi(theta):
    return tast * kp * np.exp(-Er / (R * (Tres * theta + Tres)))  # Tres= Tast


#     print(f"Valor de c: {c}")
#     print(f"Valor de 1/q: {1 / q} cuando S^L_y = {Sly} y S^R_o = {Sor}")
theta = np.linspace(start=-0.5, stop=2, num=3000)
plt.scatter(x=theta, y=f(theta=theta), s=0.5)
# plt.axhline(y=1 / 16, linewidth=0.5, color="g", linestyle="dashed")
# plt.axhline(linewidth=0.5, color="r")
# plt.axhline(y=2.5e-7, linewidth=0.5, color="g", linestyle="dashed")
# plt.axvline(x=511.5294712364778, linewidth=0.5, color="b", linestyle="dashed")
plt.title(
    # label=rf"Case 3.1.2, $f\left(\theta\right)$ with parameters $m={{{m}}}$, $\varepsilon={{{varepsilon:.2f}}}$, $\theta_{0}={{{theta0:.2f}}}$, $q={{{q:.3f}}}$"
    # label=rf"Case 3.2.1, $f\left(\theta\right)$ with parameters $m={{{m}}}$, $\varepsilon={{{varepsilon:.2f}}}$, $\theta_{0}={{{theta0:.2f}}}$, $q={{{q:.3f}}}$"
    label=rf"Case 3.2.2, $f\left(\theta\right)$ with parameters $m={{{m}}}$, $\varepsilon={{{varepsilon:.2f}}}$, $\theta_{0}={{{theta0:.2f}}}$, $q={{{q:.3f}}}$"
    + "\n"
    # + rf"$1+q\varepsilon={{{(1 + q * varepsilon):.3f}}}>0$, "
    + rf"$1+q\varepsilon={{{(1 + q * varepsilon):.3f}}}<0$, "
    # + rf"$2\theta_{0}-\varepsilon={{{(2 * theta0 - varepsilon):.3f}}}>0$",
    + rf"$2\theta_{0}-\varepsilon={{{(2 * theta0 - varepsilon):.3f}}}<0$",
    loc="center",
    wrap=True,
    fontsize=15,
)
plt.grid()
# plt.xlim(0, 1000)
# plt.ylim(-1e6, 1e6)
plt.ylim(-500, 500)
plt.tight_layout()
plt.savefig("fthetaplot3.2.2.pdf", transparent=True, bbox_inches="tight")

print(f"Valor de m: {m}")
print(f"Valor de varepsilon: {varepsilon}")
print(f"Valor de theta0: {theta0}")
print(f"Valor de q: {q}")
print(f"Valor de delta: {delta}")
# print(f"Case 3.1: {1 + q * varepsilon}")
# print(f"Case 3.1.2: {2 * theta0 - varepsilon}")
print(f"Case 3.2: {1 + q * varepsilon}")
# print(f"Case 3.2.1: {2 * theta0 - varepsilon}")
print(f"Case 3.2.2: {2 * theta0 - varepsilon}")
plt.clf()

So, theta = np.meshgrid(np.linspace(0, 10), np.linspace(0, 10))
F1 = b3 * Sly / Sor * Phi(theta) * (Sor - So) * So / (c - a3)
F2 = b1 * (1 - q * theta) / (c - a1 * So) * Phi(theta) * (So**2 - Sor + f(theta))
print(c)
print(a3)
fig, ax = plt.subplots()
ax.set_xlabel(r"$S_{\text{o}}$")
ax.set_ylabel(r"$\theta$")
ax.set_title(
    r"$S^{L}_{y}=$"
    + f"{Sly}, "
    + r"$S^{R}_{o}=$"
    + f"{Sor}, "
    + r"$b_{1}=$"
    + f"{b1}, "
    r"$b_{3}=$"
    + f"{b3}, "
    + r"$a_{1}=$"
    + f"{a1}, "
    + r"$a_{3}=$"
    + f"{a3}\n"
    + r"$c=$"
    + f"{c}, "
    + r"$\alpha=$"
    + f"{alpha}, "
    + r"$t^{\ast}=$"
    + f"{tast}, "
    + r"$C_{m}=$"
    + f"{Cm}",
    fontsize=12,
    wrap=True,
)
ax.quiver(So, theta, F1, F2, units="width")
plt.savefig("1.pdf")
plt.clf()

fig, ax = plt.subplots()
ax.streamplot(So, theta, F1, F2)
ax.set_xlabel(r"$S_{\text{o}}$")
ax.set_ylabel(r"$\theta$")
ax.set_title(
    r"$S^{L}_{y}=$"
    + f"{Sly}, "
    + r"$S^{R}_{o}=$"
    + f"{Sor}, "
    + r"$b_{1}=$"
    + f"{b1}, "
    r"$b_{3}=$"
    + f"{b3}, "
    + r"$a_{1}=$"
    + f"{a1}, "
    + r"$a_{3}=$"
    + f"{a3}\n"
    + r"$c=$"
    + f"{c}, "
    + r"$\alpha=$"
    + f"{alpha}, "
    + r"$t^{\ast}=$"
    + f"{tast}, "
    + r"$C_{m}=$"
    + f"{Cm}",
    fontsize=12,
    wrap=True,
)
plt.savefig("2.pdf")
plt.clf()
