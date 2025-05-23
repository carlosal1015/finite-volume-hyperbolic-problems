% Programa 6.1 Método de Euler para resolver problemas de valor inicial
% Use con ydot.m para evaluar el lado derecho de la ecuación diferencial
% Entrada: intervalo inter, valor inicial y0, número de pasos n
% Salida: Pasos de tiempo t, solución y
% Ejemplo de uso: euler1([0 1],1,10);
function [t, y] = euler1(inter, y0, n)
    t(1) = inter(1);
    y(1) = y0;
    h = (inter(2) - inter(1)) / n;

    for i = 1:n
        t(i + 1) = t(i) + h;
        y(i + 1) = eulerstep(t(i), y(i), h);
    end

    plot(t, y)
end
