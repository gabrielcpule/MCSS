# MCSS: Model Context Style Sheet Framework

**Transform your HTML from human-readable displays into machine-readable knowledge graphs**

The Model Context Style Sheet (MCSS) framework revolutionizes how we build user interfaces by embedding semantic meaning directly into HTML markup. Instead of relying on weak signals like class names, MCSS creates explicit, structured metadata that enables both humans and AI systems to understand component identity, composition, and purpose without inference.

## Key Features

### 🎯 **Semantic Imperative**
Transform HTML documents into structured knowledge graphs using RDFa annotations and semantic naming conventions.

### 🏗️ **5-Layer Architecture**
Systematic CSS organization with Global, Layout, Component, Utility, and Exception layers that prevent specificity conflicts.

### 📝 **Ontological Naming Convention**
Predictable class naming that acts as a "type system" for CSS, making code self-documenting and AI-friendly.

### ♿ **Accessibility First**
Built-in WCAG 2.2 AA compliance with focus management, semantic markup, and assistive technology support.

### 🔧 **Token-Driven Design**
Single source of truth design system with comprehensive tokens for colors, typography, spacing, and effects.

### 🤖 **AI-Optimized**
Structured for high-fidelity understanding by Large Language Models and automated tools.

## Quick Start

Get started with MCSS in just a few steps:

### 1. Install MCSS

```bash
npm install @mcss/framework
# or
yarn add @mcss/framework
```

### 2. Include the Core Files

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My MCSS Project</title>
    <link rel="stylesheet" href="mcss/tokens.css">
    <link rel="stylesheet" href="mcss/global.css">
    <link rel="stylesheet" href="mcss/components.css">
</head>
```

### 3. Build Your First Component

```html
<button 
    class="c-button c-button--primary"
    typeof="mcs:Component"
    property="mcs:taxonomyLevel"
    content="mcs:Atom"
    data-mcs-interaction-type="click"
    data-mcs-consequence="submit-form">
    <span property="mcs:purpose" content="Submit the user registration form">
        Create Account
    </span>
</button>
```

## Architecture Overview

MCSS is built on five foundational principles:

### The 5-Layer CSS Architecture

1. **Global Layer**: Base styles and resets
2. **Layout Layer**: Positioning and arrangement (`l-*`)
3. **Component Layer**: Reusable UI components (`c-*`)
4. **Utility Layer**: Single-purpose overrides (`u-*`)
5. **Exception Layer**: Temporary fixes and third-party code

### Component Isolation

Components never declare external margins, ensuring they can be placed in any layout context without conflicts.

### State Management

All component states are managed via `data-state` attributes, providing a consistent and predictable state API.

### Semantic Annotations

RDFa vocabulary creates machine-readable component metadata:
- `typeof="mcs:Component"` - Identifies components
- `property="mcs:purpose"` - Describes component function
- `property="mcs:taxonomyLevel"` - Atomic Design classification

## Component Library

MCSS includes production-ready components following Atomic Design principles:

### Atoms
- **Button**: Primary, secondary, and specialized button variants
- **Input**: Text inputs with validation states
- **Label**: Accessible form labels

### Molecules
- **Card**: Content containers with header, body, and footer
- **Form Field**: Input + label combinations
- **Search Box**: Input with integrated search functionality

### Organisms
- **Navigation**: Accessible menubar with dropdown support
- **Header**: Site navigation and branding
- **Modal**: Overlay dialogs with focus management

## Design Tokens

Comprehensive token system covering:

- **Colors**: Semantic color palette with accessibility-verified contrast ratios
- **Typography**: Modular scale with fluid sizing
- **Spacing**: Consistent 4px/8px grid system
- **Effects**: Shadows, transitions, and animations

## Why MCSS?

### For Developers
- **Predictable**: Clear naming conventions and architectural rules
- **Maintainable**: Token-driven system prevents technical debt
- **Scalable**: Component-based architecture grows with your project

### For Teams
- **Consistent**: Unified approach to CSS and component development
- **Collaborative**: Self-documenting code that's easy to onboard to
- **Quality**: Built-in accessibility and performance best practices

### For AI & Automation
- **Machine-Readable**: Structured semantic data enables AI understanding
- **Testable**: Behavioral contracts provide clear testing targets
- **Analyzable**: Knowledge graph structure supports automated analysis

## Browser Support

MCSS supports all modern browsers:
- Chrome 60+
- Firefox 55+
- Safari 12+
- Edge 79+

## Getting Help

- **Documentation**: Comprehensive guides and API reference
- **GitHub**: Source code, issues, and contributions
- **Discord**: Community support and discussions

## License

MCSS is open source software licensed under the MIT License.

---

**Ready to build semantic, accessible, and AI-friendly interfaces?** 

[Get Started](/getting-started/) • [View Components](/components/) • [Browse Tokens](/tokens/)