# Getting Started with MCSS

Welcome to the Model Context Style Sheet (MCSS) framework! This guide will walk you through everything you need to know to start building semantic, accessible, and AI-friendly user interfaces.

## Installation

### Via NPM

```bash
npm install @mcss/framework
```

### Via Yarn

```bash
yarn add @mcss/framework
```

### Via CDN

```html
<!-- Core MCSS files -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@mcss/framework@1.0.0/dist/tokens.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@mcss/framework@1.0.0/dist/global.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@mcss/framework@1.0.0/dist/components.css">
```

## Basic Setup

### 1. HTML Document Structure

Create a basic HTML document with the MCSS files included:

```html
<!DOCTYPE html>
<html lang="en" vocab="https://gabrielcpule.github.io/mcss-vocab/api/mcss/v1.rdf">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My MCSS Project</title>
    
    <!-- MCSS Core Files -->
    <link rel="stylesheet" href="css/tokens.css">
    <link rel="stylesheet" href="css/global.css">
    <link rel="stylesheet" href="css/components.css">
</head>
<body>
    <!-- Your content goes here -->
</body>
</html>
```

**Important**: Notice the `vocab` attribute on the `<html>` element. This declares the MCSS RDFa vocabulary namespace for semantic annotations.

### 2. Project Structure

Organize your MCSS project with this recommended structure:

```
my-mcss-project/
├── css/
│   ├── tokens.css          # Design tokens (required)
│   ├── global.css          # Global styles (required)
│   ├── components.css      # Component styles (required)
│   └── custom.css          # Your custom styles
├── js/
│   └── components.js       # Component behaviors
├── index.html
└── package.json
```

## Your First Component

Let's build a simple "Hello World" page using MCSS principles:

### Step 1: Create the Page Structure

```html
<!DOCTYPE html>
<html lang="en" vocab="https://gabrielcpule.github.io/mcss-vocab/api/mcss/v1.rdf">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello MCSS</title>
    <link rel="stylesheet" href="css/tokens.css">
    <link rel="stylesheet" href="css/global.css">
    <link rel="stylesheet" href="css/components.css">
</head>
<body>
    <div class="l-container">
        <main class="l-stack">
            <!-- Content will go here -->
        </main>
    </div>
</body>
</html>
```

### Step 2: Add a Semantic Card Component

```html
<div 
    class="c-card"
    typeof="mcs:Component"
    property="mcs:taxonomyLevel"
    content="mcs:Molecule"
    property="mcs:componentName"
    content="Welcome Card">
    
    <span property="mcs:purpose" content="Welcome new users to the MCSS framework" class="u-hidden"></span>
    
    <header class="c-card__header">
        <h1 property="mcs:part" content="Title" class="c-card__title">
            Hello, MCSS!
        </h1>
    </header>
    
    <div class="c-card__body">
        <p property="mcs:part" content="Description">
            Welcome to the Model Context Style Sheet framework. This card demonstrates
            semantic HTML with embedded machine-readable metadata.
        </p>
        
        <button 
            class="c-button c-button--primary"
            typeof="mcs:Component"
            property="mcs:taxonomyLevel"
            content="mcs:Atom"
            data-mcs-interaction-type="navigation"
            data-mcs-consequence="Navigate to documentation">
            
            <span property="mcs:purpose" content="Navigate to framework documentation" class="u-hidden"></span>
            Learn More
        </button>
    </div>
</div>
```

### Step 3: Understanding the Annotations

Let's break down the semantic annotations:

#### Component Identity
```html
typeof="mcs:Component"
property="mcs:taxonomyLevel" content="mcs:Molecule"
property="mcs:componentName" content="Welcome Card"
```
- `typeof="mcs:Component"` identifies this as an MCSS component
- `mcs:taxonomyLevel` classifies it in the Atomic Design hierarchy
- `mcs:componentName` provides a human-readable component name

#### Component Purpose
```html
<span property="mcs:purpose" content="Welcome new users..." class="u-hidden"></span>
```
- Hidden from visual display but readable by machines
- Describes the component's functional purpose
- Essential for AI understanding and automation

#### Behavioral Contract
```html
data-mcs-interaction-type="navigation"
data-mcs-consequence="Navigate to documentation"
```
- Describes what type of interaction this element provides
- Explains the expected result of user interaction
- Creates framework-agnostic behavioral hooks

## Understanding the 5-Layer Architecture

MCSS organizes CSS into five distinct layers, each with specific responsibilities:

### Layer 1: Global
**Files**: `tokens.css`, `global.css`
**Purpose**: Foundation styles and design tokens

```css
/* Global styles apply to HTML elements directly */
body {
    font-family: var(--font-family-base);
    font-size: var(--font-size-body-base);
    line-height: var(--line-height-base);
}

h1 {
    font-size: var(--font-size-heading-1);
}
```

### Layer 2: Layout
**Classes**: `l-*` (e.g., `l-container`, `l-grid`, `l-stack`)
**Purpose**: Page layout and component arrangement

```html
<div class="l-container">          <!-- Max-width container -->
    <div class="l-grid l-grid--3-col">  <!-- 3-column grid -->
        <div class="l-stack">       <!-- Vertical stack layout -->
            <!-- Components go here -->
        </div>
    </div>
</div>
```

### Layer 3: Component
**Classes**: `c-*` (e.g., `c-button`, `c-card`, `c-navigation`)
**Purpose**: Reusable UI components

```html
<button class="c-button c-button--primary">
    Primary Action
</button>
```

### Layer 4: Utility
**Classes**: `u-*` (e.g., `u-text-center`, `u-hidden`, `u-margin-0`)
**Purpose**: Single-purpose style overrides

```html
<p class="u-text-center u-margin-0">
    Centered text with no margin
</p>
```

### Layer 5: Exception
**Purpose**: Temporary overrides and third-party integration
**Use sparingly**: Only for debugging or legacy code integration

## Design Tokens in Practice

MCSS uses design tokens as the single source of truth for all design decisions:

### Using Color Tokens
```css
.my-custom-component {
    background-color: var(--color-background-primary);
    color: var(--color-text-primary);
    border: 1px solid var(--color-border-default);
}
```

### Using Spacing Tokens
```css
.my-component {
    padding: var(--space-4);
    margin-bottom: var(--space-6);
    gap: var(--space-2);
}
```

### Using Typography Tokens
```css
.my-heading {
    font-family: var(--font-family-sans);
    font-size: var(--font-size-heading-2);
    font-weight: var(--font-weight-bold);
    line-height: var(--line-height-tight);
}
```

## State Management

MCSS uses `data-state` attributes for consistent state management:

### Button States
```html
<!-- Default state -->
<button class="c-button">Default</button>

<!-- Disabled state -->
<button class="c-button" data-state="disabled" aria-disabled="true">
    Disabled
</button>

<!-- Loading state -->
<button class="c-button" data-state="loading" aria-busy="true">
    Loading...
</button>
```

### Input States
```html
<!-- Default state -->
<input class="c-input" type="email">

<!-- Error state -->
<input class="c-input" type="email" data-state="error" aria-invalid="true">

<!-- Success state -->
<input class="c-input" type="email" data-state="success" aria-invalid="false">
```

## Accessibility Best Practices

MCSS has accessibility built-in, but you should follow these practices:

### Semantic HTML
```html
<!-- Use proper semantic elements -->
<nav aria-label="Main navigation">
    <ul class="c-navigation__menu" role="menubar">
        <li role="none">
            <a href="/" role="menuitem">Home</a>
        </li>
    </ul>
</nav>
```

### ARIA Attributes
```html
<!-- Provide accessible names and descriptions -->
<button 
    class="c-button"
    aria-describedby="help-text"
    aria-expanded="false">
    Toggle Menu
</button>
<div id="help-text">Click to open the navigation menu</div>
```

### Focus Management
```css
/* Focus styles are built into components */
.c-button:focus-visible {
    outline: 2px solid var(--color-border-focus);
    outline-offset: 2px;
}
```

## Next Steps

Now that you understand the basics, explore these areas:

1. **[Core Concepts](/concepts/)** - Deep dive into MCSS architecture
2. **[Component Library](/components/)** - Browse available components  
3. **[Design Tokens](/tokens/)** - Complete token reference
4. **[Annotation System](/annotations/)** - Master semantic markup

## Common Patterns

### Form with Validation
```html
<form class="l-stack">
    <div class="c-form-field">
        <label for="email" class="c-form-field__label">Email Address</label>
        <input 
            type="email" 
            id="email" 
            class="c-input"
            required
            aria-describedby="email-error">
        <div id="email-error" class="c-form-field__error" role="alert">
            Please enter a valid email address
        </div>
    </div>
    
    <button type="submit" class="c-button c-button--primary">
        Create Account
    </button>
</form>
```

### Responsive Card Grid
```html
<div class="l-container">
    <div class="l-grid l-grid--responsive">
        <div class="c-card">
            <div class="c-card__body">
                <h3 class="c-card__title">Feature One</h3>
                <p>Description of the first feature.</p>
            </div>
        </div>
        
        <div class="c-card">
            <div class="c-card__body">
                <h3 class="c-card__title">Feature Two</h3>
                <p>Description of the second feature.</p>
            </div>
        </div>
    </div>
</div>
```

### Navigation with Dropdown
```html
<nav class="c-navigation" aria-label="Main navigation">
    <ul class="c-navigation__menu" role="menubar">
        <li class="c-navigation__item" role="none">
            <a href="/" class="c-navigation__link" role="menuitem">Home</a>
        </li>
        <li class="c-navigation__item" role="none">
            <a 
                href="/products" 
                class="c-navigation__link" 
                role="menuitem"
                aria-haspopup="true"
                aria-expanded="false">
                Products
            </a>
            <ul class="c-navigation__submenu" role="menu">
                <li role="none">
                    <a href="/products/widgets" role="menuitem">Widgets</a>
                </li>
            </ul>
        </li>
    </ul>
</nav>
```

Ready to start building? Check out our [Component Library](/components/) for more examples and patterns!