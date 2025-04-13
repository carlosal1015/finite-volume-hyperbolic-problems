function z = ab2step(t, i, y, f, h)
    %one step of the Adams-Bashforth 2-step method
    z = y(i, :) + h * (3 * f(i, :) / 2 - f(i - 1, :) / 2);

end