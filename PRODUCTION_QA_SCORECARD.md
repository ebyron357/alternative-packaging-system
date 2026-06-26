# ALTERNATIVE™ PRODUCTION QA SCORECARD
**Document:** Final Quality Judgment — Production Master Approval
**Product:** ALTERNATIVE™ SESSION™ 5MG THC Per Can — Passion Fruit
**Program Director:** Claude (AI Production System)
**Date:** 2026-06-26
**Version:** 1.0
**Authority:** No production master is approved for press without passing this scorecard. This is the final gate. A master that fails this scorecard does not ship, regardless of schedule pressure.

---

## HOW THIS SCORECARD WORKS

The scorecard contains 18 categories. Each category is scored 1–10. The 18 category scores are summed and normalized to a 100-point scale (raw total of 180 → ×0.5556 → 100-point score, or evaluated directly as raw/180 expressed as a percentage).

### Approval Requires Both Conditions

1. **Normalized total score of 90/100 or higher** (equivalent to a raw score of 162/180 or higher)
2. **Zero automatic fail conditions triggered** across all 18 categories

If either condition is not met, the master is **NOT APPROVED**. A single automatic fail condition blocks approval even if the total score is 100/100.

### Scoring Discipline

- Score against the printed physical mock-up wrapped on a can, not against the on-screen file
- Score at the three required distances (10 feet, 2 feet, arm's length) where the category specifies
- A category scoring below its pass threshold is documented with the specific failure and the required fix
- Re-scoring after a fix re-evaluates the entire scorecard, not only the failed category — fixes can introduce regressions elsewhere

### Score Bands (applied to every category)

| Band | Meaning |
|---|---|
| 9–10 | Exemplary — exceeds the standard; this is what we are trying to build |
| 7–8 | Pass — meets the standard with no meaningful weakness |
| 5–6 | Marginal — functional but below premium standard; revise |
| 3–4 | Fail — a real defect that undermines the brand or the production |
| 1–2 | Critical fail — the category is broken |

---

## SCORING SUMMARY TABLE

| # | Category | Score (1–10) | Pass Threshold | Auto-Fail? |
|---|---|---|---|---|
| 1 | 10-Foot Shelf Impact | ___ | 8 | |
| 2 | Beverage-First Impression | ___ | 8 | |
| 3 | Premium Perception | ___ | 8 | |
| 4 | Hero A Strength | ___ | 8 | |
| 5 | ALTERNATIVE™ Wordmark Hierarchy | ___ | 8 | |
| 6 | Typography Quality | ___ | 8 | |
| 7 | Whitespace and Spacing | ___ | 8 | |
| 8 | Grid Alignment | ___ | 9 | |
| 9 | Flavor Clarity | ___ | 7 | |
| 10 | THC Clarity | ___ | 9 | |
| 11 | Compliance Integration | ___ | 9 | |
| 12 | Nutrition Readability | ___ | 9 | |
| 13 | QR Scan Readiness | ___ | 9 | |
| 14 | UPC Scan Readiness | ___ | 9 | |
| 15 | Dieline Preservation | ___ | 10 | |
| 16 | Print Readiness | ___ | 9 | |
| 17 | SKU Scalability | ___ | 8 | |
| 18 | Brand Equity Protection | ___ | 8 | |
| | **RAW TOTAL** | **___ / 180** | **162 min** | |
| | **NORMALIZED** | **___ / 100** | **90 min** | |

---

## CATEGORY 1 — 10-FOOT SHELF IMPACT

*Evaluated at 10 feet from the wrapped can.*

**What it measures:** Whether the label creates desire and communicates premium identity from shelf distance before any text is legible.

| Score | Definition |
|---|---|
| 9–10 | The brand commands attention at 10 feet; the Hero A and Matte Black field create immediate desire; the can stands apart from everything around it |
| 7–8 | The label reads clearly as premium at 10 feet; primary identity elements are dominant and legible |
| 5–6 | The label is visible but does not create desire; it does not stand apart from competitors |
| 3–4 | The label is undifferentiated or unclear at 10 feet |
| 1–2 | The label is visually lost at 10 feet |

**Pass threshold:** 8

**Automatic fail conditions:**
- The Hero A is not the dominant visible element at 10 feet
- The label reads as a colored label rather than a Matte Black field at distance
- The label is visually indistinguishable from a generic beverage at 10 feet

**What to fix if it fails:**
- If Hero A is not dominant: increase Hero A scale, reduce competing element weight, increase surrounding negative space
- If the field does not read as Matte Black: verify the background field fills full bleed and no element crowds it
- If undifferentiated: reexamine the front panel composition against CREATIVE_DIRECTION.md Section 1 — the issue is composition, scale, or hierarchy

---

## CATEGORY 2 — BEVERAGE-FIRST IMPRESSION

*Evaluated at 10 feet and 2 feet.*

**What it measures:** Whether the label reads as a premium beverage that contains THC, not as a cannabis product.

| Score | Definition |
|---|---|
| 9–10 | Reads unambiguously as premium beverage; would belong on a premium spirits or fine beverage shelf; THC is a specification, not the message |
| 7–8 | Reads as beverage-first; no cannabis cues; THC present but subordinate |
| 5–6 | Neutral; could read as either beverage or cannabis depending on the viewer |
| 3–4 | A cannabis cue is present, or the dose dominates the impression |
| 1–2 | Reads as cannabis, supplement, or energy drink |

**Pass threshold:** 8

**Automatic fail conditions:**
- Any green color appears anywhere on the label
- Any cannabis visual cue is present (leaf form, haze, hand-lettering, dispensary aesthetic)
- The THC dose callout is the most prominent element at 10 feet
- The category descriptor is styled as a headline rather than a descriptor

**What to fix if it fails:**
- Remove any green or cannabis-adjacent visual cue immediately and entirely
- If dose dominates: reduce THC_STRENGTH scale/weight to its correct Level 5 hierarchy position
- If category reads as headline: reduce CATEGORY to its correct Level 6 descriptor weight (Söhne Leicht)
- Re-test against the editorial test in CREATIVE_DIRECTION.md Section 8

---

## CATEGORY 3 — PREMIUM PERCEPTION

*Evaluated at 2 feet and arm's length.*

**What it measures:** Whether the label is genuinely premium or performs premium through surface signals (cheap luxury).

| Score | Definition |
|---|---|
| 9–10 | Genuinely premium; the confident choice of an established brand; no cheap luxury signals |
| 7–8 | Premium and restrained; well-executed; no dominant surface signals |
| 5–6 | Competent but conventional; premium signal is borrowed rather than owned |
| 3–4 | Relies on surface luxury (gold, tracking, matte) as a substitute for brand idea |
| 1–2 | Reads as cheap luxury — a product trying to appear premium |

**Pass threshold:** 8

**Automatic fail conditions:**
- Gold is used decoratively (borders, rules, fills) rather than for identity and approved accents only
- The word "premium," "luxury," "craft," "artisanal," or "elevated" appears anywhere in the label copy
- More than one typeface family is used for brand text (Söhne only; Helvetica Neue is the FDA-table exception)

**What to fix if it fails:**
- Remove all decorative gold; gold remains only on the Hero A and approved structural accents (08_FINISHES)
- Remove any self-describing premium language from copy
- Eliminate any non-Söhne brand typography
- Review against the cheap luxury checklist in BRAND_DECISION_FRAMEWORK.md Section 9

---

## CATEGORY 4 — HERO A STRENGTH

*Evaluated at 10 feet and 2 feet.*

**What it measures:** Whether the Hero A functions as the primary recognition asset with correct dominance, placement, and reproduction quality.

| Score | Definition |
|---|---|
| 9–10 | The Hero A is unmistakably the primary brand mark; dominant, precisely reproduced, correctly placed; it is the thing the consumer remembers |
| 7–8 | The Hero A is dominant and correctly placed; reproduction is clean |
| 5–6 | The Hero A is present and prominent but does not command; or reproduction is acceptable but not crisp |
| 3–4 | The Hero A does not dominate, or its reproduction is degraded |
| 1–2 | The Hero A is weak, off-center, poorly reproduced, or competing with other elements |

**Pass threshold:** 8

**Automatic fail conditions:**
- The Hero A on the production master is the TEMP_HERO_A placeholder (official vector not yet supplied)
- The Hero A is rasterized or recreated from reference rather than the official approved vector
- The Hero A is positioned within the seam exclusion zone

**What to fix if it fails:**
- If still a placeholder: the master cannot be approved for production — official Hero A vector is required (see R-01)
- If rasterized/recreated: replace with the official vector per the swap protocol in PHASE3_PRODUCTION_SETUP.md Section 11
- If position conflicts with seam: reposition per the seam exclusion rule; do not move it across hierarchy

---

## CATEGORY 5 — ALTERNATIVE™ WORDMARK HIERARCHY

*Evaluated at 2 feet.*

**What it measures:** Whether ALTERNATIVE™ correctly dominates SESSION™ and anchors the brand architecture.

| Score | Definition |
|---|---|
| 9–10 | ALTERNATIVE™ is clearly the masterbrand; visually dominant over SESSION™; the brand family logic is unmistakable |
| 7–8 | ALTERNATIVE™ correctly dominates SESSION™; hierarchy is clear |
| 5–6 | ALTERNATIVE™ is larger than SESSION™ but the dominance is not decisive |
| 3–4 | ALTERNATIVE™ and SESSION™ read at near-equal weight |
| 1–2 | SESSION™ dominates, or reads as the primary brand |

**Pass threshold:** 8

**Automatic fail conditions:**
- SESSION™ is equal to or larger than ALTERNATIVE™ in visual weight
- The ™ symbol on either wordmark uses default superscript rather than cap-height manual scaling
- The official wordmark relationship cannot be maintained when the SESSION™ tier name is swapped for SOCIAL™/RESERVE™/ASCEND™

**What to fix if it fails:**
- If SESSION dominates: increase ALTERNATIVE™ scale/weight and/or reduce SESSION™ per CREATIVE_DIRECTION.md Section 6
- If ™ is default superscript: manually scale to cap height per BRAND_DESIGN_SYSTEM.md CS-02/CS-03
- If tier swap breaks hierarchy: rebuild the relationship so it holds for all four tiers

---

## CATEGORY 6 — TYPOGRAPHY QUALITY

*Evaluated at 2 feet and arm's length.*

**What it measures:** Whether every typographic decision is correct in weight, size, tracking, leading, and optical alignment.

| Score | Definition |
|---|---|
| 9–10 | Every attribute is intentional and correct; hierarchy is immediately legible; optical refinement is present throughout |
| 7–8 | Typography is correct; hierarchy is clear; minor refinements possible |
| 5–6 | Functional but unrefined; hierarchy readable but not authoritative |
| 3–4 | Errors in weight, size, or spacing undermine hierarchy or readability |
| 1–2 | Typography is incorrect for role; hierarchy broken |

**Pass threshold:** 8

**Automatic fail conditions:**
- Any brand text uses a typeface other than Söhne (Helvetica Neue permitted in the Nutrition Facts table only)
- Any text element is not assigned to its correct Character Style
- Tracking is inconsistent between elements at the same hierarchy level
- Any text is below the 6pt absolute floor

**What to fix if it fails:**
- Replace any non-Söhne brand text with the correct Söhne style
- Assign every text object to its named Character Style
- Standardize tracking within each hierarchy level
- Raise any sub-6pt text to the floor; if it does not fit, fix the panel layout, not the type size

---

## CATEGORY 7 — WHITESPACE AND SPACING

*Evaluated via the squint test and at 2 feet.*

**What it measures:** Whether negative space is used as a strategic asset and inter-element spacing is intentional and graduated.

| Score | Definition |
|---|---|
| 9–10 | Spacing is specific and intentional; composition breathes; hierarchy gaps are graduated; the label reads as confident |
| 7–8 | Spacing is generous and mostly intentional; composition has room |
| 5–6 | Spacing is default-generous rather than designed; hierarchy gaps are uniform |
| 3–4 | Spacing is insufficient or inconsistent; the composition feels crowded |
| 1–2 | The label is crowded or the spacing is arbitrary |

**Pass threshold:** 8

**Automatic fail conditions:**
- Any element touches or crosses the safe zone boundary
- The composition fails the squint test (reads as crowded or asymmetrically weighted)
- Hierarchy levels use uniform spacing (the front panel reads as a list, not a hierarchy)

**What to fix if it fails:**
- Pull any element off the safe zone into the live area
- If squint test fails: reduce element count or increase margins; the issue is density
- If spacing is uniform: graduate the gaps — largest between Hero A and wordmark, decreasing down the hierarchy (CREATIVE_DIRECTION.md Section 10)

---

## CATEGORY 8 — GRID ALIGNMENT

*Evaluated against the document guides.*

**What it measures:** Whether elements align to the established grid and optical alignment is applied where required.

| Score | Definition |
|---|---|
| 9–10 | Every element aligns to the grid; optical alignment applied to display type; alignment is precise and intentional |
| 7–8 | Elements align to the grid; minor optical refinements possible |
| 5–6 | Most elements align but some are off-grid without intention |
| 3–4 | Multiple elements are misaligned |
| 1–2 | No coherent alignment system is visible |

**Pass threshold:** 9

**Automatic fail conditions:**
- Display type is mathematically centered without optical correction (round/pointed forms appear off-center)
- Any element is off-grid without a documented intentional reason
- The front panel centerline is not consistent across hierarchy levels

**What to fix if it fails:**
- Apply optical alignment to all display type per BRAND_DECISION_FRAMEWORK.md Section 5
- Snap off-grid elements to the grid or document the intentional exception
- Align all front panel hierarchy elements to a single vertical centerline

---

## CATEGORY 9 — FLAVOR CLARITY

*Evaluated at 2 feet.*

**What it measures:** Whether PASSION FRUIT is clearly readable at its correct Level 7 hierarchy position — secondary to brand, but unambiguous.

| Score | Definition |
|---|---|
| 9–10 | Flavor is clearly readable at 2 feet and correctly subordinate to brand; the consumer knows the flavor without effort |
| 7–8 | Flavor is readable and correctly positioned |
| 5–6 | Flavor is readable but either too prominent or slightly cramped |
| 3–4 | Flavor is hard to read or competes with brand elements |
| 1–2 | Flavor is illegible or dominates the hierarchy |

**Pass threshold:** 7

**Automatic fail conditions:**
- The flavor name is illegible at 2 feet
- The flavor name competes with or exceeds the brand elements in visual weight
- The flavor name styling differs from what would carry to LYCHEE SWEET TEA (breaks the system)

**What to fix if it fails:**
- If illegible: increase to comfortable Level 7 readability without exceeding the hierarchy ceiling
- If competing: reduce to correct Level 7 weight per CREATIVE_DIRECTION.md Section 8
- If system-breaking: confirm the flavor style works for variable flavor-name lengths

---

## CATEGORY 10 — THC CLARITY

*Evaluated at 2 feet and arm's length.*

**What it measures:** Whether 5MG THC PER CAN is clear, accurate, and readable as required — without overpowering the brand.

| Score | Definition |
|---|---|
| 9–10 | THC content is unmistakably clear at purchase distance; accurate; correctly subordinate to brand |
| 7–8 | THC content is clear and correctly positioned |
| 5–6 | THC content is readable but slightly weak, or slightly too prominent |
| 3–4 | THC content is hard to read or dominates |
| 1–2 | THC content is illegible or is the dominant front-panel element |

**Pass threshold:** 9

**Automatic fail conditions:**
- The THC content (5MG) is not legible at arm's length
- The stated dose does not exactly match the confirmed product data (5mg per can)
- The THC callout is the most prominent element at 10 feet
- The THC callout uses Söhne Leicht (the rejected too-delicate weight — must be Buch or Halbfett)

**What to fix if it fails:**
- If illegible: increase to Söhne Buch/Halbfett at a shelf-readable size
- If dose mismatch: correct to 5mg immediately and verify against CONFIRMED_PRODUCT_DATA.md
- If dominating: reduce to correct Level 5 position
- If wrong weight: apply CS-04 (Söhne Buch or Halbfett) per DEC-023 correction

---

## CATEGORY 11 — COMPLIANCE INTEGRATION

*Evaluated at arm's length.*

**What it measures:** Whether compliance copy is legally complete, correctly placed, and typographically integrated rather than pasted on.

| Score | Definition |
|---|---|
| 9–10 | All required compliance present, correctly sized, and set with the same care as display type; feels integral to the design |
| 7–8 | All compliance present, correctly sized, legible; integration is good |
| 5–6 | Compliance present and legible but visually an afterthought |
| 3–4 | A compliance element is below size minimum or has legibility issues |
| 1–2 | Compliance is missing, illegible, or incorrectly specified |

**Pass threshold:** 9

**Automatic fail conditions:**
- Any compliance copy is placeholder text (40% opacity bracket notation still present)
- Compliance copy has not been approved by legal counsel (R-05 open)
- Any required warning, age statement, or state-mandated language is missing
- Manufacturer name and address is missing or placeholder (R-06 open)
- Any compliance text is below the 6pt floor

**What to fix if it fails:**
- Replace all placeholder compliance copy with counsel-approved final copy
- Confirm legal counsel sign-off is documented before approval
- Add any missing required language for the confirmed distribution states
- Insert confirmed manufacturer name and address
- Raise any sub-6pt text to the floor by adjusting the panel layout

---

## CATEGORY 12 — NUTRITION READABILITY

*Evaluated at arm's length.*

**What it measures:** Whether the FDA Nutrition Facts panel is correctly formatted, complete, and legible.

| Score | Definition |
|---|---|
| 9–10 | Nutrition Facts panel is FDA-compliant, complete, crisp, and fully legible |
| 7–8 | Panel is compliant and legible; minor refinements possible |
| 5–6 | Panel is legible but has a formatting weakness |
| 3–4 | Panel has a formatting error or a legibility issue |
| 1–2 | Panel is non-compliant or illegible |

**Pass threshold:** 9

**Automatic fail conditions:**
- Micronutrient values (Vitamin D, Calcium, Iron, Potassium) are still placeholder (FLAG-01 open)
- The panel uses a non-FDA-compliant typeface for the table body (must be Helvetica Neue per CS-17)
- Any nutrition value does not match CONFIRMED_PRODUCT_DATA.md
- The panel is set on anything other than the Brand_Nutrition_White field

**What to fix if it fails:**
- Insert manufacturer-confirmed micronutrient values
- Apply Helvetica Neue per the FDA exception (CS-17) to the table body
- Verify every value against confirmed product data
- Place the panel on the white field

---

## CATEGORY 13 — QR SCAN READINESS

*Evaluated by physical scan test on the curved mock-up.*

**What it measures:** Whether the QR code is final, correctly specified, and scans reliably on the curved can surface.

| Score | Definition |
|---|---|
| 9–10 | Final QR scans reliably on the curved surface from multiple angles; correctly sized and positioned |
| 7–8 | QR scans reliably; specification is correct |
| 5–6 | QR scans but inconsistently, or is at minimum size |
| 3–4 | QR scans only at certain angles or distances |
| 1–2 | QR does not scan |

**Pass threshold:** 9

**Automatic fail conditions:**
- The QR code is still the placeholder (URL pending, R-07 open)
- The QR destination URL is not live
- The QR code is below 20mm × 20mm
- The QR code fails a physical scan test on the curved surface
- The QR code is not vector

**What to fix if it fails:**
- Generate the final QR from the confirmed live URL (Error Correction Level H)
- Verify the destination URL resolves correctly
- Size to at least 20mm × 20mm
- Re-test on the curved mock-up; reposition away from high-curvature zones if needed
- Regenerate as vector

---

## CATEGORY 14 — UPC SCAN READINESS

*Evaluated by physical scan test on the curved mock-up.*

**What it measures:** Whether the UPC-A barcode is correct, correctly specified, and scans reliably.

| Score | Definition |
|---|---|
| 9–10 | UPC-A scans reliably on the curved surface; correct number, magnification, and quiet zone |
| 7–8 | UPC-A scans reliably; specification correct |
| 5–6 | UPC-A scans but is at minimum magnification or quiet zone |
| 3–4 | UPC-A scans inconsistently |
| 1–2 | UPC-A does not scan or has an incorrect number |

**Pass threshold:** 9

**Automatic fail conditions:**
- The barcode number is not exactly 860013732455
- The barcode is below 80% magnification
- The quiet zone is less than the UPC-A minimum
- The barcode fails a physical scan test
- The barcode is rasterized rather than vector
- The barcode bars are not on a light field (must be dark-on-light)

**What to fix if it fails:**
- Correct the number to 860013732455 (DEC-015) and verify the check digit
- Increase magnification to at least 80%
- Add the required quiet zone each side
- Regenerate as vector, dark bars on Brand_Nutrition_White
- Re-test on the curved mock-up

---

## CATEGORY 15 — DIELINE PRESERVATION

*Evaluated against the Canworks dieline.*

**What it measures:** Whether the locked Canworks dieline has been preserved exactly — trim, bleed, safe zone, and seam.

| Score | Definition |
|---|---|
| 9–10 | Dieline preserved exactly; trim, bleed, safe zone, and seam all match the Canworks template precisely |
| 7–8 | Dieline preserved; all critical dimensions match |
| 5–6 | Dieline mostly preserved with a minor deviation |
| 3–4 | A dieline dimension has been altered |
| 1–2 | The dieline has been modified |

**Pass threshold:** 10 (this category must be perfect)

**Automatic fail conditions:**
- Trim dimensions are not exactly 182.22mm × 148.00mm
- Bleed is not exactly 0.125" on all sides
- Any artwork crosses the seam centerline
- Any critical brand element is within 10mm of the seam
- The dieline geometry has been modified in any way

**What to fix if it fails:**
- Restore exact trim and bleed dimensions
- Move any seam-crossing artwork into a single panel
- Pull brand elements out of the seam exclusion zone
- The Canworks dieline is the only locked production element — it is never modified

---

## CATEGORY 16 — PRINT READINESS

*Evaluated against the production file.*

**What it measures:** Whether the file is technically ready for press — color mode, resolution, swatches, fonts, and finishes.

| Score | Definition |
|---|---|
| 9–10 | Fully press-ready; CMYK, 300 PPI, global swatches, no rogue colors, finishes correctly isolated |
| 7–8 | Press-ready; minor pre-press confirmations remaining |
| 5–6 | Mostly ready with one technical gap |
| 3–4 | A technical issue would require correction before press |
| 1–2 | The file is not press-ready |

**Pass threshold:** 9

**Automatic fail conditions:**
- The document is not in CMYK color mode
- Any raster effect is below 300 PPI
- Any color is a local color rather than a global swatch
- Any swatch still carries a TBD working value rather than a confirmed production value
- Gold elements are not isolated on layer 08_FINISHES
- The Metallic Gold production method is not confirmed with Canworks (R-04 open)
- Any font is not outlined or embedded for final production output

**What to fix if it fails:**
- Convert to CMYK; raise raster effects to 300 PPI
- Replace local colors with global swatches
- Update all TBD swatches to confirmed production values
- Move all gold to 08_FINISHES
- Confirm the gold production method with Canworks
- Outline or embed fonts for the production output (keep the editable master with live text)

---

## CATEGORY 17 — SKU SCALABILITY

*Evaluated by simulating a second SKU.*

**What it measures:** Whether the master functions as a system that carries to all current and planned SKUs without redesign.

| Score | Definition |
|---|---|
| 9–10 | The master works identically for all tiers and flavors by swapping variable content only; the system is robust |
| 7–8 | The master carries to other SKUs with minor content-length adjustments |
| 5–6 | The master carries to other SKUs but requires reconsideration of some elements |
| 3–4 | The master creates special cases that need per-SKU management |
| 1–2 | The master cannot scale without redesign |

**Pass threshold:** 8

**Automatic fail conditions:**
- Swapping SESSION™ for a longer tier name (RESERVE™, ASCEND™) breaks the layout
- Swapping PASSION FRUIT for a longer flavor name (LYCHEE SWEET TEA) breaks the layout
- Any element is hard-coded in a way that prevents variable content substitution

**What to fix if it fails:**
- Rebuild the affected element to accommodate variable content length
- Confirm the tier and flavor styles hold for the longest planned names
- Remove any hard-coded dependency that blocks substitution

---

## CATEGORY 18 — BRAND EQUITY PROTECTION

*Evaluated holistically against the brand system.*

**What it measures:** Whether the master, taken as a whole, strengthens long-term brand equity and protects the brand laws.

| Score | Definition |
|---|---|
| 9–10 | The master advances brand recognition and equity; every brand law is honored; this can builds the franchise |
| 7–8 | The master is consistent with the brand system and creates no equity risk |
| 5–6 | The master is neutral; it neither builds nor erodes equity |
| 3–4 | The master contains a decision that weakens the brand system |
| 1–2 | The master violates a brand law or fragments the brand identity |

**Pass threshold:** 8

**Automatic fail conditions:**
- Any of the 10 Brand Laws (BRAND_DESIGN_SYSTEM.md Part 3.1) is violated
- The master introduces a visual element that would not carry across the brand system
- The master would fragment brand recognition if it shipped alongside other SKUs

**What to fix if it fails:**
- Identify the violated brand law and correct the offending element
- Remove any non-systemic visual element
- Confirm the master reads as part of the family per CREATIVE_DIRECTION.md Section 12

---

## FINAL APPROVAL DECISION

| Condition | Requirement | Met? |
|---|---|---|
| Normalized total score | ≥ 90 / 100 | ___ |
| Raw total score | ≥ 162 / 180 | ___ |
| Automatic fail conditions triggered | 0 | ___ |

### Disposition

- **APPROVED FOR PRODUCTION** — Both conditions met. Document the scorecard in DECISIONS_LOG.md and proceed to Phase 8 production export.
- **NOT APPROVED** — One or both conditions not met. Document every failed category and every triggered automatic fail. Apply the prescribed fixes. Re-score the entire scorecard from the beginning.

**No master is approved for press with a score below 90/100 or with any automatic fail condition active. Schedule pressure does not override this gate.**

---

## NOTE ON CURRENT BLOCKERS

As of this scorecard's creation, the following open items would trigger automatic fail conditions and must be resolved before any approval attempt:

| Open Item | Blocks Category | Auto-Fail Trigger |
|---|---|---|
| Official Hero A vector not supplied (R-01) | 4 — Hero A Strength | Placeholder in use |
| Official wordmark vector not supplied (R-01B) | 5 — Wordmark Hierarchy | Fallback in use (confirm if permanent) |
| Compliance copy not approved (R-05) | 11 — Compliance Integration | Placeholder copy present |
| Manufacturer info missing (R-06) | 11 — Compliance Integration | Placeholder present |
| Micronutrients unconfirmed (FLAG-01) | 12 — Nutrition Readability | Placeholder values present |
| QR URL not live (R-07) | 13 — QR Scan Readiness | Placeholder QR present |
| Gold production method unconfirmed (R-04) | 16 — Print Readiness | Method not confirmed |
| Production color values unconfirmed (DEC-P003) | 16 — Print Readiness | TBD swatches present |

This scorecard cannot return an APPROVED disposition until these items are resolved. It is published now so that the standard is fixed before the work is judged — the bar is set independently of the result.

---

*This scorecard is the final quality gate for the ALTERNATIVE™ production master.*
*It is applied to the physical wrapped mock-up, not the on-screen file.*
*Approval requires 90/100 and zero automatic fails. There are no exceptions.*
