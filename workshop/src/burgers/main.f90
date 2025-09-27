c
c
efix = .true. !# Compute correct flux for transonic rarefactions
c
do 30 i=2-mbc,mx+mbc
   c
   c # Compute the wave and speed
   c
   wave(i,1,1) = ql(i,1) - qr(i-1,1)
   s(i,1) = 0.5d0 * (qr(i-1,1) + ql(i,1))
   c
   c
   c # compute left-going and right-going flux differences:
   c ------------------------------------------------------
   c
   amdq(i,1) = dmin1(s(i,1), 0.d0) * wave(i,1,1)
   apdq(i,1) = dmax1(s(i,1), 0.d0) * wave(i,1,1)
   c
   if (efix) then
      c # entropy fix for transonic rarefactions:
      if (qr(i-1,1).lt.0.d0 .and. ql(i,1).gt.0.d0) then
         amdq(i,1) = - 0.5d0 * qr(i-1,1)**2
         apdq(i,1) = 0.5d0 * ql(i,1)**2
      endif
   endif
30 continue
