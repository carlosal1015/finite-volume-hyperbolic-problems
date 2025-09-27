from numpy import sqrt, log
from clawpack import riemann
from clawpack import pyclaw
import numpy as np
import matplotlib.pyplot as plt


def xfr(t):
    return sqrt(1 + t) / 2


def qtrue(x, t):
    """
    The true solution, for comparison.
    """
    import numpy as np

    dim = x.shape[0]
    q = np.empty(dim)
    xf = xfr(t)
    for i in range(dim):
        if x[i] >= 0.0 and x[i] <= xf:
            q[i] = (x[i]) / (t + 1)
        else:
            q[i] = 0

    return q


def burgers(q_l, q_r, aux_l, aux_r, problem_data):
    r"""
    1d burgers riemann solver
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

    # Compute the wave
    # 1-Wave
    wave[0, 0, :] = delta
    s[0, :] = 0.5 * (q_r[0, :] + q_l[0, :])
    # Compute the left going and right going fluctuations
    s_index = np.zeros((2, num_rp))
    s_index[0, :] = s[0, :]
    amdq[0, :] = np.min(s_index, axis=0) * wave[0, 0, :]
    apdq[0, :] = np.max(s_index, axis=0) * wave[0, 0, :]

    # Compute entropy fix
    if problem_data["efix"]:
        transonic = (q_l[0, :] < 0.0) * (q_r[0, :] > 0.0)
        amdq[0, transonic] = -0.5 * q_l[0, transonic] ** 2
        apdq[0, transonic] = 0.5 * q_r[0, transonic] ** 2

    return wave, s, amdq, apdq


def setup(outdir="./_output", output_style=1):
    solver = pyclaw.ClawSolver1D()
    solver.rp = burgers
    solver.fwave = False
    solver.num_waves = 1
    solver.num_eqn = 1
    solver.kernel_language = "Python"
    solver.limiters = pyclaw.limiters.tvd.superbee
    solver.bc_lower[0] = pyclaw.BC.extrap
    solver.bc_upper[0] = pyclaw.BC.extrap
    solver.order = 2  # 1: Godunov, 2: Lax-Wendroff-LeVeque
    x = pyclaw.Dimension(-0.10, 1.5, 320, name="x")
    domain = pyclaw.Domain(x)
    xc = domain.grid.x.centers
    num_eqn = 1
    state = pyclaw.State(domain, num_eqn)
    state.problem_data["efix"] = True
    state.q[0, :] = qtrue(xc, 0)
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
true = qtrue(x, t)
fig, ax = plt.subplots(figsize=(5, 2.7))
w = frame.q[0, :]

ax.plot(x, w, label="Clawpack sol.")
ax.plot(x, true, ":", label="exact solution")
ax.legend(loc="right")
ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$q$")
plt.savefig("InitialValueBurgerClaw.pdf")

nsimul = np.size(claw.frames)
positionFront = []
for i in range(nsimul):
    frame = claw.frames[i]
    w = frame.q[0, :]
    xc = frame.state.grid.c_centers[0]
    nx = xc.size
    dx = (xc[-1] - xc[0]) / nx
    pos = dx * w[w > 1.0e-5].size
    positionFront.append(pos)

t = np.linspace(0, claw.tfinal, nsimul)
xfront = xfr(t)

fig, ax = plt.subplots()
ax.set_xlabel(r"$t$")
ax.set_ylabel(r"$s(t)$")

ax.plot(t, xfront, "--", color="r")
ax.plot(t, positionFront)
plt.savefig("frontBurgerClaw.pdf")
