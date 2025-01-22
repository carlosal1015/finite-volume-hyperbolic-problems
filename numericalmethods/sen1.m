% Programa 3.3 Construyendo una calculadora del seno, intento #1
% Aproxima la curva del seno con un polinomio de grado 3
% (Precaución: no utilizar para construir puentes,
% al menos hasta que hayamos discutido la precisión).
% Entrada: x
% Salida: Aproximación para sen(x)
function y = sen1(x)
    % Primero calcule el polinomio de interpolación y
    % guarda los coeficientes
    b = pi * (0:3) / 6; yb = sin(b); % b contiene puntos base
    c = newtdd(b, yb, 4);
    % Para cada entrada x, mueva x al dominio fundamental y evalúe
    % el polinomio interpolador
    s = 1;
    % Corrige el signo de seno
    x1 = mod(x, 2 * pi);

    if x1 > pi
        x1 = 2 * pi - x1;
        s = -1;
    end

    if x1 > pi / 2
        x1 = pi - x1;
    end

    y = s * nest(3, c, x1, b);
end
