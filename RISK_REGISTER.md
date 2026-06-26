# ALTERNATIVE™ LABEL PROGRAM — RISK REGISTER
**Program Director:** Claude (AI Production System)
**Last Updated:** 2026-06-26
**Version:** 2.0 — Updated after Brand Bible evaluation

Risk ratings: Impact and Probability scored 1–5. Risk Score = Impact × Probability.
Threshold: Score ≥ 15 = CRITICAL | 10–14 = HIGH | 5–9 = MEDIUM | 1–4 = LOW

---

## ACTIVE RISKS — CRITICAL

### R-01 — Hero A Vector Not Received
| Field | Value |
|---|---|
| **Description** | The Hero A is the most sacred brand element. The Brand Bible states only the approved vector may be used — it must never be recreated. The vector has not been received. |
| **Impact** | 5 — Cannot build front panel. Phase 3 (Illustrator Setup) can begin structure, but Phase 4 (Master Construction) is fully blocked without Hero A. |
| **Probability** | 5 — Confirmed missing. |
| **Risk Score** | 25 — CRITICAL |
| **Mitigation** | Reserve Hero A layer (03_BRAND) in Illustrator with correct scale placeholder. Do not proceed to Phase 4 without the vector. |
| **Owner** | Client |
| **Status** | 🔴 OPEN |

---

### R-02 — Typeface Not Explicitly Named in Brand Bible
| Field | Value |
|---|---|
| **Description** | The Brand Bible defines the typographic direction in strong terms (editorial, architectural, premium, confident) but does not name a specific typeface. However, the Canworks dieline PDF contains Futura Bold and Futura Medium — the only typefaces embedded in the template. This is strong evidence but not explicit confirmation. |
| **Impact** | 4 — If Futura is wrong, all typeset elements must be rebuilt. |
| **Probability** | 2 — Futura is highly likely correct based on dieline evidence. |
| **Risk Score** | 8 — MEDIUM |
| **Mitigation** | Client must explicitly confirm: "The brand typeface is Futura." One-word answer resolves this risk. Until confirmed, the Illustrator character styles are set up with Futura as the working typeface, clearly labelled as pending confirmation. |
| **Owner** | Client |
| **Status** | 🟡 NEEDS CONFIRMATION — See FLAG-02 |

---

### R-03 — Canworks Dieline Art Area Not Confirmed
| Field | Value |
|---|---|
| **Description** | The dieline PDF was received. The full page dimensions are confirmed (182.22mm × 148.00mm). However, the exact art area, safe zone insets, seam position, and bleed verification require opening the source file in Illustrator. The PDF cannot be rendered without poppler. |
| **Impact** | 4 — Any artwork placed before the art area is confirmed may need to be repositioned. |
| **Probability** | 2 — The Brand Bible confirms the trim and bleed values directly. Risk is limited to seam position. |
| **Risk Score** | 8 — MEDIUM |
| **Mitigation** | Open the Canworks PDF in Illustrator as the first action in Phase 3. Confirm all dimensions and record seam position before placing any artwork. |
| **Owner** | Program Director |
| **Status** | 🟡 MONITORING — Requires Illustrator session |

---

### R-04 — Metallic Gold Reproduction Method Not Confirmed
| Field | Value |
|---|---|
| **Description** | Metallic Gold is Brand Law. The Brand Bible confirms it is used for the Hero A and premium accents. Standard CMYK process printing cannot reproduce true metallic. Canworks must confirm whether metallic ink or foil is available. |
| **Impact** | 5 — If metallic reproduction is unavailable, the Gold brand identity cannot be honored. This requires a client decision before design begins. |
| **Probability** | 3 — Printer capability not yet confirmed. |
| **Risk Score** | 15 — CRITICAL |
| **Mitigation** | Contact Canworks immediately. Confirm: (1) Is metallic ink available? (2) Is foil stamping available? (3) What is the Pantone Metallic reference for Gold? Client must approve reproduction method before Phase 3 layout begins. |
| **Owner** | Client / Canworks |
| **Status** | 🔴 OPEN — REQUIRES IMMEDIATE RESOLUTION |

---

### R-05 — Compliance Copy Not Received from Legal Counsel
| Field | Value |
|---|---|
| **Description** | All compliance warnings, state-specific THC language, age restrictions, and impairment warnings must be approved by legal counsel before being placed on the label. None have been received. |
| **Impact** | 5 — No label ships without this. Incorrect compliance language creates regulatory and legal liability. |
| **Probability** | 5 — Confirmed missing. |
| **Risk Score** | 25 — CRITICAL |
| **Mitigation** | Compliance layer (06_COMPLIANCE) built with correct formatting and placeholder text only. Real copy placed only after counsel approval. |
| **Owner** | Legal Counsel / Client |
| **Status** | 🔴 OPEN |

---

### R-06 — Manufacturer Information Not Received
| Field | Value |
|---|---|
| **Description** | Manufacturer name and full mailing address are required on the label by federal law. Not yet received. |
| **Impact** | 4 — Label cannot be finalized without this. |
| **Probability** | 4 — Not provided. |
| **Risk Score** | 16 — CRITICAL |
| **Mitigation** | Manufacturer info layer (06_COMPLIANCE) holds placeholder. No production file ships without this confirmed. |
| **Owner** | Client / Manufacturer |
| **Status** | 🔴 OPEN |

---

### R-07 — QR Destination URL Not Live
| Field | Value |
|---|---|
| **Description** | The QR CTA is confirmed ("SCAN FOR LAB RESULTS & PRODUCT INFO"). The destination URL has not been provided. The QR cannot be generated without a confirmed, live URL. |
| **Impact** | 3 — Blocks QR finalization. Layout can be built with placeholder QR. |
| **Probability** | 4 — URL not yet provided. |
| **Risk Score** | 12 — HIGH |
| **Mitigation** | Build QR placeholder in 07_CODES layer at correct size. Generate final QR only when URL is confirmed and live. |
| **Owner** | Client / Development |
| **Status** | 🔴 OPEN |

---

### R-08 — Distribution States Not Confirmed
| Field | Value |
|---|---|
| **Description** | Which US states this product will be sold in drives the compliance layer requirements. Some states have unique mandatory language. Without a confirmed state list, compliance layers cannot be completed. |
| **Impact** | 4 — Incomplete compliance layers. |
| **Probability** | 4 — Not provided. |
| **Risk Score** | 16 — CRITICAL |
| **Mitigation** | Build universal compliance layer first. State-specific sublayers added when distribution list is confirmed. |
| **Owner** | Client |
| **Status** | 🔴 OPEN |

---

### R-09 — Micronutrients Not Confirmed on Nutrition Panel
| Field | Value |
|---|---|
| **Description** | Vitamin D, Calcium, Iron, and Potassium values were not shown on the Nutrition Facts panel image. FDA requires disclosure if present. If all are 0% DV, they may be omitted in certain panel formats. Manufacturer must confirm. |
| **Impact** | 2 — Small change if values are all 0. Medium if any are non-zero (requires FDA panel redesign). |
| **Probability** | 2 — Likely all 0 given the extremely clean formula. |
| **Risk Score** | 4 — LOW |
| **Mitigation** | Build Nutrition Facts panel with micronutrient rows. Client/manufacturer confirms values before Phase 6 gate. |
| **Owner** | Manufacturer / Client |
| **Status** | 🟡 MONITORING |

---

### R-10 — Ingredient Terminology Inconsistency
| Field | Value |
|---|---|
| **Description** | Passion Fruit panel reads "Hemp Derived THC." Lychee SKU reads "Hemp Derived Delta 9 THC." Syrup reads "100% Hemp-Derived Delta 9 THC Distillate." Three products, three different formulations of the same ingredient. Some states require "Delta-9 THC" specifically. |
| **Impact** | 4 — If incorrect term is used, regulatory liability exists in certain states. |
| **Probability** | 3 — Inconsistency confirmed across existing assets. |
| **Risk Score** | 12 — HIGH |
| **Mitigation** | Legal counsel must confirm exact legally correct ingredient term for each distribution state. Do not finalize ingredient copy without counsel sign-off. See FLAG-02. |
| **Owner** | Legal Counsel / Client |
| **Status** | 🔴 OPEN |

---

### R-11 — Press Gamut Narrower Than Design Assumptions
| Field | Value |
|---|---|
| **Description** | Can printing has a narrower color gamut than standard CMYK offset. Matte Black and Warm White must be confirmed against the printer's actual gamut. |
| **Impact** | 4 — Color mismatch on a luxury brand is a critical failure. |
| **Probability** | 3 — Known risk for all can printing projects. |
| **Risk Score** | 12 — HIGH |
| **Mitigation** | Request Canworks ICC color profile before locking CMYK values. All colors confirmed against printer gamut. |
| **Owner** | Program Director / Canworks |
| **Status** | 🟡 MONITORING |

---

### R-12 — QR Scanability on Curved Surface
| Field | Value |
|---|---|
| **Description** | QR codes on cylindrical surfaces can fail to scan if improperly sized or positioned. |
| **Impact** | 3 — Non-scanning QR on a shipped product is a quality failure. |
| **Probability** | 2 — Mitigated by spec (Level H, 20mm min, dark on light). |
| **Risk Score** | 6 — MEDIUM |
| **Mitigation** | Physical curved mock-up scan test required at Gate 5. |
| **Owner** | Program Director |
| **Status** | 🟡 MONITORING |

---

### R-13 — Seam Placement vs. Design Elements
| Field | Value |
|---|---|
| **Description** | The can seam falls at a specific point on the flat wrap. If the seam conflicts with a critical design element, it will distort on the finished can. |
| **Impact** | 3 — Seam through a wordmark or Hero A is a production failure. |
| **Probability** | 2 — Manageable if confirmed before layout. |
| **Risk Score** | 6 — MEDIUM |
| **Mitigation** | Confirm seam location in Illustrator at start of Phase 3. Brand elements placed minimum 10mm from seam. |
| **Owner** | Program Director |
| **Status** | 🟡 MONITORING — Requires Illustrator session |

---

## CLOSED RISKS

### R-CLOSED-01 — UPC Number Not Registered
| Field | Value |
|---|---|
| **Closed:** | 2026-06-26 |
| **Resolution:** | UPC 860013732455 confirmed in Brand Bible. |
| **Previous Status:** | CRITICAL |

### R-CLOSED-02 — QR CTA Copy Unknown
| Field | Value |
|---|---|
| **Closed:** | 2026-06-26 |
| **Resolution:** | "SCAN FOR LAB RESULTS & PRODUCT INFO" confirmed in Brand Bible. |
| **Previous Status:** | MEDIUM |

### R-CLOSED-03 — Website URL Unknown
| Field | Value |
|---|---|
| **Closed:** | 2026-06-26 |
| **Resolution:** | AlternativeBev.com confirmed in Brand Bible. |
| **Previous Status:** | MEDIUM |

### R-CLOSED-04 — Hero Visual Direction Unknown (Option A/B/C)
| Field | Value |
|---|---|
| **Closed:** | 2026-06-26 |
| **Resolution:** | Brand Bible prohibits photography and fruit illustrations. The label relies on typography, composition, and the Hero A only. Direction is confirmed as typographic/compositional — no illustration. |
| **Previous Status:** | MEDIUM |

---

## RISK SUMMARY

| Score | Count | Status |
|---|---|---|
| CRITICAL (≥15) | 5 | All Open |
| HIGH (10–14) | 3 | All Open |
| MEDIUM (5–9) | 3 | Monitoring |
| LOW (<5) | 1 | Monitoring |
| CLOSED | 4 | Resolved |
| **TOTAL ACTIVE** | **12** | |

---

*Risk register reviewed and updated after every phase gate.*
