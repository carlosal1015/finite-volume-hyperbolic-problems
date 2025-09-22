from clawpack import riemann
from clawpack import pyclaw
import numpy as np
import matplotlib.pyplot as plt


def SpatialAdvection(q_l, q_r, aux_l, aux_r, problem_data):
    r"""Basic 1d advection riemann solver
    *aux(i)* should contain -
    - *u(x_i)* - (float) advection speed
    """
    num_eqn = 1
    num_waves = 1
    # Number of Riemann problems we are solving
    num_rp = q_l.shape[1]

    # Return values
    wave = np.empty((num_eqn, num_waves, num_rp))
    s = np.empty((num_waves, num_rp))
    amdq = np.zeros((num_eqn, num_rp))
    apdq = np.zeros((num_eqn, num_rp))
    wave[0, 0, :] = q_r[0, :] - q_l[0, :]
    s[0, :] = aux_l[0, :]
    apdq[0, :] = (aux_l[0, :] > 0) * s[0, :] * wave[0, 0, :]
    amdq[0, :] = (aux_l[0, :] < 0) * s[0, :] * wave[0, 0, :]

    return wave, s, amdq, apdq


def qtrue(x, t):
    """
    The true solution, for comparison.
    """
    from numpy import mod, exp, where, logical_and

    beta = 100
    gamma = 0
    x0 = 0.75
    xm = (np.sqrt(x) - t) ** 2
    q = exp(-beta * (xm - x0) ** 2) + where(logical_and(xm > 0.1, xm < 0.4), 1, 0)

    return q


# Advection speed
def auxinit(state):
    # Initialize aux
    xc = state.grid.x.centers
    state.aux[0, :] = 2 * np.sqrt(xc)


def setup(outdir="./_output"):
    from clawpack import riemann

    solver = pyclaw.ClawSolver1D(SpatialAdvection)
    solver.fwave = False
    solver.num_waves = 1
    solver.num_eqn = 1
    solver.kernel_language = "Python"
    solver.limiters = pyclaw.limiters.tvd.MC
    solver.bc_lower[0] = pyclaw.BC.extrap
    solver.bc_upper[0] = pyclaw.BC.extrap
    solver.aux_bc_lower[0] = pyclaw.BC.extrap
    solver.aux_bc_upper[0] = pyclaw.BC.extrap

    xlower = 0.0
    xupper = 2.0
    mx = 200
    x = pyclaw.Dimension(xlower, xupper, mx, name="x")
    domain = pyclaw.Domain(x)
    num_aux, num_eqn = 1, 1
    state = pyclaw.State(domain, num_eqn, num_aux)

    xc = domain.grid.x.centers
    state.q[0, :] = qtrue(xc, 0)
    auxinit(state)

    claw = pyclaw.Controller()
    claw.outdir = outdir
    claw.solution = pyclaw.Solution(state, domain)
    claw.solver = solver

    claw.tfinal = 0.3
    claw.num_output_times = 10
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

true = qtrue(x, t)
fig, ax = plt.subplots(figsize=(5, 2.7))
w = frame.q[0, :]

ax.plot(x, w, label="Clawpack sol.")
ax.plot(x, true, ":", label="exact solution")
ax.legend(loc="right")
ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$q$")
plt.savefig("SpatiallyVaryingAdvection.pdf", bbox_inches="tight")
