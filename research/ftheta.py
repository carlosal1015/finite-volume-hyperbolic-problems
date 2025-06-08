from sympy.abc import m, theta, n, p, q
from sympy.functions import exp
from sympy import Derivative as D
from sympy import Eq
from sympy.printing import pprint
from sympy import solve

f = m * (theta) / (1 - q * theta) * exp(n / (theta + p))
equation = Eq(lhs=D(f, theta).doit(), rhs=0)
pprint(equation.lhs.factor(exp(n / (theta + p))))
soluciones = solve(equation, theta)
pprint(soluciones)
m_value = 1.8510565830976324e-11
n_value = 151361719.0281453
p_value = 1
q_value = 0.0019549215758434854

pprint(
    soluciones[0].subs(
        {
            m: m_value,
            n: n_value,
            p: p_value,
            q: q_value,
        }
    )
)
pprint(
    soluciones[1].subs(
        {
            m: m_value,
            n: n_value,
            p: p_value,
            q: q_value,
        }
    )
)
