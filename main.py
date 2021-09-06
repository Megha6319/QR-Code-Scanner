# Import QRCode from pyqrcode
import pyqrcode

# String which represents the QR code
s = "https://megha6319.github.io/"

# Generate QR code
url = pyqrcode.create(s)

# Create and save the svg file naming "myqr.svg"
url.svg("myqr.svg", scale = 10)

# Create and save the png file naming "myqr.png"
url.png('myqr.png', scale = 5 )