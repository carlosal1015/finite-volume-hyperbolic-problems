using OffsetArrays
"""
MVF. Método descentrado.
Dominio espacial : [a,b] intervalo -> celdas: c_1,c_2,...,
c_nx
xi : array de nx valores entre a y b espaciados
uniformemente
ci : velocidad de propagación en cada celda 1,...,nx
v0 : array de valores iniciales [v_1^0, v_2^0..., v_{nx}^0]
dx, dt : paso en espacio y paso en tiempo
nt : número de iteraciones de tiempo
g : array de valores de la densidad de las glı́as en cada
celda e instante de tiempo
p : coeficiente de la combinación convexa
c_0, c_nx+1: celdas fantasmas
Condición de contorno: v_0^n = v_1^n para cada instante de
tiempo t_n
v_nx+1^n = v_nx^n para cada instante de tiempo t_n
"""
function advection_neuroblastos_1D_FVM(xi, dt, nt, v0, ci, g, p)
    nx = length(v0)
    dx = xi[2] - xi[1]
    v = OffsetArray(zeros((nx + 2, nt + 1)), 0:nx+1, 0:nt)
    v[1:nx, 0] = v0
    r = dt / dx
    for n = 0:nt-1
        v[0, n] = v[1, n] # (c. c. Neumann homog)
        v[nx+1, n] = v[nx, n] # Idem
        for i = 1:nx
            if ci[i] >= 0
                t1 = r * p * (ci[i] * v[i, n] - ci[i-1] * v[i-1, n])
                if i == 1
                    v[i, n+1] = v[i, n] - t1 + r * (1 - p) * ((g[i, n] - v[i, n]) * v[i, n] + (g[
                                                   i, n] - v[i, n]) * v[i-1, n])
                else
                    v[i, n+1] = v[i, n] - t1 + r * (1 - p) * ((g[i, n] - v[i, n]) * v[i, n] + (g[
                                                   i-1, n] - v[i-1, n]) * v[i-1, n])
                end
            else
                v[i, n+1] = v[i, n] - r * (ci[i+1] * v[i+1, n] - ci[i] * v[i, n])
            end
        end
    end
    return v[1:nx, :]
end