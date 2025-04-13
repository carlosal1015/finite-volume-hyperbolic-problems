function z = weaklystable2step(t, i, y, f, h)
    %one step of a weakly-stable 2-step method
    z = y(i - 1, :) + h * 2 * f(i, :);

end