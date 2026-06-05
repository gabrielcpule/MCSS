# H1: Baseline Reproduction Protocol

## Hypothesis
MCSS v1 framework (actual compiled CSS + README + token-schema.json) as LLM context achieves >= 90% weighted accuracy on MCSS-BENCHMARK-V1, comparable to the original 94.2% achieved by the older CONTEXT_COMPENDIUM.md.

## Prediction
The v1 framework should produce similar or slightly better results than the original benchmark because:
1. The CSS is now real, compiled, and internally consistent (vs the older design-doc approach)
2. The README provides architecture context
3. The token-schema.json provides a machine-parseable reference

## Method
1. Build CONTEXT_COMPENDIUM_v2.md from v1 framework files
2. Run MCSS-BENCHMARK-V1 prompts (100 total) against Claude API
3. Compare weighted accuracy to 94.2% baseline

## Independent Variable
MCSS v1 framework files as system context (replacing 2025 CONTEXT_COMPENDIUM.md)

## Dependent Variable
Weighted accuracy = (gen_pass × 0.4) + (mod_pass × 0.4) + (comp_pass × 0.2)

## Controls
- Same LLM (Claude model)
- Same temperature (0.1)
- Same prompts (MCSS-BENCHMARK-V1)
- Same scoring rubric
- Same Pass@1 single-shot protocol

## Git Lock
Commit this protocol BEFORE running the benchmark.
