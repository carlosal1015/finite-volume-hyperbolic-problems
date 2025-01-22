% Programa 3.7 Programa de dibujo a mano alzada que utiliza splines de Bézier
% Haga clic en la ventana de la figura para localizar el primer punto y haga clic
% tres veces más para especificar 2 puntos de control y el siguiente
% punto spline. Continúa con grupos de 3 puntos para sumar más
% a la curva. Presione Enter para finalizar el programa.

function bezierdraw
    plot([-1 1], [0, 0], 'k', [0 0], [-1 1], 'k'); hold on
    t = 0:.02:1;
    [x, y] = ginput(1); % Consiga un clic del ratón

    while (0 == 0)
        [xnew, ynew] = ginput(3); % Consiga tres clics del mouse

        if length(xnew) < 3
            break; % si se presiona la tecla de retorno, finalizar
        end

        x = [x; xnew]; y = [y; ynew]; % Graficar puntos spline y puntos de control
        plot([x(1) x(2)], [y(1) y(2)], 'r:', x(2), y(2), 'rs');
        plot([x(3) x(4)], [y(3) y(4)], 'r:', x(3), y(3), 'rs');
        plot(x(1), y(1), 'bo', x(4), y(4), 'bo');
        bx = 3 * (x(2) - x(1)); by = 3 * (y(2) - y(1)); % ecuaciones spline ...
        cx = 3 * (x(3) - x(2)) - bx; cy = 3 * (y(3) - y(2)) - by;
        dx = x(4) - x(1) - bx - cx; dy = y(4) - y(1) - by - cy;
        xp = x(1) + t .* (bx + t .* (cx + t * dx)); % Método de Horner
        yp = y(1) + t .* (by + t .* (cy + t * dy));
        plot(xp, yp, 'b'); % plot spline curve
        x = x(4); y = y(4); % promote last to first and repeat
    end

    hold off
end
