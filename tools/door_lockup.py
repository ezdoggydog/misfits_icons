import re
exec(open('tree2.py').read().split('emit("r1.svg"')[0])
S = make(31, root_depth=3, root_len=40, root_squash=0.42, root_spread=0.30)
xs=[];ys=[]
for d,w in S:
    for a,b in re.findall(r'(-?\d+\.?\d*) (-?\d+\.?\d*)',d): xs.append(float(a)); ys.append(float(b))
tw, th = max(xs)-min(xs), max(ys)-min(ys)

def horiz(path, H=200, pad=18):
    s = (H - pad*2) / th
    dx = pad - min(xs)*s; dy = pad - min(ys)*s
    body="\n".join(f'    <path d="{d}" stroke-width="{w:.1f}"/>' for d,w in S)
    tx = pad + tw*s + 30
    W = int(tx + 440)
    open(path,"w").write(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
  <rect width="{W}" height="{H}" fill="#ffffff"/>
  <g transform="translate({dx:.1f},{dy:.1f}) scale({s:.3f})" stroke="#c45c26" fill="none" stroke-linecap="round" stroke-linejoin="round">
{body}
  </g>
  <text x="{tx:.0f}" y="{H*0.52:.0f}" font-family="{FONT}" font-size="62" font-weight="900" fill="#171717" letter-spacing="-0.5">GRIMWOOD</text>
  <text x="{tx:.0f}" y="{H*0.52+32:.0f}" font-family="{FONT}" font-size="18" font-weight="600" fill="#171717" letter-spacing="6.4">CARTAGE &amp; FREIGHT</text>
</svg>
''')
horiz("door_tree.svg")
print("ok")
