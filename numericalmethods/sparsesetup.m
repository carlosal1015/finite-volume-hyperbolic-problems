% Programa 2.1 Configuración de matriz dispersa
% Entrada: n = tamaño del sistema
% Salidas: matriz dispersa a, lado derecho b
function [a, b] = sparsesetup(n)
    e = ones(n, 1);
    n2 = n / 2;
    a = spdiags([-e 3 * e -e], -1:1, n, n); % Entradas de a
    c = spdiags([e / 2], 0, n, n);
    c = fliplr(c);
    a = a + c;
    % Fije 2 entradas
    a(n2 + 1, n2) = -1;
    a(n2, n2 + 1) = -1;
    b = zeros(n, 1);
    % Entradas del lado derecho b
    b(1) = 2.5;
    b(n) = 2.5;
    b(2:n - 1) = 1.5;
    b(n2:n2 + 1) = 1;
end
