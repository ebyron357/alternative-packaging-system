# ALTERNATIVE™ LABEL PROGRAM — QUALITY CHECKLIST
**Program Director:** Claude (AI Production System)
**Last Updated:** 2026-06-26
**Version:** 1.0

This checklist governs all 8 production gates. No phase advances without the prior gate signed off. Gate completion is documented in CHANGELOG.md and committed to the repository.

---

## BRAND QUALITY STANDARD

Before marking any gate complete, answer these questions:

1. Would this compete beside the finest premium beverages in the world?
2. Would a national retailer proudly stock it?
3. Would someone notice it from 10 feet away?
4. Does it communicate premium before THC?
5. Is the typography exceptional?
6. Is the hierarchy effortless?
7. Can anything be removed to improve clarity?
8. Is every element intentional and earning its place?

**If any answer is "No" — do not advance. Continue refining.**

---

## GATE 1 — BRAND INPUTS COMPLETE

**Exit criteria: All critical assets received and confirmed before Illustrator opens**

### Brand Documents
- [ ] ALTERNATIVE_MASTER_BRIEF.md received and reviewed
- [ ] BRAND_BIBLE.md received and reviewed
- [ ] All values from Brand Bible extracted and documented in LABEL_SPECIFICATION.md
- [ ] Product scope confirmed: SESSION™ 5MG Passion Fruit 12 oz only (this phase)

### Production Foundation
- [ ] Canworks dieline received and opened — dimensions recorded
- [ ] Seam position confirmed and recorded
- [ ] Bleed and safe zone confirmed from dieline
- [ ] Canworks press specifications received (print method, max ink coverage)
- [ ] Canworks ICC color profile received
- [ ] Canworks finish capabilities confirmed (matte, spot UV, foil, metallic ink)
- [ ] Metallic Gold reproduction method confirmed — Risk R-15 resolved

### Brand Assets
- [ ] ALTERNATIVE™ wordmark received — vector, fully outlined
- [ ] SESSION™ sub-brand wordmark received — vector, fully outlined
- [ ] Hero A received — format documented, dimensions confirmed
- [ ] All required logo lockup configurations received

### Typography
- [ ] Primary display typeface files received
- [ ] Primary display typeface print license confirmed
- [ ] Secondary body typeface files received
- [ ] Secondary body typeface print license confirmed

### Color System
- [ ] Matte Black CMYK values confirmed from Brand Bible
- [ ] Matte Black Pantone reference confirmed
- [ ] Metallic Gold CMYK or metallic reference confirmed
- [ ] Passion Fruit accent color CMYK confirmed
- [ ] All swatch values documented in LABEL_SPECIFICATION.md

### Legal & Compliance
- [ ] Distribution state list confirmed
- [ ] Legal counsel has reviewed and approved all compliance copy
- [ ] All state-specific warning copy received (one .txt per state)
- [ ] Universal compliance copy received
- [ ] Prop 65 determination documented
- [ ] Country of origin determination documented

### Product Data
- [ ] Final ingredient list received (exact copy, regulatory order)
- [ ] Allergen statement confirmed
- [ ] Certified nutrition data received from manufacturer/lab
- [ ] THC per serving confirmed (mg)
- [ ] THC per container confirmed (mg)
- [ ] Serving size confirmed
- [ ] Servings per container confirmed

### Barcode
- [ ] GS1 UPC-A number confirmed (12 digits)
- [ ] GS1 registration documentation received

### QR
- [ ] QR destination URL confirmed and live
- [ ] Age gate confirmed as functional on landing page
- [ ] Short URL / redirect strategy confirmed
- [ ] QR call-to-action copy confirmed

### Manufacturer Info
- [ ] Manufacturer legal name confirmed
- [ ] Manufacturer full mailing address confirmed
- [ ] Distributor info confirmed (if applicable)
- [ ] Website URL for label confirmed

**GATE 1 STATUS:** 🔴 NOT STARTED — Awaiting all assets
**GATE 1 SIGN-OFF:** __________________ DATE: __________

---

## GATE 2 — ILLUSTRATOR DOCUMENT SETUP

**Exit criteria: Master .ai file built, configured, and organized before any artwork is placed**

### Document Configuration
- [ ] Artboard dimensions match Canworks dieline exactly (mm verified)
- [ ] Bleed set per Canworks spec
- [ ] Color mode: CMYK confirmed (not RGB)
- [ ] Raster effects resolution: 300 DPI
- [ ] Units: Millimeters
- [ ] Document color profile: Canworks ICC loaded

### Swatch Panel
- [ ] Matte Black loaded as global process swatch — named "ALT Black"
- [ ] Metallic Gold loaded as spot swatch — named "ALT Gold" (Pantone specified)
- [ ] Passion Fruit accent loaded as global process swatch — named "ALT PF Accent"
- [ ] Near-White / Cream loaded as global process swatch — named "ALT Cream"
- [ ] All swatches named and organized — no unnamed colors, no default swatches
- [ ] Registration black confirmed as correct black (not 4-color black for type)

### Character Styles
- [ ] Display Wordmark style created
- [ ] Sub-brand style created
- [ ] Descriptor style created
- [ ] Body/Compliance style created
- [ ] Nutrition Label style created
- [ ] Legal Small style created

### Paragraph Styles
- [ ] Display paragraph style created
- [ ] Sub-brand paragraph style created
- [ ] Descriptor paragraph style created
- [ ] Compliance Body paragraph style created
- [ ] Nutrition Facts paragraph style created
- [ ] Ingredient List paragraph style created

### Layer Structure
- [ ] Layer 00 — DIELINE & GUIDES created and locked
- [ ] Layer 01 — NOTES & ANNOTATIONS created and locked
- [ ] Layer 02 — SPOT / FINISH EFFECTS created
- [ ] Layer 03 — BRAND ARCHITECTURE created
- [ ] Layer 04 — FLAVOR EXPRESSION created
- [ ] Layer 05 — DESCRIPTORS created
- [ ] Layer 06 — COMPLIANCE UNIVERSAL created
- [ ] Layer 07 — COMPLIANCE STATE VARIANTS created with sublayers per state
- [ ] Layer 08 — NUTRITION FACTS created
- [ ] Layer 09 — INGREDIENT LIST created
- [ ] Layer 10 — MANUFACTURER INFO created
- [ ] Layer 11 — QR CODE created
- [ ] Layer 12 — BARCODE created
- [ ] Layer 13 — BACKGROUND / COLOR FIELD created

### Guides & Grid
- [ ] Dieline placed in Layer 00 — locked, set to non-printing
- [ ] Trim guides placed
- [ ] Bleed guides placed
- [ ] Safe zone guides placed
- [ ] Panel division guides placed
- [ ] Vertical grid zones marked (cap / expression / information / foot)
- [ ] Seam position marked

### File Naming & Version
- [ ] File named: ALT_SESSION_PF_5MG_12oz_MASTER_v001.ai
- [ ] File saved in correct project folder
- [ ] Initial commit made to repository

**GATE 2 STATUS:** 🔴 NOT STARTED — Blocked by Gate 1
**GATE 2 SIGN-OFF:** __________________ DATE: __________

---

## GATE 3 — DESIGN LAYOUT APPROVAL

**Exit criteria: Front panel and all secondary panels approved for production build**

### Front Panel (Panel A)
- [ ] ALTERNATIVE™ wordmark placed correctly in cap zone
- [ ] SESSION™ sub-brand placed correctly in information zone
- [ ] Hero A placed and scaled correctly
- [ ] 5MG callout placed and sized correctly
- [ ] PASSION FRUIT flavor name placed and sized correctly
- [ ] 12 FL OZ volume statement placed correctly
- [ ] Forced reading order confirmed: Color → ALTERNATIVE™ → SESSION™ → 5MG/Flavor → Volume
- [ ] No prohibited content on front panel (barcode, QR, nutrition, compliance)

### Visual Quality Review
- [ ] 10-foot rule tested — single dominant impression confirmed
- [ ] Thumbnail test passed — brand readable at 1cm thumbnail
- [ ] No visual clutter — every element earning its place
- [ ] Negative space used as a design element
- [ ] No cannabis, wellness, energy drink, or supplement aesthetic present
- [ ] Premium beverage identity is primary — THC is secondary

### Typography Review
- [ ] One element dominant at every viewing distance
- [ ] No two elements competing for primacy at same scale
- [ ] ™ symbols manually scaled and positioned at cap height
- [ ] All-caps descriptors tracked at minimum +50/1000em
- [ ] Body/compliance text at 0 tracking
- [ ] Type hierarchy maps exactly to Section 5 of Execution Plan

### 360° Continuity Review
- [ ] Panels reviewed as a unified 360° object, not as individual faces
- [ ] Seam alignment confirmed — no element crosses the seam
- [ ] Edge compensation applied within 8mm of wrap edges
- [ ] Color field extends to bleed on all edges

### Creative Director Approval
- [ ] Brand Laws 1–10 verified (ALTERNATIVE_LABEL_EXECUTION_PLAN.md Section 1)
- [ ] Decision Principles 1–8 verified
- [ ] Quality standard questions answered "Yes" for all 8 criteria

**GATE 3 STATUS:** 🔴 NOT STARTED — Blocked by Gate 2
**GATE 3 SIGN-OFF:** __________________ DATE: __________

---

## GATE 4 — PRE-PRESS TECHNICAL REVIEW

**Exit criteria: File is technically ready for pre-press. Zero production errors.**

### Type
- [ ] All type outlined (or font embedding confirmed with printer)
- [ ] No live text in pre-press delivery file
- [ ] No missing glyphs — all characters render correctly

### Images & Links
- [ ] All images embedded — no missing links
- [ ] All embedded images confirmed at 300 DPI or higher at final print size
- [ ] No RGB images — all converted to CMYK before placement

### Colors
- [ ] Zero RGB color values in document
- [ ] Zero undefined / "None" colors on printing elements
- [ ] All spot colors defined correctly as spot (not process)
- [ ] Metallic Gold defined as spot — Pantone number specified
- [ ] All swatch names match LABEL_SPECIFICATION.md
- [ ] No duplicate or conflicting swatch names

### Overprints & Knockouts
- [ ] Overprint settings reviewed — no unintended overprints
- [ ] No unintended knockouts in black elements
- [ ] Spot color overprint behavior confirmed with printer

### Bleed & Trim
- [ ] All background elements extend to bleed on all edges
- [ ] No artwork elements trimmed too close to safe zone
- [ ] Dieline layer set to non-printing — confirmed

### File Integrity
- [ ] No stray points in document
- [ ] No empty paths in document
- [ ] No hidden layers with unexpected content
- [ ] Document swatch panel clean — no unused swatches from template or paste operations
- [ ] File packaged (Illustrator Package function run) — no missing links reported

### PDF Export
- [ ] PDF/X-4 exported (or format confirmed with Canworks)
- [ ] PDF reviewed in Adobe Acrobat preflight — zero errors
- [ ] PDF reviewed visually — matches Illustrator source

**GATE 4 STATUS:** 🔴 NOT STARTED — Blocked by Gate 3
**GATE 4 SIGN-OFF:** __________________ DATE: __________

---

## GATE 5 — BARCODE & QR VERIFICATION

### Barcode
- [ ] UPC-A generated from confirmed GS1 number (not manually drawn)
- [ ] Barcode placed minimum 10mm from seam
- [ ] Barcode orientation: bars parallel to can axis (portrait)
- [ ] Minimum 80% magnification confirmed
- [ ] Full bar height — no truncation
- [ ] Light field confirmed behind barcode
- [ ] Quiet zones confirmed in layout (minimum 9X left, 7X right)
- [ ] Human-readable digits present — minimum 8pt
- [ ] Barcode grade: ANSI/ISO B or better on press proof (tested by verifier)
- [ ] Barcode verification report received from printer

### QR Code
- [ ] QR generated from confirmed destination URL (not placeholder)
- [ ] Error correction level: H
- [ ] Minimum size: 20mm × 20mm on final can
- [ ] Quiet zone: minimum 4 modules on all sides — confirmed in layout
- [ ] QR is dark on light field — not reversed (unless curved scan tested and confirmed)
- [ ] QR placed as vector — not rasterized
- [ ] QR scanned successfully on flat proof
- [ ] QR scanned successfully on curved physical mock-up
- [ ] Destination confirmed: age gate functional, mobile-optimized
- [ ] Short URL redirect confirmed stable

**GATE 5 STATUS:** 🔴 NOT STARTED — Blocked by Gate 4
**GATE 5 SIGN-OFF:** __________________ DATE: __________

---

## GATE 6 — COMPLIANCE VERIFICATION

### Compliance Copy Accuracy
- [ ] All compliance text matches counsel-approved copy exactly (character for character)
- [ ] No compliance text was abbreviated, paraphrased, or reworded
- [ ] THC per serving value matches confirmed manufacturer data
- [ ] THC per container value matches confirmed manufacturer data

### Compliance Typography
- [ ] All compliance text at minimum 6pt
- [ ] All compliance text in clean grotesque (not display typeface)
- [ ] No compliance text on low-contrast background
- [ ] No compliance text on patterned/textured background without clear field

### Required Elements — Universal
- [ ] THC per serving disclosure — present
- [ ] THC per container disclosure — present
- [ ] "Contains THC" statement — present
- [ ] 21+ age restriction text — present
- [ ] 21+ symbol — present, minimum 1/4" diameter, high contrast
- [ ] "Keep out of reach of children" — present
- [ ] "For use only by adults 21+" — present
- [ ] "Not evaluated by the FDA" disclaimer — present
- [ ] Impairment / "do not operate" warning — present

### Required Elements — State Specific
- [ ] All target-state compliance copy present and correct in respective sublayers
- [ ] State layer toggle confirmed functional — correct copy shows for correct state
- [ ] Prop 65 status confirmed — present if required, absent if counsel confirms not required

### Nutrition Facts Panel
- [ ] Panel uses FDA-compliant format (21 CFR 101.9)
- [ ] All nutrient values match certified lab analysis data exactly
- [ ] Serving size matches confirmed manufacturer specification
- [ ] Panel typeset to FDA standards (Helvetica or approved equivalent)
- [ ] Panel on white or light field — high contrast confirmed

### Ingredient List
- [ ] Ingredients listed in INCI/regulatory order (descending by weight)
- [ ] Exact copy matches manufacturer-supplied ingredient list character for character
- [ ] Allergen statement present and correct

### Manufacturer Information
- [ ] Manufacturer legal name: correct
- [ ] Manufacturer full mailing address: correct
- [ ] Distributor info: correct (if applicable)

**GATE 6 STATUS:** 🔴 NOT STARTED — Blocked by Gate 5
**GATE 6 SIGN-OFF:** __________________ DATE: __________

---

## GATE 7 — PRESS PROOF APPROVAL

### Proof Received
- [ ] Press proof received from Canworks (wet proof preferred for launch)
- [ ] Proof reviewed against CMYK targets
- [ ] Proof reviewed against Pantone references (physical Pantone swatch fan used)

### Color Accuracy
- [ ] Matte Black: confirmed — no color shift from target
- [ ] Metallic Gold: confirmed — finish effect reads correctly
- [ ] Passion Fruit accent: confirmed — color accurate to target
- [ ] Type colors: confirmed — no color shift

### Finish Accuracy
- [ ] Matte finish: confirmed across full can
- [ ] Spot UV / foil (if specified): confirmed on proof — registers correctly to artwork
- [ ] No finish bleeds into unwanted areas

### Legibility on Physical Proof
- [ ] ALTERNATIVE™ wordmark: confirmed legible
- [ ] SESSION™ sub-brand: confirmed legible
- [ ] 5MG callout: confirmed legible
- [ ] PASSION FRUIT: confirmed legible
- [ ] 12 FL OZ: confirmed legible
- [ ] All compliance text (6pt): confirmed legible
- [ ] All Nutrition Facts text: confirmed legible
- [ ] Ingredient list: confirmed legible

### Functional Verification on Proof
- [ ] Barcode scanned on proof — confirmed functional
- [ ] QR scanned on proof — confirmed functional
- [ ] Destination verified post-scan

### Sign-Off
- [ ] Signed press proof document completed and returned to Canworks
- [ ] Physical proof retained in project archive

**GATE 7 STATUS:** 🔴 NOT STARTED — Blocked by Gate 6
**GATE 7 SIGN-OFF:** __________________ DATE: __________

---

## GATE 8 — FINAL RELEASE FOR PRODUCTION

### File Package
- [ ] Final .ai master file — all type outlined, all images embedded
- [ ] Final PDF/X-4 — preflighted, zero errors
- [ ] Final soft proof PDF — for client archive
- [ ] Fonts folder (if any non-outlined fonts required by printer)
- [ ] Links folder (if any files not embedded — should be empty)
- [ ] Canworks ICC profile included
- [ ] PRODUCTION_NOTES.txt completed

### Documentation Complete
- [ ] CHANGELOG.md updated with final release entry
- [ ] LABEL_SPECIFICATION.md — all [LOCK REQUIRED] fields resolved
- [ ] RISK_REGISTER.md — all risks addressed or formally accepted
- [ ] DECISIONS_LOG.md — all decisions recorded
- [ ] ASSET_INVENTORY.md — all assets confirmed received
- [ ] All gate sign-offs documented

### Future SKU Readiness
- [ ] Layer structure confirmed as reusable for future flavors
- [ ] State variant automation documented
- [ ] Flavor variant swap process documented
- [ ] Template file (.ait) created and saved separately from production master

### Final Brand Standard Question
- [ ] Does this label compete beside the finest premium beverages in the United States? ✅

**GATE 8 STATUS:** 🔴 NOT STARTED — Blocked by Gate 7
**GATE 8 SIGN-OFF:** __________________ DATE: __________

---

*This checklist is the production standard. No exceptions. No shortcuts.*
*Every gate sign-off is committed to the repository as a tagged release.*
