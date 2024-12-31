function [wn] = upwind_tpbc(wa, cflp, cfln, m)
    %
    % Upwind scheme for the transport equation
    %
    wam = zeros(1, m + 1);
    wan = zeros(1, m + 1);
    %
    wam(1:m) = wa(2:m + 1);
    % Periodic boundary conditions
    wam(m + 1) = wam(1);
    %
    wan(2:m + 1) = wa(1:m);
    % Periodic boundary conditions
    wan(1) = wan(m + 1);
    %
    wn(1:m + 1) = wa(1:m + 1) - cflp * (wa(1:m + 1) - wan(1:m + 1))- ...
        cfln * (wam(1:m + 1) - wa(1:m + 1));
end
