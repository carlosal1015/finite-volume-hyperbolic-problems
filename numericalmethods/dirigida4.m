for j = 1:n - 1

    if abs(a(j, j)) < eps;
        error('zero pivot encountered');
    end

    for i = j + 1:n
        mult = a(i, j) / a(j, j);

        for k = j + 1:n
            a(i, k) = a(i, k) - mult * a(j, k);
        end

        b(i) = b(i) - mult * b(j);
    end

end

for i = n:-1:1

    for j = i + 1:n
        b(i) = b(i) - a(i, j) * x(j);
    end

    x(i) = b(i) / a(i, i);
end

A = [1 1; 1.0001 1];
b = [2; 2.0001];
xa = A \ b

n = 6;
H = hilb(n);
cond(H, inf)

b = H * ones(n, 1);
xa = H \ b

n = 10;
H = hilb(n);
cond(H, inf)
b = H * ones(n, 1);
xa = H \ b

A = [2 1 5; 4 4 -4; 1 3 1];
[L, U, P] = lu(A)

A = diag(sqrt(1:n)) + diag(cos(1:(n - 10)), 10) + diag(cos(1:(n - 10)), -10)

for j = 1:n - 1
    eliminar columna j
end

for j = 1:n - 1

    for i = j + 1:n
        eliminar la entrada a(i, j)
    end

end
