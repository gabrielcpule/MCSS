#!/usr/bin/env python3
"""
Build CONTEXT_COMPENDIUM_v2.md from MCSS v1 framework files.
This is the LLM system prompt for running MCSS-BENCHMARK-V1.
"""
import json
from pathlib import Path

FRAMEWORK = Path("/home/gabrielp/Projects/MCSS/mcss-framework")

def read(path):
    return Path(path).read_text()

def build():
    tokens_css = read(FRAMEWORK / "src/tokens/tokens.css")
    token_schema = json.loads(read(FRAMEWORK / "src/tokens/token-schema.json"))
    readme = read(FRAMEWORK / "README.md")

    # Extract key sections
    token_names = []
    for line in tokens_css.split('\n'):
        line = line.strip()
        if line.startswith('--') and ':' in line:
            name = line.split(':')[0].strip()
            token_names.append(name)

    # Build compendium
    compendium = f"""# MCSS Framework v1 — Context Compendium

You are an expert MCSS (Model Context Style Sheet) developer. Use this reference to generate, modify, and analyze MCSS components.

## Architecture: 5-Layer Cascade

CSS layers enforce priority: global < layout < component < utility < exception

| Layer | Prefix | Purpose |
|---|---|---|
| Global | (none) | Reset, design tokens, element defaults |
| Layout | l-* | Page structure and component arrangement |
| Component | c-* | Reusable UI building blocks (BEM: c-block__element--modifier) |
| Utility | u-* | Single-purpose override classes (!important) |
| Exception | — | Temporary fixes, debugging |

## Design Tokens

All values MUST use CSS custom properties via var(). No magic numbers.

Available tokens ({len(token_names)} total):

```
"""
    # Group tokens by category
    categories = {}
    for name in sorted(token_names):
        parts = name.split('-')
        cat = parts[1] if len(parts) > 1 else 'other'
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(name)

    for cat, names in sorted(categories.items()):
        compendium += f"\n# {cat}\n"
        for n in names:
            compendium += f"{n}\n"

    compendium += """
```

## Component Naming Convention (ONC)

Pattern: [prefix]-[block]__[element]--[modifier]

- Block: The root component (c-button)
- Element: Component parts with __ (c-card__header)
- Modifier: Variant with -- (c-card--featured)
- State: Use data-state attribute, NOT class modifiers

## State Management

Use data-state attributes. NEVER use class modifiers for state.
Correct: .c-button[data-state="loading"]
Wrong: .c-button--loading

Available states: default, loading, disabled, error, success, warning, info, active, checked, on, off, open, closed, focused, indeterminate

## The Golden Rule

Components (c-* prefix) MUST NOT declare margin on their root element.
Layout classes (l-* prefix) control all external spacing.

## RDFa Annotations

Every component MUST have:
- typeof="mcs:Component"
- property="mcs:taxonomyLevel" content="mcs:Atom|mcs:Molecule|mcs:Organism"
- property="mcs:purpose" content="description"

Molecules use mcs:hasPart for composition:
- property="mcs:hasPart" resource="#element-id"

Behavioral attributes (optional):
- data-mcs-interaction-type (click, hover, submission, toggle, drag, focus, input)
- data-mcs-consequence (what happens)
- data-mcs-triggers-event (custom event name)

## Component Catalog

### Atoms (15)
Button (c-button), Input (c-input), Badge (c-badge), Avatar (c-avatar), Icon (c-icon),
Label (c-label), Spinner (c-spinner), Divider (c-divider), Text (c-text), Link (c-link),
Image (c-image), Checkbox (c-checkbox), Toggle (c-toggle), Tooltip (c-tooltip), Progress (c-progress)

### Molecules (8)
Card (c-card), Search Form (c-search-form), Login Form (c-login-form), Alert (c-alert),
Breadcrumb (c-breadcrumb), Pagination (c-pagination), Dropdown (c-dropdown), Navigation (c-navigation)

## Validation Rules (enforced by CLI)

1. No magic numbers — all values use var(--token)
2. Correct layer prefix for every class
3. No margin on c-* root selectors (Golden Rule)
4. Every component has typeof, taxonomyLevel, purpose
5. State via data-state, not class modifiers
6. Every var() references a defined token

## Output Format

For generation/modification tasks, output:
1. The HTML component with RDFa annotations
2. The CSS with token-driven styles
3. Brief explanation of design decisions

For comprehension tasks, analyze the component's purpose, taxonomy, structure, and interaction model.
"""

    return compendium

if __name__ == '__main__':
    compendium = build()
    out = Path("/home/gabrielp/Projects/MCSS/research/data/CONTEXT_COMPENDIUM_v2.md")
    out.write_text(compendium)
    print(f"Generated {out} ({len(compendium.split())} words, ~{len(compendium)//4} tokens)")
