# Findings

## Central Finding: MCSS Teaches Its Rules 4× More Effectively Than Tailwind

The three-way experiment (no framework, MCSS, Tailwind) on 20 identical developer prompts:

| | No Framework | MCSS | Tailwind |
|---|---|---|---|
| Own-rules compliance | 0% | **80%** | 20% |
| Lift from baseline | — | **+80%** | +20% |
| Tokens per prompt | 2,217 | 1,601 | 1,460 |

**Neither framework's conventions are innate to the LLM.** Without a system prompt, the LLM produces generic HTML/CSS that follows zero framework conventions. Both compendiums teach their rules — but MCSS teaches 4× more effectively.

## All Results

| Hypothesis | Finding | Result |
|---|---|---|
| H1: Baseline | MCSS v1 achieves 90% on 100-prompt benchmark | NFR-5 validated |
| H2: Token Naming | Short names: +10% accuracy, -27% tokens | Simpler = better |
| H3: Annotation Density | Minimal RDFa sufficient | 100% accuracy |
| H4: Compendium Size | 148 words = 90% accuracy | 38% fewer tokens |
| H5: Fair Comparison | MCSS 80% vs Tailwind 20% compliance | **4× more effective** |
| H6: Translation | Bidirectional 90% (80% + 100%) | MCSS is cleaner source |
| H7: No-Framework Baseline | 0% compliance without framework | **Both require teaching, MCSS teaches better** |

## The Three-Way Experiment (Capstone)

20 identical developer prompts, three conditions:

| Condition | System Prompt | MCSS Compliance | TW Compliance | Tokens |
|---|---|---|---|---|
| No framework | "Be an expert web developer" | 0% | 0% | 44,345 |
| MCSS | MCSS compendium (607 words) | **80%** | — | 32,020 |
| Tailwind | TW compendium (372 words) | — | 20% | 29,202 |

**The LLM knows zero framework conventions by default.** Both compendiums must teach from scratch. MCSS's 6 explicit rules (Golden Rule, ONC, data-state, RDFa, tokens, BEM) are 4× more learnable than Tailwind's dozens of implicit conventions (responsive prefixes, state variants, utility granularity, color scales, spacing scales).

## Bidirectional Translation

| Direction | Accuracy | Notes |
|---|---|---|
| Tailwind → MCSS | 80% (4/5) | Login form had minor Tailwind remnant |
| MCSS → Tailwind | 100% (3/3) | All translated perfectly |
| Average | 90% | MCSS components are easier to translate FROM |

## The Core Mechanism: Framework Learnability

The central finding across 7 hypotheses and 13 experiments:

1. **MCSS rules are explicit and few** (6 rules, ~40 tokens). The LLM can hold all of them in attention.
2. **Tailwind conventions are implicit and many** (dozens of utility classes, 5+ variant types). The LLM constantly forgets some.
3. **Without a compendium, the LLM knows neither framework** — both must be taught.
4. **MCSS teaches 4× better** because explicit rules are more learnable than implicit conventions.
5. **MCSS components are cleaner source material** for cross-framework translation (100% MCSS→TW vs 80% TW→MCSS).

## Practical Implications

For teams using LLMs for frontend development:
- MCSS-trained LLMs produce 4× more rule-compliant code than Tailwind-trained LLMs
- MCSS components are easier to translate to other frameworks
- A 607-word MCSS compendium is sufficient for 80%+ compliance
- Neither framework works without explicit teaching — the compendium matters
- Token costs are comparable between frameworks (~1,500-1,600/prompt)

## Open Questions

1. Cross-model validation (GPT-4, Gemini) of the three-way comparison
2. Does the 4× gap hold at 100+ prompts?
3. Can Tailwind's compendium be improved to close the gap?
4. What happens when both compendiums are given? (MCSS+TW hybrid)
