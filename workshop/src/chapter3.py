#!/usr/bin/env python3

from clawpack.pyclaw import ClawSolver1D
from clawpack.riemann import acoustics_1D

solver = ClawSolver1D(acoustics_1D)
solver.num_waves = 1
solver.num_eqn = 1
solver.kernel_language = "Python"
