from numpy import sqrt, log, tanh
from clawpack import riemann
from clawpack import pyclaw
import numpy as np
import matplotlib.pyplot as plt


# Travelling wave solution
def travel(x, t, ul, ur, nu):
    return (ur + ul) / 2 - abs((ul - ur)) / 2 * tanh(
        (x - (ur + ul) / 2 * t) * (ul - ur) / 4 / nu
    )


def qtrue(x, t, ul, ur, nu):
    """
    The true solution, for comparison.
    """
    import numpy as np

    dim = x.shape[0]
    q = np.empty(dim)
    for i in range(dim):
        q[i] = travel(x[i], t, ul, ur, nu)

    return q


def source_term(solver, state, dt):
    from scipy.linalg import solve_banded
    import numpy as np

    qs = state.q[0, :]
    xc = state.grid.c_centers[0]
    nx = xc.size
    dx = (xc[-1] - xc[0]) / nx
    nu = state.problem_data["nu"]
    r = nu * dt / (dx**2 * 2.0)
    m = qs.shape[0]
    b = np.empty(m)

    for i in range(m):
        if i == 0:
            b[0] = (1 - r) * qs[0] + r * qs[1]
        elif i == m - 1:
            b[m - 1] = (1 - r) * qs[m - 1] + r * qs[m - 2]
        else:
            b[i] = r * qs[i - 1] + (1 - 2 * r) * qs[i] + r * qs[i + 1]

    ab = np.empty((3, m))
    ab[0, 1:] = [-r] * (m - 1)
    ab[1, :] = [1 + 2 * r] * m
    ab[2, :-1] = [-r] * (m - 1)
    ab[1, 0] = 1 + r
    ab[1, -1] = 1 + r
    state.q[0, :] = solve_banded((1, 1), ab, b)


def setup(outdir="./_output", output_style=1):
    solver = pyclaw.ClawSolver1D()
    solver.rp = riemann.burgers_1D_py.burgers_1D

    solver.fwave = False
    solver.num_waves = 1
    solver.num_eqn = 1
    solver.kernel_language = "Python"
    solver.limiters = pyclaw.limiters.tvd.superbee
    solver.bc_lower[0] = pyclaw.BC.extrap
    solver.bc_upper[0] = pyclaw.BC.extrap
    solver.order = 2  # 1: Godunov, 2: Lax-Wendroff-LeVeque
    solver.step_source = source_term  # inclusion of source term
    mx = 600
    x = pyclaw.Dimension(-3, 3, mx, name="x")
    domain = pyclaw.Domain(x)
    num_eqn = 1
    state = pyclaw.State(domain, num_eqn)
    # Parameters
    nu = 0.5
    ul = 2
    ur = 0
    state.problem_data["efix"] = True
    state.problem_data["nu"] = nu  # diffusivity
    state.problem_data["ul"] = ul  # left state
    state.problem_data["ur"] = ur  # right state

    xc = domain.grid.x.centers
    # for i in range(mx):
    #     state.q[0,i] = travel(xc[i],0,ul,ur,nu) #initial condition

    state.q[0, :] = travel(xc, 0, ul, ur, nu)
    claw = pyclaw.Controller()
    claw.solution = pyclaw.Solution(state, domain)
    claw.solver = solver
    claw.outdir = outdir
    claw.output_style = output_style
    claw.tfinal = 2.0
    claw.num_output_times = 20
    claw.keep_copy = True

    return claw


claw = setup()
claw.run()

plt.rcParams["text.usetex"] = True
index = 10
frame = claw.frames[index]
dt = claw.tfinal / claw.num_output_times
t = dt * index
x = frame.state.grid.c_centers
x = x[0]

ul = frame.state.problem_data["ul"]
ur = frame.state.problem_data["ur"]
nu = frame.state.problem_data["nu"]
true = qtrue(x, t, ul, ur, nu)
fig, ax = plt.subplots(figsize=(5, 2.7))
w = frame.q[0, :]

ax.plot(x, w, label="Clawpack sol.")
ax.plot(x, true, ":", label="exact solution")
ax.legend(loc="right")
ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$q$")
plt.savefig("ViscousBurgerClaw.pdf")

nsimul = np.size(claw.frames)
figs = []
for i in range(nsimul):
    fig, ax = plt.subplots(figsize=(5, 3))
    frame = claw.frames[i]
    w = frame.q[0, :]
    x = frame.state.grid.c_centers
    x = x[0]
    dt = claw.tfinal / claw.num_output_times
    t = dt * i
    true = qtrue(x, t, ul, ur, nu)
    ax.set_xlabel(r"$x$")
    ax.set_ylabel(r"$q$")

plt.plot(x, w)
plt.plot(x, true, "--", color="r")
figs.append(fig)
plt.close(fig)

from clawpack.visclaw import animation_tools

animation_tools.interact_animate_figs(figs)
