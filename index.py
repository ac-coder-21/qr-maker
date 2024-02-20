import pyqrcode
import png
from pyqrcode import QRCode

s = 'https://www.youtube.com/watch?v=AeDf9UctMns'

url = pyqrcode.create(s)

url.png("myqr.png", scale = 6)