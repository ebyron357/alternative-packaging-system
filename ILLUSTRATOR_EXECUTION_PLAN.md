# ALTERNATIVE™ — ILLUSTRATOR EXECUTION PLAN
**Document:** Step-by-Step Production Plan — Illustrator Master Build
**Product:** ALTERNATIVE™ SESSION™ 5MG THC Per Can — Passion Fruit / 12 oz Sleek Can
**Dieline:** Canworks 12 oz Sleek Can Flat Wrap (locked — do not modify)
**Program Director:** Claude (AI Production System)
**Date:** 2026-06-26
**Version:** 1.0
**Status:** READY — Awaiting Söhne font installation before execution

---

## CRITICAL PRE-CONDITIONS

Before the first action in this plan, all of the following must be confirmed:

| Pre-condition | Status | Action if Not Met |
|---|---|---|
| Söhne font files installed (Leicht, Buch, Halbfett, Kräftig) | 🔴 CLIENT ACTION | Do not open Illustrator until fonts are confirmed installed |
| Canworks dieline PDF accessible | ✅ Received | Located in project folder |
| This execution plan read in full | Required | Read before opening Illustrator |
| BRAND_DESIGN_SYSTEM.md open for reference | Required | Keep open during entire session |
| PHASE3_PRODUCTION_SETUP.md open for reference | Required | Keep open during entire session |

**Do not begin execution until all five pre-conditions are met.**

---

## STOP POINTS — OVERVIEW

This plan contains eight Stop Points that require user review and approval before work continues. They are marked **STOP POINT** throughout the document. No work proceeds past a Stop Point without explicit approval. Stop Points are not suggestions — they are gates.

| Stop Point | Trigger | Action |
|---|---|---|
| SP-01 | Dieline dimensions confirmed in Illustrator | Report dimensions — await approval before continuing |
| SP-02 | Document setup complete — layers, swatches, guides built | Visual review — await approval before adding content |
| SP-03 | TEMP_HERO_A and TEMP_WORDMARK placed on front panel | Compositional review — await approval before continuing |
| SP-04 | Full front panel hierarchy placed (all 8 levels) | Hierarchy review — await approval before panel B |
| SP-05 | Information panel structure placed | Panel B review — await approval before panel C |
| SP-06 | Compliance panel and codes panel placed | Full label review — await approval before any refinement |
| SP-07 | First proof PNG and review PDF exported | Physical mock-up review — await approval before Phase 4 |
| SP-08 | Phase 3 gate checklist complete | Phase 3 sign-off — formal approval required before Phase 4 |

---

## SECTION 1 — ILLUSTRATOR DOCUMENT SETUP

### 1.1 Open the Canworks Dieline

Open the Canworks 12 oz Sleek Can dieline PDF in Adobe Illustrator.

When Illustrator opens a PDF with multiple pages, select **Page 1** (the flat wrap dieline) unless the dieline supplier has specified a different page for the artwork template.

Do not edit the dieline file itself. It is the locked reference.

### 1.2 Verify Dieline Dimensions

Before creating the new working document:

- Select all objects on the dieline page
- Open Document Info or use the Transform panel to confirm the overall flat wrap dimensions
- **Expected trim dimensions: 182.22mm × 148.00mm**
- **Expected bleed: 0.125" (3.175mm) on all sides**
- Locate the seam indicator. Record the seam position as a measurement from the left trim edge.
- Record: **Seam position = _____ mm from left trim edge**
- Confirm the safe zone inset from the Canworks template notation

If the dimensions do not match 182.22mm × 148.00mm, do not proceed. Report the discrepancy immediately.

---

### **STOP POINT SP-01**
**Report:** "Dieline dimensions confirmed: [W] × [H]. Seam at [X]mm from left trim. Safe zone: [Y]mm inset. Matches spec / Does not match spec."
**Do not continue until SP-01 is approved.**

---

### 1.3 Create New Working Document

Do not work in the dieline file. Create a new document for the production master.

| Setting | Value |
|---|---|
| File → New | New Document |
| Profile | Print |
| Units | Millimeters |
| Width | 188.57 mm (182.22 + 3.175 bleed × 2) |
| Height | 154.35 mm (148.00 + 3.175 bleed × 2) |
| Color Mode | CMYK |
| Raster Effects | 300 PPI |
| Preview Mode | Default |
| Align to Pixel Grid | Off |
| Number of Artboards | 1 |

**File name:** `ALTERNATIVE_SESSION_5MG_PASSIONFRUIT_MASTER_v001.ai`
**Save location:** `/Artwork/`

Save immediately after creation. Do not begin any work in an unsaved file.

---

## SECTION 2 — LAYER STRUCTURE

Open the Layers panel. Delete all default layers. Build the following 9 layers in exact order. Layer names are case-sensitive and must match exactly.

### 2.1 Layer Build Order

Build from bottom to top (Illustrator stacks layers from bottom of panel = back to top of panel = front):

| Panel Order | Layer Name | Role | Default State |
|---|---|---|---|
| 9 (front) | 09_EXPORT | Export reference versions only | Locked |
| 8 | 08_FINISHES | All Metallic Gold elements | Unlocked |
| 7 | 07_CODES | QR code, barcode, CTA text | Unlocked |
| 6 | 06_COMPLIANCE | Warnings, manufacturer, legal | Unlocked |
| 5 | 05_INFORMATION | Nutrition, ingredients, directions | Unlocked |
| 4 | 04_PRODUCT | SESSION™, dose, category, flavor, volume | Unlocked |
| 3 | 03_BRAND | TEMP_HERO_A, TEMP_WORDMARK, tagline | Unlocked |
| 2 | 02_BACKGROUND | Matte Black field | Locked after placement |
| 1 (back) | 01_GUIDES | All guides and reference geometry | Locked |

### 2.2 Required Sublayers

Build the following sublayers within their parent layers. Sublayer names are the named object reference throughout this plan.

**03_BRAND sublayers:**
- `TEMP_HERO_A` — Hero A placeholder
- `TEMP_WORDMARK` — ALTERNATIVE™ wordmark placeholder
- `TAGLINE` — A NEW STATE OF MIND

**04_PRODUCT sublayers:**
- `SESSION_WORDMARK` — SESSION™ text
- `THC_STRENGTH` — 5MG THC PER CAN
- `CATEGORY` — HEMP-DERIVED THC BEVERAGE
- `FLAVOR` — PASSION FRUIT
- `NET_CONTENTS` — 12 FL OZ (355 mL)

**05_INFORMATION sublayers:**
- `ACTIVE_INGREDIENT` — Active ingredient declaration
- `NUTRITION_FACTS` — FDA Nutrition Facts panel
- `INGREDIENTS` — Ingredient list
- `DIRECTIONS` — Directions for use
- `STORAGE` — Storage instructions

**06_COMPLIANCE sublayers:**
- `WARNINGS` — All legal warnings
- `MANUFACTURER` — Manufacturer name and address
- `WEBSITE` — AlternativeBev.com
- `BATCH_LOT` — Batch / Lot / Best By fields

**07_CODES sublayers:**
- `QR_LABEL` — SCAN FOR LAB RESULTS & PRODUCT INFO
- `QR_CODE` — QR code placeholder (vector)
- `BARCODE` — UPC-A barcode (860013732455)

**08_FINISHES sublayers:**
- `GOLD_HERO_A` — Gold Hero A accent (when official vector arrives)
- `GOLD_ACCENTS` — Any additional approved gold elements

---

## SECTION 3 — SWATCH SETUP

### 3.1 Clean the Swatches Panel

Open the Swatches panel. Select all default swatches. Delete all. Begin with an empty swatch panel.

### 3.2 Build Four Global Swatches

Create each swatch as a **Global** swatch. Name exactly as shown. Verify each is set to Global in the swatch options.

| Swatch Name | Type | Starting CMYK | Purpose |
|---|---|---|---|
| `Brand_Matte_Black_TBD` | Global, CMYK | C:0 M:0 Y:0 K:100 | Primary field — all background elements |
| `Brand_Metallic_Gold_TBD` | Global, CMYK | C:0 M:22 Y:100 K:15 | All gold elements — 08_FINISHES only |
| `Brand_Warm_White_TBD` | Global, CMYK | C:0 M:0 Y:0 K:0 | All typography except Nutrition Facts table |
| `Brand_Nutrition_White` | Global, CMYK | C:0 M:0 Y:0 K:0 | Nutrition Facts panel background field |

**Note on TBD swatches:** The CMYK values above are temporary working values only. They are not production-confirmed. When production values are confirmed from press proofs, update each swatch once — all artwork referencing the swatch updates automatically. This is why all artwork must reference global swatches, never local colors.

**Confirm:** All four swatches present. All four set to Global. Names exact.

---

## SECTION 4 — CHARACTER AND PARAGRAPH STYLE SETUP

### 4.1 Install Fonts First

Confirm Söhne is installed in the system font library before building character styles. If Söhne is not installed, styles cannot be correctly built and this step must wait.

Open the Character Styles panel and Paragraph Styles panel. Delete all defaults.

### 4.2 Build Character Styles

Build all 17 Character Styles in the following order. Each style is built by creating a text object, applying the attributes manually, and using "New Character Style from Selection." Name exactly as shown.

| Style Name | Typeface | Weight | Size | Tracking | Leading | Color |
|---|---|---|---|---|---|---|
| CS-01 Tagline | Söhne | Leicht | 8pt | +180 | 120% | Brand_Warm_White_TBD |
| CS-02 Wordmark | Söhne | Halbfett | 36pt | +30 | 120% | Brand_Warm_White_TBD |
| CS-03 Product Line | Söhne | Buch | 18pt | +100 | 120% | Brand_Warm_White_TBD |
| CS-04 THC Strength | Söhne | Buch | 10pt | +100 | 120% | Brand_Warm_White_TBD |
| CS-05 Beverage Category | Söhne | Leicht | 7pt | +100 | 120% | Brand_Warm_White_TBD |
| CS-06 Flavor | Söhne | Buch | 14pt | +60 | 120% | Brand_Warm_White_TBD |
| CS-07 Net Contents | Söhne | Leicht | 6pt | +50 | 120% | Brand_Warm_White_TBD |
| CS-08 Info Heading | Söhne | Halbfett | 8pt | +60 | 130% | Brand_Warm_White_TBD |
| CS-09 Body Copy | Söhne | Buch | 8pt | +30 | 135% | Brand_Warm_White_TBD |
| CS-10 Compliance | Söhne | Buch | 7pt | +20 | 130% | Brand_Warm_White_TBD |
| CS-11 Ingredients | Söhne | Buch | 7pt | +20 | 130% | Brand_Warm_White_TBD |
| CS-12 Manufacturer Info | Söhne | Buch | 6.5pt | +20 | 130% | Brand_Warm_White_TBD |
| CS-13 QR Label | Söhne | Leicht | 6.5pt | +100 | 120% | Brand_Warm_White_TBD |
| CS-14 Barcode OCR | Söhne | Buch | per UPC-A | 0 | — | Brand_Matte_Black_TBD |
| CS-15 Lot/Batch/Best By | Söhne | Buch | 6.5pt | +20 | 120% | Brand_Warm_White_TBD |
| CS-16 Nutrition Header | Söhne | Halbfett | per FDA | 0 | per FDA | Brand_Matte_Black_TBD |
| CS-17 Nutrition Body (FDA) | Helvetica Neue | Regular/Bold | per FDA | 0 | per FDA | Brand_Matte_Black_TBD |

**Verify:** 17 styles present. Names exact. Each style applied and visible in the Character Styles panel.

### 4.3 Build Paragraph Styles

Build all 14 Paragraph Styles. Each is built from the corresponding Character Style plus paragraph attributes.

| Style Name | Based On | Alignment | Space Before | Space After | Hyphenation |
|---|---|---|---|---|---|
| PS-01 Tagline | CS-01 | Center | 0 | 4pt | Off |
| PS-02 Wordmark | CS-02 | Center | 0 | 3pt | Off |
| PS-03 Product Line | CS-03 | Center | 0 | 3pt | Off |
| PS-04 THC Strength | CS-04 | Center | 0 | 3pt | Off |
| PS-05 Beverage Category | CS-05 | Center | 0 | 3pt | Off |
| PS-06 Flavor | CS-06 | Center | 0 | 3pt | Off |
| PS-07 Net Contents | CS-07 | Center | 0 | 0 | Off |
| PS-08 Info Heading | CS-08 | Left | 6pt | 2pt | Off |
| PS-09 Body Copy | CS-09 | Left | 0 | 3pt | On |
| PS-10 Compliance | CS-10 | Left | 0 | 2pt | On |
| PS-11 Ingredients | CS-11 | Left | 0 | 0 | On |
| PS-12 Manufacturer | CS-12 | Left | 0 | 0 | Off |
| PS-13 QR Label | CS-13 | Center | 0 | 3pt | Off |
| PS-14 Lot/Batch/Best By | CS-15 | Left | 0 | 2pt | Off |

**Verify:** 14 styles present. Names exact.

---

## SECTION 5 — GUIDES AND REFERENCE GEOMETRY

All guides are built on layer 01_GUIDES. Lock the layer after all guides are placed.

### 5.1 Production Boundary Guides

| Guide | Position | Color Code |
|---|---|---|
| Bleed boundary — all 4 sides | Artboard edge | Cyan |
| Trim — left | x = 3.175mm | Magenta |
| Trim — right | x = 185.395mm | Magenta |
| Trim — top | y = 3.175mm | Magenta |
| Trim — bottom | y = 151.175mm | Magenta |
| Safe zone — left | x = 8.175mm | Green |
| Safe zone — right | x = 180.395mm | Green |
| Safe zone — top | y = 8.175mm | Green |
| Safe zone — bottom | y = 146.175mm | Green |

### 5.2 Seam Guides

Using the seam position recorded at SP-01:

| Guide | Position |
|---|---|
| Seam centerline | x = [seam measurement + 3.175mm bleed offset] | Red |
| Seam exclusion — left | Seam − 10mm | Red dashed |
| Seam exclusion — right | Seam + 10mm | Red dashed |

No design element may cross the seam centerline. No design element may be positioned within 10mm of the seam on either side.

### 5.3 Panel Divider Guides

The flat wrap has four panels. Divide the trim width (182.22mm) into four panels using the seam position and Canworks panel layout. Working panel widths until Canworks confirms exact panel layout:

| Panel | Name | Working Width |
|---|---|---|
| A — Front Brand Panel | Primary brand identity | ~80mm |
| B — Information Panel | Nutrition Facts, ingredients | ~55mm |
| C — Compliance Panel | Warnings, manufacturer | ~30mm |
| D — Codes Panel | QR code, UPC barcode | ~17.22mm |

Add vertical guide lines at each panel boundary. Label each panel zone with a locked text note at 7pt in a sublayer of 01_GUIDES labeled `PANEL_LABELS`. This text is visible in layout, suppressed in export.

### 5.4 Front Panel Hierarchy Zone Guides

Add horizontal guides on Panel A for each hierarchy level. These are starting positions — all are adjusted optically during layout:

| Zone | Content | Starting Guide from Trim Top |
|---|---|---|
| Z-01 | Tagline | 10mm |
| Z-02 | TEMP_HERO_A | 20mm |
| Z-03 | TEMP_WORDMARK | 85mm |
| Z-04 | SESSION™ | 100mm |
| Z-05 | 5MG THC PER CAN | 110mm |
| Z-06 | HEMP-DERIVED THC BEVERAGE | 118mm |
| Z-07 | PASSION FRUIT | 126mm |
| Z-08 | 12 FL OZ (355 mL) | 136mm |

Lock 01_GUIDES after all guides are placed. Guides do not move unless a seam confirmation or layout review requires revision.

---

### **STOP POINT SP-02**
**Report:** Provide a screenshot or description of the document state: layers panel, swatches panel, and artboard with guides visible. Confirm all 9 layers, 4 swatches, 17 Character Styles, 14 Paragraph Styles, and all guide sets are present.
**Do not add any content to the artboard until SP-02 is approved.**

---

## SECTION 6 — BACKGROUND FIELD

On layer **02_BACKGROUND**:

1. Select the Rectangle Tool. Draw a rectangle covering the full artboard including bleed: 188.57mm × 154.35mm.
2. Align to artboard: position at x = 0, y = 0.
3. Fill: `Brand_Matte_Black_TBD` (global swatch).
4. Stroke: None.
5. Name the object: `BACKGROUND_FIELD`.
6. Lock layer 02_BACKGROUND.

**Verify:** Rectangle fills the full artboard. Color is Brand_Matte_Black_TBD. Layer is locked.

---

## SECTION 7 — FRONT PANEL BUILD SEQUENCE (PANEL A)

All front panel elements are placed on their designated sublayers within layers 03_BRAND and 04_PRODUCT. Work top to bottom through the hierarchy. Do not skip levels.

### 7.1 Tagline — A NEW STATE OF MIND (Level 1)

**Target sublayer:** 03_BRAND → TAGLINE

1. Select the Type Tool. Click on Panel A, above Zone Z-01.
2. Type: `A NEW STATE OF MIND`
3. Apply Character Style: CS-01 Tagline
4. Apply Paragraph Style: PS-01 Tagline
5. Convert to all caps if not automatically applied by the style.
6. Horizontally center the text frame on Panel A's centerline.
7. Vertically position: top of text frame at Z-01 guide (10mm from trim top).
8. Name the text object: `TAGLINE_TEXT`.

**Do not outline. Keep as live text.**

### 7.2 TEMP_HERO_A (Level 2)

**Target sublayer:** 03_BRAND → TEMP_HERO_A

1. Select the Type Tool. Click in Panel A, below the tagline.
2. Type: `A`
3. Apply typeface: Söhne Halbfett. Scale to approximately 60mm tall.
4. Color: `Brand_Metallic_Gold_TBD`.
5. Horizontally center on Panel A's centerline.
6. Vertically position: top of letter body at approximately Z-02 guide (20mm from trim top).
7. Add a second text object below the A reading: `TEMP_HERO_A`
   - Style: Söhne Buch 8pt, Brand_Warm_White_TBD
   - Position: directly below the A, centered
8. Group both objects. Name the group: `[TEMP_HERO_A — REPLACE WITH OFFICIAL VECTOR]`.
9. Name the sublayer: TEMP_HERO_A.

**Do not outline either text object. Keep as live text.**

**This is not a logo. This is a positional placeholder for the official Hero A vector.**

### 7.3 TEMP_WORDMARK — ALTERNATIVE™ (Level 3)

**Target sublayer:** 03_BRAND → TEMP_WORDMARK

1. Select the Type Tool. Click in Panel A, at approximately Z-03 (85mm from trim top).
2. Type: `ALTERNATIVE`
3. Apply Character Style: CS-02 Wordmark.
4. Apply Paragraph Style: PS-02 Wordmark.
5. Add the ™ symbol: scale manually to cap height. Position at optical top-right of the final E. Do not use default superscript.
6. Color: Brand_Warm_White_TBD.
7. Horizontally center on Panel A's centerline.
8. Optically align: check that the word appears optically centered — adjust by eye, not by transform panel.
9. Add a second text object reading: `TEMP_WORDMARK`
   - Style: Söhne Buch 7pt, Brand_Warm_White_TBD, 50% opacity
   - Position: directly below the wordmark, centered
10. Group both objects. Name the group: `[TEMP_WORDMARK — REPLACE WITH OFFICIAL VECTOR IF ONE EXISTS]`.
11. Name the sublayer: TEMP_WORDMARK.

**Do not outline. Keep as live Söhne text.**

---

### **STOP POINT SP-03**
**Report:** Provide a view of the front panel with TEMP_HERO_A and TEMP_WORDMARK placed. The tagline above. Both placeholders clearly labeled TEMPORARY. Compositional relationship visible.
**Evaluation criteria:** Does the composition read as premium? Does the TEMP_HERO_A dominate correctly? Does the TEMP_WORDMARK anchor below it correctly? Does the tagline float above with appropriate lightness?
**Do not continue to Levels 4–8 until SP-03 is approved.**

---

### 7.4 SESSION™ (Level 4)

**Target sublayer:** 04_PRODUCT → SESSION_WORDMARK

1. Type: `SESSION`
2. Apply CS-03 Product Line / PS-03 Product Line.
3. Add ™ manually scaled to cap height.
4. Position below Z-03, above Z-04. Adjust optically — SESSION™ must be clearly subordinate to ALTERNATIVE™ in visual weight.
5. Name object: `SESSION_WORDMARK_TEXT`.

### 7.5 5MG THC PER CAN (Level 5)

**Target sublayer:** 04_PRODUCT → THC_STRENGTH

1. Type: `5MG THC PER CAN`
2. Apply CS-04 THC Strength / PS-04 THC Strength.
3. Position at Z-05. Must be clearly readable at 2-foot distance.
4. Verify the Söhne Buch weight provides adequate shelf readability.
5. Name object: `THC_STRENGTH_TEXT`.

### 7.6 HEMP-DERIVED THC BEVERAGE (Level 6)

**Target sublayer:** 04_PRODUCT → CATEGORY

1. Type: `HEMP-DERIVED THC BEVERAGE`
2. Apply CS-05 Beverage Category / PS-05 Beverage Category.
3. Position at Z-06. This is a descriptor — it must read clearly but not compete with dose or brand.
4. Name object: `CATEGORY_TEXT`.

### 7.7 PASSION FRUIT (Level 7)

**Target sublayer:** 04_PRODUCT → FLAVOR

1. Type: `PASSION FRUIT`
2. Apply CS-06 Flavor / PS-06 Flavor.
3. Confirm case: title case or all caps — decide optically and lock the decision in DECISIONS_LOG.md.
4. Position at Z-07.
5. Name object: `FLAVOR_TEXT`.

### 7.8 12 FL OZ (355 mL) (Level 8)

**Target sublayer:** 04_PRODUCT → NET_CONTENTS

1. Type: `12 FL OZ (355 mL)` — FL OZ in all caps, mL in mixed case per regulatory convention.
2. Apply CS-07 Net Contents / PS-07 Net Contents.
3. Position at Z-08. This is the lowest hierarchy element on the front panel.
4. Name object: `NET_CONTENTS_TEXT`.

---

### **STOP POINT SP-04**
**Report:** Full front panel with all 8 hierarchy levels placed. All content present. All text live (not outlined).
**Evaluation criteria:** Score the front panel against all 10 criteria in BRAND_DECISION_FRAMEWORK.md. Report the score for each criterion. Any criterion below 7 is identified with a specific note on what must change before proceeding.
**Do not begin Panel B until SP-04 is approved with a total average score of 7.0 or above.**

---

## SECTION 8 — INFORMATION PANEL BUILD SEQUENCE (PANEL B)

Panel B contains the Active Ingredient declaration, FDA Nutrition Facts panel, Ingredient List, Directions, and Storage. All elements are on layer 05_INFORMATION.

### 8.1 Active Ingredient Declaration

**Target sublayer:** 05_INFORMATION → ACTIVE_INGREDIENT

1. Add heading: `ACTIVE INGREDIENT` — CS-08 Info Heading / PS-08 Info Heading.
2. Add body: `Delta-9 Tetrahydrocannabinol (THC) .......... 5mg` (or legal counsel's confirmed terminology — see R-10. Use placeholder copy until confirmed.)
   - Style: CS-09 Body Copy / PS-09 Body Copy.
3. Add a PLACEHOLDER warning note in the Illustrator Notes panel: "Active Ingredient copy awaiting legal counsel confirmation — do not approve for production until R-10 is resolved."
4. Name group: `ACTIVE_INGREDIENT_SECTION`.

### 8.2 Nutrition Facts Panel

**Target sublayer:** 05_INFORMATION → NUTRITION_FACTS

The FDA Nutrition Facts panel follows a prescribed format. Build it as a white field on the Matte Black background.

**White field construction:**
1. Draw a rectangle covering the Nutrition Facts panel area on Panel B.
2. Fill: `Brand_Nutrition_White`.
3. Stroke: None.
4. Name: `NUTRITION_FACTS_FIELD`.

**Panel content — build inside the white field:**

| Element | Style | Value |
|---|---|---|
| "Nutrition Facts" heading | CS-16 Nutrition Header | Nutrition Facts |
| Thick rule | Black rule | Per FDA spec |
| Servings per container | CS-17 Nutrition Body | 1 |
| Serving size | CS-17 Nutrition Body | 12 Ounces (1 can) |
| Thick rule | Black rule | Per FDA spec |
| Calories | CS-17 Nutrition Body (bold) | 0 |
| Daily Value header | CS-17 Nutrition Body | % Daily Value* |
| Total Fat | CS-17 Nutrition Body | 0g — 0% |
| Saturated Fat | CS-17 Nutrition Body | 0g — 0% |
| Trans Fat | CS-17 Nutrition Body | 0g |
| Cholesterol | CS-17 Nutrition Body | 0mg — 0% |
| Sodium | CS-17 Nutrition Body | 0mg — 0% |
| Total Carbohydrate | CS-17 Nutrition Body | 0g — 0% |
| Dietary Fiber | CS-17 Nutrition Body | 0g — 0% |
| Total Sugars | CS-17 Nutrition Body | 0g |
| Added Sugars | CS-17 Nutrition Body | 0g — 0% |
| Protein | CS-17 Nutrition Body | 0g |
| Thin rule | | |
| Vitamin D / Calcium / Iron / Potassium | CS-17 Nutrition Body | ⚠️ PLACEHOLDER — confirm values (FLAG-01) |
| DV footnote | CS-17 Nutrition Body | *Percent Daily Values based on a 2,000 calorie diet. |

Add a PLACEHOLDER note: "Micronutrient values (Vitamin D, Calcium, Iron, Potassium) awaiting manufacturer confirmation — see FLAG-01. Do not approve for production until confirmed."

### 8.3 Ingredient List

**Target sublayer:** 05_INFORMATION → INGREDIENTS

1. Add heading: `INGREDIENTS` — CS-08 / PS-08.
2. Add body: `Carbonated Water, Natural Passion Fruit Flavor, Hemp Derived THC.`
   - Style: CS-11 Ingredients / PS-11 Ingredients.
3. Add PLACEHOLDER note: "Ingredient terminology (Hemp Derived THC) awaiting legal counsel confirmation — see R-10 and FLAG-02."
4. Name group: `INGREDIENTS_SECTION`.

### 8.4 Directions

**Target sublayer:** 05_INFORMATION → DIRECTIONS

1. Add heading: `DIRECTIONS` — CS-08 / PS-08.
2. Add body placeholder: `[DIRECTIONS COPY — AWAITING CLIENT INPUT]`
   - Style: CS-09 Body Copy / PS-09 Body Copy.
   - Color: Brand_Warm_White_TBD at 40% opacity to visually signal placeholder.
3. Name group: `DIRECTIONS_SECTION`.

### 8.5 Storage

**Target sublayer:** 05_INFORMATION → STORAGE

1. Add heading: `STORAGE` — CS-08 / PS-08.
2. Add body placeholder: `[STORAGE COPY — AWAITING CLIENT INPUT]`
   - Style: CS-09 / PS-09 at 40% opacity.
3. Name group: `STORAGE_SECTION`.

---

### **STOP POINT SP-05**
**Report:** Panel B complete. All sections placed. Placeholder elements identified at reduced opacity. Nutrition Facts panel visible with confirmed values and flagged placeholder values clearly distinguished.
**Do not begin Panel C until SP-05 is approved.**

---

## SECTION 9 — COMPLIANCE AND CODES PANEL BUILD SEQUENCE (PANELS C AND D)

### Panel C — Compliance Panel (layer 06_COMPLIANCE)

### 9.1 Warnings

**Target sublayer:** 06_COMPLIANCE → WARNINGS

1. Add standard federal THC warning placeholder:
   `[COMPLIANCE WARNINGS — AWAITING LEGAL COUNSEL APPROVAL]`
   - Style: CS-10 Compliance / PS-10 Compliance at 40% opacity.
2. Include 21+ age restriction indicator — minimum 1/4" diameter. Build as a vector circle with "21+" in CS-10, solid opacity.
3. Add PLACEHOLDER note: "All compliance copy awaiting legal counsel approval — see R-05. Do not approve for production without counsel sign-off."
4. Name group: `WARNINGS_SECTION`.

### 9.2 Manufacturer Information

**Target sublayer:** 06_COMPLIANCE → MANUFACTURER

1. Add: `Manufactured by: [MANUFACTURER NAME AND ADDRESS — AWAITING CLIENT INPUT]`
   - Style: CS-12 Manufacturer Info / PS-12 Manufacturer at 40% opacity.
2. Add PLACEHOLDER note: "Manufacturer name and address required — see R-06."
3. Name group: `MANUFACTURER_SECTION`.

### 9.3 Website

**Target sublayer:** 06_COMPLIANCE → WEBSITE

1. Add: `AlternativeBev.com`
   - Style: CS-09 Body Copy / PS-09.
   - Full opacity — confirmed copy per DEC-014.
2. Name object: `WEBSITE_TEXT`.

### 9.4 Batch / Lot / Best By

**Target sublayer:** 06_COMPLIANCE → BATCH_LOT

1. Add three lines:
   - `Lot: [VARIABLE]`
   - `Batch: [VARIABLE]`
   - `Best By: [VARIABLE]`
   - Style: CS-15 Lot/Batch/Best By / PS-14.
   - Full opacity — structure is confirmed, values are variable data applied at print.
2. Name group: `BATCH_LOT_SECTION`.

---

### Panel D — Codes Panel (layer 07_CODES)

### 9.5 QR Label Text

**Target sublayer:** 07_CODES → QR_LABEL

1. Add: `SCAN FOR LAB RESULTS & PRODUCT INFO`
   - Style: CS-13 QR Label / PS-13.
   - Position: above QR code placeholder.
   - Name object: `QR_LABEL_TEXT`.

### 9.6 QR Code Placeholder

**Target sublayer:** 07_CODES → QR_CODE

1. Draw a square: minimum 20mm × 20mm.
2. Fill: Brand_Warm_White_TBD.
3. Add centered text inside: `QR CODE PLACEHOLDER — URL PENDING`
   - Style: CS-09 at 8pt, Brand_Matte_Black_TBD.
4. Add PLACEHOLDER note: "QR destination URL not provided — see R-07. Generate final QR only when URL is confirmed and live."
5. Name group: `QR_CODE_PLACEHOLDER`.

### 9.7 UPC-A Barcode

**Target sublayer:** 07_CODES → BARCODE

1. Generate UPC-A barcode for number: **860013732455**
   - In Illustrator: Object → Create Object Mosaic, or use a barcode plugin, or place a pre-generated vector UPC-A.
   - Barcode must be a vector — no raster barcode is acceptable.
   - Human-readable digits: `860013732455` below the bars in CS-14 Barcode OCR.
   - Color: bars in Brand_Matte_Black_TBD on Brand_Nutrition_White field.
   - Minimum magnification: 80% of full UPC-A specification.
   - Quiet zone: minimum 3mm each side of bars.
2. Name group: `BARCODE_860013732455`.

---

### **STOP POINT SP-06**
**Report:** Full 360° label with all four panels placed. All confirmed content at full opacity. All placeholder content at 40% opacity with notes. QR placeholder at correct scale. Barcode at correct specification.
**Evaluation criteria:** Is the label readable as a system? Does the compliance panel feel integrated? Are all placeholder elements clearly distinguished from confirmed content?
**Do not begin any refinement work until SP-06 is approved.**

---

## SECTION 10 — PLACEHOLDER RULES FOR MISSING OFFICIAL VECTORS AND LEGAL DATA

### 10.1 Missing Official Vectors (Hero A and Wordmark)

- All placeholder elements are live text, not outlined
- All placeholder groups are named beginning with `[TEMP_` followed by the element name
- All placeholder groups are on sublayers named with the exact element name (`TEMP_HERO_A`, `TEMP_WORDMARK`)
- No placeholder element is treated as final artwork or approved for production
- Placeholder color is consistent with the intended final color (Brand_Metallic_Gold_TBD for Hero A, Brand_Warm_White_TBD for wordmark)
- Label text inside each placeholder group reads: `TEMP_[ELEMENT NAME]` in 8pt Söhne Buch
- Final production approval is blocked until official vectors are supplied

### 10.2 Missing Legal Data (Compliance, Directions, Storage, Manufacturer, Ingredient Terminology)

- All placeholder text is set at 40% opacity to visually distinguish from confirmed copy
- All placeholder text uses bracket notation: `[ELEMENT DESCRIPTION — AWAITING SOURCE]`
- All placeholder text references its risk register entry and/or its pending decision ID
- All placeholder text is confirmed-style (correct Character Style, correct size) so it holds the correct space and can be replaced with confirmed copy without layout changes
- Confirmed copy is always full opacity
- No label goes to press with any 40% opacity placeholder element

---

## SECTION 11 — WHAT MUST BE LOCKED BEFORE DESIGN WORK BEGINS

The following elements are locked — they cannot be moved, scaled, or modified without a new locked decision entry in DECISIONS_LOG.md:

| Element | Layer | Why Locked |
|---|---|---|
| Canworks dieline dimensions (182.22 × 148.00mm) | Reference | Printer specification — non-negotiable |
| Bleed specification (0.125" all sides) | 01_GUIDES | Printer specification |
| Seam position | 01_GUIDES | Confirmed from Canworks dieline |
| Safe zone guides | 01_GUIDES | Printer specification |
| Background field | 02_BACKGROUND | Brand Law — Matte Black field never changes |
| Brand_Matte_Black_TBD swatch | Swatches | Brand Law — locked until production values confirmed |
| Brand_Metallic_Gold_TBD swatch | Swatches | Brand Law — locked until production method confirmed |
| Brand_Warm_White_TBD swatch | Swatches | Brand Law — locked until production values confirmed |
| UPC number (860013732455) | 07_CODES | Confirmed DEC-015 |
| QR CTA text | 07_CODES | Confirmed DEC-016 |
| Website copy | 06_COMPLIANCE | Confirmed DEC-014 |
| Front panel reading hierarchy (8 levels) | 03_BRAND + 04_PRODUCT | Confirmed DEC-012 |
| Tagline position (above Hero A) | 03_BRAND | Confirmed DEC-011, DEC-022 |

---

## SECTION 12 — WHAT MUST REMAIN EDITABLE

The following elements must never be outlined, rasterized, or flattened during the active production phase. They remain as live editable objects until final pre-press.

| Element | Why Must Remain Editable |
|---|---|
| TEMP_HERO_A text | Must be selectable and deletable for official vector swap |
| TEMP_WORDMARK text | Must be selectable and deletable for official vector swap |
| All placeholder copy elements | Must be replaceable with confirmed copy without layout rebuild |
| All body copy text objects | Must be editable for legal and compliance copy revisions |
| All ingredient, directions, storage copy | Awaiting legal confirmation — must remain editable |
| Batch/Lot/Best By fields | Variable data — always editable |
| Character and Paragraph Styles | Must remain live — not baked into outlines |

---

## SECTION 13 — WHAT MUST NEVER MOVE

The following positional relationships are structural. If layout pressure requires any of these to move, escalate to the Program Director before moving anything. These are not adjustable for convenience.

| Positional Relationship | Rule |
|---|---|
| Tagline above Hero A | Non-negotiable compositional rule — see CREATIVE_DIRECTION.md Section 4 |
| Hero A above wordmark | Non-negotiable hierarchy rule — see DEC-022 |
| Wordmark above SESSION™ | Non-negotiable brand architecture — see CREATIVE_DIRECTION.md Section 6 |
| No element within 10mm of seam | Production rule — violation risks distortion at can seam |
| No element outside safe zone | Production rule — violation risks trim error |
| Gold elements exclusively on 08_FINISHES | Production rule — production method still open |

---

## SECTION 14 — HOW TO SAVE THE EDITABLE MASTER

### 14.1 Version Numbering

File is saved with version number incremented after each significant session or gate:

```
ALTERNATIVE_SESSION_5MG_PASSIONFRUIT_MASTER_v001.ai   ← Phase 3 complete
ALTERNATIVE_SESSION_5MG_PASSIONFRUIT_MASTER_v002.ai   ← After SP-04 approval
ALTERNATIVE_SESSION_5MG_PASSIONFRUIT_MASTER_v003.ai   ← After SP-06 approval
```

Never overwrite a previous version. Always increment.

### 14.2 Save Settings

- Format: Adobe Illustrator (.ai) — never flatten to PDF or EPS for the editable master
- Compatibility: Save for current Illustrator version and one version back (include legacy data)
- PDF Compatibility: On (for internal review PDF — not the production PDF)
- Fonts: Do not subset. All fonts must be installed on the production machine.
- Linked Files: Embed all placed images (none at this stage)

### 14.3 Backup Protocol

After every save, copy the current version to `/Documentation/Backups/` with the timestamp appended:
```
ALTERNATIVE_SESSION_5MG_PASSIONFRUIT_MASTER_v001_2026-06-26.ai
```

---

## SECTION 15 — HOW TO EXPORT PROOF PNG AND REVIEW PDF

### 15.1 Proof PNG (for on-screen review and mock-up)

1. File → Export → Export As
2. Format: PNG
3. Resolution: 150 PPI (for screen review) or 300 PPI (for print mock-up)
4. Color Mode: RGB for screen review
5. Anti-aliasing: Art Optimized
6. Artboard: Export all
7. File name: `ALTERNATIVE_SESSION_5MG_PASSIONFRUIT_PROOF_v[###]_[date].png`
8. Save to: `/Exports/PNG/`

### 15.2 Review PDF (for stakeholder review — not production)

1. File → Save a Copy
2. Format: Adobe PDF
3. Preset: [High Quality Print]
4. Do not flatten transparency. Do not downsample images.
5. Include all printer's marks: crop marks, color bars, registration marks
6. File name: `ALTERNATIVE_SESSION_5MG_PASSIONFRUIT_REVIEW_v[###]_[date].pdf`
7. Save to: `/Exports/PDF/`

**Important:** This is a review PDF, not a production PDF. The production PDF is generated at Phase 8 with full pre-press settings after all content is confirmed.

### 15.3 Physical Mock-Up Protocol

After every major Stop Point export, print the proof PNG at 100% scale on a standard printer. Wrap the printed proof around a 12 oz sleek can (or a cylinder of equivalent diameter). Evaluate:

- Shelf impact at 10 feet
- Full hierarchy readability at 2 feet
- Compliance text legibility at arm's length
- Seam alignment (does anything critical land at the seam?)
- Color relationships (bearing in mind the proof is on a standard printer, not on press)

Record observations. Update evaluation notes in DECISIONS_LOG.md before the next Stop Point.

---

### **STOP POINT SP-07**
**Report:** Proof PNG and review PDF exported. Physical mock-up completed. Observations recorded.
**Evaluation criteria:** Score the physical mock-up against the BRAND_DECISION_FRAMEWORK.md rubric. Identify any elements that perform differently on physical wrap vs. screen. Report specific changes required before Phase 3 gate.
**Do not proceed to Phase 3 gate until SP-07 is approved.**

---

## SECTION 16 — PHASE 3 GATE — FINAL CHECKLIST

The Phase 3 gate is a formal approval. Every item must be checked before Phase 4 begins.

### Document and File
- [ ] File named `ALTERNATIVE_SESSION_5MG_PASSIONFRUIT_MASTER_v[final Phase 3 version].ai`
- [ ] Saved to `/Artwork/`
- [ ] Backup saved to `/Documentation/Backups/`
- [ ] Color mode: CMYK confirmed
- [ ] Raster effects: 300 PPI confirmed

### Layers (all 9 present, named correctly, in correct stacking order)
- [ ] 09_EXPORT — locked
- [ ] 08_FINISHES — empty (gold placed at Phase 4)
- [ ] 07_CODES — QR placeholder and UPC-A barcode placed
- [ ] 06_COMPLIANCE — all compliance sections placed with placeholder copy
- [ ] 05_INFORMATION — all information sections placed with confirmed and placeholder copy
- [ ] 04_PRODUCT — all 8-level hierarchy elements placed
- [ ] 03_BRAND — TEMP_HERO_A and TEMP_WORDMARK placed and labeled
- [ ] 02_BACKGROUND — Matte Black field placed, layer locked
- [ ] 01_GUIDES — all guides placed, layer locked

### Swatches (all 4 present, all Global, names exact)
- [ ] Brand_Matte_Black_TBD
- [ ] Brand_Metallic_Gold_TBD
- [ ] Brand_Warm_White_TBD
- [ ] Brand_Nutrition_White

### Typography (all styles built and correctly named)
- [ ] CS-01 through CS-17 — 17 Character Styles
- [ ] PS-01 through PS-14 — 14 Paragraph Styles

### Guides
- [ ] Trim guides (all 4)
- [ ] Bleed boundary
- [ ] Safe zone guides (all 4)
- [ ] Seam position recorded and documented: _____ mm from left trim
- [ ] Seam exclusion zone (10mm each side)
- [ ] Panel dividers (A/B/C/D)
- [ ] Hierarchy zone guides (Z-01 through Z-08)

### Content
- [ ] All 8 hierarchy levels present on front panel
- [ ] Tagline above TEMP_HERO_A
- [ ] TEMP_HERO_A above TEMP_WORDMARK
- [ ] TEMP_WORDMARK above SESSION™
- [ ] All placeholder content at 40% opacity with bracket notation
- [ ] All confirmed content at full opacity
- [ ] No element within seam exclusion zone
- [ ] No element outside safe zone

### Exports
- [ ] Proof PNG exported
- [ ] Review PDF exported
- [ ] Physical mock-up completed and reviewed

---

### **STOP POINT SP-08 — PHASE 3 GATE**
**This is the formal Phase 3 gate. It requires explicit approval from the client before Phase 4 begins.**
**Report:** Phase 3 gate checklist completed item by item. All checks confirmed. Proof PNG and review PDF attached. Physical mock-up observations summarized. BRAND_DECISION_FRAMEWORK.md score for overall Phase 3 output: [score]/10 per criterion.
**Phase 4 begins only upon explicit written approval of SP-08.**

---

*This execution plan governs the Illustrator production session for the ALTERNATIVE™ SESSION™ 5MG Passion Fruit label master.*
*Every Stop Point is a gate. No gate is skipped.*
*Every decision made during execution that is not covered by this plan or an existing specification is escalated before it is made.*
