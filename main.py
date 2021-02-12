import qrcode
import qrcode.image.svg


size = input("Size: ")
border = input("Border: ")
data = input("Data: ")
color_qr = input("Qr color: ")
color_bg = input("Qr background color: ")
path_file = input("Path to file: ")
file_name = input("File name: ")
format_file = input("File format: ")

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=size,
    border=border
)
qr.add_data(data)
qr.make(fit=True)
if format_file.lower() == "svg":
    img = qr.make_image(fill_color=color_qr,back_color=color_bg, image_factory=qrcode.image.svg.SvgPathImage)
else:
    img = qr.make_image(fill_color=color_qr,back_color=color_bg)

path = path_file
path += file_name
path += "."
path += format_file

img.save(path)

