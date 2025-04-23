#!/usr/bin/env python

"""Fidel Jara"""

from sympy.abc import x, t, xi, psi, beta, c, K
from sympy import Derivative as D
from sympy.printing import pprint
from sympy.core import Eq, symbols, Function
from sympy.solvers import solve

# Unknown functions
theta = Function("theta")(x, t)
So = Function("S_o")(x, t)
Sy = Function("S_y")(x, t)

# Model parameters
a1 = symbols("a_1")
a2 = symbols("a_2")
a3 = symbols("a_3")
b1 = symbols("b_1")
b2 = symbols("b_2")
b3 = symbols("b_3")

eq6 = Eq(
    lhs=D(theta, t) + a1 * D(So * theta, x),
    rhs=b1 * So * Sy * psi - beta * theta,
)
eq7 = Eq(
    lhs=D(Sy, t) + a2 * D(Sy, x),
    rhs=-b2 * So * Sy * psi,
)
eq8 = Eq(
    lhs=D(So, t) + a3 * D(So, x),
    rhs=-b3 * So * Sy * psi,
)

print("PDE system (x, t)")
print()
pprint(eq6)
print()
pprint(eq7)
print()
pprint(eq8)

travelling_wave_subs = {
    D(theta, x): D(theta, xi),
    D(theta, t): -c * D(theta, xi),
    D(So, x): D(So, xi),
    D(So, t): -c * D(So, xi),
    D(Sy, x): D(Sy, xi),
    D(Sy, t): -c * D(Sy, xi),
}

eq15 = eq6.subs(travelling_wave_subs)
eq16 = eq7.subs(travelling_wave_subs)
eq17 = eq8.subs(travelling_wave_subs)

print()
print("PDE system (ξ, t)")
print()
pprint(eq15)
print()
pprint(eq16)
print()
pprint(eq17)

# Boundary conditions
SoL = symbols("S^{L}_{o}")
SoR = symbols("S^{R}_{o}")
SyL = symbols("S^{L}_{y}")
SyR = symbols("S^{R}_{y}")

eq18 = Eq(
    lhs=b2 * (c - a3) * So - b3 * (c - a2) * Sy,
    rhs=K,
)
eq19 = Eq(
    lhs=eq18.lhs.subs({So: SoL, Sy: SyL}),
    rhs=eq18.lhs.subs({So: SoR, Sy: SyR}),
)
eq20 = Eq(
    lhs=c,
    rhs=solve(eq19.subs({SoL: 0, SyR: 0}), c)[0],
)
eq21 = Eq(
    lhs=SyL,
    rhs=solve(eq19.subs({SoL: 0, SyR: 0}), SyL)[0],
)
eq22 = Eq(
    lhs=Sy,
    rhs=solve(Eq(lhs=eq18.lhs, rhs=eq19.lhs.subs({SoL: 0})), Sy)[0],
)
eq23 = Eq(
    lhs=D(So, xi),
    rhs=solve(eq17, D(So, xi))[0],
)

eq26 = Eq(
    lhs=D(theta, xi),
    rhs=solve(
        Eq(
            lhs=b2 * eq15.lhs + b1 * eq16.lhs,
            rhs=b2 * eq15.rhs + b1 * eq16.rhs,
        ),
        D(theta, xi),
    )[0],
)

eq35 = Eq(
    lhs=Sy,
    rhs=0,
)
eq36 = Eq(
    lhs=D(theta, xi),
    rhs=0,
)
eq37 = Eq(
    lhs=D(So, xi),
    rhs=0,
)

print()
print("Equation 18")
pprint(eq18)
print()
print("Equation 19")
pprint(eq19)
print()
print("Equation 20")
pprint(eq20)
print()
print("Equation 21")
pprint(eq21)
print()
print("Equation 22")
pprint(eq22)
print()
print("Equation 23")
pprint(eq23)
print()
print("Equation 26")
pprint(eq26)
print()
print("Equation 35")
pprint(eq35)
print()
print("Equation 36")
pprint(eq36)
print()
print("Equation 37")
pprint(eq37)
print()
