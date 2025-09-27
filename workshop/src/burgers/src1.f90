c =========================================================
2
subroutine src1(meqn,mbc,mx,xlower,dx,q,maux,aux,t,dt)
3 c =========================================================
4
implicit double precision (a-h,o-z)
5
dimension q(meqn,1-mbc:mx+mbc)
6 c
7 c
# solve the diffusion equation q_t = q_{xx} using Crank-Nicolson
8 c
# The LAPACK tridiagonal solver dgtsv is used, which is in tridiag.f
9 c
# local storage:
10
parameter (maxldb = 5000)
11
dimension b(maxldb,1), d(maxldb), dl(maxldb), du(maxldb)
12
common /comsrc/ dcoef
13
14
if (mx .gt. maxldb) then
15
write(6,*) ’ERROR:
increase maxldb in src1.f’
16
endif
17
ldb = maxldb
18
nrhs = 1
19
dtdx2 = dcoef * dt / (2.d0*dx*dx)
20 c
# set coefficients in tridiagonal matrix and RHS:
21
do i=1,mx
22
dl(i) = -dtdx2
23
d(i) = 1.d0 + 2.d0*dtdx2
24
du(i) = -dtdx2
25
b(i,1) = q(1,i) + dtdx2 * (q(1,i-1) - 2.d0*q(1,i) + q(1,i+1))
26
enddo
27 c
# no-flux boundary conditions for diffusion step:
28 c
# Adjust matrix entries to use q(1,0)=q(1,1) and q(1,mx+1)=q(1,mx)
29 c
# at end of time step:
30
d(1) = d(1) - dtdx2
31
d(mx) = d(mx) - dtdx2
32 c
# solve the tridiagonal system:
33
call dgtsv(mx,nrhs,dl,d,du,b,ldb,info)
34
35
if (info .ne. 0) then
36
write(6,*) ’ERROR in src1 from call to dgtsv... info = ’,info
37
stop
endif
39
40
do i=1,mx
q(1,i) = b(i,1)
42
enddo
43
return
44
end
