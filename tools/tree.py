import math, random

def branch(x, y, ang, length, w, depth, out, rnd, spread, shrink):
    if depth == 0 or length < 3:
        return
    x2 = x + math.cos(ang) * length
    y2 = y + math.sin(ang) * length
    # slight bow in the limb
    mx = (x + x2) / 2 + math.cos(ang + math.pi/2) * length * rnd.uniform(-0.12, 0.12)
    my = (y + y2) / 2 + math.sin(ang + math.pi/2) * length * rnd.uniform(-0.12, 0.12)
    out.append((f"M{x:.1f} {y:.1f} Q{mx:.1f} {my:.1f} {x2:.1f} {y2:.1f}", w))
    n = 2 if depth > 2 else rnd.choice([2, 2, 3])
    for i in range(n):
        t = (i / (n - 1)) * 2 - 1 if n > 1 else 0
        a2 = ang + t * spread * rnd.uniform(0.75, 1.25) + rnd.uniform(-0.09, 0.09)
        branch(x2, y2, a2, length * shrink * rnd.uniform(0.85, 1.0),
               max(0.9, w * 0.62), depth - 1, out, rnd, spread * 0.92, shrink)

def make(seed):
    rnd = random.Random(seed)
    out = []
    cx, base = 500, 452          # where trunk meets ground
    top = base - 70              # crown starts
    out.append((f"M{cx} {base} L{cx} {top}", 11))
    # crown: three main limbs up and out
    for a in (-math.pi/2 - 0.78, -math.pi/2 - 0.26, -math.pi/2 + 0.26, -math.pi/2 + 0.78):
        branch(cx, top, a, 66, 7.0, 5, out, rnd, 0.60, 0.78)
    # roots: mirror of the crown, shallower and wider
    for a in (math.pi/2 - 0.95, math.pi/2 - 0.38, math.pi/2 + 0.38, math.pi/2 + 0.95):
        branch(cx, base, a, 52, 6.0, 4, out, rnd, 0.46, 0.72)
    return out

for seed in (7, 19, 23, 31):
    segs = make(seed)
    paths = "\n".join(f'    <path d="{d}" stroke-width="{w:.1f}"/>' for d, w in segs)
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 680" width="1000" height="680">
  <rect width="1000" height="680" fill="#ffffff"/>
  <text x="500" y="150" text-anchor="middle" font-family="'Archivo','Inter',sans-serif" font-size="132" font-weight="900" fill="#171717" letter-spacing="-1">GRIMWOOD</text>
  <text x="500" y="200" text-anchor="middle" font-family="'Archivo','Inter',sans-serif" font-size="30" font-weight="600" fill="#171717" letter-spacing="9">CARTAGE &amp; FREIGHT</text>
  <g stroke="#c45c26" fill="none" stroke-linecap="round" stroke-linejoin="round">
{paths}
  </g>
  <text x="500" y="620" text-anchor="middle" font-family="Georgia,'Bitstream Charter',serif" font-size="27" font-style="italic" fill="#171717">If it moved, we moved it.</text>
</svg>'''
    open(f"t{seed}.svg", "w").write(svg)
print("built")
