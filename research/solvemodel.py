#!/usr/bin/env python

import numpy as np
from scipy.optimize import fsolve
from model import f, g, h


def i(θ):
    return f(θ) - 1 / 4


def j(θ):
    θ1 = fsolve(g, [0.1])[0]
    return f(θ) - f(θ1)


if __name__ == "__main__":
    θ1, θ2 = fsolve(g, [0.1])[0], fsolve(g, [20])[0]
    print(f"Solution of f'(θ) = 0 are {θ1} and {θ2}")
    assert np.allclose(a=[g(θ1), g(θ2)], b=np.zeros((2, 1)))

    root = fsolve(h, [0.1])[0]
    print(f"Solution of f''(θ) = 0 is {root}")
    assert np.allclose(a=[h(root)], b=np.zeros((1, 1)))

    θM = fsolve(i, [580.54])[0]
    θMguess = 580.54360750848110229
    # assert np.allclose(a=[f(θMguess)], b=np.zeros((1, 1)))
    # print(i(θM))
    # print(f(θMguess))
    print(f(θ1), f(θ2))
    θ3 = fsolve(j, [500])[0]
    θ3 = 580.52183
    print(θ3, f(θ3), f(θ1))
