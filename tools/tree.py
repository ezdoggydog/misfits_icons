import math, random, re

def branch(x,y,ang,length,w,depth,out,rnd,spread,shrink,taper,minw,ysquash=1.0):
    if depth==0 or length<3: return
    x2=x+math.cos(ang)*length; y2=y+math.sin(ang)*length*ysquash
    mx=(x+x2)/2+math.cos(ang+math.pi/2)*length*rnd.uniform(-0.10,0.10)
    my=(y+y2)/2+math.sin(ang+math.pi/2)*length*rnd.uniform(-0.10,0.10)
    out.append((f"M{x:.1f} {y:.1f} Q{mx:.1f} {my:.1f} {x2:.1f} {y2:.1f}", w))
    n=2 if depth>2 else rnd.choice([2,2,3])
    for i in range(n):
        t=(i/(n-1))*2-1 if n>1 else 0
        a2=ang+t*spread*rnd.uniform(0.75,1.25)+rnd.uniform(-0.08,0.08)
        branch(x2,y2,a2,length*shrink*rnd.uniform(0.86,1.0),max(minw,w*taper),
               depth-1,out,rnd,spread*0.92,shrink,taper,minw,ysquash)

def make(seed, root_depth=3, root_len=40, root_squash=0.42, root_spread=0.30, crown_len=72):
    rnd=random.Random(seed); out=[]
    cx,base=500,452; top=base-78
    out.append((f"M{cx} {base} L{cx} {top}",18))
    for a in (-math.pi/2-0.80,-math.pi/2-0.27,-math.pi/2+0.27,-math.pi/2+0.80):
        branch(cx,top,a,crown_len,11.5,5,out,rnd,0.60,0.78,0.70,1.8)
    # roots: wide, flat, short, blunt -- not a mirrored crown
    for a in (math.pi/2-1.18, math.pi/2-0.52, math.pi/2+0.52, math.pi/2+1.18):
        branch(cx,base,a,root_len,11.0,root_depth,out,rnd,root_spread,0.62,0.66,2.6,root_squash)
    return out

FONT="'Archivo','Inter','Archivo Black','Arial Black',sans-serif"

def emit(path,segs):
    xs=[];ys=[]
    for d,w in segs:
        for a,b in re.findall(r'(-?\d+\.?\d*) (-?\d+\.?\d*)',d): xs.append(float(a)); ys.append(float(b))
    dx=500-(min(xs)+max(xs))/2; dy=248-min(ys); H=int(dy+max(ys)+56)
    body="\n".join(f'    <path d="{d}" stroke-width="{w:.1f}"/>' for d,w in segs)
    open(path,"w").write(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 {H}" width="1000" height="{H}">
  <rect width="1000" height="{H}" fill="#ffffff"/>
  <text x="500" y="132" text-anchor="middle" font-family="{FONT}" font-size="132" font-weight="900" fill="#171717" letter-spacing="-1">GRIMWOOD</text>
  <text x="500" y="180" text-anchor="middle" font-family="{FONT}" font-size="30" font-weight="600" fill="#171717" letter-spacing="9">CARTAGE &amp; FREIGHT</text>
  <g transform="translate({dx:.1f},{dy:.1f})" stroke="#c45c26" fill="none" stroke-linecap="round" stroke-linejoin="round">
{body}
  </g>
</svg>
''')

emit("r1.svg", make(31, root_depth=3, root_len=40, root_squash=0.42, root_spread=0.30))
emit("r2.svg", make(31, root_depth=2, root_len=46, root_squash=0.30, root_spread=0.26))
emit("r3.svg", make(31, root_depth=2, root_len=34, root_squash=0.22, root_spread=0.22))
print("ok")

def emit_air(path,segs):
    xs=[];ys=[]
    for d,w in segs:
        for a,b in re.findall(r'(-?\d+\.?\d*) (-?\d+\.?\d*)',d): xs.append(float(a)); ys.append(float(b))
    dx=500-(min(xs)+max(xs))/2; dy=284-min(ys); H=int(dy+max(ys)+56)
    body="\n".join(f'    <path d="{d}" stroke-width="{w:.1f}"/>' for d,w in segs)
    open(path,"w").write(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 {H}" width="1000" height="{H}">
  <rect width="1000" height="{H}" fill="#ffffff"/>
  <text x="500" y="132" text-anchor="middle" font-family="{FONT}" font-size="132" font-weight="900" fill="#171717" letter-spacing="-1">GRIMWOOD</text>
  <text x="500" y="180" text-anchor="middle" font-family="{FONT}" font-size="30" font-weight="600" fill="#171717" letter-spacing="9">CARTAGE &amp; FREIGHT</text>
  <text x="500" y="216" text-anchor="middle" font-family="{FONT}" font-size="30" font-weight="600" fill="#171717" letter-spacing="9">AIR DIVISION</text>
  <g transform="translate({dx:.1f},{dy:.1f})" stroke="#c45c26" fill="none" stroke-linecap="round" stroke-linejoin="round">
{body}
  </g>
</svg>
''')

def emit_mark(path, segs):
    xs=[];ys=[]
    for d,w in segs:
        for a,b in re.findall(r'(-?\d+\.?\d*) (-?\d+\.?\d*)',d): xs.append(float(a)); ys.append(float(b))
    W=int(max(xs)-min(xs)+40); H=int(max(ys)-min(ys)+40)
    dx=20-min(xs); dy=20-min(ys)
    body="\n".join(f'    <path d="{d}" stroke-width="{w:.1f}"/>' for d,w in segs)
    open(path,"w").write(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
  <rect width="{W}" height="{H}" fill="#ffffff"/>
  <g transform="translate({dx:.1f},{dy:.1f})" stroke="#c45c26" fill="none" stroke-linecap="round" stroke-linejoin="round">
{body}
  </g>
</svg>
''')

S = make(31, root_depth=3, root_len=40, root_squash=0.42, root_spread=0.30)
emit("grimwood_cartage_white.svg", S)
emit_air("grimwood_cartage_air_white.svg", S)
emit_mark("grimwood_tree.svg", S)
print("final")
