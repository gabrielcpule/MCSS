# H3: Annotation Density Optimization Protocol

## Hypothesis
Standard annotations (typeof + taxonomyLevel + purpose + hasPart for molecules) outperform both minimal and verbose annotation levels. There's a sweet spot where enough metadata helps comprehension without wasting tokens on generation/modification.

## Prediction
- Minimal: Good generation/modification (fewer rules), worse comprehension (less metadata to analyze)
- Standard: Best overall — enough metadata for comprehension without over-constraining generation
- Verbose: Worse generation/modification (more rules to violate), no comprehension gain (diminishing returns)

## Method
Build 3 compendium variants differing only in RDFa annotation requirements:
1. **Minimal**: typeof + taxonomyLevel only (no purpose, no hasPart, no behavioral attrs)
2. **Standard** (current): typeof + taxonomyLevel + purpose + hasPart for molecules + data-mcs-* optional
3. **Verbose**: All annotations + componentName + ARIA sync + behavioral contracts required

Run 10-prompt validation subset on each. Compare accuracy and token usage.
