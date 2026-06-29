# PROJECT TRUTH — ALTERNATIVE™ Label Program

**Purpose:** The reconciled "what is actually true right now" layer for the program — what is locked, what is provisional, what is rejected/paused, where the live conflict is, and what is owed by whom. Derived strictly from the current repository.
**Last synchronized:** 2026-06-29 · **Branch:** `claude/project-state-summary-l85bxh` · **Commit:** `b5a7392`
**Read order:** START_HERE.md → HANDOFF.md → **PROJECT_TRUTH.md**

> Where this file references a decision or risk, the authoritative detail lives in DECISIONS_LOG.md and RISK_REGISTER.md. This file does not supersede them; it reconciles them into current truth.

---

## Current objective
Produce the print-ready label master for **ALTERNATIVE™ SESSION™ 5MG Passion Fruit** (12 oz Canworks sleek can) as the production foundation for all future SKUs — beverage-first, THC-second, typography-led, Matte Black + Metallic Gold, no illustration. Immediate objective is completing **Phase 3 (Illustrator Production Setup)** with placeholders; final production approval is gated on official brand vectors and compliance inputs.

---

## Locked decisions (confirmed — do not relitigate)
| Ref | Decision |
|---|---|
| DEC-011 | Tagline **"A NEW STATE OF MIND"** — Level 1 of front hierarchy, above the Hero A |
| DEC-012 | **8-level front-panel reading hierarchy** (LABEL_SPECIFICATION Part 3) |
| DEC-013 | Category descriptor **"HEMP-DERIVED THC BEVERAGE"** (Level 6) |
| DEC-014 | Website **AlternativeBev.com** on label, consistent across SKUs |
| DEC-015 | **UPC 860013732455** confirmed |
| DEC-016 | QR CTA **"SCAN FOR LAB RESULTS & PRODUCT INFO"** |
| DEC-017 | **No-illustration policy** — no photography, fruit, or decorative icons; typography + Hero A only |
| DEC-018 | **9-layer Illustrator structure** (01_GUIDES → 09_EXPORT) supersedes old 13-layer plan |
| DEC-019 | File naming `ALTERNATIVE_SESSION_5MG_PASSIONFRUIT_MASTER_v[###].ai` |
| DEC-020 | **Product architecture**: SESSION 5mg / SOCIAL 10mg / RESERVE 50mg / ASCEND 100mg; Passion Fruit master = foundation |
| DEC-021 | **Information panel content** set (adds Directions, Storage, Batch, Lot, Best By) |
| DEC-022 | **Hero A at Level 2**, directly below tagline; dominates the front panel; typography supports, does not compete |
| DEC-023 | **Söhne (Klim Type Foundry)** = exclusive brand typeface — FINAL LOCK with 3 corrections (CS-02 vector wordmark primary / CS-04 Söhne Buch–Halbfett for dose / CS-17 Helvetica Neue is FDA-only compliance exception) |
| Brand | **Matte Black + Metallic Gold** locked as brand identity (CREATIVE_DIRECTION §3) |
| Spec | Dieline: **182.22mm × 148.00mm** trim, **0.125"** bleed (Canworks 12 oz sleek can) |

---

## Provisional / unconfirmed items (in use but not final)
- **TEMP_HERO_A** and **TEMP_WORDMARK** placeholders — live, editable, explicitly TEMPORARY; layout built to receive official vectors with zero repositioning (R-01 / R-01B).
- **Gold rendering** in current SVG proofs is a **screen simulation** of the R-04 finish — not a confirmed production method.
- **Söhne in artwork** is a temporary stand-in until the font is licensed/installed (klim.co.nz).
- **CMYK/Pantone** for Matte Black + Warm White — not yet provided (DEC-P003); no swatch work is final.
- **Compliance, manufacturer, ingredient, micronutrient, QR URL, distribution-states** copy — placeholder only.
- **Progress percentage** — source files disagree (**42%** header vs **35%** body in PROJECT_STATUS.md; CHANGELOG 2.2.0 cites 42%). Treated as **~35–42%**, unreconciled pending a single owner figure.
- **Default branch** — `origin/HEAD` not set on the remote; only `claude/project-state-summary-l85bxh` is advertised.

---

## Rejected / paused directions
- **Futura as brand typeface** — ❌ REJECTED. Futura appeared in the Canworks dieline as template documentation only; explicitly superseded by Söhne (DEC-023 / DEC-P001 closed). R-02 CLOSED.
- **Photography, fruit illustrations, decorative icons** — ❌ REJECTED by DEC-017.
- **Green / cannabis-coded accents** — ❌ REJECTED (CREATIVE_DIRECTION §2/§3); reads as cannabis, closes the premium-beverage channel.
- **Original 13-layer Illustrator structure** — ⏸ SUPERSEDED by the 9-layer Brand Bible structure (DEC-018).
- **Option A/B/C hero visual direction decision** — ⏸ CLOSED (R-CLOSED-04); answer is typographic/compositional + Hero A only.

---

## Current design direction conflict (DOCUMENT ONLY — do not reconcile)
There is an unresolved tension between the **locked specification** and the **latest exploration**:

- **Locked (DEC-022 + CREATIVE_DIRECTION §2):** the **Hero A dominates** the front panel at Level 2; the wordmark and typography support it.
- **Latest commits (Phase 4 v008–v009):** front-panel exploration has shifted toward **wordmark-led / wordmark-authority** treatment ("Hero A rebuilt as monoline mark + wordmark authority" → "wordmark-led front exploration").
- **Secondary tension:** R-01 states the **official Hero A may never be recreated** — yet the explorations **rebuild** a Hero A mark (v005–v008). This is acceptable only because the marks are explicitly TEMPORARY placeholders, not final art. It must not be mistaken for final Hero A approval.

**Status:** Open. Requires client/creative-director direction on whether the front panel is **Hero A-dominant** (current lock) or **wordmark-led** (latest exploration) before Phase 4 is formally gated. No reconciliation in this session.

---

## External dependencies (owned outside this repo)
| Dependency | Owner | Unblocks |
|---|---|---|
| Official Hero A vector + wordmark vector | Client | Final production approval (R-01) |
| Metallic Gold method + Pantone Metallic ref | Client / Canworks | Color system (R-04, DEC-P002) |
| CMYK + Pantone for Matte Black / Warm White | Client | Swatches (R-04 area, DEC-P003) |
| Compliance copy (warnings, state THC language) | Legal counsel | Phase 6 (R-05) |
| Manufacturer name + address | Client / Manufacturer | Information panel (R-06) |
| Distribution states list | Client | Compliance sublayers (R-08, DEC-P004) |
| QR destination URL (live) | Client / Dev | QR finalization (R-07) |
| Ingredient terminology sign-off (Delta-9) | Legal counsel | Ingredient copy (R-10) |
| Söhne Print + Desktop license | Client | Production-file delivery (DEC-023) |
| Canworks ICC profile / press gamut | Canworks | Color accuracy (R-11) |

---

## Internal tasks (owned in this repo)
- Open Canworks dieline in Illustrator; verify trim/bleed/safe-zone and record **seam position** (R-03, R-13).
- Build Illustrator document: artboard, 9-layer structure, global swatches (deferred until CMYK arrives), grid/guides.
- Create Söhne Character Styles (17) and Paragraph Styles (14) per BRAND_DESIGN_SYSTEM.md.
- Maintain placeholder swap protocol so official vectors drop in with zero repositioning.
- Keep PROJECT_STATUS / CHANGELOG / RISK_REGISTER / DECISIONS_LOG current after each action.
- Resolve the progress-percentage discrepancy once a single authoritative figure is chosen (not in this session).
- Carry SVG explorations into a native `.ai` master once direction conflict is resolved.

---

*This document is the reconciled truth layer. When it conflicts with memory or assumption, this file and the source documents it cites win.*
