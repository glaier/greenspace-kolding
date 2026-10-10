# Architecture and analysis decision log

Use an entry per consequential decision, including alternatives, rationale, evidence, and implications.

| ID | Decision | Status | Owner | Date |
|---|---|---|---|---|
| ADR-001 | Use Kolding **urban area** rather than Kolding Municipality as study area | Proposed | Project owner | 2026-10-10 |
| ADR-002 | Use **pedestrian-network distance** rather than Euclidean distance as primary metric | Accepted | Project owner | 2026-10-10 |
| ADR-003 | Treat 300/500/1000 m thresholds as exploratory | Proposed | Project owner | 2026-10-10 |
| ADR-004 | Choose residential origins (addresses, buildings or population grid) after source assessment | Open | Project owner | 2026-10-10 |
| ADR-005 | Define public-access eligibility and green-space entrances before routing | Open | Project owner | 2026-10-10 |

## Approved research objective — 2026-10-10

**Decision:** GreenSpace Kolding will investigate how easily residents of Kolding urban area can reach publicly accessible green spaces on foot, measured along an actual pedestrian network.

**Approved by:** Project owner (in conversation, 2026-10-10).

**Implications:** The primary metric is network-based walking distance, not straight-line distance. Residential origins, green-space inclusion rules, pedestrian access points, thresholds and boundary handling must be specified and validated before analytical claims are published. This approval does **not** yet approve any particular dataset, geographic boundary or residential denominator.

## Decision template
### ADR-XXX: Title
- **Status:** Proposed / Accepted / Superseded
- **Context:**
- **Options considered:**
- **Decision:**
- **Evidence and rationale:**
- **Consequences and risks:**
- **Date:**
