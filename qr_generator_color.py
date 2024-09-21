import qrcode
from PIL import Image

qr=qrcode.QRCode(version=3,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=10,border=5)
qr.add_data("https://www.youtube.com/watch?v=ekwPDGyd79s")
qr.make(fit=True)
img=qr.make_image(fill_color="white",back_color="black")
img.save("Ayush1.png")
