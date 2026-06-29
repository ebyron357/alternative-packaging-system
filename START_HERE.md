# START HERE — ALTERNATIVE™ Label Program

**Purpose:** One-page onboarding for any new session. Read this first, then HANDOFF.md, then PROJECT_TRUTH.md.
**Last synchronized:** 2026-06-29
**Branch:** `claude/project-state-summary-l85bxh` · **Commit at sync:** `b5a7392`

> This is a packaging/label design program (Adobe Illustrator production), not a software project. "Production" means building the print-ready label master, not deploying code.

---

## What this project is
Designing and producing the print-ready label for **ALTERNATIVE™ SESSION™ 5MG Passion Fruit**, a hemp-derived THC beverage (12 oz sleek can). The Passion Fruit master is the foundation for all future SKUs (SOCIAL 10mg, RESERVE 50mg, ASCEND 100mg).

---

## Files to read first (in order)
1. **START_HERE.md** — this file (orientation)
2. **HANDOFF.md** — session-to-session handoff: state, repo coordinates, next-session prompt
3. **PROJECT_TRUTH.md** — locked vs provisional decisions, conflicts, dependencies
4. **PROJECT_STATUS.md** — phase board, progress, blocker table
5. **DECISIONS_LOG.md** — full decision history (DEC-011 → DEC-023)
6. **RISK_REGISTER.md** — active/closed risks with scores
7. Reference as needed: BRAND_DESIGN_SYSTEM.md, LABEL_SPECIFICATION.md, CREATIVE_DIRECTION.md, ASSET_INVENTORY.md, CHANGELOG.md, ILLUSTRATOR_EXECUTION_PLAN.md, PHASE3_PRODUCTION_SETUP.md

---

## Current phase
**Phase 3 — Illustrator Production Setup (IN PROGRESS).** Phase 4 master artwork has been explored in SVG (up to v009), but formal Phases 4–8 remain gated. Brand system (Phases 1–2) is complete and locked.

> Progress figure is inconsistent across source files (PROJECT_STATUS header says **42%**, its body says **35%**). Treat as **~35–42%**. Do not silently "fix" — see PROJECT_TRUTH.md provisional items.

---

## Current blockers (critical)
- **R-01** — Official **Hero A vector + wordmark vector not received** (TEMP placeholders in use). Final production approval is blocked until official vectors arrive. *Do not re-request from client at this time.*
- **R-04** — **Metallic Gold** reproduction method (ink vs. foil) unconfirmed with Canworks.
- **R-05** — **Compliance copy** from legal counsel not received.
- **R-06** — **Manufacturer name/address** not received.
- **R-08** — **Distribution states** not confirmed.

High: R-07 QR destination URL · R-10 ingredient terminology (Delta-9 wording) · R-11 press gamut.

---

## Next task
Continue **Phase 3 in Illustrator**: open the Canworks dieline, verify all dimensions (trim, bleed, safe zone, **seam position**), then build the artboard, 9-layer structure, global swatches, and Söhne character/paragraph styles — using TEMP_HERO_A / TEMP_WORDMARK placeholders. (See HANDOFF.md for the exact next-session prompt.)

---

## Do NOT do
- ❌ **Do not redesign or modify existing artwork** (Artwork/, Exports/) without explicit instruction.
- ❌ **Do not reconcile the creative-direction conflict** (Hero A-dominant vs wordmark-led) — document only; await client direction.
- ❌ **Do not re-request the Hero A / wordmark vectors** from the client right now (per standing directive).
- ❌ **Do not recreate the official Hero A** as if final — R-01 states the official Hero A may never be recreated; current marks are explicitly TEMPORARY.
- ❌ **Do not finalize** compliance copy, manufacturer info, ingredient terminology, CMYK/Pantone values, or the QR code until the owning blocker is resolved.
- ❌ **Do not create duplicate STATUS/ROADMAP/DECISIONS files** — equivalents already exist (PROJECT_STATUS.md, DECISIONS_LOG.md, RISK_REGISTER.md, CHANGELOG.md, ASSET_INVENTORY.md, ILLUSTRATOR_EXECUTION_PLAN.md).
- ❌ **Do not push to any branch other than** `claude/project-state-summary-l85bxh` without explicit permission.
