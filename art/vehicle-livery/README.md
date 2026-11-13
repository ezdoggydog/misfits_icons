# Vehicle livery

Artwork for painting vehicles: wordmarks, door marks and stencils, by company.

Everything here is **flat, clean and unweathered on a transparent background**. The
distressing belongs to the vehicle, not to the artwork — age it when you apply it, so the
same file can be used on a new van and a forty-year-old one.

SVG is the source. The PNGs are rendered from it at a size that suits a texture; if you need
another size, render the SVG rather than scaling the PNG. The generators are in `tools/`
(`tree.py`, `door_lockup.py`, `strip_lockup.py`, `rear_notice.py`, `old_lockup.py`).

Type is `Archivo / Inter / Arial Black`; the tagline is Georgia italic.

---

## grimwood/ — Grimwood Cartage & Freight

Two marks. **The old mark goes only on the old black stepvan; everything newer takes the new
one.** That is deliberate — the fleet modernised and the old truck did not.

### The new fleet (white Transits)

| File | Where it goes |
|---|---|
| `grimwood_cartage_white` | the flank of a panel van or box truck |
| `grimwood_cartage_air_white` | same, with AIR DIVISION |
| `grimwood_cartage_door_tree` | cab door — tree left, wordmark stacked right |
| `grimwood_cartage_door` | cab door, wordmark only, where the tree won't survive the resolution |
| `grimwood_cartage_strip` / `_oneline` | a long shallow panel, such as a dropside's drop gate |
| `grimwood_tree` | the mark alone |

A flatbed has no panel to paint, so it splits: **tree on the cab door, wordmark along the
gate.** Near-black lettering, tree in rust orange (`#c45c26`).

**The new mark carries no tagline.** A company that had modernised would have retired a 1931
slogan, so the old truck keeps something the new ones don't. Don't add it back.

### The old stepvan

| File | Where it goes |
|---|---|
| `grimwood_cartage_old` | the flank — wordmark, tree and tagline, all in rust orange |
| `grimwood_rear_notice` | NO VALUABLES LEFT IN THIS VEHICLE OVERNIGHT, centred, rear doors |

The rear notice is a stencil rather than a logo, so it can go on any Grimwood body with a
back door, the new fleet included.

Reference photographs of the real thing are in `art/vans/`.

### Sizing notes

- The tree should fill most of a cab door. Its outer twigs are thin, and small it turns into
  an orange smudge.
- `CARTAGE & FREIGHT` is the first thing to disappear at distance. That's fine — the name is
  what has to read — but don't shrink it further.
- Never mirror any of this. It has lettering in it.
