"""Featured-work card: eyebrow, title (wrapped to two lines if needed), a stats line, the paper's first
page, and a figure on a white panel, over a dark background with a coloured glow.

python scripts/make_card.py out.png "EYEBROW" "Title" "stat · stat" page1.png figure.png \
    --accent 214,120,60 --glow 67,42,28 --glow2 42,29,23
"""
import argparse

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

W, H = 1280, 720
BASE = np.array([12, 13, 16], float)
AVENIR = "/System/Library/Fonts/Avenir Next.ttc"
MENLO = "/System/Library/Fonts/Menlo.ttc"


def rgb(s):
    return tuple(int(x) for x in s.split(","))


def background(glow, glow2):
    y, x = np.mgrid[0:H, 0:W].astype(float)
    g1 = np.exp(-((x - W) ** 2 + y ** 2) / (2 * 620.0 ** 2))[..., None]
    g2 = np.exp(-(x ** 2 + (y - H) ** 2) / (2 * 520.0 ** 2))[..., None]
    img = BASE + (np.array(glow) - BASE) * g1 + (np.array(glow2) - BASE) * g2
    return Image.fromarray(np.clip(img, 0, 255).astype(np.uint8))


def wrap(draw, text, font, width):
    words, lines = text.split(), [""]
    for w in words:
        trial = (lines[-1] + " " + w).strip()
        if draw.textlength(trial, font=font) <= width or not lines[-1]:
            lines[-1] = trial
        else:
            lines.append(w)
    return lines


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument("eyebrow")
    ap.add_argument("title")
    ap.add_argument("stats")
    ap.add_argument("page")
    ap.add_argument("figure")
    ap.add_argument("--accent", type=rgb, default=(217, 136, 63))
    ap.add_argument("--glow", type=rgb, default=(67, 42, 28))
    ap.add_argument("--glow2", type=rgb, default=(42, 29, 23))
    a = ap.parse_args()

    bg = background(a.glow, a.glow2)
    d = ImageDraw.Draw(bg)
    d.text((64, 52), a.eyebrow, font=ImageFont.truetype(AVENIR, 21, index=0), fill=a.accent)
    tfont = ImageFont.truetype(AVENIR, 46, index=2)
    lines = wrap(d, a.title, tfont, W - 128)
    for i, line in enumerate(lines):
        d.text((62, 84 + 58 * i), line, font=tfont, fill=(244, 241, 236))
    sy = 152 + 58 * (len(lines) - 1)
    d.text((64, sy), a.stats, font=ImageFont.truetype(MENLO, 19), fill=(178, 174, 168))
    top = sy + 50

    panel = (405, top, 1222, H - 44)
    d.rounded_rectangle(panel, radius=18, fill=(255, 255, 255))
    f = Image.open(a.figure).convert("RGB")
    bw, bh = panel[2] - panel[0] - 48, panel[3] - panel[1] - 40
    s = min(bw / f.width, bh / f.height)
    f = f.resize((int(f.width * s), int(f.height * s)), Image.LANCZOS)
    bg.paste(f, (panel[0] + (panel[2] - panel[0] - f.width) // 2, panel[1] + (panel[3] - panel[1] - f.height) // 2))

    p = Image.open(a.page).convert("RGB")
    p = p.resize((340, int(340 * p.height / p.width)), Image.LANCZOS)
    p = p.crop((0, 0, 340, min(p.height, H - top - 20)))
    shadow = Image.new("RGBA", (p.width + 40, p.height + 40), (0, 0, 0, 0))
    ImageDraw.Draw(shadow).rectangle((20, 20, p.width + 20, p.height + 20), fill=(0, 0, 0, 150))
    shadow = shadow.filter(ImageFilter.GaussianBlur(10)).rotate(4, expand=True, resample=Image.BICUBIC)
    pr = p.convert("RGBA").rotate(4, expand=True, resample=Image.BICUBIC)
    bg.paste(shadow, (52, top - 6), shadow)
    bg.paste(pr, (64, top - 2), pr)
    bg.save(a.out)


if __name__ == "__main__":
    main()
