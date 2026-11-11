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
