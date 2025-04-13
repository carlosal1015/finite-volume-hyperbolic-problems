% Programa 6.8 Adams-Bashforth-Moulton segundo-orden p-c
% Entrada: Intervalo de tiempo inter,
%          ic=[y0] condición inicial
%          número de pasos n, número de multipasos s para el método explícito
% Salida: pasos de tiempo t, solución y
% Llama a métodos multipaso como ab2step.m y am1step.m
% Ejemplo de uso: [t,y]=predcorr([0 1],1,20,2)
function [t, y] = predcorr(inter, ic, n, s)
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
        y(i + 1, :) = ab2step(t(i), i, y, f, h); % predict
        f(i + 1, :) = ydot(t(i + 1), y(i + 1, :));
        y(i + 1, :) = am1step(t(i), i, y, f, h); % correct
    end

    plot(t, y)

end