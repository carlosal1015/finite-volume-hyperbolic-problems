#!/usr/bin/env python

from qrcode import QRCode
from qrcode.constants import ERROR_CORRECT_Q
from qrcode.image.svg import SvgPathFillImage
from qrcode.image.styles.moduledrawers.svg import SvgPathSquareDrawer

qr = QRCode(
    version=1,
    error_correction=ERROR_CORRECT_Q,
    box_size=10,
    border=1,
    image_factory=SvgPathFillImage,
)
qr.add_data(
    "https://maticus-7.github.io/lane-emden"
)
img = qr.make_image(module_drawer=SvgPathSquareDrawer())
img.save(stream="qrcode.svg")
