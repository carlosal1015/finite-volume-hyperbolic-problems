% Programa 1.2 Iteración de punto fijo
% Calcula la solución aproximada de g(x) = x.
% Entrada: manejador de función g, estimación inicial x0,
%          número de pasos de iteración k
% Salida: Solución aproximada xc

function xc = fpi(g, x0, k)
    x(1) = x0;

    for i = 1:k
        x(i + 1) = g(x(i));
    end

    xc = x(k + 1);
end
