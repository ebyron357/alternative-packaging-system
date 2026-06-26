# ALTERNATIVE™ — PHASE 3 ILLUSTRATOR PRODUCTION SETUP
**Document:** Phase 3 Specification — Illustrator Document Setup + Placeholder Construction
**Program Director:** Claude (AI Production System)
**Date:** 2026-06-26
**Version:** 1.0
**Status:** ✅ READY TO EXECUTE — Proceed with TEMPORARY placeholders per approved directive

---

## EXECUTIVE SUMMARY

Phase 3 proceeds using TEMP_HERO_A and TEMP_WORDMARK placeholders per client directive (2026-06-26).

**Rules governing placeholders:**
1. Placeholders labeled TEMP_HERO_A and TEMP_WORDMARK at all times
2. Neither placeholder is treated as final artwork
3. No new permanent logo or brand mark is invented
4. Layout grid built so official vectors swap in without repositioning
5. R-01 and R-01B remain CRITICAL open risks in RISK_REGISTER.md
6. Both assets marked TEMPORARY in ASSET_INVENTORY.md
7. Final production approval blocked until official vectors are supplied

---

## SECTION 1 — DOCUMENT SETUP

### 1.1 New Document Settings

| Setting | Value |
|---|---|
| Application | Adobe Illustrator (latest) |
| Color Mode | CMYK |
| Raster Effects | 300 PPI |
| Units | Millimeters |
| Artboard Count | 1 (master) |
| Artboard Width | 188.57 mm (182.22mm trim + 3.175mm bleed each side) |
| Artboard Height | 154.35 mm (148.00mm trim + 3.175mm bleed each side) |
| Align to Pixel Grid | Off |
| Preview Mode | Default (not Pixel) |

### 1.2 File Naming

```
ALTERNATIVE_SESSION_5MG_PASSIONFRUIT_MASTER_v001.ai
```

Saved to: `/Artwork/` folder

### 1.3 First Guides — Trim, Bleed, Seam

After opening the new document, build the following locked guide structure on layer 01_GUIDES before any artwork:

| Guide | Position | Color |
|---|---|---|
| Bleed boundary (all sides) | Artboard edge | Cyan |
| Trim — left | x = 3.175mm | Magenta |
| Trim — right | x = 185.395mm | Magenta |
| Trim — top | y = 3.175mm | Magenta |
| Trim — bottom | y = 151.175mm | Magenta |
| Safe zone — left | x = 8.175mm (5mm inside trim) | Green |
| Safe zone — right | x = 180.395mm | Green |
| Safe zone — top | y = 8.175mm | Green |
| Safe zone — bottom | y = 146.175mm | Green |
| Seam position | [CONFIRM FROM CANWORKS DIELINE IN ILLUSTRATOR — record mm from left] | Red |
| Seam exclusion — left | Seam − 10mm | Red dashed |
| Seam exclusion — right | Seam + 10mm | Red dashed |

**Action required:** Open the Canworks dieline PDF in Illustrator as first action. Measure and record the seam position in mm from the left trim edge. Enter that value in the seam guide above before proceeding.

---

## SECTION 2 — LAYER STRUCTURE

Build exactly 9 layers in this order (top to bottom in Layers panel). Names must be exact — no variation.

| Order | Layer Name | Lock State | Contents |
|---|---|---|---|
| 1 | 09_EXPORT | Locked | Export copies only — never edit here |
| 2 | 08_FINISHES | Unlocked | All Metallic Gold elements — isolated |
| 3 | 07_CODES | Unlocked | QR code + CTA text, UPC-A barcode |
| 4 | 06_COMPLIANCE | Unlocked | Warnings, manufacturer info, website, batch, lot, best by |
| 5 | 05_INFORMATION | Unlocked | Nutrition Facts, ingredients, directions, storage, active ingredient |
| 6 | 04_PRODUCT | Unlocked | SESSION™, dose, category, flavor, net contents |
| 7 | 03_BRAND | Unlocked | TEMP_HERO_A placeholder, TEMP_WORDMARK placeholder |
| 8 | 02_BACKGROUND | Unlocked | Matte Black field |
| 9 | 01_GUIDES | Locked | All guides, panel dividers, trim/bleed/safe indicators |

**Layer note on 03_BRAND:** When official vectors arrive, they replace the TEMP placeholders in place. The layer receives the final vectors — nothing else moves.

**Layer note on 08_FINISHES:** All Metallic Gold objects live here and nowhere else. Gold swatch is `Brand_Metallic_Gold_TBD` globally. If production method changes (CMYK simulation → Pantone Metallic ink → foil), only this layer and swatch require updating.

---

## SECTION 3 — GLOBAL SWATCHES

Open the Swatches panel. Delete all default swatches. Build these four global swatches only:

| Swatch Name | Type | Color Mode | Value | Note |
|---|---|---|---|---|
| Brand_Matte_Black_TBD | Global | CMYK | C:0 M:0 Y:0 K:100 (temporary registration black) | Label clearly as TBD — replace with confirmed press values |
| Brand_Metallic_Gold_TBD | Global | CMYK | C:0 M:22 Y:100 K:15 (temporary process approximation) | Label clearly as TBD — production method open. All gold objects reference this swatch. Replace swatch value only when method confirmed — artwork updates globally. |
| Brand_Warm_White_TBD | Global | CMYK | C:0 M:0 Y:0 K:0 (paper white temporary) | Label clearly as TBD — replace with confirmed press values |
| Brand_Nutrition_White | Global | CMYK | C:0 M:0 Y:0 K:0 | Nutrition Facts panel field — paper white convention |

**Critical:** All artwork references these named global swatches — never local colors. When confirmed production values arrive, update the swatch and all artwork updates automatically.

**Swatch naming is exact.** Do not abbreviate or vary the names — they are referenced in documentation.

---

## SECTION 4 — TEMPORARY PLACEHOLDER SPECIFICATIONS

### 4.1 TEMP_HERO_A

The Hero A is described in the Brand Bible as a stylized capital A — the brand's primary identity mark. It is sacred. The official vector has not been received and must not be recreated.

**Placeholder construction:**

Build a simple geometric capital letter "A" in Söhne Halbfett or a clean geometric sans as a temporary positional marker only. This is not a logo recreation — it is a labeled space-holder.

| Attribute | Value |
|---|---|
| Layer | 03_BRAND |
| Element type | Live Söhne Halbfett "A" — do not outline |
| Color | Brand_Metallic_Gold_TBD |
| Size | Dominant — approximately 55–65mm tall, centered on front panel |
| Position | Vertically centered in the upper two-thirds of front panel |
| Label | Text object reading "TEMP_HERO_A" in 8pt Söhne Buch, Brand_Warm_White_TBD, directly below the A |
| Group name | Group labeled: [TEMP_HERO_A — REPLACE WITH OFFICIAL VECTOR] |
| Sublayer name | Sublayer in 03_BRAND labeled: TEMP_HERO_A |
| Lock | Do not lock — must be easily selectable for replacement |
| Outline | Do NOT outline — keep as live text so it is obviously a placeholder |

**When official Hero A arrives:** Select the TEMP_HERO_A group, delete it, place the official vector in its position at the same scale and center alignment. Lock the official vector. Update ASSET_INVENTORY.md and DECISIONS_LOG.md.

---

### 4.2 TEMP_WORDMARK

The official ALTERNATIVE™ wordmark vector is not available. The approved fallback per DEC-023 (CS-02) is Söhne Halbfett live text.

| Attribute | Value |
|---|---|
| Layer | 03_BRAND |
| Element type | Live Söhne Halbfett text — "ALTERNATIVE™" — do not outline |
| Case | All caps |
| Color | Brand_Warm_White_TBD |
| Size | Large display — optically dominant below TEMP_HERO_A |
| Tracking | +30 |
| ™ symbol | Manually scaled to cap height — not default superscript |
| Label | Text object reading "TEMP_WORDMARK" in 7pt Söhne Buch, 50% opacity Brand_Warm_White_TBD, directly below the wordmark |
| Group name | Group labeled: [TEMP_WORDMARK — REPLACE WITH OFFICIAL VECTOR IF ONE EXISTS] |
| Sublayer name | Sublayer in 03_BRAND labeled: TEMP_WORDMARK |
| Lock | Do not lock — must be easily selectable for replacement |
| Outline | Do NOT outline — keep as live Söhne text |

**When official wordmark vector arrives:** Select the TEMP_WORDMARK group, delete it, place the official vector at the same baseline and horizontal center. Lock the official vector. Update ASSET_INVENTORY.md and DECISIONS_LOG.md.

**If no official wordmark vector ever exists:** Client explicitly confirms Söhne Halbfett is the permanent wordmark. "TEMP_WORDMARK" label is removed, text is outlined and moved to a permanent sublayer. Decision is locked with a new DEC entry.

---

## SECTION 5 — CHARACTER STYLES SETUP

Build all 17 Character Styles in Illustrator's Character Styles panel. Styles must be named exactly as documented in BRAND_DESIGN_SYSTEM.md. No deviation from naming.

Build in this order:

| Style | Name | Typeface | Weight | Size (starting point) | Tracking | Notes |
|---|---|---|---|---|---|---|
| CS-01 | Tagline | Söhne | Leicht | 8pt | +180 | All caps — adjust at layout |
| CS-02 | Wordmark | Söhne | Halbfett | 36pt | +30 | Fallback — see placeholder rules |
| CS-03 | Product Line | Söhne | Buch | 18pt | +100 | All caps |
| CS-04 | THC Strength | Söhne | Buch | 10pt | +100 | All caps — shelf-readable |
| CS-05 | Beverage Category | Söhne | Leicht | 7pt | +100 | All caps |
| CS-06 | Flavor | Söhne | Buch | 14pt | +60 | Lock case at layout |
| CS-07 | Net Contents | Söhne | Leicht | 6pt | +50 | Regulatory minimum |
| CS-08 | Info Heading | Söhne | Halbfett | 8pt | +60 | All caps |
| CS-09 | Body Copy | Söhne | Buch | 8pt | +30 | Mixed case |
| CS-10 | Compliance | Söhne | Buch | 7pt | +20 | Mixed case — 6pt floor |
| CS-11 | Ingredients | Söhne | Buch | 7pt | +20 | Mixed case |
| CS-12 | Manufacturer Info | Söhne | Buch | 6.5pt | +20 | Mixed case |
| CS-13 | QR Label | Söhne | Leicht | 6.5pt | +100 | All caps |
| CS-14 | Barcode OCR | Söhne | Buch | Per UPC-A spec | Per spec | Numeric |
| CS-15 | Lot/Batch/Best By | Söhne | Buch | 6.5pt | +20 | Mixed case |
| CS-16 | Nutrition Header | Söhne | Halbfett | Per FDA spec | 0 | On white field |
| CS-17 | Nutrition Body (FDA) | Helvetica Neue | Regular/Bold | Per FDA spec | 0 | FDA exception only |

**Note:** All point sizes above are starting points for layout. Final sizes confirmed at Phase 4 layout review against physical can mock-up.

---

## SECTION 6 — PARAGRAPH STYLES SETUP

Build all 14 Paragraph Styles. Each is based on the corresponding Character Style with paragraph-level additions.

| Style | Name | Based On | Alignment | Space Before | Space After | Hyphenation |
|---|---|---|---|---|---|---|
| PS-01 | Tagline | CS-01 | Center | 0 | 4pt | Off |
| PS-02 | Wordmark | CS-02 | Center | 0 | 3pt | Off |
| PS-03 | Product Line | CS-03 | Center | 0 | 3pt | Off |
| PS-04 | THC Strength | CS-04 | Center | 0 | 3pt | Off |
| PS-05 | Beverage Category | CS-05 | Center | 0 | 3pt | Off |
| PS-06 | Flavor | CS-06 | Center | 0 | 3pt | Off |
| PS-07 | Net Contents | CS-07 | Center | 0 | 0 | Off |
| PS-08 | Info Heading | CS-08 | Left | 6pt | 2pt | Off |
| PS-09 | Body Copy | CS-09 | Left | 0 | 3pt | On |
| PS-10 | Compliance | CS-10 | Left | 0 | 2pt | On |
| PS-11 | Ingredients | CS-11 | Left | 0 | 0 | On |
| PS-12 | Manufacturer | CS-12 | Left | 0 | 0 | Off |
| PS-13 | QR Label | CS-13 | Center | 0 | 3pt | Off |
| PS-14 | Lot/Batch/Best By | CS-15 | Left | 0 | 2pt | Off |

---

## SECTION 7 — BACKGROUND FIELD

On layer 02_BACKGROUND:

- Rectangle: full artboard width and height including bleed
- Fill: Brand_Matte_Black_TBD (global swatch)
- Stroke: None
- Lock the layer after placement

This is the primary canvas. It must extend to the bleed boundary on all sides.

---

## SECTION 8 — PANEL DIVIDER GUIDES

The flat wrap label has four panels. Exact panel widths are determined by the seam position confirmed from the Canworks dieline.

**Working assumption until seam is confirmed (update immediately once confirmed):**

| Panel | Name | Approximate Width |
|---|---|---|
| A — Front Brand Panel | Primary identity | ~80mm |
| B — Information Panel | Nutrition, ingredients, directions | ~55mm |
| C — Compliance Panel | Warnings, manufacturer, legal | ~30mm |
| D — Codes Panel | QR + barcode | ~17.22mm |

Add vertical guide lines at each panel boundary on 01_GUIDES. Lock guides. Label each panel zone with a small 7pt note in a locked sublayer (visible in layout, suppressed on export).

---

## SECTION 9 — FRONT PANEL LAYOUT ZONES

On the front panel (Panel A), establish horizontal zone guides for all 8 hierarchy levels. These zones govern text placement and ensure the reading sequence is spatially enforced.

| Zone | Content | Approximate Top Edge from Trim |
|---|---|---|
| Z-01 | Tagline — A NEW STATE OF MIND | 10mm from top |
| Z-02 | TEMP_HERO_A | 20mm from top |
| Z-03 | TEMP_WORDMARK | 85mm from top (below Hero A) |
| Z-04 | SESSION™ | 100mm from top |
| Z-05 | 5MG THC PER CAN | 110mm from top |
| Z-06 | HEMP-DERIVED THC BEVERAGE | 118mm from top |
| Z-07 | PASSION FRUIT | 126mm from top |
| Z-08 | 12 FL OZ (355 mL) | 136mm from top |

**These are starting zone positions — all are adjusted optically at Phase 4 layout. Zone guides are reference only, not final positions.**

---

## SECTION 10 — PHASE 3 GATE CHECKLIST

Before Phase 3 is marked complete and Phase 4 begins, every item below must be checked off:

**Document**
- [ ] File named `ALTERNATIVE_SESSION_5MG_PASSIONFRUIT_MASTER_v001.ai`
- [ ] Saved to `/Artwork/` folder
- [ ] Color mode: CMYK confirmed
- [ ] Raster effects: 300 PPI confirmed
- [ ] Units: millimeters confirmed

**Layers**
- [ ] All 9 layers present, named exactly, in correct order
- [ ] 01_GUIDES — locked
- [ ] 02_BACKGROUND — Matte Black field placed, layer locked
- [ ] 03_BRAND — TEMP_HERO_A and TEMP_WORDMARK present, labeled, NOT outlined
- [ ] 04_PRODUCT — empty, ready
- [ ] 05_INFORMATION — empty, ready
- [ ] 06_COMPLIANCE — empty, ready
- [ ] 07_CODES — empty, ready
- [ ] 08_FINISHES — empty, ready (gold elements placed at Phase 4)
- [ ] 09_EXPORT — locked

**Swatches**
- [ ] Brand_Matte_Black_TBD — global, named correctly
- [ ] Brand_Metallic_Gold_TBD — global, named correctly
- [ ] Brand_Warm_White_TBD — global, named correctly
- [ ] Brand_Nutrition_White — global, named correctly
- [ ] All default swatches deleted

**Typography**
- [ ] Söhne installed on production machine (all required weights)
- [ ] CS-01 through CS-17 — all 17 Character Styles built and named correctly
- [ ] PS-01 through PS-14 — all 14 Paragraph Styles built and named correctly

**Guides**
- [ ] Trim guides on all four sides
- [ ] Bleed boundary guides
- [ ] Safe zone guides (5mm inside trim)
- [ ] Seam position recorded: ______mm from left trim edge
- [ ] Seam exclusion zone (10mm each side of seam)
- [ ] Panel divider guides (A/B/C/D)
- [ ] Front panel hierarchy zone guides (Z-01 through Z-08)

**Placeholders**
- [ ] TEMP_HERO_A present on 03_BRAND, labeled, NOT outlined
- [ ] TEMP_WORDMARK present on 03_BRAND, labeled, NOT outlined
- [ ] Both placeholders clearly read as temporary, not final artwork

**Phase 3 Gate Sign-Off**
- [ ] All above items confirmed
- [ ] DECISIONS_LOG.md updated with Phase 3 complete entry
- [ ] PROJECT_STATUS.md updated: Phase 3 → COMPLETE
- [ ] CHANGELOG.md updated: v2.3.0 Phase 3 entry
- [ ] Phase 4 begins immediately upon Phase 3 gate passing

---

## SECTION 11 — PLACEHOLDER SWAP PROTOCOL (for when official vectors arrive)

When the official Hero A vector or official ALTERNATIVE™ wordmark vector is received:

**Step 1:** Confirm the asset is the official approved vector (not a rasterized version, not a screenshot, not a PDF without paths).

**Step 2:** Open `ALTERNATIVE_SESSION_5MG_PASSIONFRUIT_MASTER_v[current].ai`.

**Step 3:** On layer 03_BRAND, select the TEMP_HERO_A group (or TEMP_WORDMARK group).

**Step 4:** Note the bounding box position and dimensions of the placeholder.

**Step 5:** Delete the placeholder group.

**Step 6:** Place the official vector at the exact same center alignment and approximate scale. Adjust scale to fit the zone — the zone does not change.

**Step 7:** Lock the official vector object.

**Step 8:** Update the sublayer name from "TEMP_HERO_A" to "HERO_A_OFFICIAL".

**Step 9:** Save as incremented version: `ALTERNATIVE_SESSION_5MG_PASSIONFRUIT_MASTER_v[next].ai`

**Step 10:** Update ASSET_INVENTORY.md — change status from ⚠️ TEMPORARY to ✅ RECEIVED.

**Step 11:** Update RISK_REGISTER.md — close R-01 or R-01B accordingly.

**Step 12:** Update DECISIONS_LOG.md with new locked decision entry.

**Step 13:** Continue from current production phase — no layout rebuild required.

---

*This document governs the Phase 3 Illustrator production setup session.*
*No Phase 4 work begins until the Phase 3 gate checklist is fully signed off.*
