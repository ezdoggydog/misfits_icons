import math, random, re
exec(open('tree.py').read().split('for seed in')[0])

segs = make(31)
xs, ys = [], []
for d, w in segs:
    for mx, my in re.findall(r'(-?\d+\.?\d*) (-?\d+\.?\d*)', d):
        xs.append(float(mx)); ys.append(float(my))
tminx, tmaxx, tminy, tmaxy = min(xs), max(xs), min(ys), max(ys)

def tree_group(dx, dy, scale=1.0):
    body = "\n".join(f'    <path d="{d}" stroke-width="{w:.1f}"/>' for d, w in segs)
    return (f'  <g transform="translate({dx:.1f},{dy:.1f}) scale({scale})" '
            f'stroke="#c45c26" fill="none" stroke-linecap="round" stroke-linejoin="round">\n{body}\n  </g>')

FONT = "'Archivo','Inter','Archivo Black','Arial Black',sans-serif"
SERIF = "Georgia,'Bitstream Charter','Times New Roman',serif"

def build(path, air=False):
    W, H = 1000, 640
    cx = 500
    y_word, y_sub = 132, 180
    y_air = 216
    tree_top = 248 if not air else 282
    s = 1.0
    dx = cx - (tminx + tmaxx) / 2 * s
    dy = tree_top - tminy * s
    tag_y = dy + tmaxy * s + 52
    H = int(tag_y + 40)
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">',
             f'  <rect width="{W}" height="{H}" fill="#ffffff"/>',
             f'  <text x="{cx}" y="{y_word}" text-anchor="middle" font-family="{FONT}" font-size="132" font-weight="900" fill="#171717" letter-spacing="-1">GRIMWOOD</text>',
             f'  <text x="{cx}" y="{y_sub}" text-anchor="middle" font-family="{FONT}" font-size="30" font-weight="600" fill="#171717" letter-spacing="9">CARTAGE &amp; FREIGHT</text>']
    if air:
        parts.append(f'  <text x="{cx}" y="{y_air}" text-anchor="middle" font-family="{FONT}" font-size="30" font-weight="600" fill="#171717" letter-spacing="9">AIR DIVISION</text>')
    parts.append(tree_group(dx, dy, s))
    parts.append(f'  <text x="{cx}" y="{tag_y:.0f}" text-anchor="middle" font-family="{SERIF}" font-size="27" font-style="italic" fill="#171717">If it moved, we moved it.</text>')
    parts.append('</svg>')
    open(path, "w").write("\n".join(parts) + "\n")

def door(path):
    W, H = 760, 150
    open(path, "w").write(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
  <rect width="{W}" height="{H}" fill="#ffffff"/>
  <text x="{W//2}" y="78" text-anchor="middle" font-family="{FONT}" font-size="72" font-weight="900" fill="#171717" letter-spacing="-0.5">GRIMWOOD</text>
  <text x="{W//2}" y="112" text-anchor="middle" font-family="{FONT}" font-size="20" font-weight="600" fill="#171717" letter-spacing="7">CARTAGE &amp; FREIGHT</text>
</svg>
''')

build("grimwood_cartage_white.svg")
build("grimwood_cartage_air_white.svg", air=True)
door("grimwood_cartage_door.svg")
print("ok")
