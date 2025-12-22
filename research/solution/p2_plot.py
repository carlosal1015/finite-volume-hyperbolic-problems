#!/usr/bin/env python

"""Programa p2_plot.py"""

from scipy.optimize import fsolve
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

plt.rcParams["text.usetex"] = True
plt.rcParams["font.serif"] = ["Computer Modern"]
# plt.rcParams["figure.autolayout"] = True
# plt.rcParams["figure.figsize"] = [10, 10]

nx = 201
x = np.linspace(start=-20.0, stop=20.0, num=nx)

x_, y_ = np.meshgrid(x, x)
equation_1 = x_**2 + x_ * y_ - 77
equation_2 = x_ * y_ + y_**2 - 44

root_0 = fsolve(
    func=lambda x: [x[0] ** 2 + x[0] * x[1] - 77, x[0] * x[1] + x[1] ** 2 - 44],
    x0=[-10, 0],
)

root_1 = fsolve(
    func=lambda x: [x[0] ** 2 + x[0] * x[1] - 77, x[0] * x[1] + x[1] ** 2 - 44],
    x0=[0, 10],
)

if __name__ == "__main__":
    fig, ax = plt.subplots()
    ax.grid()
    # ax.plot(x, y, "b", lw=0.5)
    # https://matplotlib.org/stable/gallery/subplots_axes_and_figures/axis_equal_demo.html
    # https://stackoverflow.com/a/39500357/9302545
    ax.axis("equal")
    CS_1 = ax.contour(x_, y_, equation_1, [0], linewidths=0.5, colors=["red"])
    CS_2 = ax.contour(x_, y_, equation_2, [0], linewidths=0.5, colors=["blue"])
    # h, _ = CS.legend_elements()
    # label=r"$x + y = 24$"
    black_patch = mpatches.Patch(
        color="red", label=r"$x^{2} + xy = 77$", linewidth=0.1, linestyle="-"
    )
    red_patch = mpatches.Patch(
        color="blue", label=r"$xy + y^{2}= 44$", linewidth=0.1, linestyle="-"
    )
    ax.legend(
        handles=[black_patch, red_patch], shadow=True, title="Leyenda", fancybox=True
    )
    fig.savefig("p2_plot.pdf", transparent=True, bbox_inches="tight")
    print(f"Ceros: {root_0}, {root_1}")
