import qrcode

from PIL import Image

qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,
                    box_size=10,border=4,)
# We also paste a url our youtube channel, any website to generate a QR code for this.
qr.add_data("Hello Tanuj Choudhary")
qr.make(fit=True)
img = qr.make_image(fill_color = "green",back_color  = "black")
img.save("tanuj_choudhary.png")
print("T")

# import qrcode as qr

# # We also paste a url our youtube channel, any website to generate a QR code for this.
# img = qr.make("Hello Tanuj")
# img.save("tanuj_ch.png")