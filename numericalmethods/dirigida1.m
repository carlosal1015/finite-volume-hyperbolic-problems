#!/usr/bin/env -S octave -qf

d = 4;
c = [-1 5 -3 3 2];
x = 1/2;
nest(d, c, x);

d = 4;
c = [-1 5 -3 3 2];
x = [-2 -1 0 1 2];
nest(d, c, x);

d = 3;
c = [1 1/2 1/2 -1/2];
x = 1;
b = [0 2 3];
nest(d, c, x, b);

f = @(x) x^3 + x - 1;
xc = bisect(f, 0, 1, 0.00005);

g = @(x) cos(x);

xc = fpi(g, 0, 10);
format long
fzero(@wilkpoly, 16);

%f = @(x) x^3 + x - 1;
%fzero(f, [0 1], optimset('Display', 'iter'));
%fzero(f, 1);
n = 6;
H = hilb(n);
cond(H, inf)

b = H * ones(n, 1);
xa = H \ b

n = 10;
H = hilb(n);
cond(H, inf)

b = H * ones(n, 1);
xa = H \ b;
full(sparsesetup(12))
%spy(sparsesetup(12))