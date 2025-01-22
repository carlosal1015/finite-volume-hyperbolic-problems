% Programa 3.4 Construyendo una calculadora del seno, intento #2
% Aproxima la curva del seno con un polinomio de grado 9
% Entrada: x
% Salida: Aproximación de sin(x), correcta hasta 10 decimales
function y = sen2(x)
    % Primero calcule el polinomio de interpolación y
    % guarda los coeficientes
    n = 10;
    b = pi / 4 + (pi / 4) * cos((1:2:2 * n - 1) * pi / (2 * n));
    yb = sin(b);
    % b contiene los puntos base de Chebyshev
    c = newtdd(b, yb, n);
    % Para cada entrada x, mueva x al dominio fundamental y evalúe
    % el polinomio de interpolación
    s = 1; % Corrije el signo de sin
    x1 = mod(x, 2 * pi);

    if x1 > pi
        x1 = 2 * pi - x1;
        s = -1;
    end

    if x1 > pi / 2
        x1 = pi - x1;
    end

    y = s * nest(n - 1, c, x1, b);
end
