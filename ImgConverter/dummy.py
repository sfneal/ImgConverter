import os
import textwrap
from PIL import Image, ImageDraw


def dummy_img(source, target):
    astr = "ImgConverter error: unsupported file type\n" + os.path.basename(source)
    para = textwrap.wrap(astr, width=50)

    MAX_W, MAX_H = 400, 200
    im = Image.new('RGB', (MAX_W, MAX_H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(im)

    current_h, pad = 100, 10
    for line in para:
        w, h = draw.textsize(line)
        draw.text(((MAX_W - w) / 2, current_h), line)
        current_h += h + pad

    im.save(target)
    return target
