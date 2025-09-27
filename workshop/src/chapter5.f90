! =====================================================
subroutine rp1(maxm,meqn,mwaves,maux,mbc,mx,ql,qr,auxl,auxr,wave,s,amdq, apdq)
! =====================================================

   implicit double precision (a-h,o-z)
   dimension wave(meqn, mwaves, 1-mbc:maxm+mbc)
   dimension s(mwaves,1-mbc:maxm+mbc)
   dimension ql(meqn, 1-mbc:maxm+mbc)
   dimension qr(meqn, 1-mbc:maxm+mbc)
   dimension apdq(meqn, 1-mbc:maxm+mbc)
   dimension amdq(meqn, 1-mbc:maxm+mbc)

! local arrays
! ------------
   dimension delta(2)
! # density, bulk modulus, and sound speed, and impedance of medium:
! # (should be set in setprob.f)
   common /cparam/ rho,bulk,cc,zz

! # find a1 and a2, the coefficients of the 2 eigenvectors:
   do 20 i = 2-mbc, mx+mbc
      delta(1) = ql(1,i) - qr(1,i-1)
      delta(2) = ql(2,i) - qr(2,i-1)
      a1 = (-delta(1) + zz*delta(2)) / (2.d0*zz)
      a2 = (delta(1) + zz*delta(2)) / (2.d0*zz)

! # Compute the waves.

      wave(1,1,i) = -a1*zz
      wave(2,1,i) = a1
      s(1,i) = -cc

      wave(1,2,i) = a2*zz
      wave(2,2,i) = a2
      s(2,i) = cc

20 END DO
! # compute the leftgoing and rightgoing flux differences:
! # Note s(1,i) < 0 and s(2,i) > 0.

   do 220 m=1,meqn
      do 220 i = 2-mbc, mx+mbc
         amdq(m,i) = s(1,i)*wave(m,1,i)
         apdq(m,i) = s(2,i)*wave(m,2,i)
220 END DO
   return
end subroutine rp1
