! =====================================================
subroutine rp1(maxm,meqn,mwaves,maux,mbc,mx,ql,qr,auxl,auxr,wave,s,amdq, apdq)
! =====================================================

   implicit double precision (a-h,o-z)

   dimension wave(meqn, mwaves, 1-mbc:maxm+mbc)

   dimension
   s(mwaves,1-mbc:maxm+mbc)

   dimension
   ql(meqn, 1-mbc:maxm+mbc)

   dimension
   qr(meqn, 1-mbc:maxm+mbc)

   dimension apdq(meqn, 1-mbc:maxm+mbc)

   dimension amdq(meqn, 1-mbc:maxm+mbc)

! # advection velocity:
! # (should be set in setprob.f)

   common /cparam/ a

! # define the wave:
   do 20 i = 2-mbc, mx+mbc

! # Compute the waves.

      wave(1,1,i) = ql(1,i) - qr(1,i-1)
      s(1,i) = a
20 END DO
! # compute the leftgoing and rightgoing flux differences:
! # Note s(1,i) < 0 and s(2,i) > 0.
   do 220 m=1,meqn
      do 220 i = 2-mbc, mx+mbc
         amdq(m,i) = dmin1(0.d0,s(1,i))*wave(m,1,i)
         apdq(m,i) = dmax1(0.d0,s(1,i))*wave(m,1,i)
220 END DO
   return
end subroutine rp1
