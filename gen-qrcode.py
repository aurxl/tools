import qrcode
import io
import sys
from getpass import getpass

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

if  len(sys.argv) > 1:
    if sys.argv[1] == 'wifi':
        data = f'WIFI:S:{input("SSID: ")};T:{input("Type(WPA): ") or "WPA"};P:{getpass("Secret: ")};H:{input("Hidden(false): ") or "false"};'
    else:
        print('Unknown Keyword')
        sys.exit(1)
else:
    data = input('QRCode Data: ')

qr.add_data(data)

img = qr.make_image(fill_color=COLOR, back_color=BG_COLOR)

filename = input(f'Filename({FILENAME}): ')
try:
    f = img.save(f"{filename or FILENAME}.png")
    print(f'Saved: {filename or FILENAME}.png')
except Exception as exc:
    print(f'Failed to save IMG ({exc})')

f = io.StringIO(data)
qr.print_ascii(out=f)
f.seek(0)
print(f.read())
