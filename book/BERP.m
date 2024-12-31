function BERP
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %
    % Finite volume methods for Burgers equation
    %
    % w + w w =0
    %  t     x
    %
    % Domain: [a,b]
    %
    % Riemann Problem
    %
    % w0(x)=wl if x<xb=(b+a)/2; else w0(x)=wr
    %
    % Transmissive boundary conditions
    % Deltat is obtained from CFL number
    %
    % Numerical methods:
    % * Godunov method
    % * Lax Friedrichs
    % * Q-scheme van Leer / Roe
    % * Q-scheme
    %           + Harten regularization
    %           + Local Lax Friedrichs regularization
    % * Non conservative
    % * Steger-Warming flux splitting
    % * Vijayasundaram splitting
    % * Vijayasundaram splitting
    %           + Local Lax Friedrichs regularization
    %           + Harten regularization
    %
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    clear all
    clc
    disp('---------------------------------------------')
    disp('Finite volume methods for Burgers equation')
    disp('---------------------------------------------')
    disp('w + w w =0')
    disp(' t
    x')
    disp('Domain: [a,b]')
    disp('Transmissive boundary conditions')
    disp('Riemann problem for Burgers equation')
    disp('w0(x)=wp if x=xp0=(b-a)/2; else w0(x)=0')
    disp('Exact solution')
    disp('---------------------------------------------')
    a = 0;
    disp(['Lower end of the interval a = ', num2str(a)])
    b = 5;
    disp(['Upper end of the interval b = ', num2str(b)])
    m = 200;
    disp(['Number of nodes m=', num2str(m)])
    deltax = (b - a) / (m);
    xb = (b + a) / 2;
    disp(['Initial location of the discontinuity, xb = ' ...
            , num2str(xb)])
    disp(['deltax =', num2str(deltax)])
    x = [a:deltax:b];
    cfl = 0.5;
    disp(['Courant number = ', num2str(cfl)])
    %
    wl=-1;
    wr = 2;
    %
    % Deltat from Courant number
    deltat = cfl * deltax / max(abs(wl), abs(wr));
    %
    disp(['Time step from Courant number = ', ...
            num2str(deltat)])
    tmax = 1;
    disp(['Time end = ', num2str(tmax)])
    mt = tmax / deltat;
    disp('---------------------------------------------')
    disp(['Initial condition:'])
    disp(['wl= ', num2str(wl)])
    disp(['wr= ', num2str(wr)])
    disp(['w0(x)=', num2str(wl), ' if x<=', num2str(xb)])
    disp(['w0(x)=', num2str(wr), ' if x>', num2str(xb)])
    %
    disp('---------------------------------------------')

    if wl > wr
        s = (wl + wr) / 2;
        disp(['The speed of the shock'])
        disp(['from the Rankine Hugoniot condition s=', ...
                num2str(s)])
        disp(['The exact solution is an entropy shock'])
        disp(['w(x,t)=', num2str(wl), ...
                ' if (x-', num2str(xb), ')/t<=', num2str(s)])
        disp(['w(x,t)=', num2str(wr), ...
                ' if (x-', num2str(xb), ')/t>', num2str(s)])
    elseif wl < wr
        s = (wl + wr) / 2;
        disp(['The exact solution is a rarefaction wave'])
        disp(['w(x,t)=', num2str(wl), ...
                ' if (x-', num2str(xb), ')/t<=', num2str(wl)])
        disp(['w(x,t)= (x-', num2str(xb), ')/t', ...
                ' if ', num2str(wl), '<= (x-', num2str(xb), ...
                ')/t<=', num2str(wr)])
        disp(['w(x,t)=', num2str(wr), ...
                ' if (x-', num2str(xb), ')/t>', num2str(wr)])
    elseif wl == wr
        disp('The exact solution is')
        disp('a constant solution w(x,t)=wl=wr')
    end

    disp('---------------------------------------------')
    disp(['Numerical methods:'])
    disp([' * Godunov'])
    disp([' * Lax Friedrichs'])
    disp([' * Q-scheme van Leer / Roe'])
    disp([' * Q-scheme with'])
    disp(['
        Harten regularization (HR)'])
    epshr = 0.9;
    disp(['
        eps for Harten regularization = ', ...
            num2str(epshr)])
    disp([' * Q-scheme with'])
    disp(['
        Local Lax Friedrichs regularization (LLFR)'])
    disp([' * Steger-Warming flux splitting'])
    disp([' * Vijayasundaram flux splitting'])
    disp([' * Vijayasundaram flux splitting with'])
    disp(['
        Local Lax Friedrichs regularization (LLFR)'])
    disp('---------------------------------------------')
    %
    % Plot the initial condition at [a,b]
    %
    for i = 1:m + 1

        if x(i) <= xb
            w0(i) = wl;
        else
            w0(i) = wr;
        end

    end

    %
    wmin = min(wl, wr) - 0.2; %lower limit for the y axis
    wmax = max(wl, wr) + 0.2; %upper limit for the y axis
    figure(1)
    %
    plot(x, w0, 'ok')
    axis([a b wmin wmax])
    xlabel('x'); ylabel('w(x,0)');
    title('Initial condition');
    hold off
    %
    % Initialization
    %
    t = 0;
    %
    we = w0; %Exact solution
    wagod = w0; % Godunov method
    walxf = w0; % Lax Friedrichs
    waq = w0; % Q-scheme (Roe=van leer for Burgers equation)
    waqhr = w0; % Q-scheme Harten regularization
    waqllfr = w0; % Q-scheme LLF regularization
    wanc = w0; % Non conservative scheme
    wasw = w0; % Steger-Warming flux splitting
    wav = w0; % Vijayasundaram flux splitting
    wavhr = w0; % Vijayasundaram flux splitting Harten regularization
    wavllfr = w0; % Vijayasundaram flux splitting LLF regularization
    %
    dtdx = deltat / deltax;
    %
    for n = 1:mt
        % Godunov method
        wngod = god_btbc(wagod, dtdx, m);
        % Lax Friedrichs scheme
        wnlxf = lxf_btbc(walxf, dtdx, m);
        % Q-scheme
        wnq = qscheme_btbc(waq, dtdx, m);
        % Non conservative scheme
        wnnc = ncon_btbc(wanc, dtdx, m);
        % Q-scheme Harten regularization
        wnqhr = qscheme_hr_btbc(waqhr, dtdx, m, epshr);
        % Q-scheme LLF regularization
        wnqllfr = qscheme_llfr_btbc(waqllfr, dtdx, m);
        % Steger-Warming flux splitting
        wnsw = steger_warming_btbc(wasw, dtdx, m);
        % Vijayasundaram flux splitting
        wnv = vijaya_btbc(wav, dtdx, m);
        % Vijayasundaram flux splitting Harten regularization
        wnvhr = vijaya_hr_btbc(wavhr, dtdx, m, epshr);
        % Vijayasundaram flux splitting LLF regularization
        wnvllfr = vijaya_llfr_btbc(wavllfr, dtdx, m);
        %
        % Exact solution
        %
        t = t + deltat;
        we = exact_burgers(x, t, xb, m, wl, wr, s);
        %
        %
        figure(2)
        %
        plot(x, wngod, '-x', x, wnlxf, '-x', ...
            x, wnnc, '-*', x, we, '-ok')
        axis([a b wmin wmax])
        xlabel('x'); ylabel('w(x,t)');
        title(['Burgers equation, t = ', num2str(t)]);
        legend('Godunov', 'Lax Friedrichs', ...
            'Non conservative', 'Exact solution', ...
            'Location', 'NorthOutside')
        figure(3)
        %
        plot(x, wnq, '-+', x, wnqhr, '-o', x, wnqllfr, '-d', ...
            x, we, '-ok')
        axis([a b wmin wmax])
        xlabel('x'); ylabel('w(x,t)');
        title(['Burgers equation, t = ', num2str(t)]);
        legend('Q-scheme', 'Q-scheme Harten R.', ...
            'Q-scheme LLF R.', 'Exact solution', ...
            'Location', 'NorthOutside')
        figure(4)
        %
        plot(x, wnsw, '-v', x, wnv, '-s', x, wnvhr, '-<', ...
            x, wnvllfr, '-ˆ', x, we, '-ok')
        axis([a b wmin wmax])
        xlabel('x'); ylabel('w(x,t)');
        title(['Burgers equation, t = ', num2str(t)]);
        legend('Steger-Warming', ...
            'Vijayasundaram', 'Vijayasundaram Harten R.', ...
            'Vijayasundaram LLF R.', ...
            'Exact solution', ...
            'Location', 'NorthOutside')
        %
        figure(5)
        plot(x, abs(we - wngod), '-x', x, abs(we - wnlxf), '-x', ...
            x, abs(we - wnq), '-+', x, abs(we - wnnc), '-*', ...
            x, abs(we - wnqhr), '-o', x, abs(we - wnqllfr), '-d', ...
            x, abs(we - wnsw), '-v', x, abs(we - wnv), '-s', ...
            x, abs(we - wnvhr), '-<', x, abs(we - wnvllfr), '-')
        xlabel('x'); ylabel('|we(x,t)-w(x,t)|');
        axis([a b wmin wmax])
        title(['Burgers equation, t = ', num2str(t)]);
        legend('Error Godunov', 'Error Lax Friedrichs', ...
            'Error Q-scheme', 'Error Non conservative', ...
            'Error Q-scheme Harten R.', ...
            'Error Q-scheme LLF R.', ...
            'Error Steger-Warming', ...
            'Error Vijayasundaram', ...
            'Error Vijayasundaram Harten R.', ...
            'Error Vijayasundaram LLF R.', ...
            'Location', 'NorthOutside')
        % Update
        walxf = wnlxf;
        wagod = wngod;
        waq = wnq;
        waqhr = wnqhr;
        waqllfr = wnqllfr;
        wanc = wnnc;
        wasw = wnsw;
        wav = wnv;
        wavhr = wnvhr;
        wavllfr = wnvllfr;
    end

    disp('---------------------------------------------')
    disp(['Error at time t=', num2str(t)])
    disp(['* Godunov max(|we-wngod|)=..........', ...
            num2str(max(abs(we - wngod)))])
    disp(['* Lax Friedrichs máx|we-wnlxf|=.....', ...
            num2str(max(abs(we - wnlxf)))])
    disp(['* Non conservative max|we-wnnc|=....', ...
            num2str(max(abs(we - wnnc)))])
    disp(['* Q-scheme max|we-wnlxf|=...........', ...
            num2str(max(abs(we - wnq))
        )])
    disp(['* Q-scheme + Harten R. max|we-wnnc|=', ...
            num2str(max(abs(we - wnqhr)))])
    disp(['* Q-scheme + LLF R. max|we-wnqllfr|=', ...
            num2str(max(abs(we - wnqllfr)))])
    disp(['* Steger-Warming max|we-wnsw|=.....', ...
            num2str(max(abs(we - wnsw)))])
    disp(['* Vijayasundaram max|we-wnv|=.....', ...
            num2str(max(abs(we - wnv)))])
    disp(['* Vijayasundaram LLF R. max|we-wnvlhr|=', ...
            num2str(max(abs(we - wnvhr)))])
    disp(['* Vijayasundaram LLF R. max|we-wnvllfr|=', ...
            num2str(max(abs(we - wnvllfr)))])
    disp('---------------------------------------------')
    disp('---------------------------------------------')
    %
    % Figures all scheme at final time
    %
    % Godunov
    %
    figure(6)
    %
    plot(x, wngod, '-x', x, we, 'k')
    axis([a b wmin wmax])
    xlabel('x'); ylabel('w(x,t)');
    title(['Burgers equation, t = ', num2str(t)]);
    legend('Godunov', 'Exact solution', ...
        'Location', 'NorthOutside')
    %
    % Lax Friedrichs
    %
    figure(7)
    %
    plot(x, wnlxf, '-x', x, we, 'k')
    axis([a b wmin wmax])
    xlabel('x'); ylabel('w(x,t)');
    title(['Burgers equation, t = ', num2str(t)]);
    legend('Lax Friedrichs', 'Exact solution', ...
        'Location', 'NorthOutside')
    %
    % Non conservative
    %
    figure(8)
    %
    plot(x, wnnc, '-*', x, we, 'k')
    axis([a b wmin wmax])
    xlabel('x'); ylabel('w(x,t)');
    title(['Burgers equation, t = ', num2str(t)]);
    legend('Non conservative', 'Exact solution', ...
        'Location', 'NorthOutside')
    %
    % Q-scheme
    %
    figure(9)
    %
    plot(x, wnq, '-+', x, we, 'k')
    axis([a b wmin wmax])
    xlabel('x'); ylabel('w(x,t)');
    title(['Burgers equation, t = ', num2str(t)]);
    legend('Q-scheme', 'Exact solution', ...
        'Location', 'NorthOutside')
    figure(10)
    %
    plot(x, wnqhr, '-+', x, we, 'k')
    axis([a b wmin wmax])
    xlabel('x'); ylabel('w(x,t)');
    title(['Burgers equation, t = ', num2str(t)]);
    legend('Q-scheme + Harten R', 'Exact solution', ...
        'Location', 'NorthOutside')
    figure(11)
    %
    plot(x, wnqllfr, '-+', x, we, 'k')
    axis([a b wmin wmax])
    xlabel('x'); ylabel('w(x,t)');
    title(['Burgers equation, t = ', num2str(t)]);
    legend('Q-scheme + LLF R', 'Exact solution', ...
        'Location', 'NorthOutside')
    %
    % Flux splitting
    %
    % Steger-Warming
    figure(12)
    %
    plot(x, wnsw, '-v', x, we, 'k')
    axis([a b wmin wmax])
    xlabel('x'); ylabel('w(x,t)');
    title(['Burgers equation, t = ', num2str(t)]);
    legend('Steger-Warming', 'Exact solution', ...
        'Location', 'NorthOutside')
    % Vijayasundaram
    figure(13)
    %
    plot(x, wnv, '-v', x, we, 'k')
    axis([a b wmin wmax])
    xlabel('x'); ylabel('w(x,t)');
    title(['Burgers equation, t = ', num2str(t)]);
    legend('Vijayasundaram', 'Exact solution', ...
        'Location', 'NorthOutside')
    figure(14)
    %
    plot(x, wnvhr, '-v', x, we, 'k')
    axis([a b wmin wmax])
    xlabel('x'); ylabel('w(x,t)');
    title(['Burgers equation, t = ', num2str(t)]);
    legend('Vijayasundaram + Harten R', 'Exact solution', ...
        'Location', 'NorthOutside')
    figure(15)
    %
    plot(x, wnvllfr, '-v', x, we, 'k')
    axis([a b wmin wmax])
    xlabel('x'); ylabel('w(x,t)');
    title(['Burgers equation, t = ', num2str(t)]);
    legend('Vijayasundaram + LLF R', 'Exact solution', ...
        'Location', 'NorthOutside')
