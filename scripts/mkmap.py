import math, os, subprocess, sys
from PIL import Image
Z = 11
T = sys.argv[1]; OUT = sys.argv[2]
W_LON, E_LON, N_LAT, S_LAT = 6.12, 6.83, 50.69, 50.42
def px(lat, lon):
    n = 2 ** Z * 256
    x = (lon + 180) / 360 * n
    y = (1 - math.asinh(math.tan(math.radians(lat))) / math.pi) / 2 * n
    return x, y
x0, y0 = px(N_LAT, W_LON); x1, y1 = px(S_LAT, E_LON)
tx0, ty0, tx1, ty1 = int(x0 // 256), int(y0 // 256), int(x1 // 256), int(y1 // 256)
big = Image.new('RGB', ((tx1 - tx0 + 1) * 256, (ty1 - ty0 + 1) * 256))
for tx in range(tx0, tx1 + 1):
    for ty in range(ty0, ty1 + 1):
        f = f'{T}/{Z}_{tx}_{ty}.png'
        if not os.path.exists(f):
            subprocess.run(['curl', '-sf', '-A', 'Eifel-Weihnacht static map (personal, low volume)',
                            '-o', f, f'https://tile.openstreetmap.org/{Z}/{tx}/{ty}.png'], check=True)
        big.paste(Image.open(f).convert('RGB'), ((tx - tx0) * 256, (ty - ty0) * 256))
ox, oy = tx0 * 256, ty0 * 256
crop = big.crop((int(x0 - ox), int(y0 - oy), int(x1 - ox), int(y1 - oy)))
crop.save(OUT, 'JPEG', quality=82, optimize=True)
print('size', crop.size, os.path.getsize(OUT))
for name, lat, lon in [('Reifferscheid', 50.4767979, 6.4663515), ('Monschau', 50.5552388, 6.2422802), ('Satzvey', 50.6199284, 6.7065)]:
    x, y = px(lat, lon)
    print(name, round((x - x0) / crop.size[0] * 100, 2), round((y - y0) / crop.size[1] * 100, 2))
