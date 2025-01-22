% Programa 3.2 Programa de interpolación polinomial
% Haga clic en la ventana de la figura de Octave / MATLAB para localizar el punto de datos.
% Continúa, para sumar más puntos.
% Presione Enter para finalizar el programa.

function clickinterp
    xl=-3; xr = 3; yb=-3; yt = 3;
    plot([xl xr], [0 0], 'k', [0 0], [yb yt], 'k'); grid on;
    xlist = []; ylist = [];
    k = 0; % initialize counter k

    while (0 == 0)
        [xnew, ynew] = ginput(1); % get mouse click

        if length (xnew) < 1
            break; % if return pressed, terminate
        end

        k = k + 1; % k counts clicks
        xlist(k) = xnew; ylist(k) = ynew; % add new point to the list
        c = newtdd(xlist, ylist, k); % get interpolation coeffs
        x = xl:.01:xr; % define x coordinates of curve
        y = nest(k - 1, c, x, xlist); % get y coordinates of curve
        plot(xlist, ylist, 'o', x, y, [xl xr], [0, 0], 'k', [0 0], [yb yt], 'k');
        axis([xl xr yb yt]); grid on;
    end

end
