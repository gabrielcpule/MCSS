# MCSS Framework v1 — Context Compendium

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

Available tokens (103 total):

```

# 
--border-radius-full
--border-radius-lg
--border-radius-md
--border-radius-none
--border-radius-sm
--breakpoint-desktop
--breakpoint-mobile
--breakpoint-tablet
--breakpoint-wide
--color-background-brand
--color-background-brand-hover
--color-background-error
--color-background-primary
--color-background-secondary
--color-background-success
--color-background-warning
--color-black
--color-border-default
--color-border-error
--color-border-focus
--color-border-interactive
--color-border-success
--color-brand-100
--color-brand-200
--color-brand-300
--color-brand-400
--color-brand-50
--color-brand-500
--color-brand-600
--color-brand-700
--color-brand-800
--color-brand-900
--color-gray-100
--color-gray-200
--color-gray-300
--color-gray-400
--color-gray-50
--color-gray-500
--color-gray-600
--color-gray-700
--color-gray-800
--color-gray-900
--color-green-100
--color-green-500
--color-green-800
--color-red-100
--color-red-500
--color-red-800
--color-text-error
--color-text-link
--color-text-link-hover
--color-text-on-brand
--color-text-primary
--color-text-secondary
--color-text-success
--color-text-warning
--color-white
--color-yellow-100
--color-yellow-500
--color-yellow-800
--container-max-desktop
--container-max-mobile
--container-max-tablet
--container-max-wide
--font-family-mono
--font-family-sans
--font-size-body
--font-size-caption
--font-size-display
--font-size-heading
--font-size-overline
--font-size-subtitle
--font-size-title
--font-weight-bold
--font-weight-medium
--font-weight-regular
--font-weight-semibold
--line-height-base
--line-height-loose
--line-height-tight
--shadow-lg
--shadow-md
--shadow-sm
--space-1
--space-10
--space-12
--space-16
--space-2
--space-3
--space-4
--space-5
--space-6
--space-8
--transition-base
--transition-fast
--transition-slow
--z-index-base
--z-index-behind
--z-index-dropdown
--z-index-modal
--z-index-overlay
--z-index-sticky
--z-index-toast

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
