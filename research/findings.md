# Findings

## Current Understanding

MCSS v1 is a freshly built CSS framework implementing the Model Context Style Sheet architecture. It has not yet been benchmarked against the MCSS-BENCHMARK-V1 suite. The original benchmark (dated July 2025) achieved 94.2% weighted accuracy using Claude 3.5 Sonnet with a CONTEXT_COMPENDIUM.md system prompt (8,847 tokens). The v1 framework now exists as real, compilable CSS with validation tooling — the benchmark must be re-run with the actual framework as context rather than the older compendium.

## Patterns and Insights

(No experiments run yet.)

## Lessons and Constraints

- The original benchmark used `--mcs-*` prefixed tokens (e.g., `--mcs-color-background-secondary`). MCSS v1 uses short semantic names (`--color-background-secondary`). This difference may affect accuracy.
- The original benchmark gold standards used `property="mcs:taxonomyLevel"` inline syntax. MCSS v1 documentation uses the same pattern.
- The benchmark was validated against Claude 3.5 Sonnet. Different models may produce different results.

## Open Questions

1. What is the actual accuracy of MCSS v1 as system context (not the old CONTEXT_COMPENDIUM.md)?
2. Which task categories (generation, modification, comprehension) benefit most from the framework?
3. Does the token naming convention affect LLM comprehension?
4. What's the minimum viable context to achieve 90%+ accuracy?
