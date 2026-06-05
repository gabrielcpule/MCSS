# MCSS Framework v1 — Design Specification

**Date**: 2026-06-04
**Status**: Approved
**Scope**: Core CSS framework + validation tooling (single package)

## Overview

Build the first production release of `@mcss/framework` — an LLM-optimized CSS framework that implements the MCSS 5-layer architecture, ontological naming convention, design token system, RDFa semantic annotations, and validation tooling. The framework is validated against the MCSS-BENCHMARK-V1 suite (94.2% weighted accuracy baseline).

### Non-Goals for v1

- Organism components (scoped to Atoms + Molecules only)
- CI/CD pipeline templates (deliver the CLI; integration docs are enough)
- Migration tools from Tailwind/Bootstrap
- Documentation site (the existing MCSS documentation covers concepts; the framework ships with inline docs and README)
- Agent system (Validator/Generator/Analyzer/Optimizer/Educator — future work)

---

## Package Structure

```
mcss-framework/
├── package.json
├── postcss.config.js                  # PostCSS build config
├── README.md
├── LICENSE
│
├── src/
│   ├── tokens/
│   │   ├── tokens.css                 # All design tokens as CSS custom properties
│   │   └── token-schema.json          # Token definitions for validation (name, type, allowed values)
│   │
│   ├── layers/
│   │   ├── global.css                 # Layer 1: Reset + element defaults (no class selectors)
│   │   ├── layout.css                 # Layer 2: l-container, l-grid, l-stack, l-center, l-cluster, l-switcher
│   │   ├── component.css             # Layer 3: Aggregates all c-* components via @import
│   │   ├── utility.css               # Layer 4: Generated u-* single-property classes (from token-schema.json)
│   │   └── exception.css             # Layer 5: Empty scaffold for user overrides
│   │
│   ├── components/
│   │   ├── atoms/
│   │   │   ├── button.css
│   │   │   ├── input.css
│   │   │   ├── badge.css
│   │   │   ├── avatar.css
│   │   │   ├── icon.css
│   │   │   ├── label.css
│   │   │   ├── spinner.css
│   │   │   ├── divider.css
│   │   │   ├── text.css
│   │   │   ├── link.css
│   │   │   ├── image.css
│   │   │   ├── checkbox.css
│   │   │   ├── toggle.css
│   │   │   ├── tooltip.css
│   │   │   └── progress.css
│   │   └── molecules/
│   │       ├── card.css
│   │       ├── search-form.css
│   │       ├── login-form.css
│   │       ├── alert.css
│   │       ├── breadcrumb.css
│   │       ├── pagination.css
│   │       ├── dropdown.css
│   │       └── navigation.css
│   │
│   ├── annotations/
│   │   └── rdfa-vocabulary.ttl        # mcs:v1 RDF vocabulary definition
│   │
│   └── mcss.css                       # Entry point — @imports all layers in cascade order
│
├── dist/                              # Compiled output (shipped, not committed)
│   ├── mcss.css
│   ├── mcss.min.css
│   └── mcss.min.css.map
│
├── cli/
│   ├── index.js                       # CLI entry point: mcss-validate
│   ├── validators/
│   │   ├── html-validator.js          # HTML well-formedness + RDFa annotation checks
│   │   ├── css-validator.js           # Token usage + ONC compliance
│   │   ├── layer-validator.js         # Architecture rules (Golden Rule, layer ordering)
│   │   └── semantic-validator.js      # hasPart relationship + vocabulary pattern matching
│   └── reporters/
│       └── terminal.js                # Formatted output with PASS/FAIL counts + compliance score
│
├── eslint-plugin/
│   ├── index.js
│   └── rules/
│       ├── no-magic-numbers.js
│       ├── require-rdfa.js
│       ├── golden-rule.js
│       ├── onc-compliance.js
│       ├── require-data-state.js
│       └── token-defined.js
│
└── test/
    ├── tokens.test.js
    ├── layers.test.js
    ├── components.test.js
    ├── cli.test.js
    └── fixtures/
        ├── valid-component.html
        ├── valid-component.css
        ├── invalid-margin.html
        ├── invalid-magic-number.css
        └── ...
```

### Entry Point

`src/mcss.css` uses PostCSS `@import` to assemble layers in cascade order:

```css
/* src/mcss.css */
@import "tokens/tokens.css";
@import "layers/global.css"    layer(global);
@import "layers/layout.css"    layer(layout);
@import "layers/component.css"  layer(component);
@import "layers/utility.css"   layer(utility);
@import "layers/exception.css"  layer(exception);
```

`src/layers/component.css` imports all individual atom/molecule files so they compile into a single component layer. Consumers can customize by overriding this file to include only the components they need.

---

## Build Pipeline

### Flow

```
src/tokens/tokens.css ──┐
src/layers/global.css ──┤
src/layers/layout.css ──┤
src/components/atoms/* ──┼── src/layers/component.css ──┐
src/components/molecules/* ─┘                            │
src/layers/utility.css ──────────────────────────────────┤
src/layers/exception.css ────────────────────────────────┤
                                                          │
                                                     postcss-import
                                                     postcss-preset-env
                                                     cssnano (minified output only)
                                                          │
                                                     ┌────┴────┐
                                                     ↓         ↓
                                               dist/mcss.css  dist/mcss.min.css
```

### PostCSS Plugins

| Plugin | Role |
|---|---|
| `postcss-import` | Resolves `@import` statements; bundles into single file |
| `postcss-preset-env` | Stage 3+ features (nesting, `@layer`, custom media queries, `:is()`) |
| `cssnano` | Minification for `.min.css` only |

Target browsers: `last 2 versions, > 0.5%, not dead`

### What is explicitly NOT used

- **Sass/SCSS** — Modern CSS features (via postcss-preset-env) cover nesting, custom media, and layers natively
- **postcss-mixins / postcss-extend** — MCSS avoids abstractions; `var()` tokens are the only abstraction layer
- **Autoprefixer** — postcss-preset-env handles vendor prefixes via browserslist

### Utility Layer Generation

The utility layer (`src/layers/utility.css`) is generated from `token-schema.json` rather than hand-authored. A build script reads the schema, generates single-property utility classes, and writes the output before the main PostCSS pass. This guarantees every utility class maps to a defined token.

---

## Design Token System

### Naming Convention

Pattern: `--{category}-{property}-{variant}`

Tokens describe **purpose**, not value. Example: `--color-text-primary` not `--color-gray-900`.

### Categories

#### Color

```
--color-white
--color-black
--color-gray-{50, 100, 200, 300, 400, 500, 600, 700, 800, 900}

--color-brand-{50, 100, 200, 300, 400, 500, 600, 700, 800, 900}    # Default: blue

--color-green-{100, 500, 800}    # Status success (compact scale)
--color-red-{100, 500, 800}      # Status error (compact scale)
--color-yellow-{100, 500, 800}   # Status warning (compact scale)

# Semantic aliases (map to scale tokens via var())
--color-text-primary              → gray-900
--color-text-secondary            → gray-600
--color-text-on-brand             → white
--color-text-link                 → brand-600
--color-background-primary        → white
--color-background-secondary      → gray-50
--color-background-brand          → brand-600
--color-background-success        → green-100
--color-background-error          → red-100
--color-background-warning        → yellow-100
--color-border-default            → gray-200
--color-border-interactive        → brand-500
--color-border-error              → red-500
--color-border-success            → green-500
--color-status-success-text       → green-800
--color-status-error-text         → red-800
--color-status-warning-text       → yellow-800
```

#### Spacing

```
--space-1: 0.25rem     (4px)
--space-2: 0.5rem      (8px)
--space-3: 0.75rem     (12px)
--space-4: 1rem        (16px)
--space-5: 1.25rem     (20px)
--space-6: 1.5rem      (24px)
--space-8: 2rem        (32px)
--space-10: 2.5rem     (40px)
--space-12: 3rem       (48px)
--space-16: 4rem       (64px)
```

Even numbers for the common scale; gaps filled by odd numbers (3, 5) for fine-tuning.

#### Typography

**Font Family:**
```
--font-family-sans    # System UI stack
--font-family-mono    # Monospace stack
```

**Font Size (named for usage, not size):**
```
--font-size-display       # Hero headlines, marketing
--font-size-title         # Page titles, H1 equivalents
--font-size-heading       # Section headings, H2
--font-size-subtitle      # Subheadings, H3, card headers
--font-size-body          # Default body text (16px base)
--font-size-caption       # Supporting text, labels, footnotes
--font-size-overline      # Smallest — all-caps labels, badges, legal
```

**Font Weight:**
```
--font-weight-regular: 400
--font-weight-medium: 500
--font-weight-semibold: 600
--font-weight-bold: 700
```

**Line Height:**
```
--line-height-tight: 1.25
--line-height-base: 1.5
--line-height-loose: 1.75
```

#### Border Radius

```
--border-radius-none: 0
--border-radius-sm: 0.25rem     (4px)
--border-radius-md: 0.5rem      (8px)
--border-radius-lg: 1rem        (16px)
--border-radius-full: 9999px
```

#### Shadow (Elevation)

```
--shadow-sm: 0 1px 2px rgba(0,0,0,0.05)
--shadow-md: 0 4px 6px rgba(0,0,0,0.07)
--shadow-lg: 0 10px 15px rgba(0,0,0,0.1)
```

#### Responsive Breakpoints

```
--breakpoint-mobile:     0            # Phone portrait/landscape
--breakpoint-tablet:     641px        # Tablet, large phone landscape
--breakpoint-desktop:    769px        # Laptop, small desktop
--breakpoint-wide:       1025px       # Large desktop, external monitor
```

#### Z-Index Scale

```
--z-index-behind: -1
--z-index-base: 0
--z-index-dropdown: 100
--z-index-sticky: 200
--z-index-overlay: 300
--z-index-modal: 400
--z-index-toast: 500
```

#### Transitions

```
--transition-fast: 150ms ease
--transition-base: 250ms ease
--transition-slow: 400ms ease
```

#### Container Widths

```
--container-max-mobile: 100%
--container-max-tablet: 640px
--container-max-desktop: 768px
--container-max-wide: 1024px
```

### Theming

Semantic tokens (`--color-text-primary`, `--color-background-brand`, etc.) alias to scale tokens (`--color-gray-900`, `--color-brand-600`, etc.) via `var()`. This creates two theming mechanisms:

1. **Swap the scale** — change `--color-brand-500` from blue to purple; everything referencing it updates
2. **Remap the semantic alias** — point `--color-text-link` from `--color-brand-600` to `--color-green-500`

---

## 5-Layer Architecture

CSS Cascade Layers enforce priority: `global < layout < component < utility < exception`. Higher layers always win, regardless of selector specificity.

### Layer 1: Global

- **Files**: `global.css`
- **Scope**: Element selectors only — `body`, `h1-h6`, `a`, `img`, `button`, `input`, `table`, `p`, etc.
- **No class selectors allowed**
- Must use design tokens for all values
- Contains the CSS reset (modern reset: box-sizing, margin strip, font smoothing)

### Layer 2: Layout

- **Prefix**: `l-*`
- **Scope**: Positioning and spacing between components
- Must never style component internals
- Ships with: `l-container`, `l-grid`, `l-stack`, `l-center`, `l-cluster`, `l-switcher`
- `l-stack` uses the owl selector (`> * + *`) for automatic spacing

### Layer 3: Component

- **Prefix**: `c-*`
- **Golden Rule**: No external margins on root component selectors
- **State**: Managed via `data-state` attributes (NOT class modifiers)
- **Naming**: ONC — `c-[block]__[element]--[modifier]`
- All component files in `src/components/atoms/` and `src/components/molecules/`

### Layer 4: Utility

- **Prefix**: `u-*`
- **One property per class**
- **All rules use `!important`**
- **Immutable** — existing utilities are never changed
- Generated from `token-schema.json`

### Layer 5: Exception

- **Usage**: Temporary fixes, debugging, third-party integration
- **Document with inline comments** explaining why the exception exists
- Empty by default — user populates as needed

---

## Component Catalog

### Atoms (15)

| # | Component | Class | Data States |
|---|---|---|---|
| 1 | Button | `c-button` | default, loading, disabled, error |
| 2 | Input | `c-input` | default, disabled, error, focused |
| 3 | Badge | `c-badge` | success, warning, error, info, neutral |
| 4 | Avatar | `c-avatar` | small, medium, large |
| 5 | Icon | `c-icon` | small, medium, large |
| 6 | Label | `c-label` | default |
| 7 | Spinner | `c-spinner` | small, medium, large |
| 8 | Divider | `c-divider` | horizontal, vertical |
| 9 | Text | `c-text` | body, caption, overline, code |
| 10 | Link | `c-link` | default, subtle, external (data-variant) |
| 11 | Image | `c-image` | responsive, fixed-ratio (1:1, 4:3, 16:9) |
| 12 | Checkbox | `c-checkbox` | checked, disabled, indeterminate |
| 13 | Toggle | `c-toggle` | on, off, disabled |
| 14 | Tooltip | `c-tooltip` | top, bottom, left, right (data-position) |
| 15 | Progress | `c-progress` | indeterminate, determinate (0-100%) |

### Molecules (8)

| # | Component | Class | Elements | Composes |
|---|---|---|---|---|
| 1 | Card | `c-card` | `__header`, `__body`, `__footer`, `__image` | text, button |
| 2 | Search Form | `c-search-form` | `__input`, `__button` | input, button |
| 3 | Login Form | `c-login-form` | `__field`, `__submit`, `__recovery` | input ×2, button, link |
| 4 | Alert | `c-alert` | `__icon`, `__content`, `__dismiss` | icon, text, button |
| 5 | Breadcrumb | `c-breadcrumb` | `__list`, `__item`, `__separator` | link |
| 6 | Pagination | `c-pagination` | `__list`, `__item`, `__ellipsis` | button |
| 7 | Dropdown | `c-dropdown` | `__trigger`, `__menu`, `__item` | button, link |
| 8 | Navigation | `c-navigation` | `__list`, `__item`, `__link` | link |

### Component Template Pattern

Every component CSS file follows this structure:

```css
/* ============================================
 * Component: [Name]
 * Taxonomy: mcs:[Atom|Molecule]
 * Purpose: [One-line functional description]
 * States: [data-state values]
 * LLM Hint: [Usage guidance for AI code generation]
 * ============================================ */

/* Base styles */

/* State styles */

/* Modifier/variant styles (data-variant where applicable) */

/* Element styles (molecules only) */
```

---

## RDFa Annotation System

### Namespace

```html
<html vocab="https://gabrielcpule.github.io/mcss-vocab/api/mcss/v1.rdf">
```

### Required Component Declarations

Every component MUST declare:
1. `typeof="mcs:Component"` — identifies element as an MCSS component
2. `property="mcs:taxonomyLevel" content="mcs:Atom|mcs:Molecule|mcs:Organism"` — Atomic Design classification
3. `property="mcs:purpose" content="..."` — functional description (on hidden span, separated from presentation)

### Molecular Composition

Molecules use `property="mcs:hasPart"` with `resource="#id"` to declare structural relationships:

```html
<div class="c-card" typeof="mcs:Component" property="mcs:taxonomyLevel" content="mcs:Molecule">
  <div property="mcs:hasPart" resource="#card-header">
    <header id="card-header" class="c-card__header">...</header>
  </div>
</div>
```

### Behavioral Attributes

`data-mcs-*` attributes describe interactive behavior:
- `data-mcs-interaction-type` — click, hover, submission, toggle, drag
- `data-mcs-consequence` — what happens when activated
- `data-mcs-triggers-event` — custom event name fired on interaction
- `data-mcs-receives-event` — custom event this component listens for

---

## Validation CLI

### Commands

```
mcss-validate [path]            # Run all 10 checks (default)
mcss-validate [path] --strict   # All checks + fail on warnings
mcss-validate [path] --html     # RDFa & semantic checks only (checks 1-5)
mcss-validate [path] --css      # Token & layer checks only (checks 6-10)
```

### Check Pipeline

| # | Check | Domain | Description |
|---|---|---|---|
| 1 | HTML well-formedness | HTML | Valid markup via htmlparser2 |
| 2 | RDFa completeness | HTML | typeof, taxonomyLevel, purpose present on all components |
| 3 | RDFa vocabulary | HTML | Only valid mcs:v1 properties used |
| 4 | hasPart relationships | HTML | Child component resource references valid |
| 5 | Accessibility basics | HTML | Labels on inputs, alt on images, ARIA state sync |
| 6 | No magic numbers | CSS | All non-trivial values use var() |
| 7 | ONC compliance | CSS | Correct prefix for layer (l-, c-, u-) |
| 8 | Token existence | CSS | Every var() references a token in token-schema.json |
| 9 | Golden Rule | CSS | No margin on c-* root selectors |
| 10 | Layer integrity | CSS | No !important below utility; utility is single-property |

### Output

Terminal report with per-check PASS/FAIL, specific file:line:message for each violation, and a compliance score (0-100%).

### Explicit v1 Non-Goals for CLI

- No SPARQL engine or full RDF store — semantic checks use pattern matching on parsed RDFa
- No full WCAG audit — basic accessibility checks only
- No auto-fix mode (`--fix` deferred to future release)

---

## ESLint Plugin

Ships within the package at `@mcss/framework/eslint-plugin`.

### Rules

| Rule | Domain | Catches |
|---|---|---|
| `@mcss/no-magic-numbers` | CSS, HTML | Hard-coded values not from tokens |
| `@mcss/require-rdfa` | HTML | Components missing typeof/taxonomyLevel/purpose |
| `@mcss/golden-rule` | CSS | Margin on c-* root selectors |
| `@mcss/onc-compliance` | CSS, HTML | Wrong prefix for layer; c-* in layout layer |
| `@mcss/require-data-state` | CSS, HTML | Class modifier (.c-button--disabled) instead of data-state |
| `@mcss/token-defined` | CSS | var() referencing undefined token |

### Configuration

```js
// .eslintrc.js
module.exports = {
  plugins: ['@mcss/framework'],
  rules: {
    '@mcss/no-magic-numbers': 'error',
    '@mcss/require-rdfa': 'error',
    '@mcss/golden-rule': 'error',
    '@mcss/onc-compliance': 'error',
    '@mcss/require-data-state': 'error',
    '@mcss/token-defined': 'warn'
  }
};
```

---

## Delivery

### npm Package: `@mcss/framework`

**Compiled entry point (drop-in):**
```css
@import '@mcss/framework';              /* dist/mcss.css */
@import '@mcss/framework/dist/mcss.min'; /* dist/mcss.min.css */
```

**Source entry point (customization):**
```css
@import '@mcss/framework/src/mcss.css';  /* PostCSS source */
```

### package.json exports

```json
{
  "name": "@mcss/framework",
  "version": "1.0.0",
  "main": "dist/mcss.css",
  "exports": {
    ".": "./dist/mcss.css",
    "./dist/mcss.min.css": "./dist/mcss.min.css",
    "./src/mcss.css": "./src/mcss.css",
    "./eslint-plugin": "./eslint-plugin/index.js"
  },
  "bin": {
    "mcss-validate": "./cli/index.js"
  }
}
```

---

## Research Variables (Noted for Future Autoresearch)

These are design decisions that should be empirically validated:

1. **Token naming A vs B** — Does `--color-text-primary` or `--mcss-color-text-primary` produce higher LLM accuracy on MCSS-BENCHMARK-V1?
2. **Annotation density curve** — Optimal amount of RDFa metadata before diminishing returns on LLM comprehension
3. **Cross-model validation** — Does MCSS's accuracy hold across GPT-4, Gemini, DeepSeek, or is it Claude-specific?

---

## Architecture Rules (Immutable)

These are enforced by the CLI and ESLint plugin; they cannot be relaxed:

1. Higher CSS layer always overrides lower, regardless of specificity
2. Components (`c-*`) MUST NOT declare external margins (Golden Rule)
3. All non-trivial values MUST come from design tokens via `var()`
4. Every class MUST have the correct layer prefix
5. State MUST be managed via `data-state` attributes, not class modifiers
6. Every component MUST declare typeof, taxonomyLevel, and purpose via RDFa
