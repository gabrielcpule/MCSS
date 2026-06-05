# MCSS Framework — Micro Reference

You are an expert MCSS developer. Follow these rules exactly.

## Architecture
CSS layers: global < layout < component < utility < exception
Prefixes: l-* (layout), c-* (component), u-* (utility)

## The Golden Rule (CRITICAL)
Components (c-* prefix) MUST NOT declare margin, margin-top, margin-bottom, 
margin-left, or margin-right on their root element. Layout classes control spacing.

WRONG:
```css
.c-button { margin: 8px; }
```

CORRECT:
```css
.c-button { padding: var(--space-3); } /* NO margin */
```

## Naming Convention
Pattern: c-[block]__[element]--[modifier]
- Block: c-button
- Element: c-card__header
- State: use data-state="loading", NEVER c-button--loading

## State Management
Use data-state attributes. Available: default, loading, disabled, error, success, 
warning, info, active, checked, on, off, open, closed, focused.

## Design Tokens
All values MUST use var(--token). No magic numbers.
Common tokens: --color-text-primary, --color-background-brand, --space-4, 
--font-size-body, --border-radius-md, --shadow-sm.

## Required for all components
- typeof="mcs:Component"
- property="mcs:taxonomyLevel" content="mcs:Atom|mcs:Molecule|mcs:Organism"
