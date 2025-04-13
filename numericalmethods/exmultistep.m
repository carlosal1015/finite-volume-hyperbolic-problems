% Programa 6.7 Método multipaso
% Entradas: El intervalo de tiempo inter, ic=[y0] condición inicial, número de pasos n,
%           s=número de multipasos, por ejemplo 2 para el método de 2 pasos
% Salida: pasos de tiempo t, solución y
% Calls a multistep method such as ab2step.m
% Example usage: [t,y]=exmultistep([0,1],1,20,2)
function [t, y] = exmultistep(inter, ic, n, s)
    h = (inter(2) - inter(1)) / n;
    % Start-up phase
    y(1, :) = ic; t(1) = inter(1);

    for i = 1:s - 1
        % start-up phase, using one-step method
        t(i + 1) = t(i) + h;
        y(i + 1, :) = trapstep(t(i), y(i, :), h);
        f(i, :) = ydot(t(i), y(i, :));
    end

    for i = s:n
        % multistep method loop
        t(i + 1) = t(i) + h;
        f(i, :) = ydot(t(i), y(i, :));
        y(i + 1, :) = ab2step(t(i), i, y, f, h);
    end

    plot(t, y)
end