FONT="'Archivo','Inter','Archivo Black','Arial Black',sans-serif"
# one line, for a shallow drop gate
W,H = 1400, 170
open("grimwood_cartage_strip.svg","w").write(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
  <rect width="{W}" height="{H}" fill="#ffffff"/>
  <text x="{W//2}" y="92" text-anchor="middle" font-family="{FONT}" font-size="84" font-weight="900" fill="#171717" letter-spacing="-0.5">GRIMWOOD</text>
  <text x="{W//2}" y="132" text-anchor="middle" font-family="{FONT}" font-size="26" font-weight="600" fill="#171717" letter-spacing="10">CARTAGE &amp; FREIGHT</text>
</svg>
''')
# even shallower: everything on one line
W2,H2 = 1600, 120
open("grimwood_cartage_strip_oneline.svg","w").write(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W2} {H2}" width="{W2}" height="{H2}">
  <rect width="{W2}" height="{H2}" fill="#ffffff"/>
  <text x="{W2//2}" y="82" text-anchor="middle" font-family="{FONT}" font-size="72" font-weight="900" fill="#171717" letter-spacing="-0.5">GRIMWOOD <tspan font-size="40" font-weight="600" letter-spacing="7">CARTAGE &amp; FREIGHT</tspan></text>
</svg>
''')
print("ok")
