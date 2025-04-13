#!/usr/bin/env -S octave -qf

x0 = [0 2 3];
y0 = [1 2 4];
c = newtdd(x0, y0, 3);
x = 0:.01:4;
y = nest(2, c, x, x0);
figure('visible', 'off');
plot(x0, y0, 'o', x, y);
saveas(gcf, "interpolation.pdf", 'pdfcrop')

clickinterp