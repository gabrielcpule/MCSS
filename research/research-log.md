# Research Log

## 2026-06-05 — Bootstrap

**Decision:** Launched autoresearch to benchmark MCSS v1 framework and evolve it through the two-loop architecture.

**Context:** MCSS v1 framework was just built (31-task implementation plan completed). The framework contains 15 atoms, 8 molecules, 5-layer CSS architecture, design token system, RDFa vocabulary, validation CLI, and ESLint plugin. 126 tests pass, build produces dist/mcss.css (44KB).

**Research question:** "How does MCSS v1 perform against the MCSS-BENCHMARK-V1 suite, and what targeted improvements increase LLM accuracy beyond the 94.2% baseline?"

**Initial hypotheses:**
- H1: Can we reproduce the baseline (>= 90%)?
- H2: Does token naming (short vs namespaced) affect accuracy?
- H3: What's the optimal RDFa annotation density?
- H4: Does a structured context compendium outperform raw source?

**First action:** Run H1 — benchmark MCSS v1 against a representative subset of MCSS-BENCHMARK-V1 to establish the real baseline. The original 94.2% was from Claude 3.5 Sonnet + CONTEXT_COMPENDIUM.md (8,847 token system prompt). We now test with the actual v1 framework files as context.
