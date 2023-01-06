import pyqrcode
import png

link = "https://www.youtube.com/channel/UCnfrGRp1GbzgiO635XN3o5w"

qr_code= pyqrcode.create(link)

qr_code.png("samayal.png",scale=5)
