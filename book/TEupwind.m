function TEupwind
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %
    %
    Upwind scheme for the transport equation
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
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    clear all
    clc
    disp('Upwind scheme')
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
    disp('-------------------------------------------')
    a=-3;
    disp(['Lower end of the interval a = ', num2str(a)])
    b = 3;
    disp(['Upper end of the interval b = ', num2str(b)])
    lambda = 1;
    disp(['Velocity of propagation lambda =', num2str(lambda)])
    m = 60;
    disp(['Number of nodes =', num2str(m)])
    deltax = (b - a) / (m);
    disp(['deltax =', num2str(deltax)])
    x = [a:deltax:b];
    deltat = 0.1;
    disp(['Time step =', num2str(deltat)])
    tmax = 1;
    disp(['Time end = ', num2str(tmax)])
    mt = tmax / deltat;
    % Courant number
    cfl = lambda * deltat / deltax;
    disp(['Courant number = ', num2str(cfl)])
    wp = 1;
    disp(['Value of the pulse wp=w0(xp) =', num2str(wp)])
    disp('-------------------------------------------')
    %
    % Plot the initial condition at [a,b]
    %
    w0 = zeros(1, m + 1);
    w0(m / 2 + 1) = wp;
    figure(1)
    plot(x, w0, 'or')
    xlabel('x'); ylabel('w(x,0)');
    title('Initial condition');
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
        %       at time t = n * deltat
        %
        xp = lambda * n * deltat;
        %
        for i = 1:m + 1
            %
            if (abs(x(i) - xp) <= deltax / 2)
                we(i) = wp;
            else
                we(i) = 0;
            end

        end

        %
        % Transmissive boundary conditions
        %
        wn(1) = wn(2);
        wn(m + 1) = wn(m);
        %
        figure(2)
        plot(x, wn, 'xb', x, wn, 'b', x, we, 'or')
        xlabel('x'); ylabel('w(x,t)');
        title(['Upwind scheme t = ', num2str(n * deltat)]);
        pause(1)
        % Update
        wa = wn;
    end
