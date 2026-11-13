import math, random, re

def branch(x,y,ang,length,w,depth,out,rnd,spread,shrink,taper,minw):
    if depth==0 or length<3: return
    x2=x+math.cos(ang)*length; y2=y+math.sin(ang)*length
    mx=(x+x2)/2+math.cos(ang+math.pi/2)*length*rnd.uniform(-0.10,0.10)
    my=(y+y2)/2+math.sin(ang+math.pi/2)*length*rnd.uniform(-0.10,0.10)
    out.append((f"M{x:.1f} {y:.1f} Q{mx:.1f} {my:.1f} {x2:.1f} {y2:.1f}", w))
    n=2 if depth>2 else rnd.choice([2,2,3])
    for i in range(n):
        t=(i/(n-1))*2-1 if n>1 else 0
        a2=ang+t*spread*rnd.uniform(0.75,1.25)+rnd.uniform(-0.08,0.08)
        branch(x2,y2,a2,length*shrink*rnd.uniform(0.86,1.0),max(minw,w*taper),
               depth-1,out,rnd,spread*0.92,shrink,taper,minw)

def make(seed,trunk_w,limb_w,taper,minw,depth):
    rnd=random.Random(seed); out=[]
    cx,base=500,452; top=base-70
    out.append((f"M{cx} {base} L{cx} {top}",trunk_w))
    for a in (-math.pi/2-0.78,-math.pi/2-0.26,-math.pi/2+0.26,-math.pi/2+0.78):
        branch(cx,top,a,66,limb_w,depth,out,rnd,0.60,0.78,taper,minw)
    for a in (math.pi/2-0.95,math.pi/2-0.38,math.pi/2+0.38,math.pi/2+0.95):
        branch(cx,base,a,52,limb_w*0.86,depth-1,out,rnd,0.46,0.72,taper,minw)
    return out

FONT="'Archivo','Inter','Archivo Black','Arial Black',sans-serif"
SERIF="Georgia,'Bitstream Charter','Times New Roman',serif"

def emit(path,segs):
    xs=[];ys=[]
    for d,w in segs:
        for a,b in re.findall(r'(-?\d+\.?\d*) (-?\d+\.?\d*)',d): xs.append(float(a)); ys.append(float(b))
    dx=500-(min(xs)+max(xs))/2; dy=248-min(ys); tag=dy+max(ys)+52; H=int(tag+40)
    body="\n".join(f'    <path d="{d}" stroke-width="{w:.1f}"/>' for d,w in segs)
    open(path,"w").write(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 {H}" width="1000" height="{H}">
  <rect width="1000" height="{H}" fill="#ffffff"/>
  <text x="500" y="132" text-anchor="middle" font-family="{FONT}" font-size="132" font-weight="900" fill="#171717" letter-spacing="-1">GRIMWOOD</text>
  <text x="500" y="180" text-anchor="middle" font-family="{FONT}" font-size="30" font-weight="600" fill="#171717" letter-spacing="9">CARTAGE &amp; FREIGHT</text>
  <g transform="translate({dx:.1f},{dy:.1f})" stroke="#c45c26" fill="none" stroke-linecap="round" stroke-linejoin="round">
{body}
  </g>
  <text x="500" y="{tag:.0f}" text-anchor="middle" font-family="{SERIF}" font-size="27" font-style="italic" fill="#171717">If it moved, we moved it.</text>
</svg>
''')

# a: current.  b: heavier.  c: heaviest, fewer twigs.
emit("w_a.svg", make(31, 11, 7.0, 0.62, 0.9, 5))
emit("w_b.svg", make(31, 17, 11.0, 0.70, 1.8, 5))
emit("w_c.svg", make(31, 23, 15.0, 0.74, 3.0, 4))
print("ok")

def emit_air(path, segs):
    xs=[];ys=[]
    for d,w in segs:
        for a,b in re.findall(r'(-?\d+\.?\d*) (-?\d+\.?\d*)',d): xs.append(float(a)); ys.append(float(b))
    dx=500-(min(xs)+max(xs))/2; dy=282-min(ys); tag=dy+max(ys)+52; H=int(tag+40)
    body="\n".join(f'    <path d="{d}" stroke-width="{w:.1f}"/>' for d,w in segs)
    open(path,"w").write(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 {H}" width="1000" height="{H}">
  <rect width="1000" height="{H}" fill="#ffffff"/>
  <text x="500" y="132" text-anchor="middle" font-family="{FONT}" font-size="132" font-weight="900" fill="#171717" letter-spacing="-1">GRIMWOOD</text>
  <text x="500" y="180" text-anchor="middle" font-family="{FONT}" font-size="30" font-weight="600" fill="#171717" letter-spacing="9">CARTAGE &amp; FREIGHT</text>
  <text x="500" y="216" text-anchor="middle" font-family="{FONT}" font-size="30" font-weight="600" fill="#171717" letter-spacing="9">AIR DIVISION</text>
  <g transform="translate({dx:.1f},{dy:.1f})" stroke="#c45c26" fill="none" stroke-linecap="round" stroke-linejoin="round">
{body}
  </g>
  <text x="500" y="{tag:.0f}" text-anchor="middle" font-family="{SERIF}" font-size="27" font-style="italic" fill="#171717">If it moved, we moved it.</text>
</svg>
''')

S = make(31, 17, 11.0, 0.70, 1.8, 5)
emit("grimwood_cartage_white.svg", S)
emit_air("grimwood_cartage_air_white.svg", S)
print("final written")
