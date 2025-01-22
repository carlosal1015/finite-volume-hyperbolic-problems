% Programa 2.2 Método de Jacobi
% Entradas: matriz dispersa o llena a, lado derecho b,
%           número de iteraciones de Jacobi, k
% Salida: solución x
function x = jacobi(a, b, k)
    n = length(b); % find n
    d = diag(a); % extract diagonal of a
    r = a - diag(d); % r is the remainder
    x = zeros(n, 1); % initialize vector x

    for j = 1:k% loop for Jacobi iteration
        x = (b - r * x) ./ d;
    end % End of Jacobi iteration loop

end
