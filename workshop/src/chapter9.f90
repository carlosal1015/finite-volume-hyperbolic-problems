! =========================================================
subroutine rp1(maxmx,meqn,mwaves,maux,mbc,mx,ql,qr,auxl,auxr,wave,s,amdq, apdq)
! =========================================================

   implicit double precision (a-h,o-z)

   dimension ql(meqn,1-mbc:maxmx+mbc)
   dimension qr(meqn,1-mbc:maxmx+mbc)
   dimension qs(meqn,1-mbc:maxmx+mbc)
   dimension auxl(maux,1-mbc:maxmx+mbc)
   dimension auxr(maux,1-mbc:maxmx+mbc)
   dimension s(mwaves,1-mbc:maxmx+mbc)
   dimension wave(meqn, mwaves,1-mbc:maxmx+mbc)
   dimension amdq(meqn,1-mbc:maxmx+mbc)
   dimension apdq(meqn,1-mbc:maxmx+mbc)
   common /comrp/ u, p

   do 30 i=1-mbc,mx+mbc

      u = auxl(1,i)
      p = auxr(1,i-1)

      if (u > 0.d0) then
         qs(1,i) = qr(1,i-1) * p / u
         wave(1,1,i) = ql(1,i) - qs(1,i)
         s(1,i) = u
         amdq(1,i) = 0.d0
         apdq(1,i) = u * wave(1,1,i)
      endif
      if (u == 0.d0) then
         wave(1,1,i) = 0.d0
         s(1,i) = 0.d0
         amdq(1,i) = 0.d0
         apdq(1,i) = 0.d0
      endif

30 end do
   return
end subroutine rp1
