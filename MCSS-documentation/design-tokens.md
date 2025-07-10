# Design Tokens

Design tokens are the foundational elements of the MCSS design system. They serve as the single source of truth for all design decisions, ensuring consistency, maintainability, and scalability across your entire application.

## Token Philosophy

### Single Source of Truth

Every visual property in MCSS—from colors to spacing to typography—is defined as a CSS Custom Property (token) in the `tokens.css` file. This approach eliminates "magic numbers" and centralizes all design decisions.

```css
/* ❌ Hard-coded values - inconsistent and unmaintainable */
.my-component {
    color: #1A1D20;
    padding: 16px;
    border-radius: 8px;
    font-size: 18px;
}

/* ✅ Token-driven - consistent and maintainable */
.my-component {
    color: var(--color-text-primary);
    padding: var(--space-4);
    border-radius: var(--border-radius-medium);
    font-size: var(--font-size-large);
}
```

### Semantic Naming

Token names describe **purpose** rather than **value**. This makes the system more intuitive and allows values to change without breaking the semantic meaning.

```css
/* ❌ Value-based naming */
--color-blue-500: #005A9C;
--font-18px: 1.125rem;

/* ✅ Semantic naming */
--color-text-link: #005A9C;
--font-size-large: 1.125rem;
```

### Token Categories

MCSS organizes tokens into logical categories that follow a consistent naming convention: `--category-property-variant`

## Color System

### Neutral Colors

The foundation of any color system, neutral colors provide the primary text and background colors.

| Token Name | Value | Usage | WCAG Compliance |
|------------|-------|-------|-----------------|
| `--color-white` | #FFFFFF | Primary background | ✅ AAA with all text colors |
| `--color-gray-50` | #F8F9FA | Secondary backgrounds | ✅ AA with dark text |
| `--color-gray-100` | #E9ECEF | Tertiary backgrounds | ✅ AA with dark text |
| `--color-gray-900` | #1A1D20` | Primary text | ✅ AAA on white background |
| `--color-gray-600` | #495057 | Secondary text | ✅ AA on light backgrounds |

```css
/* Usage examples */
.page-background {
    background-color: var(--color-white);
    color: var(--color-gray-900);
}

.sidebar {
    background-color: var(--color-gray-50);
    color: var(--color-gray-600);
}
```

### Brand Colors

Your brand identity expressed through primary and accent colors.

| Token Name | Value | Usage |
|------------|-------|-------|
| `--color-primary` | #005A9C | Primary brand color |
| `--color-primary-hover` | #004A80 | Interactive hover state |
| `--color-primary-active` | #003860 | Interactive active state |
| `--color-accent` | #00D4AA | Secondary brand color |

```css
/* Button using brand colors */
.c-button--primary {
    background-color: var(--color-primary);
    color: var(--color-white);
    border: 1px solid var(--color-primary);
}

.c-button--primary:hover {
    background-color: var(--color-primary-hover);
    border-color: var(--color-primary-hover);
}
```

### Semantic Feedback Colors

Colors that communicate system status and user feedback.

| Category | Background | Text | Border | Usage |
|----------|------------|------|--------|-------|
| **Success** | `--color-background-success` | `--color-text-success` | `--color-border-success` | Confirmations, completions |
| **Warning** | `--color-background-warning` | `--color-text-warning` | `--color-border-warning` | Cautions, alerts |
| **Error** | `--color-background-error` | `--color-text-error` | `--color-border-error` | Errors, validation failures |
| **Info** | `--color-background-info` | `--color-text-info` | `--color-border-info` | Information, help text |

```css
/* Success message styling */
.c-alert--success {
    background-color: var(--color-background-success);
    color: var(--color-text-success);
    border: 1px solid var(--color-border-success);
}

/* Form validation error */
.c-input[data-state="error"] {
    border-color: var(--color-border-error);
}
```

### Interactive States

Colors specifically designed for interactive elements and their various states.

| Token Name | Purpose | Usage |
|------------|---------|-------|
| `--color-text-link` | Default link color | Text links, buttons |
| `--color-text-link-hover` | Link hover state | Interactive feedback |
| `--color-border-focus` | Focus indicator | Keyboard navigation |
| `--color-background-interactive` | Interactive backgrounds | Buttons, form fields |

```css
/* Link styling */
a {
    color: var(--color-text-link);
    transition: color var(--transition-fast);
}

a:hover {
    color: var(--color-text-link-hover);
}

/* Focus ring for accessibility */
.c-button:focus-visible {
    outline: 2px solid var(--color-border-focus);
    outline-offset: 2px;
}
```

## Typography System

### Font Families

MCSS provides carefully selected font stacks optimized for readability and cross-platform compatibility.

| Token Name | Value | Usage |
|------------|-------|-------|
| `--font-family-sans` | -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif | Body text, UI elements |
| `--font-family-mono` | 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace | Code, technical content |

```css
body {
    font-family: var(--font-family-sans);
}

code, pre {
    font-family: var(--font-family-mono);
}
```

### Modular Type Scale

MCSS uses a mathematically consistent type scale based on a 1.25 ratio (Major Third), providing harmonious size relationships.

| Token Name | Value (rem) | Pixel Equivalent | Usage |
|------------|-------------|------------------|-------|
| `--font-size-xs` | 0.75rem | 12px | Captions, fine print |
| `--font-size-sm` | 0.875rem | 14px | Small text, metadata |
| `--font-size-base` | 1rem | 16px | Body text (default) |
| `--font-size-lg` | 1.125rem | 18px | Large body text |
| `--font-size-xl` | 1.25rem | 20px | Small headings |
| `--font-size-2xl` | 1.5rem | 24px | Medium headings |
| `--font-size-3xl` | 1.875rem | 30px | Large headings |
| `--font-size-4xl` | 2.25rem | 36px | Extra large headings |
| `--font-size-5xl` | 3rem | 48px | Display headings |

```css
/* Semantic heading sizes */
h1 { font-size: var(--font-size-4xl); }
h2 { font-size: var(--font-size-3xl); }
h3 { font-size: var(--font-size-2xl); }
h4 { font-size: var(--font-size-xl); }

/* Component-specific sizing */
.c-card__title {
    font-size: var(--font-size-lg);
}

.c-caption {
    font-size: var(--font-size-xs);
}
```

### Fluid Typography

For major headings, MCSS includes fluid typography that scales smoothly across viewport sizes:

```css
--font-size-heading-1: clamp(2rem, 5vw, 3rem);
```

This creates responsive typography without media queries, scaling from 32px on small screens to 48px on large screens.

### Font Weights

| Token Name | Value | Usage |
|------------|-------|-------|
| `--font-weight-normal` | 400 | Body text, default weight |
| `--font-weight-medium` | 500 | Emphasized text, button labels |
| `--font-weight-semibold` | 600 | Subheadings, important text |
| `--font-weight-bold` | 700 | Headings, strong emphasis |

### Line Heights

Optimized for readability and vertical rhythm:

| Token Name | Value | Usage |
|------------|-------|-------|
| `--line-height-tight` | 1.25 | Headings, compact text |
| `--line-height-normal` | 1.5 | Body text, default |
| `--line-height-relaxed` | 1.75 | Long-form content |

```css
/* Typography component example */
.c-text-content {
    font-family: var(--font-family-sans);
    font-size: var(--font-size-base);
    font-weight: var(--font-weight-normal);
    line-height: var(--line-height-normal);
    color: var(--color-text-primary);
}
```

## Spacing System

### 4px Grid System

MCSS uses a consistent spacing scale based on a 4px grid, ensuring visual harmony and predictable layouts.

| Token Name | Value (rem) | Pixel Equivalent | Usage |
|------------|-------------|------------------|-------|
| `--space-0` | 0 | 0px | Reset spacing |
| `--space-1` | 0.25rem | 4px | Fine adjustments |
| `--space-2` | 0.5rem | 8px | Small gaps |
| `--space-3` | 0.75rem | 12px | Medium gaps |
| `--space-4` | 1rem | 16px | Standard spacing |
| `--space-5` | 1.25rem | 20px | Large gaps |
| `--space-6` | 1.5rem | 24px | Section spacing |
| `--space-8` | 2rem | 32px | Major sections |
| `--space-10` | 2.5rem | 40px | Large sections |
| `--space-12` | 3rem | 48px | Page sections |
| `--space-16` | 4rem | 64px | Major layouts |
| `--space-20` | 5rem | 80px | Hero sections |
| `--space-24` | 6rem | 96px | Large layouts |

```css
/* Component spacing examples */
.c-card {
    padding: var(--space-6);
    margin-bottom: var(--space-4);
}

.c-button {
    padding: var(--space-3) var(--space-5);
}

.l-section {
    padding: var(--space-16) 0;
}
```

### Semantic Spacing

Beyond the base scale, MCSS provides semantic spacing tokens for common use cases:

| Token Name | Value | Usage |
|------------|-------|-------|
| `--space-component-padding` | var(--space-4) | Standard component internal padding |
| `--space-element-gap` | var(--space-3) | Gap between related elements |
| `--space-section-gap` | var(--space-8) | Gap between page sections |

## Border & Effects

### Border Radius

Consistent corner rounding for a cohesive visual language:

| Token Name | Value | Usage |
|------------|-------|-------|
| `--border-radius-none` | 0 | Sharp corners |
| `--border-radius-sm` | 0.125rem (2px) | Subtle rounding |
| `--border-radius-base` | 0.25rem (4px) | Standard rounding |
| `--border-radius-md` | 0.375rem (6px) | Medium rounding |
| `--border-radius-lg` | 0.5rem (8px) | Large rounding |
| `--border-radius-xl` | 0.75rem (12px) | Extra large rounding |
| `--border-radius-2xl` | 1rem (16px) | Container rounding |
| `--border-radius-full` | 9999px | Pill shape |

```css
.c-button {
    border-radius: var(--border-radius-md);
}

.c-card {
    border-radius: var(--border-radius-lg);
}

.c-avatar {
    border-radius: var(--border-radius-full);
}
```

### Border Widths

| Token Name | Value | Usage |
|------------|-------|-------|
| `--border-width-0` | 0 | No border |
| `--border-width-thin` | 1px | Standard borders |
| `--border-width-thick` | 2px | Emphasis, focus states |
| `--border-width-thicker` | 4px | Strong emphasis |

### Shadows

Layered shadow system for depth and hierarchy:

| Token Name | Value | Usage |
|------------|-------|-------|
| `--shadow-xs` | 0 1px 2px rgba(0,0,0,0.05) | Subtle elevation |
| `--shadow-sm` | 0 1px 3px rgba(0,0,0,0.1) | Small cards |
| `--shadow-base` | 0 4px 6px rgba(0,0,0,0.1) | Standard elevation |
| `--shadow-md` | 0 8px 25px rgba(0,0,0,0.1) | Medium elevation |
| `--shadow-lg` | 0 25px 50px rgba(0,0,0,0.15) | High elevation |
| `--shadow-xl` | 0 25px 50px rgba(0,0,0,0.25) | Maximum elevation |

```css
.c-card {
    box-shadow: var(--shadow-sm);
    transition: box-shadow var(--transition-base);
}

.c-card:hover {
    box-shadow: var(--shadow-md);
}

.c-modal {
    box-shadow: var(--shadow-xl);
}
```

## Motion & Transitions

### Timing Functions

| Token Name | Value | Usage |
|------------|-------|-------|
| `--ease-linear` | linear | Constant speed |
| `--ease-in` | ease-in | Slow start |
| `--ease-out` | ease-out | Slow end (preferred) |
| `--ease-in-out` | ease-in-out | Slow start and end |

### Duration

| Token Name | Value | Usage |
|------------|-------|-------|
| `--duration-instant` | 0ms | Immediate changes |
| `--duration-fast` | 150ms | Quick interactions |
| `--duration-base` | 250ms | Standard transitions |
| `--duration-slow` | 350ms | Complex animations |
| `--duration-slower` | 500ms | Major state changes |

```css
/* Smooth interactive transitions */
.c-button {
    transition: 
        background-color var(--duration-fast) var(--ease-out),
        border-color var(--duration-fast) var(--ease-out),
        transform var(--duration-fast) var(--ease-out);
}

.c-button:hover {
    transform: translateY(-1px);
}
```

## Z-Index Scale

Organized layering system for overlapping elements:

| Token Name | Value | Usage |
|------------|-------|-------|
| `--z-index-hide` | -1 | Hidden behind content |
| `--z-index-base` | 0 | Default stacking |
| `--z-index-docked` | 10 | Docked elements |
| `--z-index-dropdown` | 1000 | Dropdown menus |
| `--z-index-sticky` | 1020 | Sticky headers |
| `--z-index-modal-backdrop` | 1040 | Modal backgrounds |
| `--z-index-modal` | 1050 | Modal content |
| `--z-index-popover` | 1060 | Popovers, tooltips |
| `--z-index-toast` | 1070 | Toast notifications |
| `--z-index-tooltip` | 1080 | Tooltips (highest) |

## Token Usage Guidelines

### Best Practices

1. **Always Use Tokens**: Never hard-code values that have corresponding tokens
2. **Semantic Selection**: Choose tokens based on meaning, not appearance
3. **Consistent Application**: Use the same tokens for similar purposes
4. **Documentation**: Comment complex token usage for team clarity

### Common Patterns

#### Component Spacing
```css
.c-component {
    /* Use consistent internal padding */
    padding: var(--space-4);
    
    /* Use margin only for layout components */
    /* margin: 0; Components don't set external spacing */
    
    /* Use consistent gaps */
    gap: var(--space-3);
}
```

#### Interactive States
```css
.c-interactive {
    /* Base state */
    background-color: var(--color-background-interactive);
    border: 1px solid var(--color-border-interactive);
    
    /* Hover state */
    &:hover {
        background-color: var(--color-background-interactive-hover);
        border-color: var(--color-border-interactive-hover);
    }
    
    /* Focus state */
    &:focus-visible {
        outline: 2px solid var(--color-border-focus);
        outline-offset: 2px;
    }
    
    /* Disabled state */
    &[data-state="disabled"] {
        background-color: var(--color-background-disabled);
        color: var(--color-text-disabled);
        cursor: not-allowed;
    }
}
```

#### Responsive Typography
```css
.c-responsive-text {
    /* Use fluid typography for major headings */
    font-size: var(--font-size-heading-1); /* Includes clamp() */
    
    /* Use standard tokens for body text */
    font-size: var(--font-size-base);
    line-height: var(--line-height-normal);
}
```

### Custom Token Creation

When creating new tokens, follow the established patterns:

```css
/* ✅ Follow naming convention */
--color-background-custom-state: #value;
--space-custom-component: var(--space-6);
--font-size-custom-heading: 1.75rem;

/* ❌ Avoid breaking patterns */
--customColor: #value;
--my-special-spacing: 18px;
--bigText: 2rem;
```

The token system forms the foundation of visual consistency in MCSS. By religiously using tokens instead of hard-coded values, you create a maintainable, scalable, and themeable design system that can evolve with your project's needs.