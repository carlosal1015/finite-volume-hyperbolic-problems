function [wn] = vijaya_hr_btbc(wa, dtdx, m, epshr)
    %
    % Vijayasundaram flux splitting
    %   for the Burgers equation
    %
    % Harten regularization
    %
    wam = zeros(1, m + 1); % w_(j+1)
    wan = zeros(1, m + 1); % w_(j-1)
    %
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
    % Harten regularization
    %
    epsr = epshr * ones(1, m + 1);
    %
    ablanm = 0.25 * abs(wa(1:m + 1) + wam(1:m + 1));
    regm = ablanm + 0.5 * (1 + sign(epsr - ablanm)) .* ...
        ((ablanm.^2 + epsr.^2) ./ (2 * epsr) - ablanm);
    ablann = 0.25 * abs(wa(1:m + 1) + wan(1:m + 1));
    regn = ablann + 0.5 * (1 + sign(epsr - ablann)) .* ...
        ((ablann.^2 + epsr.^2) ./ (2 * epsr) - ablann);
    %
    am(1:m + 1) = 0.5 * (0.25 .* (wa(1:m + 1) + wam(1:m + 1)) + regm(1:m + 1));
    amn(1:m + 1) = 0.5 * (0.25 .* (wa(1:m + 1) + wan(1:m + 1)) + regn(1:m + 1));
    an(1:m + 1) = 0.5 * (0.25 .* (wa(1:m + 1) + wam(1:m + 1)) - regm(1:m + 1));
    ann(1:m + 1) = 0.5 * (0.25 .* (wa(1:m + 1) + wan(1:m + 1)) - regn(1:m + 1));
    %
    % Numerical flux
    %
    phim(1:m + 1) = am(1:m + 1) .* wa(1:m + 1) + an(1:m + 1) .* wam(1:m + 1);
    phin(1:m + 1) = amn(1:m + 1) .* wan(1:m + 1) + ann(1:m + 1) .* wa(1:m + 1);
    %
    wn(1:m + 1) = wa(1:m + 1) - dtdx * (phim(1:m + 1) - phin(1:m + 1));
end
