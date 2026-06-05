# H2: Token Naming Impact Protocol

## Hypothesis
Short semantic token names (--color-text-primary) produce equal or higher LLM accuracy compared to namespaced tokens (--mcss-color-text-primary), while using fewer tokens.

## Prediction
Short names will:
1. Reduce prompt token count (shorter token references)
2. Maintain or improve comprehension accuracy (less visual noise)
3. Reduce generation mistakes (simpler names to remember)

## Method
1. Build CONTEXT_COMPENDIUM_v2_namespaced.md — identical to v2 but with --mcss-* prefix on all tokens
2. Run same 10-prompt validation subset
3. Compare: accuracy, prompt tokens, output tokens

## Independent Variable
Token naming convention:
- A (control): --color-text-primary, --space-4, --font-size-body
- B (variant): --mcss-color-text-primary, --mcss-space-4, --mcss-font-size-body

## Controls
- Same LLM (Claude Sonnet 4.6)
- Same prompts (10-prompt validation subset)
- Same temperature (0.1)
- Same compendium structure (only token names differ)
- Same scoring logic
