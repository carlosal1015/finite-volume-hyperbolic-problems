function z = am1step(t, i, y, f, h)
    %one step of the Adams-Moulton 1-step method
    z = y(i, :) + h * (f(i + 1, :) + f(i, :)) / 2;

end
