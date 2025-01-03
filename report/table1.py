#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate
from matplotlib.axes import Axes
from matplotlib.figure import Figure
from h5py import File


plt.style.use("seaborn-v0_8-white")


def U(x):
    np.exp(-200 * np.power(x - 0.25, 2))


c = 0.5
r = 1 / 3
Δxs = np.logspace(start=-9, stop=-5, num=5, base=2)
error = []
# Stability conditions
# assert ((cfls >= -1) & (cfls <= 0)).all()
# α = 1 + cfls
# β = -cfls
# assert ((np.absolute(α) + np.absolute(β)) <= 1).all()


for Δx in Δxs:
    Δt = Δx * r
    CFL = c * Δt / Δx
    x = np.linspace(start=0, stop=1, num=np.reciprocal(np.power(Δx, 2)).astype(int))
    t = np.linspace(start=0, stop=1, num=np.reciprocal(np.power(Δt, 2)).astype(int))
    U1 = U(x=x)

    for timestep in t:
        U1[1:] -= CFL * (U1 - np.roll(U1, 1))[1:]
        U1[0] = U1[2]
        U1[-1] = U1[-3]

    t_final = t[-1]
    U_final = U(x=x - c * t_final)
    # U1.size, np.linspace(start=0, stop=1, num=t_points[0]) * t_points[0]
    error.append(np.linalg.vector_norm(U_final - U1, ord=2))


print(
    tabulate(
        tabular_data=np.c_[
            np.flipud(m=Δxs),
            np.flipud(m=Δxs * r),
            # np.flipud(m=error1_fou1d),
            # np.flipud(
            #     m=np.concatenate((order1_fou1d, np.full(shape=(1,), fill_value=np.nan)))
            # ),
            # np.flipud(m=errorinf_fou1d),
            # np.flipud(
            #     m=np.concatenate(
            #         (orderinf_fou1d, np.full(shape=(1,), fill_value=np.nan))
            #     )
            # ),
            # np.flipud(m=error2_fou1d),
            # np.flipud(
            #     m=np.concatenate((order2_fou1d, np.full(shape=(1,), fill_value=np.nan)))
            # ),
        ],
        headers=[
            "Δx",
            "Δt",
            # "Error ℓ1",
            # "Orden ℓ1",
            # "Error ℓ∞",
            # "Orden ℓ∞",
            # "Error ℓ2",
            # "Orden ℓ2",
        ],
        floatfmt=(
            ".3E",
            ".3E",
            # ".3E",
            # ".3f",
            # ".3E",
            # ".3f",
            # ".3E",
            # ".3f",
        ),
        colalign=(
            "center",
            "center",
            # "center",
            # "left",
            # "center",
            # "left",
            # "center",
            # "left",
        ),
    )
)

# fig: Figure
# ax: Axes
# fig, ax = plt.subplots(layout="constrained")
# Errors and convergence order of explicit upwind scheme with r = s = 1 / 3
# \Delta x  \Delta t    error   orden
# 1 / 2^5   1/3*1/2^5
# 1 / 2^6   1/3*1/2^6
# 1 / 2^7   1/3*1/2^7
# 1 / 2^8   1/3*1/2^8
# 1 / 2^9   1/3*1/2^9

# r = 1 / 2
# cfls = c * Δts / Δxs * r

# α = 1 + cfls
# β = -cfls
# assert ((cfls >= -1) & (cfls <= 0)).all()
# assert ((np.absolute(α) + np.absolute(β)) <= 1).all()
# Errors and convergence order of explicit upwind scheme with r = s = 1 / 2
# \Delta x  \Delta t    error   orden
# 1 / 2^5   1/2*1/2^5
# 1 / 2^6   1/2*1/2^6
# 1 / 2^7   1/2*1/2^7
# 1 / 2^8   1/2*1/2^8
# 1 / 2^9   1/2*1/2^9
