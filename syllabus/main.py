from qrcode import make

make(data="https://docs.google.com/spreadsheets/d/1a9oeJ7al-g58u4nRNeKJQ2sihxVG7mZTZM-kIhISZEA/edit?usp=sharing").save(
    stream="qrcode.pdf", format="pdf"
)