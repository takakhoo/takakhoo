"""Featured-work card: eyebrow, title, a stats line, the paper's first page, and a figure.
python scripts/make_card.py out.png "EYEBROW" "Title" "stat · stat" page1.png figure.png"""
import sys

from PIL import Image, ImageDraw, ImageFilter, ImageFont

W, H = 1280, 720
out, eyebrow, title, stats, page, fig = sys.argv[1:7]

bg = Image.new("RGB", (W, H))
px = bg.load()
for x in range(W):
    for y in range(H):
        t = (x / W) ** 2 * 0.8 + (y / H) * 0.2
        px[x, y] = (int(14 + 52 * t), int(14 + 30 * t), int(18 + 14 * t))
d = ImageDraw.Draw(bg)
avenir = "/System/Library/Fonts/Avenir Next.ttc"
d.text((64, 52), eyebrow, font=ImageFont.truetype(avenir, 21, index=0), fill=(217, 136, 63))
d.text((62, 84), title, font=ImageFont.truetype(avenir, 46, index=2), fill=(244, 241, 236))
d.text((64, 152), stats, font=ImageFont.truetype("/System/Library/Fonts/Menlo.ttc", 19), fill=(178, 174, 168))

p = Image.open(page).convert("RGB")
p = p.resize((340, int(340 * p.height / p.width)), Image.LANCZOS)
p = p.crop((0, 0, 340, min(p.height, 470)))
shadow = Image.new("RGBA", (p.width + 40, p.height + 40), (0, 0, 0, 0))
ImageDraw.Draw(shadow).rectangle((20, 20, p.width + 20, p.height + 20), fill=(0, 0, 0, 150))
shadow = shadow.filter(ImageFilter.GaussianBlur(10)).rotate(4, expand=True, resample=Image.BICUBIC)
pr = p.convert("RGBA").rotate(4, expand=True, resample=Image.BICUBIC)
bg.paste(shadow, (52, 196), shadow)
bg.paste(pr, (64, 200), pr)

panel = (405, 202, 1222, 676)
d.rounded_rectangle(panel, radius=18, fill=(255, 255, 255))
f = Image.open(fig).convert("RGB")
bw, bh = panel[2] - panel[0] - 48, panel[3] - panel[1] - 40
s = min(bw / f.width, bh / f.height)
f = f.resize((int(f.width * s), int(f.height * s)), Image.LANCZOS)
bg.paste(f, (panel[0] + (panel[2] - panel[0] - f.width) // 2, panel[1] + (panel[3] - panel[1] - f.height) // 2))
bg.save(out)
