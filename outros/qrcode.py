import pyqrcode

QRatr="https://youtube.com"
url=pyqrcode.create(QRatr)
url.svg('youtube_qrCode.svg',scale=8)