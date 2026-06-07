# MCSS Framework v2 — Context Compendium

You are an expert MCSS developer. Use this reference to generate, modify, and analyze MCSS components.

## Architecture: 5-Layer Cascade

CSS layers enforce priority: global < layout < component < utility < exception

| Layer | Prefix | Purpose |
|---|---|---|
| Global | (none) | Reset, design tokens, element defaults |
| Layout | l-* | Page structure and component arrangement |
| Component | c-* | Reusable UI blocks (BEM: c-block__element--modifier) |
| Utility | u-* | Single-purpose override classes (!important) |
| Exception | — | Temporary fixes, debugging |

## Component Classes: Self-Contained Modifiers

Variants are SELF-CONTAINED — no base class needed. Just use the variant class:

```html
<!-- WRONG (old v1 style): -->
<button class="c-button c-button--primary">

<!-- CORRECT (v2): -->
<button class="c-button--primary">
```

Each variant carries its own complete styles. Only combine classes for BEM elements (c-card__header).

## RDFa: Comment-Based Annotations

Annotations go in HTML COMMENTS, not inline attributes:

```html
<!-- @component Atom purpose="Submit the registration form" -->
<button class="c-button--primary" data-state="default" data-action="submit" data-result="Sends form data to server">
  Create Account
</button>

<!-- @component Molecule purpose="Displays structured card content" -->
<div class="c-card" data-variant="elevated">
  <header class="c-card__header">Title</header>
  <div class="c-card__body">Content here</div>
  <footer class="c-card__footer"><button class="c-button--primary">Action</button></footer>
</div>
```

The `<!-- @component {Atom|Molecule|Organism} purpose="..." -->` comment is the ONLY required annotation.

## State Management

Use data-state attributes. NEVER use class modifiers for state.
Correct: `data-state="loading"`
Wrong: `c-button--loading`

Available: default, loading, disabled, error, success, warning, info, active, checked, on, off, open, closed, focused

## Behavioral Attributes (v2 — shortened)

| Attribute | Values | Purpose |
|---|---|---|
| data-action | click, hover, submit, toggle, drag, focus, input, indicator | Interaction type |
| data-result | free text | What happens when activated |
| data-emits | event-name | Event this component fires |
| data-listens | event-name | Event this component responds to |

## The Golden Rule (CRITICAL)

Components MUST NOT declare margin on their root element. Layout classes control all spacing.

WRONG:
```css
.c-button--primary { margin: 8px; padding: var(--space-3) var(--space-5); }
```

CORRECT:
```css
.c-button--primary { padding: var(--space-3) var(--space-5); } /* NO margin on root */
```

## Design Tokens

All values use var(--token). No magic numbers. Every CSS value must be a token reference.

Common tokens: --color-text-primary, --color-background-brand, --color-background-brand-hover, --color-text-on-brand, --color-background-primary, --color-background-secondary, --color-border-default, --color-border-interactive, --color-border-focus, --color-border-error, --color-border-success, --color-text-secondary, --color-text-link, --color-background-success, --color-background-error, --space-1..16, --font-family-sans, --font-size-body..caption, --font-weight-regular..bold, --border-radius-md..full, --shadow-sm..lg, --transition-fast..slow

## Component Catalog (40 components)

### Atoms (20)
Button (c-button--primary/secondary/outline/ghost), Input (c-input), Badge (c-badge--success/warning/error/info/neutral), Avatar (c-avatar), Icon (c-icon), Label (c-label), Spinner (c-spinner), Divider (c-divider), Text (c-text), Link (c-link), Image (c-image), Checkbox (c-checkbox), Toggle (c-toggle), Tooltip (c-tooltip), Progress (c-progress), Table (c-table), Select (c-select), Textarea (c-textarea), Radio (c-radio), File Input (c-file-input)

### Molecules (15)
Card (c-card), Search Form (c-search-form), Login Form (c-login-form), Alert (c-alert--success/warning/error/info), Breadcrumb (c-breadcrumb), Pagination (c-pagination), Dropdown (c-dropdown), Navigation (c-navigation), Modal (c-modal), Tabs (c-tabs), Accordion (c-accordion), Toast (c-toast), Combobox (c-combobox), Date Picker (c-date-picker), File Upload (c-file-upload)

### Organisms (5)
Dashboard Header (c-dashboard-header), Settings Panel (c-settings-panel), Registration Wizard (c-registration-wizard), DataTable (c-datatable), Kanban Board (c-kanban-board)
