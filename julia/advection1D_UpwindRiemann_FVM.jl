using OffsetArrays
"""
Ecuación de transporte. MVF. Método descentrado con flujo
aguas arriba.
Dominio espacial : [a,b] intervalo -> celdas: c_1,c_2,...,
c_nx
xi : array de nx valores entre a y b espaciados
uniformemente
c : velocidad de propagación
u0: array de valores iniciales [u_1^0, u_2^0..., u_{nx}^0]
dx, dt: paso en espacio y paso en tiempo
nt: número de iteraciones de tiempo
c_0: celda fantasma
Condición de contorno: u_0^n = u_1^n para cada instante de
tiempo t_n
"""
function advection1D_UpwindRiemann_FVM(xi, nx, dt, nt, c, u0)
    dx = xi[2] - xi[1]
    u = OffsetArray(zeros((nx + 1, nt + 1)), 0:nx, 0:nt)
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