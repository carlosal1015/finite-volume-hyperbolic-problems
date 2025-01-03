import numpy as np
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D

plt.style.use("seaborn-v0_8-white")

x = np.linspace(start=-1, stop=1, num=200)
y = np.linspace(start=-1, stop=1, num=200)
X, Y = np.meshgrid(x, y)
U0 = np.sin(np.pi * X) + np.sin(np.pi * Y)
fig: Figure
ax: Axes
fig, ax = plt.subplots(layout="constrained")
img = ax.imshow(
    X=U0,
    extent=(x[0], x[-1], y[0], y[-1]),
    cmap="jet",
    interpolation="none",
)
ax.set_xlabel(xlabel=r"$x$")
ax.set_ylabel(ylabel=r"$y$")
ax.set_xticks(ticks=np.linspace(start=x[0], stop=x[-1], num=3))
ax.set_yticks(ticks=np.linspace(start=y[0], stop=y[-1], num=3))
ax.set_title(
    label=r"Condición inicial $U_{0}\left(x,y\right)$",
    loc="center",
    wrap=True,
)
cbar = fig.colorbar(
    mappable=img,
    ticks=[U0.min(), 0.5 * (U0.min() + U0.max()), U0.max()],
    orientation="horizontal",
)
labels = cbar.ax.get_xticklabels()
labels[0].set_horizontalalignment("left")
labels[-1].set_horizontalalignment("right")
plt.savefig("2dinitialimshow.pdf", transparent=True, bbox_inches="tight")
plt.close()

ax: Axes3D
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
surface = ax.plot_surface(
    X,
    Y,
    U0,
    antialiased=False,
    cmap="jet",
    cstride=1,
    linewidth=0,
    rstride=1,
    shade=False,
)
ax.set_xlabel(xlabel=r"$x$")
ax.set_ylabel(ylabel=r"$y$")
ax.set_zlabel(zlabel=r"$U_{0}\left(x,y\right)$")
ax.set_xlim(left=x[0], right=x[-1])
ax.set_ylim(bottom=y[0], top=y[-1])
ax.set_zlim(bottom=U0.min(), top=U0.max())
ax.set_xticks(ticks=np.linspace(start=x[0], stop=x[-1], num=3))
ax.set_yticks(ticks=np.linspace(start=y[0], stop=y[-1], num=3))
ax.set_zticks(ticks=np.linspace(start=U0.min(), stop=U0.max(), num=3))
ax.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.set_title(
    label=r"Condición inicial $U_{0}\left(x,y\right)$",
    loc="center",
)
ax.set_aspect(aspect="equal", adjustable="box")
plt.savefig("2dinitialsurface.pdf", transparent=True, bbox_inches="tight")
plt.close()
