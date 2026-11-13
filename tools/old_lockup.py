import math, random, re
exec(open('tree2.py').read().split('emit("r1.svg"')[0])

S = make(31, root_depth=3, root_len=40, root_squash=0.42, root_spread=0.30)
xs=[];ys=[]
for d,w in S:
    for a,b in re.findall(r'(-?\d+\.?\d*) (-?\d+\.?\d*)',d): xs.append(float(a)); ys.append(float(b))
tw, th = max(xs)-min(xs), max(ys)-min(ys)

ORANGE = "#c45c26"
FONT  = "'Archivo','Inter','Archivo Black','Arial Black',sans-serif"
SERIF = "Georgia,'Bitstream Charter','Times New Roman',serif"

W, H = 1100, 740
cx = W//2
tree_h = 360.0
s = tree_h/th
dx = cx - (min(xs)+max(xs))/2*s
dy = 270 - min(ys)*s

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
  <text x="{cx}" y="150" text-anchor="middle" font-family="{FONT}" font-size="150" font-weight="900" fill="{ORANGE}" letter-spacing="1">GRIMWOOD</text>
  <text x="{cx}" y="212" text-anchor="middle" font-family="{FONT}" font-size="52" font-weight="700" fill="{ORANGE}" letter-spacing="5">CARTAGE &amp; FREIGHT</text>
  <g transform="translate({dx:.1f},{dy:.1f}) scale({s:.4f})" stroke="{ORANGE}" fill="none" stroke-linecap="round" stroke-linejoin="round">
{chr(10).join(f'    <path d="{d}" stroke-width="{w:.1f}"/>' for d,w in S)}
  </g>
  <text x="{cx}" y="{H-30}" text-anchor="middle" font-family="{SERIF}" font-size="58" font-style="italic" fill="{ORANGE}">If it moved, we moved it.</text>
</svg>
'''
open("grimwood_cartage_old.svg","w").write(svg)
print("ok")
