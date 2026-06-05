# @mcss/framework

**Model Context Style Sheet** — LLM-optimized CSS framework achieving 94.2% first-attempt accuracy with AI code generation.

## Quick Start

```bash
npm install @mcss/framework
```

### Drop-in (compiled CSS)

```css
@import '@mcss/framework';
/* or minified: */
@import '@mcss/framework/dist/mcss.min.css';
```

```html
<link rel="stylesheet" href="node_modules/@mcss/framework/dist/mcss.min.css">
```

### Custom Build (PostCSS source)

```css
@import '@mcss/framework/src/mcss.css';
```

## Architecture

MCSS uses a **5-layer cascade architecture** with CSS `@layer` directives:

| Layer | Prefix | Purpose |
|---|---|---|
| Global | _(none)_ | Reset, design tokens, element defaults |
| Layout | `l-*` | Page structure and component arrangement |
| Component | `c-*` | Reusable UI building blocks (BEM syntax) |
| Utility | `u-*` | Single-purpose override classes |
| Exception | — | Temporary fixes and debugging |

## Key Principles

- **The Semantic Imperative**: RDFa annotations on every component (`typeof="mcs:Component"`)
- **Ontological Naming Convention**: `[prefix]-[block]__[element]--[modifier]`
- **Token-Driven**: All values use CSS custom properties — no magic numbers
- **Component Isolation**: Components never declare external margins (Golden Rule)
- **State via `data-state`**: `[data-state="loading"]`, not `.c-button--loading`

## Component Library (23 components)

**Atoms (15):** Button, Input, Badge, Avatar, Icon, Label, Spinner, Divider, Text, Link, Image, Checkbox, Toggle, Tooltip, Progress

**Molecules (8):** Card, Search Form, Login Form, Alert, Breadcrumb, Pagination, Dropdown, Navigation

## Validation

```bash
npx mcss-validate ./src           # Full validation (HTML + CSS)
npx mcss-validate ./src --strict  # Fail on warnings
npx mcss-validate ./src --css     # CSS-only checks
```

### ESLint Plugin

```js
// .eslintrc.js
module.exports = {
  plugins: ['@mcss/framework'],
  extends: ['plugin:@mcss/framework/recommended']
};
```

| Rule | Description |
|---|---|
| `@mcss/no-magic-numbers` | No hard-coded values — use tokens |
| `@mcss/token-defined` | var() must reference defined token |
| `@mcss/golden-rule` | No margin on c-* root selectors |
| `@mcss/onc-compliance` | Correct layer prefixes |
| `@mcss/require-rdfa` | Components must declare typeof + taxonomyLevel |
| `@mcss/require-data-state` | Use data-state, not class modifiers |

## License

MIT
