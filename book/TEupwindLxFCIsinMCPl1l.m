function TEupwindLxFCIsinMCPl1lm
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %
    %
    Lax Friedrichs and Upwind schemes
    %
    % w +lambda w =0
    %  t         x
    %
    % Domain: [a,b]
    % Initial condition: sin
    %
    % w0(x)=sin(2*pi*)
    %
    % Periodic boundary conditions
    % w(x_1,tn)=w(x_(m+1),tn)
    %
    %
    Exact solution:
    %
    w(x, t) = w0(x - lambda * t)
    %
    % Observed Order of accuracy in space and time L1 Lm
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    clear all
    clc
    disp('Lax Friedrichs and Upwind schemes')
    disp('-------------------------------------------')
    disp('w +lambda w =0')
    disp(' t
    x')
    disp('Domain: [a,b]')
    disp('Periodic boundary conditions')
    disp('Initial condition: sin')
    disp('w0(x)=sin(2*pi*x)')
    disp('Exact solution')
    disp('w(x,t)=w0(x-lambda*t)')
    disp('---------------------------------------------')
    a = 0;
    disp(['Lower end of the interval = ', num2str(a)])
    b = 1;
    disp(['Upper end of the interval = ', num2str(b)])
    lambda = 1;
    disp(['Velocity of propagation =', num2str(lambda)])
    mi = 60
    disp(['Number of nodes mesh M(1)=', num2str(mi)])
    cfl = 0.9;
    disp(['Courant number = ', num2str(cfl)])
    tmax = 1;
    disp(['Time end = ', num2str(tmax)])
    disp('-------------------------------------------')
    %
    clf
    % Mesh definition
    m1vals = [mi mi * 2 mi * 4 mi * 8 mi * 16]'
    ntest = size(m1vals, 1)% Number of meshes

    for jtest = 1:ntest
        m = m1vals(jtest);
        disp(['Number of nodes mesh M(', ...
                num2str(jtest), ')=', num2str(m)])
        deltaxvals(jtest) = (b - a) / (m);
        deltax = deltaxvals(jtest);
        disp(['deltax =', num2str(deltax)])
        x = [a:deltax:b];
        % Plot the initial condition at [a,b]
        %
        w0 = sin(2 * pi * x);
        figure(1)
        plot(x, w0, 'or')
        hold on
        xlabel('x'); ylabel('w(x,0)');
        title('Initial condition');
        %
        % Initialization
        %
        walxf = w0; % Lax Friedrichs
        wau = w0; % Upwind
        we = w0;
        %
        % Deltat from Courant number
        deltatvals(jtest) = cfl * deltax / lambda;
        deltat = deltatvals(jtest);
        disp(['Time step from Courant number =' ...
                , num2str(deltat)])
        mt = tmax / deltat;
        %
        cflp = 0.5 * (lambda + abs(lambda)) * deltat / deltax;
        cfln = 0.5 * (lambda - abs(lambda)) * deltat / deltax;
        %
        for n = 1:mt
            %
            % Lax Friedrichs scheme
            wnlxf = lxf_tpbc(walxf, cfl, m);
            % Upwind scheme
            wnu = upwind_tpbc(wau, cflp, cfln, m);
            %
            %
            % Exact solution
            %
            we = sin(2 * pi * (x - lambda * n * deltat));
            %
            %
            figure(2)
            plot(x, wnlxf, 'xb', x, wnlxf, 'b', x, wnu, '+b', ...
                x, wnu, 'b', x, we, 'or')
            xlabel('x'); ylabel('w(x,t)');
            title(['Lax Friedrichs and Upwind schemes t =' ...
                    , num2str(n * deltat)]);
            % Update
            walxf = wnlxf;
            wau = wnu;
        end

        %
        % Mass conservation
        %
        intw0 = deltax * sum(w0);
        intwnlxf = deltax * sum(wnlxf);
        intwnu = deltax * sum(wnu);
        disp('Test Conservation property =')
        disp(['deltax*sum(w0) =', num2str(intw0)])
        disp(['Lax Friedrichs deltax*sum(wn)=', ...
                num2str(intwnlxf)])
        errorconservation = abs(intw0 - intwnlxf);
        disp(['error=abs(deltax*sum(w0)-deltax*sum(wn))=', ...
                num2str(errorconservation)])
        disp(['Upwind deltax*sum(wn)=', num2str(intwnu)])
        errorconservation = abs(intw0 - intwnu);
        disp(['error=abs(deltax*sum(w0)-deltax*sum(wn))=', ...
                num2str(errorconservation)])
        disp('---------------------------------------------')
        %
        % Error L1
        %
        errorLxFl1(jtest) = deltax * sum(abs(wnlxf - we));
        errorul1(jtest) = deltax * sum(abs(wnu - we));
        %
        % Error L infinity
        %
        errorLxFlm(jtest) = max(abs(wnlxf - we));
        errorulm(jtest) = max(abs(wnu - we));
        %
        coefoxLxFl1(jtest) = errorLxFl1(jtest) ...
            /(deltaxvals(jtest));
        coefotLxFl1(jtest) = errorLxFl1(jtest) ...
            /(deltatvals(jtest));
        %
        coefoxLxFlm(jtest) = errorLxFlm(jtest) ...
            /(deltaxvals(jtest));
        coefotLxFlm(jtest) = errorLxFlm(jtest) ...
            /(deltatvals(jtest));
        %
        coefoxul1(jtest) = errorul1(jtest) ...
            /(deltaxvals(jtest));
        coefotul1(jtest) = errorul1(jtest) ...
            /(deltatvals(jtest));
        %
        coefoxulm(jtest) = errorulm(jtest) ...
            /(deltaxvals(jtest));
        coefotulm(jtest) = errorulm(jtest) ...
            /(deltatvals(jtest));
    end

    %
    disp(['
        Deltax
        errorLxFl1
        coefoxLxFl1 '])
    LxFs = [deltaxvals; errorLxFl1; coefoxLxFl1]'
    disp(['
        Deltat
        errorLxFl1
        coefotLxFl1
        '])
    LxFt = [deltatvals; errorLxFl1; coefotLxFl1]'
    %
    disp(['
        Deltax
        errorLxFlm
        coefoxLxFlm '])
    LxFs = [deltaxvals; errorLxFlm; coefoxLxFlm]'
    disp(['
        Deltat
        errorLxFlm
        coefotLxFlm
        '])
    LxFt = [deltatvals; errorLxFlm; coefotLxFlm]'
    %
    disp(['
        Deltax
        errorul1
        coefoxul1 '])
    Us = [deltaxvals; errorul1; coefoxul1]'
    disp(['
        Deltat
        errorul1
        coefotul1 '])
    Ut = [deltatvals; errorul1; coefotul1]'
    %
    disp(['
        Deltax
        errorulm
        coefoxulm '])
    Us = [deltaxvals; errorulm; coefoxulm]'
    disp(['
        Deltat
        errorulm
        coefotulm '])
    Ut = [deltatvals; errorulm; coefotulm]'
    %
    % Lax-Friedrish
    %
    cerrorLxFl1 = errorLxFl1(1:(ntest - 1)) ./ ...
        errorLxFl1(2:ntest);
    ordenLxFl1 = log(cerrorLxFl1) ./ log(2);
    disp('Observed Order of accuracy in space')
    disp(['Lax-Friedrichs l1=', ...
            num2str(ordenLxFl1)])
    % Linear regresion to obtain the Observed Order
    % of accuracy in space L1
    pxLxFl1 = polyfit(log(deltaxvals), log(errorLxFl1), 1);
    disp('Observed Order of accuracy in space')
    disp('Lax-Friedrichs l1')
    disp('via Linear regresion pxLxFl1(1)=');
    disp(pxLxFl1(1))
    %
    cerrorLxFlm = errorLxFlm(1:(ntest - 1)) ./ ...
        errorLxFlm(2:ntest);
    ordenLxFlm = log(cerrorLxFlm) ./ log(2);
    disp(['Observed Order Lax-Friedrichs linfinity=', ...
            num2str(ordenLxFlm)])
    % Linear regresion to obtain the Observed Order
    % of accuracy in space Lm
    pxLxFlm = polyfit(log(deltaxvals), log(errorLxFlm), 1);
    disp('Observed Order of accuracy in space')
    disp('Lax-Friedrichs linfinity')
    disp('via Linear regresion pxLxFlm(1)=');
    disp(pxLxFlm(1))
    % Representation Linear regresion
    % Order of accuracy in space L1, Lm LxF
    figure(3)
    rgxLxFl1 = @(x) exp(pxLxFl1(2)) * x.ˆpxLxFl1(1);
    rgxLxFlm = @(x) exp(pxLxFlm(2)) * x.ˆpxLxFlm(1);
    loglog(deltaxvals, rgxLxFl1(deltaxvals), 'r', ...
        deltaxvals, errorLxFl1, 'x' ...
        , deltaxvals, rgxLxFlm(deltaxvals), 'r' ...
        , deltaxvals, errorLxFlm, 'o')
    title('Linear regresion Lax-Friedrichs l1,linfinity')
    legend(sprintf('Linear regresion, slope=%0.3g', ...
        pxLxFl1(1)), 'Error l1 log-log', ...
        sprintf('Linear regresion, slope=%0.3g', ...
        pxLxFlm(1)), 'Error L infinity log-log')
    %
    % Upwind scheme
    %
    cerrorul1 = errorul1(1:(ntest - 1)) ./ errorul1(2:ntest);
    ordenul1 = log(cerrorul1) ./ log(2);
    disp('Observed Order of accuracy in space')
    disp(['Upwind scheme l1=', ...
            num2str(ordenul1)])
    % Linear regresion to obtain the Observed Order
    % of accuracy in space L1
    pxul1 = polyfit(log(deltaxvals), log(errorul1), 1);
    disp('Observed Order of accuracy in space')
    disp('Upwind scheme l1')
    disp('via Linear regresion pxul1(1)=');
    disp(pxul1(1))
    %
    cerrorulm = errorulm(1:(ntest - 1)) ./ ...
        errorulm(2:ntest);
    ordenulm = log(cerrorulm) ./ log(2);
    disp(['Observed Order Upwind scheme linfinity=', ...
            num2str(ordenulm)])
    % Linear regresion to obtain the Observed Order
    % of accuracy in space L1
    pxulm = polyfit(log(deltaxvals), log(errorulm), 1);
    disp('Observed Order of accuracy in space')
    disp('Upwind scheme linfinity')
    disp('via Linear regresion pxulm(1)=');
    disp(pxulm(1))
    % Representation Linear regresion Order
    % of accuracy in space L1, linfinity Upwind
    figure(4)
    rgxul1 = @(x) exp(pxul1(2)) * x.ˆpxul1(1);
    rgxulm = @(x) exp(pxulm(2)) * x.ˆpxulm(1);
    loglog(deltaxvals, rgxul1(deltaxvals), 'r', ...
        deltaxvals, errorul1, 'x', ...
        deltaxvals, rgxulm(deltaxvals), 'r', ...
        deltaxvals, errorulm, 'o')
    title('Linear regresion Upwind l1, linfinity')
    legend(sprintf('Linear regresion, slope=%0.3g', ...
        pxul1(1)), 'Error l1 log-log', ...
        sprintf('Linear regresion, slope=%0.3g', ...
        pxulm(1)), 'Error L infinity log-log')
