# ALTERNATIVE™ LABEL PROGRAM — DECISIONS LOG
**Program Director:** Claude (AI Production System)
**Last Updated:** 2026-06-26
**Version:** 1.0

Every design, production, and strategic decision is logged here with full rationale. This document is the audit trail for all choices made during the ALTERNATIVE™ production program.

Format: Decision ID | Date | Decision | Rationale | Principle | Made By | Status

---

## DECISIONS — CONFIRMED

### DEC-001
| Field | Value |
|---|---|
| **Date** | 2026-06-26 |
| **Decision** | SOURCE OF TRUTH: Brand Bible and Master Brief supersede all previous label versions |
| **Context** | The repository was empty. Previous labels were referenced in the brief as existing. Client directive established that previous labels are NOT the source of truth. |
| **Rationale** | Building from a previous label preserves its constraints, compromises, and errors. Building from the Brand Bible produces a design system that serves the brand's long-term equity. |
| **Principle** | Brand consistency. Long-term brand equity. |
| **Made By** | Client directive |
| **Status** | ✅ CONFIRMED — LOCKED |

---

### DEC-002
| Field | Value |
|---|---|
| **Date** | 2026-06-26 |
| **Decision** | DIELINE: Canworks flat wrap dieline is the only locked production element. No other production constraints are inherited from previous work. |
| **Context** | Client directive established the dieline as the single locked element. |
| **Rationale** | The dieline is a physical constraint (can format, supplier) that cannot be redesigned. All other design elements are being established fresh. |
| **Principle** | Production reliability. |
| **Made By** | Client directive |
| **Status** | ✅ CONFIRMED — LOCKED |

---

### DEC-003
| Field | Value |
|---|---|
| **Date** | 2026-06-26 |
| **Decision** | BRAND IDENTITY: Matte Black + Metallic Gold are the defining brand colors |
| **Context** | Established as Brand Law #7 in the Executive Directive. |
| **Rationale** | Matte Black signals luxury, sophistication, and confidence. Metallic Gold provides the premium accent that elevates the product above commodity. This pairing is category-defying in THC beverages and positions ALTERNATIVE™ against high-end spirits, not cannabis products. |
| **Principle** | Premium perception. Shelf impact. Brand consistency. |
| **Made By** | Client / Brand Law |
| **Status** | ✅ CONFIRMED — LOCKED — Specific CMYK/Pantone values pending Brand Bible |

---

### DEC-004
| Field | Value |
|---|---|
| **Date** | 2026-06-26 |
| **Decision** | BRAND LAW: Hero A is sacred. It cannot be modified, reinterpreted, or replaced without client approval. |
| **Context** | Established in Executive Directive. Hero A is referenced as a protected brand element. |
| **Rationale** | The most recognizable premium brands are built on consistent, protected marks. Modifying Hero A at any stage undermines the system. |
| **Principle** | Brand consistency. Long-term brand equity. |
| **Made By** | Client / Brand Law |
| **Status** | ✅ CONFIRMED — LOCKED — Hero A asset not yet received |

---

### DEC-005
| Field | Value |
|---|---|
| **Date** | 2026-06-26 |
| **Decision** | PRODUCTION STRATEGY: Design for state-variant scalability from day one. Compliance layers are toggle-able per state within the master .ai file. |
| **Context** | THC beverage regulations vary by state and are actively evolving. |
| **Rationale** | Building a single master with toggle-able state compliance layers eliminates the need to maintain multiple divergent source files. A state variant can be updated and exported without redesign. This reduces error risk and production cost for every future reprint. |
| **Principle** | Scalability. Production reliability. |
| **Made By** | Program Director |
| **Status** | ✅ CONFIRMED |

---

### DEC-006
| Field | Value |
|---|---|
| **Date** | 2026-06-26 |
| **Decision** | QR SPECIFICATION: Error correction level H, minimum 20×20mm, dark on light field |
| **Context** | QR codes on curved cylindrical surfaces require higher fault tolerance than flat surface QR codes. |
| **Rationale** | Error Correction Level H restores up to 30% of data — critical when printing imperfections, surface curvature, and lighting conditions all reduce scan reliability. A QR that fails to scan on a sold product is a brand failure and a consumer experience failure. 20mm minimum ensures reliable scanning at arm's length on a curved surface. Dark-on-light is the established standard for curved surface reliability. |
| **Principle** | Production quality. Consumer trust. |
| **Made By** | Program Director |
| **Status** | ✅ CONFIRMED |

---

### DEC-007
| Field | Value |
|---|---|
| **Date** | 2026-06-26 |
| **Decision** | BARCODE SPECIFICATION: UPC-A, minimum 80% magnification, portrait orientation, minimum 10mm from seam |
| **Context** | Standard US retail barcode requirements. |
| **Rationale** | 80% magnification is the GS1-specified minimum for reliable scanning. Below 80%, scan failure rates increase significantly. Portrait orientation (bars parallel to can axis) is standard and preferred for sleek cans. 10mm seam clearance prevents the seam distortion from affecting bar width accuracy. |
| **Principle** | Production reliability. |
| **Made By** | Program Director |
| **Status** | ✅ CONFIRMED |

---

### DEC-008
| Field | Value |
|---|---|
| **Date** | 2026-06-26 |
| **Decision** | COMPLIANCE COPY RULE: No compliance copy is placed in the production master without legal counsel approval. Placeholder text is used during construction phases only and is clearly marked. |
| **Context** | THC beverages carry regulatory and legal liability. Incorrect compliance language creates business risk. |
| **Rationale** | The design system can be built with correctly-sized and correctly-formatted compliance text areas using placeholder text. Only counsel-approved final copy is placed in the production layer. This protects the brand from compliance errors at every gate. |
| **Principle** | Consumer trust. Production quality. |
| **Made By** | Program Director |
| **Status** | ✅ CONFIRMED |

---

### DEC-009
| Field | Value |
|---|---|
| **Date** | 2026-06-26 |
| **Decision** | MINIMUM TYPE SIZE: 6pt absolute floor across all compliance, legal, and body copy. 7–8pt preferred for compliance text. |
| **Context** | FDA minimum, state regulatory minimums, and readability best practice. |
| **Rationale** | 6pt is the regulatory floor. Premium brands do not push to the legal minimum — they build legibility into the system. A consumer who cannot read the compliance copy is a regulatory risk and a trust failure. 7–8pt on a can surface reads cleanly even under retail lighting conditions. |
| **Principle** | Consumer trust. Production reliability. |
| **Made By** | Program Director |
| **Status** | ✅ CONFIRMED |

---

### DEC-010
| Field | Value |
|---|---|
| **Date** | 2026-06-26 |
| **Decision** | METALLIC GOLD RISK ESCALATED: Canworks must confirm metallic ink or foil capability before design begins. If unavailable, client must approve alternative Gold reproduction strategy before Phase 4. |
| **Context** | Metallic Gold cannot be reproduced by standard CMYK process printing. CMYK Gold is a flat, muted approximation. It does not deliver the premium signal that is the point of the Gold identity. |
| **Rationale** | If the printer cannot achieve true metallic, the Gold brand law cannot be honored through print alone. The client must make an informed decision about reproduction method — not discover the limitation after the design is built. This is a critical risk that must be resolved before a single pixel of Gold is designed. |
| **Principle** | Brand consistency. Premium perception. |
| **Made By** | Program Director |
| **Status** | ✅ ESCALATED — Awaiting Canworks confirmation and client resolution |

---

## DECISIONS — PENDING CLIENT INPUT

### DEC-P001
| Field | Value |
|---|---|
| **Date** | 2026-06-26 |
| **Decision Required** | Hero visual direction: Option A (pure typography), Option B (abstract), or Option C (illustration) |
| **Context** | Section 2.4 of Execution Plan presents three approaches for the front panel hero visual element. |
| **Recommendation** | Option A or Option B. Pure type or abstraction places ALTERNATIVE™ in the same visual category as the world's most premium brands. Illustration risks reading as flavor-first rather than brand-first at 10 feet. |
| **Decision Deadline** | Before Phase 5 begins |
| **Made By** | Pending client |
| **Status** | 🔴 OPEN |

---

### DEC-P002
| Field | Value |
|---|---|
| **Date** | 2026-06-26 |
| **Decision Required** | Distribution states — which states is this label being sold in? |
| **Context** | Drives compliance layer count, legal copy requirements, and Prop 65 determination. |
| **Recommendation** | Provide a confirmed state list. If distribution is being built out incrementally, provide the launch states now and the full target list. |
| **Decision Deadline** | Before Phase 7 begins |
| **Made By** | Pending client |
| **Status** | 🔴 OPEN |

---

### DEC-P003
| Field | Value |
|---|---|
| **Date** | 2026-06-26 |
| **Decision Required** | Metallic Gold reproduction method — confirm with Canworks which method is available: metallic ink, foil stamp, or alternative |
| **Context** | Risk R-15. CMYK cannot reproduce true metallic. |
| **Recommendation** | Confirm Canworks capability immediately before design begins. If foil is available, specify it. If metallic ink is available, provide the Pantone Metallic reference. |
| **Decision Deadline** | Before Phase 4 begins |
| **Made By** | Pending client / Canworks |
| **Status** | 🔴 OPEN |

---

### DEC-P004
| Field | Value |
|---|---|
| **Date** | 2026-06-26 |
| **Decision Required** | Secondary brand elements on label — website, social handles, secondary certifications |
| **Context** | Panel real estate must be allocated before layout begins. |
| **Recommendation** | Less is more on a premium label. Include website URL. Evaluate whether social handles serve the brand or add clutter. Skip certifications unless they add genuine consumer value (organic, etc.). |
| **Decision Deadline** | Before Phase 5 begins |
| **Made By** | Pending client |
| **Status** | 🔴 OPEN |

---

*Decisions log is updated every time a decision is made, escalated, or resolved.*
*Every entry is permanent — decisions are never deleted, only superseded (with cross-reference).*
