% Programa 0.1 Multiplicación anidada
% Evalúa un polinomio a partir de una forma anidada utilizando el método de Horner
% Entrada: grado d del polinomio,
%          arreglo c de d + 1 coeficientes (primero el término constante),
%          coordenada x en la que se va a evaluar, y
%          arreglo de d puntos base b, si es necesario
% Salida: valor y del polinomio en x

function y = nest(d, c, x, b)

    if nargin < 4
        b = zeros(d, 1);
    end

    y = c(d + 1);

    for i = d:-1:1
        y = y .* (x - b(i)) + c(i);
    end

end
