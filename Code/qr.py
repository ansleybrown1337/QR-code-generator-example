'''
QR code generator
A.J. Brown
ansleybrown1337@gmail.com
16 September 2022

Documentation: https://pypi.org/project/qrcode/
'''

# Basic Usage
import qrcode
img = qrcode.make('https://sites.google.com/view/ansleyjbrown')
type(img)  # qrcode.image.pil.PilImage
img.save("my_first_qr.png")

# Advanced Usage
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('https://sites.google.com/view/ansleyjbrown')
qr.make(fit=True)

img2 = qr.make_image(fill_color="black", back_color="white")
img2.save("my_second_qr.png")
