import qrcode
import io

SIZE=1
BOX_SIZE=20
BORDER=1
COLOR='black'
BG_COLOR='white'

FILENAME='qrcode'

qr = qrcode.QRCode(
    version=SIZE,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=BOX_SIZE,
    border=BORDER,
)

data = input('QRCode Data: ')
qr.add_data(data)

img = qr.make_image(fill_color=COLOR, back_color=BG_COLOR)

name = input(f'Name({FILENAME}): ')
img.save(f"{name or FILENAME}.png")

f = io.StringIO(data)
qr.print_ascii(out=f)
f.seek(0)
print(f.read())
