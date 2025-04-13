function z = unstable2step(t, i, y, f, h)
    %one step of an unstable 2-step method
    z=-y(i, :) + 2 * y(i - 1, :) + h * (5 * f(i, :) / 2 + f(i - 1, :) / 2);

end