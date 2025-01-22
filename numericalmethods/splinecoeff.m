% Programa 3.5 Cálculo de coeficientes de spline
% Calcula los coeficientes del spline cúbico
% Entrada: Vectores x, y de puntos de datos
% más dos datos extra opcionales v1, vn
% Salida: matriz de coeficientes b1,c1,d1;b2,c2,d2;...
function coeff = splinecoeff(x, y)
    n = length(x); v1 = 0; vn = 0;
    A = zeros(n, n); % La matriz A es nxn
    r = zeros(n, 1);

    for i = 1:n - 1
        % definir los deltas
        dx(i) = x(i + 1) - x(i); dy(i) = y(i + 1) - y(i);
    end

    for i = 2:n - 1
        % cargar la matriz A
        A(i, i - 1:i + 1) = [dx(i - 1) 2 * (dx(i - 1) + dx(i)) dx(i)];
        r(i) = 3 * (dy(i) / dx(i) - dy(i - 1) / dx(i - 1)); % right-hand side
    end

    % Establecer condiciones de punto final
    % Utilice sólo uno de los siguientes 5 pares:
    A(1, 1) = 1; % natural spline conditions
    A(n, n) = 1;
    %A(1,1)=2;r(1)=v1; % condiciones de ajuste de curvatura
    %A(n,n)=2;r(n)=vn;
    %A(1,1:2)=[2*dx(1) dx(1)];r(1)=3*(dy(1)/dx(1)-v1); %clamped
    %A(n,n-1:n)=[dx(n-1) 2*dx(n-1)];r(n)=3*(vn-dy(n-1)/dx(n-1));
    %A(1,1:2)=[1 -1]; % condiciones de término parabólico, para n>=3
    %A(n,n-1:n)=[1 -1];
    %A(1,1:3)=[dx(2) -(dx(1)+dx(2)) dx(1)]; % no es un lazo, for n>=4
    %A(n,n-2:n)=[dx(n-1) -(dx(n-2)+dx(n-1)) dx(n-2)];
    coeff = zeros(n, 3);
    coeff(:, 2) = A \ r; % resuelve para los coeficientes c

    for i = 1:n - 1; % resuelve para b y d
        coeff(i, 3) = (coeff(i + 1, 2) - coeff(i, 2)) / (3 * dx(i));
        coeff(i, 1) = dy(i) / dx(i) - dx(i) * (2 * coeff(i, 2) + coeff(i + 1, 2)) / 3;
    end

    coeff = coeff(1:n - 1, 1:3);
end
