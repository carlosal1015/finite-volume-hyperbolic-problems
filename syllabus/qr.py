#!/usr/bin/env python

from qrcode import make

make(data="https://www.wikipedia.org").save(
    stream="qrcode.pdf", format="pdf"
)

make(data="https://portal.uni.edu.pe").save(
    stream="qrcodefuncionaliii.pdf", format="pdf"
)