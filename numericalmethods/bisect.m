% Programa 1.1 Método de la bisección
% Calcula la solución aproximada de f(x) = 0.
% Entrada: manejador de la función f; a,b tales que f(a)*f(b)<0,
%          y la tolerancia tol
% Salida: Solución aproximada xc

function xc = bisect(f, a, b, tol)

    if sign(f(a)) * sign(f(b)) >= 0
        error('¡f(a)f(b) < 0 no es satisfecho!'); % cesa la ejecución
    end

    fa = f(a);
    fb = f(b);

    while (b - a) / 2 > tol
        c = (a + b) / 2;
        fc = f(c);

        if fc == 0; % c es una solución, listo
            break
        end

        if sign(fc) * sign(fa) < 0; % a y c forman el nuevo intervalo
            b = c;
            fb = fc;
        else % c y b forman el nuevo intervalo
            a = c;
            fa = fc;
        end

    end

    xc = (a + b) / 2; % el nuevo punto medio es la mejor estimación
end
