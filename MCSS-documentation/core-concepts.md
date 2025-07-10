# Core Concepts

Understanding the fundamental principles behind MCSS will help you build better, more maintainable user interfaces. This section covers the key concepts that make MCSS unique and powerful.

## The Semantic Imperative

### From Strings to Things

Traditional HTML development relies on weak signals like class names to convey meaning. A developer might use `.btn-primary` and hope that other team members understand its purpose. MCSS rejects this ambiguity by implementing the **Semantic Imperative**: transforming HTML documents from human-readable displays into structured, machine-readable knowledge graphs.

```html
<!-- Traditional approach: weak semantic signals -->
<button class="btn btn-primary large">
    Submit Form
</button>

<!-- MCSS approach: explicit semantic meaning -->
<button 
    class="c-button c-button--primary"
    typeof="mcs:Component"
    property="mcs:taxonomyLevel" content="mcs:Atom"
    property="mcs:purpose" content="Submit the user registration form"
    data-mcs-interaction-type="submission"
    data-mcs-consequence="Sends form data to server for processing">
    Submit Form
</button>
```

### Machine-Readable Metadata

By embedding explicit, structured metadata using RDFa (Resource Description Framework in Attributes), MCSS enables:

- **AI Understanding**: Large Language Models can comprehend component purpose without inference
- **Automated Testing**: Tools can identify interactive elements and their expected behaviors
- **Analytics**: Systems can track user interactions based on semantic meaning
- **Quality Assurance**: Automated tools can verify accessibility and compliance

### Knowledge Graph Structure

Each MCSS component becomes a node in a queryable knowledge graph where:
- **Subjects**: HTML elements with `typeof="mcs:Component"`
- **Predicates**: Properties like `mcs:purpose`, `mcs:taxonomyLevel`  
- **Objects**: Values that describe component characteristics

This creates a web of semantic relationships that machines can traverse and understand.

## The 5-Layer Architecture

MCSS employs a rigorous 5-layer architecture that maps directly to CSS Cascade Layers, ensuring predictable style application and preventing specificity conflicts.

### Layer Hierarchy (Low to High Priority)

```css
@layer global, layout, component, utility, exception;
```

Layer order **always** takes precedence over selector specificity. A simple utility class in Layer 4 will override a complex component selector in Layer 3.

### Layer 1: Global
**Purpose**: Foundation styles and design tokens  
**Files**: `tokens.css`, `global.css`  
**Scope**: HTML elements (no classes)

```css
/* Global layer styles */
body {
    font-family: var(--font-family-base);
    font-size: var(--font-size-body-base);
    line-height: var(--line-height-base);
    color: var(--color-text-primary);
}

h1, h2, h3, h4, h5, h6 {
    line-height: var(--line-height-heading);
    color: var(--color-text-primary);
}
```

**Rules**:
- Only styles HTML elements directly
- Must use design tokens for all values
- No class selectors allowed
- Provides "it just works" defaults

### Layer 2: Layout  
**Purpose**: Page structure and component arrangement  
**Prefix**: `l-*`  
**Examples**: `l-container`, `l-grid`, `l-stack`

```css
/* Layout classes arrange components */
.l-container {
    max-width: var(--container-max-width);
    margin: 0 auto;
    padding: 0 var(--space-4);
}

.l-grid {
    display: grid;
    gap: var(--space-6);
}

.l-stack > * + * {
    margin-top: var(--space-4);
}
```

**Rules**:
- Controls positioning and spacing between components
- Never styles component internals
- Responsive layout patterns only

### Layer 3: Component
**Purpose**: Reusable UI building blocks  
**Prefix**: `c-*`  
**Examples**: `c-button`, `c-card`, `c-navigation`

```css
/* Component styles define appearance and behavior */
.c-button {
    display: inline-flex;
    align-items: center;
    padding: var(--space-3) var(--space-5);
    border: 1px solid var(--color-border-interactive);
    border-radius: var(--border-radius-medium);
    background-color: var(--color-background-interactive);
    color: var(--color-text-interactive);
    font-weight: var(--font-weight-medium);
    cursor: pointer;
    transition: all var(--transition-fast);
}

.c-button--primary {
    background-color: var(--color-background-brand-primary);
    border-color: var(--color-border-brand-primary);
    color: var(--color-text-on-brand);
}

.c-button[data-state="disabled"] {
    opacity: 0.6;
    cursor: not-allowed;
    pointer-events: none;
}
```

**Rules**:
- Must follow the Ontological Naming Convention
- Cannot declare external margins (Golden Rule)
- Must use design tokens for all values
- State managed via `data-state` attributes

### Layer 4: Utility
**Purpose**: Single-purpose style overrides  
**Prefix**: `u-*`  
**Examples**: `u-text-center`, `u-hidden`, `u-margin-0`

```css
/* Utility classes provide targeted overrides */
.u-text-center { text-align: center !important; }
.u-text-left { text-align: left !important; }
.u-hidden { display: none !important; }
.u-margin-0 { margin: 0 !important; }
.u-font-bold { font-weight: var(--font-weight-bold) !important; }
```

**Rules**:
- Single CSS property per class
- Use `!important` to ensure override capability
- Immutable - never change existing utilities
- Generate systematically from tokens

### Layer 5: Exception
**Purpose**: Temporary fixes and third-party integration  
**Usage**: Debugging, legacy code, external libraries

```css
/* Exception layer for temporary overrides */
.legacy-widget {
    /* Temporary styles for third-party component */
    z-index: 9999 !important;
}

.debug-outline * {
    outline: 1px solid red !important;
}
```

**Rules**:
- Use sparingly and temporarily
- Document why exceptions are needed
- Plan migration to proper layers
- Never use for permanent solutions

## Ontological Naming Convention (ONC)

The ONC provides a strict grammar that acts as a "type system" for CSS, making class names self-documenting and predictable.

### Basic Structure
```
[prefix]-[component][__element][--modifier]
```

### Prefixes Define Architectural Layer

| Prefix | Layer | Purpose | Example |
|--------|-------|---------|---------|
| `c-` | Component | Reusable UI patterns | `c-button`, `c-card` |
| `l-` | Layout | Positioning and spacing | `l-grid`, `l-container` |
| `u-` | Utility | Single-purpose helpers | `u-text-center`, `u-hidden` |

### BEM Syntax for Component Structure

**Block**: The root component name
```html
<div class="c-card">
```

**Element**: Component parts (double underscore)
```html
<div class="c-card">
    <header class="c-card__header">
    <div class="c-card__body">
    <footer class="c-card__footer">
</div>
```

**Modifier**: Variations or states (double hyphen)
```html
<div class="c-card c-card--featured">
    <h2 class="c-card__title c-card__title--large">
```

### Naming Predictability

The ONC enables developers to construct valid class names without consulting documentation:

```javascript
// Predictable class construction
const buttonClass = `c-button c-button--${variant}`;
const textUtility = `u-text-${alignment}`;
const layoutGrid = `l-grid l-grid--${columns}-col`;
```

## Component Isolation: The Golden Rule

**The Golden Rule**: Components (classes with `c-` prefix) **MUST NOT** declare margin on their root element.

### Why This Rule Exists

```css
/* ❌ WRONG: Component controls its own spacing */
.c-card {
    margin-bottom: 20px; /* Breaks isolation! */
    padding: 16px;
    border: 1px solid #ccc;
}

/* ✅ CORRECT: Component only controls internal styling */
.c-card {
    /* No margin declared */
    padding: var(--space-4);
    border: 1px solid var(--color-border-default);
}
```

### Separation of Concerns

**Components** are responsible for:
- Internal appearance and behavior
- State management
- Accessibility features

**Layout classes** are responsible for:
- External spacing and positioning
- Arrangement relationships
- Responsive behavior

### Implementation Example

```html
<!-- Layout controls spacing -->
<div class="l-stack">
    <!-- Components focus on appearance -->
    <div class="c-card">
        <h2 class="c-card__title">Card Title</h2>
        <p class="c-card__content">Card content goes here.</p>
    </div>
    
    <!-- Stack automatically adds spacing between components -->
    <div class="c-card">
        <h2 class="c-card__title">Another Card</h2>
        <p class="c-card__content">More content here.</p>
    </div>
</div>
```

### Benefits of Isolation

1. **Reusability**: Components work in any layout context
2. **Predictability**: No unexpected spacing side effects
3. **Maintainability**: Clear responsibility boundaries
4. **Composability**: Easy to arrange components differently

## State Management via Data Attributes

MCSS uses `data-state` attributes for consistent, framework-agnostic state management.

### Traditional Problems

```css
/* ❌ Inconsistent state naming */
.button.active { }
.button.is-active { }
.button-active { }
.button--active { }

/* ❌ Class-based state management */
.button.loading.disabled.error { /* Complex state combinations */ }
```

### MCSS Solution

```html
<!-- ✅ Consistent state management -->
<button class="c-button" data-state="default">Default</button>
<button class="c-button" data-state="loading">Loading</button>
<button class="c-button" data-state="disabled">Disabled</button>
<button class="c-button" data-state="error">Error</button>
```

```css
/* ✅ Predictable state selectors */
.c-button[data-state="loading"] {
    opacity: 0.7;
    cursor: wait;
}

.c-button[data-state="disabled"] {
    opacity: 0.5;
    cursor: not-allowed;
    pointer-events: none;
}

.c-button[data-state="error"] {
    border-color: var(--color-border-error);
    background-color: var(--color-background-error);
}
```

### JavaScript Integration

```javascript
// Easy state manipulation
const button = document.querySelector('.c-button');

// Set state
button.dataset.state = 'loading';

// Check state  
if (button.dataset.state === 'disabled') {
    // Handle disabled state
}

// Clear state
button.dataset.state = 'default';
```

### Accessibility Integration

Coordinate visual states with ARIA attributes:

```html
<button 
    class="c-button"
    data-state="disabled"
    aria-disabled="true">
    Can't Click Me
</button>

<input 
    class="c-input"
    data-state="error"
    aria-invalid="true"
    aria-describedby="error-message">
```

### State Combinations

Handle complex state combinations:

```html
<!-- Multiple boolean attributes for complex states -->
<button 
    class="c-button"
    data-state="loading"
    data-variant="primary"
    data-size="large">
    Processing...
</button>
```

```css
.c-button[data-state="loading"][data-variant="primary"] {
    background-color: var(--color-background-brand-primary-disabled);
}
```

## Token-Driven Development

Design tokens serve as the single source of truth for all design decisions in MCSS.

### Token Categories

**Color Tokens**
```css
:root {
    --color-text-primary: #1A1D20;
    --color-text-secondary: #6C757D;
    --color-background-primary: #FFFFFF;
    --color-border-default: #DEE2E6;
}
```

**Typography Tokens**
```css
:root {
    --font-family-sans: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto;
    --font-size-heading-1: clamp(2rem, 5vw, 3rem);
    --font-weight-bold: 700;
    --line-height-tight: 1.25;
}
```

**Spacing Tokens**
```css
:root {
    --space-1: 0.25rem;   /* 4px */
    --space-2: 0.5rem;    /* 8px */
    --space-4: 1rem;      /* 16px */
    --space-6: 1.5rem;    /* 24px */
}
```

### Benefits of Token-Driven Development

1. **Consistency**: All components use the same design values
2. **Maintainability**: Change one token to update entire system
3. **Themability**: Swap token sets for different themes
4. **Scalability**: Add new tokens as the system grows

### Token Usage Rules

```css
/* ✅ CORRECT: Use tokens for all values */
.c-card {
    padding: var(--space-4);
    border-radius: var(--border-radius-medium);
    background-color: var(--color-background-surface);
    box-shadow: var(--shadow-medium);
}

/* ❌ WRONG: Hard-coded values */
.c-card {
    padding: 16px;
    border-radius: 8px;
    background-color: #ffffff;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}
```

This systematic approach ensures that every design decision is deliberate, documented, and reusable across the entire system.