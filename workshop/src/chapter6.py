from clawpack import riemann
from clawpack import pyclaw
import numpy as np
import matplotlib.pyplot as plt

claw = pyclaw.Controller()  # Creation of the controller
claw.tfinal = 1.0  # Final time
claw.keep_copy = True  # Keep solution data in memory for plotting
claw.output_format = None  # Don’t write solution data to file
claw.num_output_times = 50  # Write 50 output frames

# Riemann solver
# Here we use the one provided in Clawpack
# We could have also used SharpClawSolver1D
riemann_solver = riemann.acoustics_1D
claw.solver = pyclaw.ClawSolver1D(riemann_solver)

# Boundary conditions
claw.solver.all_bcs = pyclaw.BC.periodic
# claw.solver.bc.lower[0] = pyclaw.BC.wall
# claw.solver.bc.upper[0] = pyclaw.BC.wall

domain = pyclaw.Domain((0.0,), (1.0,), (100,))
claw.solution = pyclaw.Solution(claw.solver.num_eqn, domain)
x = domain.grid.x.centers
beta = 100
gamma = 5
x0 = 0.75
claw.solution.q[0, :] = np.exp(-beta * (x - x0) ** 2) * np.cos(gamma * (x - x0))
claw.solution.q[1, :] = 0.0

density = 1.0
bulk_modulus = 1.0
impedance = np.sqrt(density * bulk_modulus)
sound_speed = np.sqrt(density / bulk_modulus)

claw.solution.state.problem_data = {
    "rho": density,
    "bulk": bulk_modulus,
    "zz": np.sqrt(density * bulk_modulus),
    "cc": np.sqrt(bulk_modulus / density),
}

claw.solver.dt_initial = 1.0e-99
status = claw.run()

pressure = claw.frames[50].q[0, :]
plt.rcParams["text.usetex"] = True
# plt.plot(x,pressure,’-’)
fig, ax = plt.subplots(figsize=(6, 4), tight_layout=True)
ax.plot(x, pressure)

ax.set_xlabel(r"$x$ (m)", fontsize=16)
ax.set_ylabel(r"$p$ (Pa)", fontsize=16)
plt.savefig("solution50.pdf")

from clawpack.visclaw import ianimate

ianimate.ianimate(claw)

from matplotlib import animation
from IPython.display import HTML

fig = plt.figure(figsize=(10, 6))
ax = plt.axes(xlim=(0, 1), ylim=(-0.8, 1.2))

frame = claw.frames[0]
pressure = frame.q[0, :]
(line1,) = ax.plot([], [], lw=2)
(line2,) = ax.plot([], [], lw=2)
plt.legend([r"$p$", r"$u$"])


def fplot(frame_number):
    frame = claw.frames[frame_number]
    pressure = frame.q[0, :]
    velocity = frame.q[1, :]
    line1.set_data(x, pressure)
    line2.set_data(x, velocity)

    return (line1,)


anim = animation.FuncAnimation(
    fig, fplot, frames=len(claw.frames), interval=30, repeat=False
)
plt.close()
HTML(anim.to_jshtml())
