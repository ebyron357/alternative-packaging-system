# ALTERNATIVE™ LABEL PROGRAM — RISK REGISTER
**Program Director:** Claude (AI Production System)
**Last Updated:** 2026-06-26
**Version:** 1.0

Risk ratings: Impact and Probability scored 1–5. Risk Score = Impact × Probability.
Threshold: Score ≥ 15 = CRITICAL | 10–14 = HIGH | 5–9 = MEDIUM | 1–4 = LOW

---

## ACTIVE RISKS

### R-01 — Brand Bible Not Finalized
| Field | Value |
|---|---|
| **Description** | The Brand Bible has not been received. All typography, color, logo, spacing, and visual system decisions depend on it. |
| **Impact** | 5 — Cannot set CMYK values, typefaces, or logo lockups. All Phase 3–6 work is blocked. |
| **Probability** | 5 — Asset is confirmed missing. |
| **Risk Score** | 25 — CRITICAL |
| **Mitigation** | Phase 3 blocked until received. Strategy documented to allow instant execution upon receipt. |
| **Owner** | Client |
| **Status** | 🔴 OPEN |

---

### R-02 — Master Brief Not Received
| Field | Value |
|---|---|
| **Description** | ALTERNATIVE_MASTER_BRIEF.md has not been uploaded to the repository. |
| **Impact** | 4 — Product spec, flavor direction, dose confirmation, and scope cannot be verified. |
| **Probability** | 5 — Asset is confirmed missing. |
| **Risk Score** | 20 — CRITICAL |
| **Mitigation** | Phase 3 blocked until received. |
| **Owner** | Client |
| **Status** | 🔴 OPEN |

---

### R-03 — Canworks Dieline Not Confirmed
| Field | Value |
|---|---|
| **Description** | The production dieline from Canworks has not been received. Without exact flat wrap dimensions, no Illustrator document can be set up and no artwork can be built. |
| **Impact** | 5 — Blocks Illustrator Phase 4 entirely. Any artwork built to assumed dimensions must be rebuilt. |
| **Probability** | 5 — Asset is confirmed missing. |
| **Risk Score** | 25 — CRITICAL |
| **Mitigation** | Phase 4 hard-blocked. Do not begin Illustrator setup on assumed dimensions. |
| **Owner** | Client / Canworks |
| **Status** | 🔴 OPEN |

---

### R-04 — ALTERNATIVE™ Wordmark Vector Not Available
| Field | Value |
|---|---|
| **Description** | The ALTERNATIVE™ master wordmark in vector format (.ai / .eps, outlined) has not been received. |
| **Impact** | 5 — Cannot build front panel composition. A re-created or rasterized logo is not acceptable for production. |
| **Probability** | 5 — Asset is confirmed missing. |
| **Risk Score** | 25 — CRITICAL |
| **Mitigation** | Phase 5 blocked. Logo must be received from brand owner, not reconstructed. |
| **Owner** | Client |
| **Status** | 🔴 OPEN |

---

### R-05 — SESSION™ Sub-brand Wordmark Not Available
| Field | Value |
|---|---|
| **Description** | The SESSION™ sub-brand wordmark in vector format has not been received. |
| **Impact** | 5 — Cannot build front panel hierarchy. |
| **Probability** | 5 — Asset is confirmed missing. |
| **Risk Score** | 25 — CRITICAL |
| **Mitigation** | Phase 5 blocked alongside R-04. |
| **Owner** | Client |
| **Status** | 🔴 OPEN |

---

### R-06 — UPC Number Not GS1 Registered
| Field | Value |
|---|---|
| **Description** | A GS1-registered UPC barcode number has not been provided. Without it, no barcode can be generated. A barcode is required for retail distribution. |
| **Impact** | 4 — Blocks Phase 7 barcode integration. Cannot ship to retail without a valid UPC. |
| **Probability** | 4 — Not confirmed as registered or in process. |
| **Risk Score** | 16 — CRITICAL |
| **Mitigation** | Initiate GS1 registration immediately (gs1us.org). Timeline: 1–5 business days. Do not finalize label without confirmed number. |
| **Owner** | Client |
| **Status** | 🔴 OPEN |

---

### R-07 — Compliance Copy Not Legally Approved
| Field | Value |
|---|---|
| **Description** | State-specific THC beverage compliance copy has not been received from legal counsel. This includes age warnings, THC disclosures, impairment warnings, and state-mandated language. |
| **Impact** | 5 — No label ships without this. Incorrect compliance copy creates regulatory and legal liability. |
| **Probability** | 5 — Confirmed missing. |
| **Risk Score** | 25 — CRITICAL |
| **Mitigation** | Compliance layer in Illustrator will be built as a placeholder structure. Only counsel-approved copy is placed in the final layer. |
| **Owner** | Legal Counsel / Client |
| **Status** | 🔴 OPEN |

---

### R-08 — Nutrition Facts Data Not Received
| Field | Value |
|---|---|
| **Description** | Certified lab analysis / nutrition facts data has not been received from the manufacturer. Cannot build an accurate FDA-compliant Nutrition Facts panel without it. |
| **Impact** | 4 — Blocks Phase 7. Estimated or placeholder nutrition values cannot appear on a production label. |
| **Probability** | 5 — Confirmed missing. |
| **Risk Score** | 20 — CRITICAL |
| **Mitigation** | Panel layout will be built to the correct FDA format with placeholder values. Actual values are dropped in when received. |
| **Owner** | Manufacturer / Client |
| **Status** | 🔴 OPEN |

---

### R-09 — Typeface Print License Not Confirmed
| Field | Value |
|---|---|
| **Description** | The Brand Bible typefaces have not been received, and print license status is unknown. Some typeface licenses (web, desktop) do not include commercial print. |
| **Impact** | 3 — If print license is absent, typeface must be swapped, affecting visual system. |
| **Probability** | 3 — Unknown until Brand Bible is received. |
| **Risk Score** | 9 — MEDIUM |
| **Mitigation** | Upon Brand Bible receipt, immediately verify print license for all specified typefaces. |
| **Owner** | Client / Type Foundry |
| **Status** | 🟡 MONITORING |

---

### R-10 — QR Scanability on Curved Surface
| Field | Value |
|---|---|
| **Description** | QR codes on curved cylindrical surfaces can fail to scan if the module density is too high, the size is too small, or the quiet zone is compressed. |
| **Impact** | 3 — A non-scanning QR on a shipped product is a quality failure. |
| **Probability** | 2 — Risk is mitigated by design spec (Section 8 of Execution Plan). |
| **Risk Score** | 6 — MEDIUM |
| **Mitigation** | QR must be minimum 20×20mm, Error Correction Level H, tested on a curved physical mock-up before Gate 6 approval. |
| **Owner** | Program Director |
| **Status** | 🟡 MONITORING |

---

### R-11 — Press Gamut Narrower Than Design Assumptions
| Field | Value |
|---|---|
| **Description** | Can printing (typically dry offset or digital direct-to-can) has a narrower color gamut than standard CMYK sheet-fed offset. Colors that look correct on screen or in proofing may be out of gamut on the final can. |
| **Impact** | 4 — Color mismatch on a luxury brand is a critical failure. Matte Black must be true. Metallic Gold must be consistent. |
| **Probability** | 3 — A known risk for all can printing projects. |
| **Risk Score** | 12 — HIGH |
| **Mitigation** | Request Canworks ICC color profile and press proof specification before locking final CMYK values. All colors are confirmed against the printer's actual gamut. |
| **Owner** | Program Director / Canworks |
| **Status** | 🟡 MONITORING |

---

### R-12 — Seam Placement Conflicts With Design Elements
| Field | Value |
|---|---|
| **Description** | The can seam is a physical join point on the flat wrap. If the seam falls within a critical typographic or visual element, it will distort the design on the finished can. |
| **Impact** | 3 — Seam through a wordmark or hero element is a production failure. |
| **Probability** | 2 — Manageable through proper dieline review before layout begins. |
| **Risk Score** | 6 — MEDIUM |
| **Mitigation** | Seam location confirmed on Canworks dieline before Phase 5 begins. Brand elements placed with minimum 10mm clearance from seam. |
| **Owner** | Program Director |
| **Status** | 🟡 MONITORING |

---

### R-13 — State Regulatory Change Post-Production
| Field | Value |
|---|---|
| **Description** | THC beverage regulations are actively evolving in multiple US states. A regulatory change after production could render shipped compliance copy incorrect. |
| **Impact** | 4 — Regulatory non-compliance is a business and legal risk. |
| **Probability** | 2 — Possible but not predictable. |
| **Risk Score** | 8 — MEDIUM |
| **Mitigation** | Layer-based state compliance system in Illustrator enables rapid reprint of a specific state variant without full redesign. Distribution state list reviewed against current regulations at press approval gate. |
| **Owner** | Legal Counsel / Client |
| **Status** | 🟡 MONITORING |

---

### R-14 — Hero A Visual Not Yet Defined
| Field | Value |
|---|---|
| **Description** | The execution plan references "Hero A" as a sacred brand element. The nature, format, and specification of Hero A has not been confirmed or received. |
| **Impact** | 5 — If Hero A is the primary visual element on the label, its absence blocks the entire front panel design. |
| **Probability** | 4 — Not confirmed as existing in final form. |
| **Risk Score** | 20 — CRITICAL |
| **Mitigation** | Confirm Hero A status and format as part of Brand Bible review. If Hero A is a commissioned illustration or custom mark, confirm delivery timeline immediately. |
| **Owner** | Client / Creative Director |
| **Status** | 🔴 OPEN |

---

### R-15 — Gold Metallic Reproduction on Matte Can Surface
| Field | Value |
|---|---|
| **Description** | "Metallic Gold" as a brand color requires either a Pantone metallic ink, a hot foil stamp, or a metallic substrate — it cannot be reproduced by standard CMYK process printing on a matte can surface. |
| **Impact** | 4 — If Gold is a non-negotiable brand element, the print method must support it. If Canworks cannot apply foil or metallic ink, the Gold identity cannot be faithfully reproduced. |
| **Probability** | 3 — Printer capability not yet confirmed. |
| **Risk Score** | 12 — HIGH |
| **Mitigation** | Confirm with Canworks immediately: (1) Is metallic ink available? (2) Is foil stamping available? (3) What is the Gold reference — Pantone 871 C, 876 C, or custom? If metallic ink/foil is unavailable, client must approve an alternative Gold reproduction strategy before design begins. |
| **Owner** | Program Director / Canworks / Client |
| **Status** | 🔴 OPEN — REQUIRES IMMEDIATE RESOLUTION |

---

## CLOSED RISKS
None yet.

---

## RISK SUMMARY

| Score | Count | Status |
|---|---|---|
| CRITICAL (≥15) | 9 | All Open |
| HIGH (10–14) | 2 | Monitoring |
| MEDIUM (5–9) | 4 | Monitoring |
| LOW (<5) | 0 | — |
| **TOTAL** | **15** | |

---

*Risk register reviewed and updated after every phase gate. New risks added as identified.*
