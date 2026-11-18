"""Prepare the CV's images from the site's own assets.

Usage: python -I assets.py <repo> <build-dir>   (needs pillow and segno)

Writes <build-dir>/img/: the round headshot, company logos as PNG, the
portfolio images as JPEG crops sized for the cards, the portfolio QR code,
and the email address as an image for the public copy.
"""
import base64
import re
import sys
from pathlib import Path

import segno
from PIL import Image, ImageDraw, ImageFont

repo, build = Path(sys.argv[1]), Path(sys.argv[2])
img, out = repo / "assets/img", build / "img"
out.mkdir(parents=True, exist_ok=True)

# Headshot: head and shoulders from the cutout, on a tinted disc.
src = Image.open(img / "lance_full.webp").convert("RGBA")
size = 576
crop = src.crop((22, 0, 214, 192)).resize((size, size), Image.LANCZOS)
disc = Image.new("RGBA", (size, size), (230, 241, 240, 255))
disc.alpha_composite(crop, (0, 24))
mask = Image.new("L", (size * 4, size * 4), 0)
ImageDraw.Draw(mask).ellipse((0, 0, size * 4 - 1, size * 4 - 1), fill=255)
disc.putalpha(mask.resize((size, size), Image.LANCZOS))
disc.save(out / "headshot.png")

LOGOS = {
    "pfp": "resume/purpose-factory-partners.webp", "flowconnect": "resume/flowconnect.webp",
    "accruvia": "resume/accruvia.jpg", "adminout": "logo-mini.webp", "g2g": "resume/g2g.webp",
    "wlast": "resume/wlast.webp", "wits": "resume/wits.webp",
    "fezile": "resume/fezile-dabi.webp", "springbok": "resume/springbok.webp",
}
for name, rel in LOGOS.items():
    im = Image.open(img / rel).convert("RGBA")
    bg = Image.new("RGBA", im.size, (255, 255, 255, 255))
    bg.alpha_composite(im)
    bg.convert("RGB").save(out / f"logo-{name}.png")

# Card crops: "wide" (2:1) for the featured card, "short" (2.8:1) for the rest.
# Screenshots keep their top edge, where the app header is; illustrations are
# cropped about the centre.
ILLUSTRATIONS = {"flowconnect", "contact-centre", "crypto-rollout"}
for f in sorted((img / "portfolio").glob("*.webp")):
    base = Image.open(f).convert("RGB").resize((960, 540), Image.LANCZOS)
    for tag, ratio in (("wide", 2.0), ("short", 2.8)):
        h = round(960 / ratio)
        y = (540 - h) // 2 if f.stem in ILLUSTRATIONS else 0
        base.crop((0, y, 960, y + h)).save(
            out / f"{f.stem}-{tag}.jpg", quality=84, optimize=True, progressive=True)

# The email address as an image, for the public copy. Drawn in Inter Medium at
# 8pt and 720 dpi on a transparent line box of the sidebar's line height (1.45),
# with the baseline where the text's own would sit, so it lines up as text does.
encoded = re.search(r'emailEncoded: "([^"]+)"', (repo / "data/resume.ts").read_text()).group(1)
email = base64.b64decode(encoded).decode()[::-1]
em = 80
font = ImageFont.truetype(str(Path(__file__).parent / "fonts/Inter-Medium.ttf"), em)
ascent, descent = font.getmetrics()
line = round(1.45 * em)
baseline = (line - (ascent + descent)) / 2 + ascent
width = round(font.getlength(email)) + 2
canvas = Image.new("RGBA", (width, line), (0, 0, 0, 0))
ImageDraw.Draw(canvas).text((0, baseline), email, font=font, fill=(255, 255, 255, 255), anchor="ls")
canvas.save(out / "email.png")

segno.make("https://adminout.net/resume/portfolio", error="m").save(
    out / "qr-portfolio.svg", scale=4, border=0, dark="#172A2E", light=None)
