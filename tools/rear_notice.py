ORANGE = "#c45c26"
FONT = "'Archivo','Inter','Archivo Black','Arial Black',sans-serif"
lines = ["NO VALUABLES", "LEFT IN THIS VEHICLE", "OVERNIGHT"]
size, lead, ls = 86, 112, 4.5
pad = 40
W, H = 1180, pad*2 + lead*(len(lines)-1) + size
rows = "\n".join(
    f'  <text x="{pad}" y="{pad + size*0.80 + i*lead:.0f}" font-family="{FONT}" font-size="{size}" '
    f'font-weight="700" fill="{ORANGE}" letter-spacing="{ls}">{t}</text>'
    for i, t in enumerate(lines))
open("grimwood_rear_notice.svg","w").write(
f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
{rows}
</svg>
''')
print("ok", W, H)
