import numpy as np
import matplotlib.pyplot as plt

from clawpack import riemann
from clawpack import pyclaw


def burgers_1D(q_l, q_r, aux_l, aux_r, problem_data):
    r"""
    Riemann solver for Burgers equation in 1d
    *problem_data* should contain -
    - *efix* - (bool) Whether a entropy fix should be used, if not present, false is assumed
    """
    num_rp = q_l.shape[1]
    # Output arrays
    wave = np.empty((num_eqn, num_waves, num_rp))
    s = np.empty((num_waves, num_rp))
    amdq = np.empty((num_eqn, num_rp))
    apdq = np.empty((num_eqn, num_rp))

    # Basic solve
    wave[0, :, :] = q_r - q_l
    s[0, :] = 0.5 * (q_r[0, :] + q_l[0, :])
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


x = np.array([[1, 4], [2, 5], [3, -2]])
np.min(x, axis=None)
np.min(x, axis=0)
np.min(x, axis=1)


def qsol(x, t, ql, qr):
    """
    The initial and true solution.
    """
    import numpy as np

    dim = x.shape[0]
    q = np.empty(dim)

    if qr < ql:
        s = (qr + ql) / 2
        for i in range(dim):
            if x[i] >= s * t:
                q[i] = qr
            else:
                q[i] = ql
    else:
        if t > 0:
            xr = qr * t
            xl = ql * t
            for i in range(dim):
                if x[i] >= xl and x[i] <= xr:
                    q[i] = x[i] / t
                elif x[i] > xr:
                    q[i] = qr
                elif x[i] < xl:
                    q[i] = ql
        else:
            for i in range(dim):
                if x[i] >= 0:
                    q[i] = qr
                else:
                    q[i] = ql
    return q


def setup(ql, qr):
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

    x = pyclaw.Dimension(-1, 1.0, 200, name="x")
    domain = pyclaw.Domain(x)
    num_eqn = 1
    state = pyclaw.State(domain, num_eqn)
    state.problem_data["efix"] = True

    xc = domain.grid.x.centers

    state.q[0, :] = qsol(xc, 0, ql, qr)

    claw = pyclaw.Controller()
    claw.solution = pyclaw.Solution(state, domain)
    claw.solver = solver
    claw.outdir = "./_output"
    claw.output_style = 1
    claw.tfinal = 2.0
    claw.num_output_times = 20
    claw.keep_copy = True

    return claw


claw = setup(2, 0)
claw.run()
plt.rcParams["text.usetex"] = True
index = 3
frame = claw.frames[index]
dt = claw.tfinal / claw.num_output_times
t = dt * index
x = frame.state.grid.c_centers
x = x[0]
true = qsol(x, t, 2, 0)
fig, ax = plt.subplots(figsize=(3, 3))
w = frame.q[0, :]

ax.plot(x, w, label="Clawpack sol.")
ax.plot(x, true, ":", label="exact solution")
ax.legend(loc="lower left")
ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$q$")
plt.text(-1, 1.5, "(a)")
plt.savefig("ShockBurgerClaw.pdf", bbox_inches="tight")
