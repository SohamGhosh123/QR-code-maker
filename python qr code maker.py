import pyqrcode
import png
from pyqrcode import QRCode
#string represents the qr code
s="www.google.com"
#generate qr code
url=pyqrcode.create(s)
#create and save the svg file naming myqrcode.svg
url.svg("myqrcode.svg",scale=8)
#create and save the png file myqrcode.png
url.png("myqrcode.png",scale=8)