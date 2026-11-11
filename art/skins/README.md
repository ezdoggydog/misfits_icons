# Stripe overlays for clothing skins

Transparent PNGs to upload as the overlay layer in the skin editor. The stripes are **white at low
alpha**, not a color, so they lighten whatever base is underneath and the hue matches on its own.
The same file works over Vinnie's purple, a gray suit, or anything else.

Made Nov 11, 2026 for **Vinnie's purple suit** (`jacket.snow` + `pants`, base `#5B3B7E`).

| File | Stripe / pitch (at 1024) | Alpha | Stripes across |
|---|---|---|---|
| `chalkstripe_*` | 4px / 34px | 25% | ~31 |
| `pinstripe_*` | 3px / 16px | 18% | ~64 |
| `pinstripe_subtle_*` | 2px / 14px | 13% | ~74 |

**Use the chalkstripe.** Both finer ones were tested by shrinking to player-distance scale and they
collapse into uneven banding — moiré, the stripes beating against the pixel grid. The chalkstripe
survives it and still reads as a striped suit from across the room. It's also the period-correct
choice for a mob suit, which is a happy accident.

`preview_1to1.png` and `preview_at_distance.png` show all three over `#5B3B7E` — the distance one
is the argument.

**The catch: vertical in the texture is not vertical on the model.** A Rust garment is unwrapped
into islands and some are rotated, so stripes can come out diagonal on sleeves or the back even
when they're perfectly vertical here. Check the sleeves and the back in the editor's preview before
committing. If an island runs the wrong way, that's the UV layout, not the file.

Regenerate or change the spacing with the script in the commit that added this folder.

## Baked base textures (Nov 11, 2026)

`vinnie_suit_base_1024/2048.png` — **opaque**, `#5B3B7E` with the chalkstripe already composited,
edge to edge. For a tool that takes a whole texture rather than a transparent overlay.

Why they exist: in My Server Gear (Windows desktop app), the transparent overlay landed on the
torso front only and left the sleeves flat purple. The overlay file covers the entire square, so
the tool is placing it as a region decal, not across the UV. A complete texture should reach
everything the UV touches.

A Rust clothing skin is, underneath, one full texture over the item's UV — whatever the tool's UI
calls it. So the thing to look for in any skin app is a template download or a full-texture import.

## Skin IDs

| Skin | ID | Worn by |
|---|---|---|
| [Vinnie's purple pinstripe coat](https://steamcommunity.com/sharedfiles/filedetails/?id=3837745342) (`jacket.snow`) | **3837745342** | Vinnie — in GrimwoodStory's `DefaultWear` since 1.9.2 |
| [Vinnie's purple pinstripe trousers](https://steamcommunity.com/sharedfiles/filedetails/?id=3837747305) (`pants`) | **3837747305** | Vinnie — since 1.9.3. Built from the **denser** trousers file, see below |
| Black boots (`shoes.boots`) | **2552297736** | Vinnie — since 1.9.5. **Not ours**, an existing public workshop skin, so no upload or visibility to manage |
| [Gunny's red PT shirt](https://steamcommunity.com/sharedfiles/filedetails/?id=3837763379) (`tshirt`) | **3837763379** | Gunny — since 1.9.7. Faded brick `#8E3A33`, gold `#C2A964`, EGA on the left chest and the full lockup across the back |
| Blue jeans (`pants`) | **3686433346** | Gunny — since 1.9.8. **Not ours.** Mid-indigo, honest fade, orange contrast stitching |
| Black fedora (`hat.boonie`) | **2255866690** | Vinnie — since 1.9.6. Also not ours. A boonie underneath, but the skin gives it a pinched crown and a firm brim, so it reads as a real fedora |

`jacket.snow`, not `jacket`: it's the only Rust coat with real lapels, and lapels are what make a
jacket read as a suit. The field jacket has a zip and a shirt collar and reads as a purple coat.

Still to make: cream `shirt.collared` (`#EADFC8`), for the light behind the lapel V.

Measured after the reskin: 21 stripes across the hips against the coat's 22 across the chest. They
read as one cloth now.

## Trousers need a denser file than the coat (Nov 11, 2026)

Measured off the renders: the coat shows **22 stripes across the full chest front** (~11 per
panel), the trousers only 12 across both legs at the hip. Same file, different UV magnification —
so on the body the trouser stripes sit about **1.6x further apart** than the coat's. On a real suit
those pitches are identical, so the mismatch reads as separates rather than a suit.

`chalkstripe_trousers_*` and `vinnie_trousers_base_*` are 1.6x denser (pitch 21px at 1024 against
the coat's 34px) to come out matching once the UV has stretched them. Use these for `pants` and the
ordinary chalkstripe for `jacket.snow`.

**The general rule: match the stripes on the body, not in the file.** Every garment magnifies the
texture differently, so the same file on two pieces will not match. Measure on the model.

**Workshop visibility must be Public.** Other players' clients fetch the texture from the workshop,
so a skin set to Friends Only, Unlisted or Private shows correctly for whoever made it and as the
default item for everyone else. That's the usual reason a server skin "works" and then doesn't.
Facepunch approval is not needed — that only matters for the in-game item store; a published
workshop skin works by ID on a server regardless.

## Black on black needs a value difference, not a color difference (Nov 11, 2026)

A boot skin painted flat `#000000` came back as a boot-shaped hole — no laces, no toe cap, no sole,
just a silhouette. Rust's lighting can't pull shape out of a texture that has none in it. The one
that worked keeps the laces, toe and sole readable at different values while still reading black.

Same lesson as the pinstripes: contrast carries the form, color only carries the mood.

## Vinnie's outfit, finished (GrimwoodStory 1.9.5)

`jacket.snow` (purple pinstripe) + `pants` (purple pinstripe, denser file) + `shoes.boots` (black).
**No shirt**, deliberately: a shirt and a jacket both want the chest body slot, so whichever is
listed first wins and the other is created and silently thrown away. That cost us an evening — it
looked exactly like a skin failing to load. Since 1.9.4 the plugin prints a warning naming the
garment it couldn't put on.

Plus the fedora. **No shirt and no other headwear** — a shirt would fight the coat for the chest
slot, and a second hat is impossible anyway.

**One loud thing at a time.** A pinstriped boonie with playing cards in the band was considered and
rejected: the suit is already the loud thing, and a second stripe pattern at a different scale
fights the one we spent the evening matching. Plain black hat, plain black boots, loud suit.
