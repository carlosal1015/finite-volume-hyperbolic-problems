% Programa 3.1 Método de interpolación de diferencias divididas de Newton
% Calcula los coeficientes del polinomio de interpolación.
% Entrada: x e y son vectores que contienen las coordenadas x e y
%          de los n puntos de datos
% Salida: coeficientes c del polinomio de interpolación en forma anidada
% Úselo con nest.m para evaluar el polinomio de interpolación
function c = newtdd(x, y, n)

    for j = 1:n
        v(j, 1) = y(j); % Rellene la columna y del triángulo de Newton
    end

    for i = 2:n; % Para la columna i,

        for j = 1:n + 1 - i; % Rellene la columna de arriba a abajo
            v(j, i) = (v(j + 1, i - 1) - v(j, i - 1)) / (x(j + i - 1) - x(j));
        end

    end

    for i = 1:n
        c(i) = v(1, i); % Leer a lo largo de la parte superior del triángulo
    end % para los coeficientes de salida

end
