# Project plan — GreenSpace Kolding

**Status:** Draft for review · **Updated:** 2026-10-10

## Purpose and audience
Independent GIS portfolio project for public-sector GIS, spatial analytics and urban planning audiences. **Approved research objective (2026-10-10):** GreenSpace Kolding will investigate how easily residents of Kolding urban area can reach publicly accessible green spaces on foot, measured along an actual pedestrian network.

**Operational research question:** How accessible are publicly accessible green spaces to residential areas in urban Kolding, and where are potential gaps?

This is not a municipal policy assessment or official analysis.

## Decision principles
1. Prioritize **defensible methods and reproducibility** over feature count.
2. Publish **no accessibility claims** before source validation and route spot checks.
3. Keep the **city boundary** distinct from the municipal boundary.
4. Treat 300, 500 and 1,000 m as **exploratory thresholds**, not legal or municipal standards.
5. Record source licensing, attribution, coordinate reference systems, acquisition dates and known limitations.
6. Record unresolved questions as issues and block downstream analysis when a critical assumption is unresolved.

## Phase gates

| Phase | Deliverables | Exit gate |
|---|---|---|
| M0: Foundation | Charter, issue board, local environment, CI, data governance | Research scope accepted; clean install/tests verified; governance documented |
| M1: Data readiness | Study boundary, source inventory, green-space classification, access rules | Licenses checked, data available, completeness assessed, origin units defined |
| M2: Baseline | Clean green-space polygons, baseline map, QA | Map reproducible; geometry/classification QA complete |
| M3: Accessibility | Walking network, entrance connections, network distances, indicators | Route samples validated; edge cases and uncertainty documented |
| M4: Communication | Maps, methods, results, accessible project website | A reader can understand provenance, methods and limitations |
| M5: Release | v1.0, test evidence, portfolio walkthrough | Final review passed; release tagged and documented |

**Target dates:** M0 2026-10-16; M1 2026-10-23; M2 2026-10-30; M3 2026-11-06; M4 2026-11-20; M5 2026-11-27. Dates are provisional; failing a gate delays the next phase.

## M0 readiness checklist
- [ ] Approve project charter and analytical scope (issue #4)
- [ ] Configure Kanban, priority conventions and releases (issue #5)
- [ ] Verify clean installation and CI (issues #1, #6)
- [ ] Approve data governance and QA checklist (issue #7)
- [ ] Document risks, assumptions and decision log

## M1 readiness checklist
- [ ] Define Kolding city study boundary (#2)
- [ ] Review dataset inventory, terms and licenses (#3)
- [ ] Define green-space public access and entrances (#8)
- [ ] Choose residential origin/denominator unit and justify choice
- [ ] Confirm usable pedestrian network coverage

## Workflow
Backlog → Ready → In Progress → Review → Done. Every issue has acceptance criteria. PRs document testing, provenance and limitations. Do not mark a phase complete because a calendar date passed.

## Risk register
| Risk | Impact | Mitigation |
|---|---|---|
| Public access cannot be established from polygon labels | Incorrect accessibility | Document entrance/access evidence; exclude uncertain features or flag them |
| Missing pedestrian links | False low coverage | Connectivity QA and sample route checks |
| Inappropriate origin/denominator | Misleading coverage | Choose units before analysis; publish denominator |
| Incompatible data licenses | Cannot redistribute results/data | Check and record license before acquisition/publication |
| Study boundary effects | Biased edge estimates | Include network buffer and test edge sensitivity |
| Timeline overrun | Portfolio delayed | Prefer a credible static map + documented method over an unfinished interactive app |

## Success criteria
A reviewer can clone the repository, understand the data provenance and assumptions, run verified checks, reproduce at least one map or indicator from permitted inputs, and inspect documented validation evidence.

## Links
- [Issues](https://github.com/glaier/greenspace-kolding/issues)
- [README](../README.md)
- [Methodology](methodology.md)
- [Data sources](data-sources.md)
