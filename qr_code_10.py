import qrcode
data = "https://www.donationalerts.com/r/piroschock1"
filename = "C:/Users/dmitr/Desktop/T-Bot 1/qr-donations.jpg"
img = qrcode.make(data)
img.save(filename)