#!/usr/bin/env julia

# https://juliaarrays.github.io/OffsetArrays.jl/stable
using Pkg
Pkg.activate(".")

using OffsetArrays
using Plots

"""
Ecuación de transporte
"""

function advection(xi, nx, dt, nt, c, u0)
    dx = xi[2] - xi[1]
    u = OffsetArrays(zeros(nx + 1, nt + 1), 0:nx, 0:nt)
    u[1:nx, 0] = u0
    r = c * dt / dx
    for n = 0:nt-1
        u[0, n] = u[1, n]
        for i = 1:nx
            u[i, n+1] = u[i, n] - r * (u[i, n] - u[i-1, n])
        end
    end
    return u[1:nx, :]
end

x = range(0, 10, length=100)
y = sin.(x)
p = plot(x, y)
savefig(p, "myplot.pdf")
