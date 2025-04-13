function y = trapstep(t, x, h)
    %one step of the Trapezoid Method from section 6.2
    z1 = ydot(t, x);
    g = x + h * z1;
    z2 = ydot(t + h, g);
    y = x + h * (z1 + z2) / 2;

end
