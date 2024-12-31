function TEupwindFV
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %
    % Upwind scheme for the transport equation
    %
    % w +lambda w =0
    %  t         x
    %
    % Domain: [a,b]
    % Initial condition: Pulse
    %
    % w0(x)=wp if x=xp=(b+a)/2; else w0(x)=0
    %
    % Transmissive boundary conditions
    %
    % Exact solution:
    % w(x,t)=w0(x-lambda*t)
    %
    % Approximated solution constant per finite volume
    %
    % Deltat is obtained from CFL number
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    clear all
    clc
    disp('---------------------------------------------')
    disp('Upwind scheme to solve the transport equation')
    disp('---------------------------------------------')
    disp('w +lambda w =0')
    disp(' t
    x')
    disp('Domain: [a,b]')
    disp('Transmissive boundary conditions')
    disp('Initial condition: Pulse')
    disp('w0(x)=wp if x=xp=(b+a)/2; else w0(x)=0')
    disp('Exact solution')
    disp('w(x,t)=w0(x-lambda*t)')
    disp('---------------------------------------------')
    a=-6;
    disp(['Lower end of the interval a = ', num2str(a)])
    b = 6;
    disp(['Upper end of the interval b = ', num2str(b)])
    lambda = 1;
    disp(['Velocity of propagation lambda =', num2str(lambda)])
    m = 12;
    disp(['Number of nodes m=', num2str(m)])
    deltax = (b - a) / (m);
    disp(['deltax =', num2str(deltax)])
    x = [a:deltax:b];
    xm = linspace(a + deltax / 2, b - deltax / 2, m);
    xm = [a, xm, b];
    cfl = 1.5;
    disp(['Courant number = ', num2str(cfl)])
    % Deltat from Courant number
    deltat = cfl * deltax / lambda;
    disp(['Time step from Courant number =', num2str(deltat)])
    tmax = 4;
    disp(['Time end = ', num2str(tmax)])
    mt = tmax / deltat;
    %
    wp = 1;
    disp(['Value of the pulse wp=w0(xp) =', num2str(wp)])
    disp('---------------------------------------------')
    %
    % Plot the initial condition at [a,b]
    %
    w0 = zeros(1, m + 1);
    w0(m / 2 + 1) = wp;
    figure(1)
    %
    for i = 1:1:m
        plot([xm(i), xm(i), xm(i + 1), xm(i + 1)], [0, w0(i), w0(i), 0], 'b')
        hold on
    end

    plot(xm, zeros(1, m + 2), '*g')
    xlabel('x'); ylabel('w(x,0)');
    title('Initial condition');
    hold off
    %
    % Initialization
    %
    wa = w0;
    we = w0;
    %
    cflp = 0.5 * (lambda + abs(lambda)) * deltat / deltax;
    cfln = 0.5 * (lambda - abs(lambda)) * deltat / deltax;
    %
    for n = 1:mt
        %
        wam(1:m) = wa(2:m + 1);
        wan(2:m + 1) = wa(1:m);
        %
        wn(2:m) = wa(2:m) - cflp * (wa(2:m) - wan(2:m))- ...
            cfln * (wam(2:m) - wa(2:m));
        %
        % Exact solution
        %
        % Exact position of the pulse
        %       at time t=n*deltat
        %
        xp = lambda * n * deltat;
        %
        for i = 1:m
            %
            if (abs(x(i) - xp) <= deltax / 2)
                we(i) = wp;
            else
                we(i) = 0;
            end

            % Approximated solution constant per finite volume
            figure(2)
            plot([xm(i), xm(i), xm(i + 1), xm(i + 1)], [0, wn(i), wn(i), 0], 'b')
            hold on
        end

        %
        % Transmissive boundary conditions
        %
        wn(1) = wn(2);
        wn(m + 1) = wn(m);
        %
        we(m + 1) = wa(m + 1);
        %
        plot([xm(1), xm(1), xm(2), xm(2)], [0, wn(1), wn(1), 0], 'b')
        hold on
        wn(m + 1) = wa(m + 1);
        plot([xm(m), xm(m), x(m + 1), xm(m + 1)], [0, wn(m + 1), wn(m + 1), 0], 'b')
        hold on
        %
        plot(x, wn, 'xb', x, we, 'or', xm, zeros(1, m + 2), '*g')
        xlabel('x'); ylabel('w(x,t)');
        t = n * deltat;
        title(['Upwind scheme t = ', num2str(t)]);
        pause(1)
        % Update
        wa = wn;
        hold off
    end

    %
    % Mass conservation
    %
    intw0 = deltax * sum(w0);
    intwn = deltax * sum(wn);
    errorconservation = abs(intw0 - intwn);
    disp('Test Conservation property =')
    disp(['deltax*sum(w0) =', num2str(intw0)])
    disp(['deltax*sum(wn) =', num2str(intwn)])
    disp(['error=abs(deltax*sum(w0)-deltax*sum(wn)) =', ...
            num2str(errorconservation)])
    disp('---------------------------------------------')
