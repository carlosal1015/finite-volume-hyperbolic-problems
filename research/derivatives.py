#!/usr/bin/env python

from sympy.abc import theta, epsilon, m, q, alpha
from sympy import exp
from sympy.printing import pprint
from sympy import Derivative as D

f = m * (theta) / (1 - q * theta) * exp(epsilon / (theta + alpha))
pprint(f)
pprint(D(f, theta).doit()) # Primera derivada
pprint(D(f, theta, 2).doit()) # Segunda derivada
