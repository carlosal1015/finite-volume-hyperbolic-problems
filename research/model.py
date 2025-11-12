#!/usr/bin/env python

import numpy as np

# β calculation
α = 1
kp = 24556
Cm = 2e6
β = (α * 1e8) / (kp * Cm)

# q calculation
a1 = 0.00189
b3 = 1
b1 = 1.1
c = 1
a3 = 0.00252
q = (a1 * b3) / (b1 * (c - a3))

# θ0 calculation
θ0 = 1

# ε calculation
Er = 51247
R = 8.314
Tast = 300
ε = Er / (R * Tast)

# SyL calculation
b2 = 30.4
a2 = 27.6
SoR = 1
SyL = -(b2 * (c - a3) * SoR) / (b3 * (c - a2))
# print(f"SyL = {SyL}")
# m calculation
m = (β * SoR) / (b1 * Tast * kp * SyL)


def f(θ):
    return m * θ / (1 - q * θ) * np.exp(ε / (θ + θ0))


def fprime(θ):
    return f(θ) * (1 / θ + q / (1 - q * θ) - ε / (θ0 + θ) ** 2)


def fprimeprime(θ):
    return -f(θ) * (
        (2 * ε * q) / ((1 - q * θ) * (θ0 + θ) ** 2)
        - ε * (2 + ε / (θ0 + θ)) / (θ0 + θ) ** 3
        + 2 * ε / (θ * (θ0 + θ) ** 2)
        - 2 * q**2 / (1 - q * θ) ** 2
        - 2 * q / (θ * (1 - q * θ))
    )


def g(θ):
    return (1 + ε * q) * θ**2 + (2 * θ0 - ε) * θ + θ0**2


def h(θ):
    return (
        ε**2 * q**2 * θ**3
        - 2 * ε**2 * q * θ**2
        + ε**2 * θ
        + 2 * ε * q**2 * θ**4
        + 2 * ε * q**2 * θ**3 * θ0
        - 2 * ε * q * θ**3
        + 2 * ε * q * θ * θ0**2
        - 2 * ε * θ * θ0
        - 2 * ε * θ0**2
        + 2 * q * θ**4
        + 8 * q * θ**3 * θ0
        + 12 * q * θ**2 * θ0**2
        + 8 * q * θ * θ0**3
        + 2 * q * θ0**4
    )


if __name__ == "__main__":
    print(f"Parámetros del modelo: m = {m}\t, ε = {ε}\t, θ0 = {θ0}\t, q = {q}")
    print(c / a1)
    print(f(3e8))
    print(f"1 / q = {1 / q}")
