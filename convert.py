import colorsys
import sys
from PIL import Image

palette = [0x00,0x00,0x00,0x1d,0x2b,0x53,0x7e,0x25,0x53,0x00,0x87,0x51,0xab,0x52,0x36,0x5f,0x57,0x4f,0xc2,0xc3,0xc7,0xff,0xf1,0xe8,0xff,0x00,0x4d,0xff,0xa3,0x00,0xff,0xec,0x27,0x00,0xe4,0x36,0x29,0xad,0xff,0x83,0x76,0x9c,0xff,0x77,0xa8,0xff,0xcc,0xaa]
palette_realsz = len(palette) // 3

img = Image.open('mali.png')

for spr_y in range(4):
    for spr_x in range(12):
        spr_id = 192 + spr_y * 16 + spr_x
        sys.stdout.write('-- %d:' % spr_id)
        for dy in range(8):
            y = spr_y * 8 + dy
            for dx in range(8):
                x = spr_x * 8 + dx
                (r, g, b, a) = img.getpixel((x, y))
                h, s, v = colorsys.rgb_to_hsv(r, g, b)
                if a == 0: continue
                best = 1 << 63
                idx = -1
                for i in range(palette_realsz):
                    r0, g0, b0 = palette[i*3 : i*3+3]
                    h0, s0, v0 = colorsys.rgb_to_hsv(r0, g0, b0)
                    #if x == 0 and y == 0: print(r0, g0,  b0, h0, s0, v0)
                    val = 15 * abs(h - h0) ** 2 + abs(s - s0) ** 2 + (abs(v - v0) / 255) ** 2
                    (best, idx) = min((best, idx), (val, i))
                sys.stdout.write('%x' % idx)
        sys.stdout.write('\n')
