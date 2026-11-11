#!/usr/bin/env python3
"""Cut a Karuza preview into an MVM shop icon (512 + 128, transparent).

Karuza's previews sit on their dark navy (2,6,23). This lifts the subject off it, mirrors to
front-left, scales every icon so the subject fills the same fraction of the square (so a shop grid
looks even however the source was framed), and writes <key>.png and <key>_icon_128.png.

    python3 tools/cut_karuza_icon.py <image> <key> [--no-mirror]

--no-mirror for anything with LETTERING on it. Never mirror text: the PoliceBird, the Cobras'
MARINES, the KPC van, Karuza Express semis, kart numbers. See notes/ICON_JOB.md in misfits-plugins.

Background is found by flood from the border, so navy trapped inside the frame stays; only large
enclosed patches (wheel centres) are cleared. The cut is tight (distance < 16) so black paint and
dark visors survive -- that is the whole difficulty with these.
"""
import sys
from PIL import Image
import numpy as np
from scipy import ndimage

FILL = 0.94          # subject's long side as a fraction of the 512 square
THRESHOLD = 16       # colour distance from the navy that still counts as background
ENCLOSED_MIN = 3000  # enclosed navy patches bigger than this are cleared, smaller ones kept

def cut(path, key, mirror=True):
    a = np.asarray(Image.open(path).convert("RGB")).astype(int)
    bg = a[2, 2]
    navy = np.sqrt(((a - bg) ** 2).sum(axis=2)) < THRESHOLD
    lab, n = ndimage.label(navy)
    edge = (set(lab[0, :]) | set(lab[-1, :]) | set(lab[:, 0]) | set(lab[:, -1])) - {0}
    back = np.isin(lab, list(edge))
    for i in range(1, n + 1):
        if i not in edge and (lab == i).sum() > ENCLOSED_MIN:
            back |= (lab == i)
    al = ndimage.uniform_filter(np.where(back, 0, 255).astype(float), size=3)
    al = np.where(back & (al < 60), 0, al).astype(np.uint8)

    # Drop specks and stray lines before cropping. Some previews carry a faint 1px band out to the
    # frame edge; left in, it inflates the bounding box and the bike ends up tiny in its square.
    solid = al > 40
    lab2, m = ndimage.label(solid)
    if m > 1:
        sizes = ndimage.sum(solid, lab2, range(1, m + 1))
        biggest = sizes.max()
        keep = {i + 1 for i, s in enumerate(sizes) if s >= biggest * 0.01}
        al = np.where(np.isin(lab2, list(keep)) | (lab2 == 0) & False, al, 0).astype(np.uint8)

    im = Image.fromarray(np.dstack([a.astype(np.uint8), al]), "RGBA")
    im = im.crop(im.getbbox())
    if mirror:
        im = im.transpose(Image.FLIP_LEFT_RIGHT)
    sc = int(512 * FILL) / max(im.size)
    im = im.resize((max(1, round(im.width * sc)), max(1, round(im.height * sc))), Image.LANCZOS)
    sq = Image.new("RGBA", (512, 512), (0, 0, 0, 0))
    sq.paste(im, ((512 - im.width) // 2, (512 - im.height) // 2))
    sq.save(f"{key}.png")
    sq.resize((128, 128), Image.LANCZOS).save(f"{key}_icon_128.png")
    print(f"{key}.png + {key}_icon_128.png   ({'mirrored' if mirror else 'NOT mirrored - lettering'})")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(__doc__); sys.exit(1)
    cut(sys.argv[1], sys.argv[2], "--no-mirror" not in sys.argv)
