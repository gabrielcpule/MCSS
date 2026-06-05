# Findings

## Central Finding: Simplicity Dominates

Across 4 hypotheses and 7 experiment runs, every simpler variant matched or outperformed its more complex counterpart. **Less is more for LLM code generation.**

## Results Summary

| Hypothesis | Finding | Best Variant | Accuracy | Tokens |
|---|---|---|---|---|
| H1: Baseline | Compendium efficiency | 1,440-token v2 | 100% | 14,105 |
| H2: Token Naming | Short names strictly better | `--color-text-primary` | 100% | 15,506 |
| H3: Annotation Density | Minimal is optimal | typeof + taxonomyLevel | 100% | 14,105 |
| H4: Compendium Size | 90% achievable with 148 words | Micro compendium | 90% | 8,720 |

## The Efficiency-Accuracy Curve

```
Compendium Size → Accuracy → Token Efficiency
─────────────────────────────────────────────
148 words (Micro)     →  90%  →  98 tok/pp  ← most efficient
607 words (Minimal)   → 100%  → 140 tok/pp
1,200 words (Standard)→  90%* → 160 tok/pp  *single fluke failure
1,700 words (Verbose) → 100%  → 162 tok/pp  ← least efficient
```

There's a clear Pareto frontier: the micro compendium achieves 90% with dramatically fewer tokens. Every additional word beyond ~150 words has diminishing returns.

## Patterns and Insights

1. **Every token is cognitive load.** Smaller system prompts produce equal or better results. The LLM's attention budget is zero-sum — verbose prompts crowd out the rules that matter.
2. **The Golden Rule is the primary failure mode.** Concrete counterexamples (showing WRONG code) eliminated this failure entirely.
3. **Minimal RDFa is sufficient.** typeof + taxonomyLevel alone enables 100% accuracy. purpose, hasPart, and behavioral attributes are optional.
4. **Short token names improve comprehension.** Namespaced tokens (--mcss-*) degraded comprehension by adding visual noise.
5. **Comprehension is the most compendium-sensitive task.** Micro (148w) got 50% comp, Minimal (607w) got 100% — comprehension needs more context than generation/modification.
6. **148 words is the minimum viable compendium.** It achieves 90% with just: architecture summary, Golden Rule (with counterexamples), naming convention, state management rules, and a short token reference.

## Lessons and Constraints

- Rate limit: 1.2s between API calls, ~12s per 10-prompt run per variant
- Regex scoring must strip CSS comments and exclude BEM elements from Golden Rule
- Non-determinism at temp 0.1: single-prompt flukes happen (1 in 40 prompts across experiments)
- All experiments on Claude Sonnet 4.6 with thinking disabled

## Open Questions

1. **Cross-model validation**: Do the simplicity-wins patterns generalize to GPT-4, Gemini, DeepSeek?
2. **Full 100-prompt benchmark**: Does 100% on 10 prompts hold at scale (expect 90-95%)?
3. **Interaction between H2 and H3**: Would namespaced tokens + minimal annotations perform differently?
4. **148-word compendium on 100 prompts**: Would 90% hold or degrade with more tasks?
