from numpy import sqrt, exp, cos, logical_and, where
from clawpack import riemann
from clawpack import pyclaw


def advection(q_l, q_r, aux_l, aux_r, problem_data):
    r"""
    1d linear advection riemann solver
    """
    import numpy as np

    num_eqn = 1
    num_waves = 1

    # Convenience
    num_rp = q_l.shape[1]

    # Return values
    wave = np.empty((num_eqn, num_waves, num_rp))
    s = np.empty((num_waves, num_rp))
    amdq = np.empty((num_eqn, num_rp))
    apdq = np.empty((num_eqn, num_rp))

    # Local values
    delta = np.empty(np.shape(q_l))

    delta = q_r - q_l
    a = problem_data["a"]

    # Compute the wave
    # 1-Wave
    wave[0, 0, :] = delta
    s[0, :] = a

    # Compute the left going and right going fluctuations
    for m in range(num_eqn):
        amdq[m, :] = min(a, 0) * wave[m, 0, :]
        apdq[m, :] = max(a, 0) * wave[m, 0, :]

    return wave, s, amdq, apdq


def setup(outdir="./_output", output_style=1):
    solver = pyclaw.ClawSolver1D(advection)
    solver.fwave = False
    solver.num_waves = 1
    solver.num_eqn = 1
    solver.kernel_language = "Python"
    solver.limiters = pyclaw.limiters.tvd.MC
    solver.bc_lower[0] = pyclaw.BC.periodic
    solver.bc_upper[0] = pyclaw.BC.periodic
    solver.order = 1  # 1: Godunov, 2: Lax-Wendrow-LeVeque

    x = pyclaw.Dimension(0.0, 1.0, 100, name="x")
    domain = pyclaw.Domain(x)
    num_eqn = 1

    state = pyclaw.State(domain, num_eqn)
    a = 0.5  # advection velocity
    state.problem_data["a"] = a

    xc = domain.grid.x.centers
    beta = 100
    gamma = 0
    x0 = 0.75
    state.q[0, :] = exp(-beta * (xc - x0) ** 2) + where(
        logical_and(xc > 0.1, xc < 0.4), 1, 0
    )

    claw = pyclaw.Controller()
    claw.solution = pyclaw.Solution(state, domain)
    claw.solver = solver
    claw.outdir = outdir
    claw.output_style = output_style
    claw.tfinal = 4.0
    claw.num_output_times = 10
    claw.keep_copy = True
    # claw.setplot = setplot

    return claw


def setplot(plotdata):
    """
    Plot solution using VisClaw.
    """
    plotdata.clearfigures()  # clear any old figures,axes,items data

    plotfigure = plotdata.new_plotfigure(name="q", figno=1)
    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes()
    plotaxes.ylimits = [-0.2, 1.0]
    plotaxes.title = "q"

    # Set up for item on these axes:
    plotitem = plotaxes.new_plotitem(plot_type="1d_plot")
    plotitem.plot_var = 0
    plotitem.plotstyle = "-o"
    plotitem.color = "b"
    plotitem.kwargs = {"linewidth": 2, "markersize": 5}

    return plotdata


def qtrue(x, t):
    """
    The true solution, for comparison.
    """

    from numpy import mod, exp, where, logical_and

    beta = 100
    gamma = 0
    x0 = 0.75
    u = claw.solution.state.problem_data["a"]
    xm = x - u * t
    xm = mod(xm, 1.0)  # because of periodic boundary conditions
    q = exp(-beta * (xm - x0) ** 2) + where(logical_and(xm > 0.1, xm < 0.4), 1, 0)

    return q


claw = setup()
claw.run()


from clawpack.visclaw import data
from clawpack.visclaw import frametools


plotdata = data.ClawPlotData()
plotdata.setplot = setplot
claw.plotdata = frametools.call_setplot(setplot, plotdata)
frame = claw.load_frame(10)
f = claw.plot_frame(frame)

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["text.usetex"] = True
frame = claw.frames[5]
dt = claw.tfinal / claw.num_output_times
t = dt * 5
w = frame.q[0, :]
x = frame.state.grid.c_centers
x = x[0]
true = qtrue(x, t)
fig, ax = plt.subplots(figsize=(5, 2.7))
ax.plot(x, w, label="pyclaw")
ax.plot(x, true, ":", label="exact solution")
ax.legend(loc="right")
ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$q$")
plt.savefig("frameAdvection5.pdf")

nsimul = np.size(claw.frames)
figs = []
for i in range(nsimul):
    fig = plt.figure(figsize=(5, 3))
    frame = claw.frames[i]
    w = frame.q[0, :]
    x = frame.state.grid.c_centers
    x = x[0]
    dt = claw.tfinal / claw.num_output_times
    t = dt * i
    true = qtrue(x, t)
    plt.plot(x, w)
    plt.plot(x, true, "--", color="r")
    figs.append(fig)
    plt.close(fig)

from clawpack.visclaw import animation_tools

animation_tools.interact_animate_figs(figs)
