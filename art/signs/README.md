# Signs

Every sign in the world, in one place. `*_original.png` is the generator's output as it came
back; the file without the suffix is the one that has been cleaned, trimmed or had text set into
it, and that is the one to use.

## Gambini & Sons — towing, recovery, impound

Gunny's business. He **is** Gambini; "Gunny" is what people call a Gunnery Sergeant. See
`misfits-plugins/notes/GUNNY_ART_BRIEF.md` and `notes/SUNNY.md`.

| File | What it is | Where it goes |
|---|---|---|
| `gambini_and_sons_sign.png` | Bulb-lit marquee lockup, "Taking Things Back Since Before You Were Born" | gate sign, and anything seen up close |
| `gambini_painted_panel.png` | The same mark hand-painted on a rusted steel panel, heavily weathered | a flat panel, or the garage door |
| `gambini_impound_fees.png` | Fee schedule, numbers set: 25 / 5 / 10 / 20 | the impound office wall, where the player stands to argue |
| `gambini_impound_fees_blank.png` | Same sign, leaders empty | reset the figures when the plugin's prices change |
| `sign_gambini_towing.png` | The three-generations sign — Grandpa, Dad, Son | the yard |

**The fee sign carries the whole joke**: PRICES NEGOTIABLE (upward, one scrap per attempt), and
SOLD FOR SCRAP AFTER 30 DAYS in the smallest type on the board. The mechanics are in
`notes/SUNNY.md`.

**No NO PARKING sign exists, and none should.** The gag is that there are no signs; Sunny hands
the player one across the counter when they push it. Putting one up in the street kills it.

## Grimwood

| File | What it is |
|---|---|
| `sign_grimwood_financial.png` | Grimwood Financial |
| `sign_grimwood_mutual.png` | Grimwood Mutual |

## The car trade

| File | What it is |
|---|---|
| `sign_honest_joes.png` | Honest Joe's — the lot O'Malley's took over |
| `vinnies_billboard.png`, `_v2` | Vinnie's billboard, two versions |
| `sign_customer_of_the_month.png` | Customer of the month |

## The road

| File | What it is |
|---|---|
| `sign_welcome.png` | Coming into town |
| `sign_leaving.png` | Leaving |
| `sign_leaving_horseman.png` | Leaving, the horseman version |

---

## Using one on a garage door

The door's panels are **x 0–1777, y 170–2048** of a 2048 sheet, measured from
`wall.frame.garagedoor.obj`; the rest is edges and rollers. `art/skins/garagedoor_uv_template_2048.png`
is the UV wireframe rendered from the model and will serve any door skin.

Two shapes of job:

- **A sign plate on a door** — the sign is a rectangle bolted to a painted door. Used for
  `gambini_garagedoor_diffuse` and `grimwood_garagedoor_diffuse`.
- **A painted door** — the artwork IS the door surface, extended to fill the panel. Used for
  `gambini_painted_garagedoor_diffuse`.

**Extend with synthesised texture, never by mirroring.** Mirroring the panel to fill height drags
reversed lettering into frame, which breaks our own icon rule and looks it. Tiling a narrow strip
turns into vertical wallpaper. Noise at three scales, in colours sampled from the artwork's own
plain areas, has no repeat to spot.

Pair every diffuse with a **matte spec map** (flat dark grey). Without one a dark door becomes a
black mirror in game — see `misfits-plugins/notes/RUST_BUILDING_FACTS.md`.
