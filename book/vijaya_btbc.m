function [wn] = vijaya_btbc(wa, dtdx, m)
    %
    % Vijayasundaram flux splitting
    % for the Burgers equation
    %
    wam = zeros(1, m + 1); % w_(j+1)
    wan = zeros(1, m + 1); % w_(j-1)
    % a=0.5*wa
    am = zeros(1, m + 1); % a+(0.25(w_j+w_(j+1)))
    amn = zeros(1, m + 1); % a+(0.25(w_j+w_(j-1)))
    an = zeros(1, m + 1); % a-(0.25(w_j+w_(j+1)))
    ann = zeros(1, m + 1); % a-(0.25(w_j+w_(j-1)))
    phim = zeros(1, m + 1); % phi(w_j,w_(j+1))
    phin = zeros(1, m + 1); % phi(w_(j-1),w_j)
    %
    wam(1:m) = wa(2:m + 1);
    % Transmissive boundary conditions
    wam(m + 1) = wa(m);
    %
    wan(2:m + 1) = wa(1:m);
    % Transmissive boundary conditions
    wan(1) = wa(2);
    %
    for i = 1:m + 1
        am(i) = max(0.25 * (wa(i) + wam(i)), 0);
        an(i) = min(0.25 * (wa(i) + wam(i)), 0);
    end

    %
    amn(2:m + 1) = am(1:m);
    amn(1) = am(1);
    %
    ann(2:m + 1) = an(2:m + 1);
    anm(m + 1) = an(m + 1);
    %
    % Numerical flux
    %
    phim(1:m + 1) = am(1:m + 1) .* wa(1:m + 1) + an(1:m + 1) .* wam(1:m + 1);
    phin(1:m + 1) = amn(1:m + 1) .* wan(1:m + 1) + ann(1:m + 1) .* wa(1:m + 1);
    %
    wn(1:m + 1) = wa(1:m + 1) - dtdx * (phim(1:m + 1) - phin(1:m + 1));
end
