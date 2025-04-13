function y = eulerstep(t, y, h)
    % Método de Euler de un paso
    % Entrada: tiempo actual t, valor actual y, tamaño de paso h
    % Salida: Valor aproximado de la solución en el tiempo t+h
    y = y + h * ydot(t, y);
end
