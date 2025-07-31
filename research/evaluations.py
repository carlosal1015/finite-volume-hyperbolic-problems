#!/usr/bin/env python

import numpy as np
from scipy.optimize import fsolve

"""Case Δ > 0, q < 0, 1 + q * ε < 0
"""

m = 3.702113166195264e-12
ε = 20.546467805308318
θ0 = 1
q = -1e-2


def f(θ):
    return m * θ / (1 - q * θ) * np.exp(ε / (θ0 + θ))


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


# f'(θ) = 0
# root1 = fsolve(g, [0.1])
# root2 = fsolve(g, [20])
# print(root1)
# print(root2)
# print(np.isclose(g(root1), [0.0]))
# print(np.isclose(g(root2), [0.0]))

# # f''(θ) = 0
# root3 = fsolve(h, [0.1])
# root4 = fsolve(h, [45])
# print(root3)
# print(root4)
# print(np.isclose(h(root3), [0.0]))
# print(np.isclose(h(root4), [0.0]))

"""Case Δ > 0, q < 0, 1 + q * ε > 0
"""

m = 3.702113166195264e-1
ε = 20.546467805308318
θ0 = 1
q = -1.1


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


# f'(θ) = 0
root1 = fsolve(g, [0.1])
# root2 = fsolve(g, [20])
print(root1)
# print(root2)
print(np.isclose(g(root1), [0.0]))
# print(np.isclose(g(root2), [0.0]))

# f''(θ) = 0
root3 = fsolve(h, [0.1])
# root4 = fsolve(h, [45])
print(root3)
# print(root4)
print(np.isclose(h(root3), [0.0]))
# print(np.isclose(h(root4), [0.0]))
# theta = 23.288490301174345
# values = np.array(
#     [
#         theta,
#         2 * theta,
#         5 * theta,
#         10 * theta,
#         100 * theta,
#         # 1000 * theta,
#     ]
# )
# print(values)
# print(fprimeprime(values))
