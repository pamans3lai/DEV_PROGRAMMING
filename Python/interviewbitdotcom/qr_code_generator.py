# Run 'pip install pyqrcode' before running this program
import pyqrcode

data = input("Masukkan text atau link untuk generate QR code: ")\

# using pyqrcode.create() to create a qr code of the input data
qr = pyqrcode.create(data)

# Using .svg method to save the qr code as SVG file of probided name & compile
qr.svg('qr_code.svg', scale = 8)
