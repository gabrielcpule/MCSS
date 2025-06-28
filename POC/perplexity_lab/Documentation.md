Model Context Style Sheet (MCSS) v1.0.0-poc
A five-layer, LLM-optimized CSS framework designed to achieve 70% first-attempt success rates for AI-generated UI components through semantic transparency, accessibility compliance, and ontological naming conventions.

Table of Contents
Quick Start

Architecture Overview

Design Tokens

Component Library

Layout Primitives

Utility Classes

RDFa Annotations

Accessibility Features

LLM Integration Guide

API Reference

Contributing

Quick Start
Installation
xml
<!-- Include MCSS framework -->
<link rel="stylesheet" href="mcss-framework.css">

<!-- Add namespace declaration -->
<html prefix="mcs: http://schema.model-context.org/v1/">
Basic Usage
xml
<!-- Simple button component -->
<button class="c-button c-button--primary" 
        typeof="mcs:Component"
        property="mcs:purpose" content="Primary action button"
        data-mcs-interaction-type="click">
  Click Me
</button>

<!-- Card layout with stack -->
<div class="l-stack l-stack--md">
  <article class="c-card" typeof="mcs:Component">
    <header class="c-card__header">
      <h2>Card Title</h2>
    </header>
    <div class="c-card__content">
      <p>Card content goes here</p>
    </div>
  </article>
</div>
Architecture Overview
MCSS implements a five-layer architecture that separates concerns and provides clear semantic boundaries for both human developers and LLM agents.

Layer Hierarchy
Layer	Prefix	Purpose	Specificity
1. Global	:root	Design tokens and CSS custom properties	Lowest
2. Composition	l-*	Layout primitives and containers	Low
3. Utilities	u-*	Single-purpose helper classes	Medium
4. Blocks	c-*	Component blocks using BEM methodology	High
5. Exceptions	data-mcs-*	State and variant attributes	Highest
Ontological Naming Convention (ONC)
The framework uses systematic prefixes that enable LLMs to understand class semantics:

Layout: l-[layout-name] (e.g., l-grid, l-stack)

Components: c-[block-name] with BEM elements and modifiers

Utilities: u-[utility-name] (e.g., u-visually-hidden)

Design Tokens
Color System
css
:root {
  /* Brand Colors */
  --mcs-color-brand-primary: #005A9C;
  --mcs-color-brand-secondary: #6c757d;
  
  /* Neutral Scale */
  --mcs-color-neutral-100: #f8f9fa;
  --mcs-color-neutral-900: #212529;
  
  /* Semantic Colors */
  --mcs-color-success: #28a745;
  --mcs-color-warning: #ffc107;
  --mcs-color-error: #dc3545;
  --mcs-color-info: #17a2b8;
}
Typography Scale
css
:root {
  /* Font Sizes */
  --mcs-font-size-xs: 0.75rem;
  --mcs-font-size-sm: 0.875rem;
  --mcs-font-size-base: 1rem;
  --mcs-font-size-lg: 1.25rem;
  --mcs-font-size-xl: 1.5rem;
  
  /* Line Heights */
  --mcs-line-height-tight: 1.25;
  --mcs-line-height-base: 1.5;
  --mcs-line-height-loose: 1.75;
}
Spacing System
css
:root {
  /* Spacing Scale */
  --mcs-spacing-xs: 0.25rem;
  --mcs-spacing-sm: 0.5rem;
  --mcs-spacing-md: 1rem;
  --mcs-spacing-lg: 1.5rem;
  --mcs-spacing-xl: 2rem;
}
Component Library
Button Component (c-button)
A flexible button component with semantic variants and full accessibility support.

Basic Structure
xml
<button class="c-button" 
        typeof="mcs:Component"
        property="mcs:purpose" content="Generic action button"
        data-mcs-interaction-type="click">
  Button Text
</button>
Variants
xml
<!-- Primary Button -->
<button class="c-button c-button--primary">Primary</button>

<!-- Secondary Button -->
<button class="c-button c-button--secondary">Secondary</button>

<!-- Outline Button -->
<button class="c-button c-button--outline">Outline</button>

<!-- Danger Button -->
<button class="c-button c-button--danger">Danger</button>
Sizes
xml
<!-- Small Button -->
<button class="c-button c-button--sm">Small</button>

<!-- Large Button -->
<button class="c-button c-button--lg">Large</button>
States
xml
<!-- Loading State -->
<button class="c-button" data-mcs-loading="true">Loading...</button>

<!-- Disabled State -->
<button class="c-button" disabled>Disabled</button>
Card Component (c-card)
A flexible container component for displaying related information.

Basic Structure
xml
<article class="c-card" 
         typeof="mcs:Component"
         property="mcs:purpose" content="Content container">
  <header class="c-card__header">
    <h3 class="c-card__title">Card Title</h3>
  </header>
  
  <div class="c-card__content">
    <p>Card content goes here.</p>
  </div>
  
  <footer class="c-card__footer">
    <button class="c-button c-button--primary">Action</button>
  </footer>
</article>
Modifiers
xml
<!-- Elevated Card -->
<article class="c-card c-card--elevated">...</article>

<!-- Interactive Card -->
<article class="c-card c-card--interactive" 
         data-mcs-interaction-type="click">...</article>
Form Input Component (c-input)
Accessible form input with validation states and help text.

Basic Structure
xml
<div class="c-input" typeof="mcs:Component">
  <label class="c-input__label" for="email">
    Email Address
  </label>
  
  <input class="c-input__field" 
         type="email" 
         id="email" 
         name="email"
         aria-describedby="email-help">
  
  <div class="c-input__help" id="email-help">
    Enter your email address
  </div>
</div>
Validation States
xml
<!-- Error State -->
<div class="c-input c-input--error">
  <label class="c-input__label" for="email">Email</label>
  <input class="c-input__field" type="email" id="email" aria-invalid="true">
  <div class="c-input__error" role="alert">Please enter a valid email</div>
</div>

<!-- Success State -->
<div class="c-input c-input--success">
  <label class="c-input__label" for="email">Email</label>
  <input class="c-input__field" type="email" id="email">
  <div class="c-input__success">Email is valid</div>
</div>
Layout Primitives
Stack Layout (l-stack)
Provides consistent vertical spacing between child elements.

xml
<!-- Basic Stack -->
<div class="l-stack">
  <h1>Heading</h1>
  <p>Paragraph</p>
  <button class="c-button">Button</button>
</div>

<!-- Stack with Custom Gap -->
<div class="l-stack l-stack--lg">
  <!-- Large gap between children -->
</div>
Gap Modifiers
l-stack--xs: Extra small gap

l-stack--sm: Small gap

l-stack--md: Medium gap (default)

l-stack--lg: Large gap

l-stack--xl: Extra large gap

Grid Layout (l-grid)
Responsive grid system with auto-fitting columns.

xml
<!-- Basic Grid -->
<div class="l-grid">
  <div class="c-card">Card 1</div>
  <div class="c-card">Card 2</div>
  <div class="c-card">Card 3</div>
</div>

<!-- Grid with Custom Column Size -->
<div class="l-grid l-grid--250">
  <!-- Columns minimum 250px wide -->
</div>
Utility Classes
Visibility
xml
<!-- Screen Reader Only -->
<span class="u-visually-hidden">Screen reader text</span>

<!-- Focus Visible -->
<button class="u-focus-ring">Focusable Element</button>
Colors
xml
<!-- Background Colors -->
<div class="u-bg-primary">Primary Background</div>
<div class="u-bg-neutral-100">Neutral Background</div>

<!-- Text Colors -->
<p class="u-text-error">Error Text</p>
<p class="u-text-success">Success Text</p>
Typography
xml
<!-- Font Sizes -->
<p class="u-text-lg">Large Text</p>
<p class="u-text-sm">Small Text</p>

<!-- Font Weights -->
<p class="u-font-bold">Bold Text</p>
<p class="u-font-normal">Normal Text</p>
Spacing
xml
<!-- Padding -->
<div class="u-p-md">Medium Padding</div>
<div class="u-px-lg">Large Horizontal Padding</div>

<!-- Margin -->
<div class="u-m-sm">Small Margin</div>
<div class="u-mt-xl">Extra Large Top Margin</div>
RDFa Annotations
MCSS uses RDFa (Resource Description Framework in Attributes) to provide machine-readable semantic information about components.

Namespace Declaration
xml
<html prefix="mcs: http://schema.model-context.org/v1/">
Component Annotations
xml
<button class="c-button" 
        typeof="mcs:Component"
        property="mcs:purpose" content="Primary action button"
        data-mcs-interaction-type="click"
        data-mcs-consequence="form-submit">
  Submit Form
</button>
Available Properties
typeof="mcs:Component": Identifies element as an MCSS component

property="mcs:purpose": Describes the component's intended purpose

data-mcs-interaction-type: Type of interaction (click, hover, focus, etc.)

data-mcs-consequence: What happens when interacted with

data-mcs-state: Current state of the component

Accessibility Features
MCSS is designed to meet WCAG 2.2 AA compliance standards by default.

Color Contrast
All color combinations maintain minimum contrast ratios:

Normal text: 4.5:1

Large text (18pt+): 3:1

UI components: 3:1

Focus Management
css
.u-focus-ring:focus-visible {
  outline: 2px solid var(--mcs-color-brand-primary);
  outline-offset: 2px;
}
Motion Preferences
css
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
High Contrast Mode
css
@media (prefers-contrast: high) {
  :root {
    --mcs-color-brand-primary: #000000;
    --mcs-color-neutral-100: #ffffff;
  }
}
LLM Integration Guide
Prompting Best Practices
When working with LLMs to generate MCSS markup:

Specify Layer Requirements: Request components by layer (composition, utility, block)

Include Semantic Annotations: Always request RDFa properties

Reference Existing Components: Use the component library as examples

Example Prompts
text
"Create a primary button using MCSS that submits a form, with proper RDFa annotations"

"Generate a card component with header, content, and footer using MCSS classes"

"Build a responsive grid layout containing three cards using MCSS primitives"
LLM-Friendly Features
Predictable Naming: ONC prefixes reduce hallucination

Rich Metadata: RDFa provides context for generation

Layer Separation: Clear boundaries prevent cascading errors

Token System: Authoritative design values

API Reference
CSS Custom Properties API
css
/* Component theming */
.c-button {
  background-color: var(--mcs-color-brand-primary);
  padding: var(--mcs-spacing-sm) var(--mcs-spacing-md);
  font-size: var(--mcs-font-size-base);
}
Data Attribute API
xml
<!-- Loading state -->
<button data-mcs-loading="true">Loading...</button>

<!-- Selected state -->
<div data-mcs-selected="true">Selected Item</div>

<!-- Elevated state -->
<div data-mcs-elevated="true">Elevated Component</div>
Responsive Modifiers
xml
<!-- Responsive grid columns -->
<div class="l-grid l-grid--200@sm l-grid--300@lg">
  <!-- Responsive column sizing -->
</div>
Contributing
Development Setup
Clone the repository

Install dependencies: npm install

Run development server: npm run dev

Run tests: npm test

Component Development Guidelines
Follow ONC: Use appropriate prefixes for all classes

Add RDFa: Include semantic annotations for all interactive elements

Test Accessibility: Verify WCAG 2.2 AA compliance

Document Purpose: Write clear purpose descriptions for LLM consumption

Testing LLM Integration
bash
# Run LLM generation tests
npm run test:llm

# Validate semantic annotations
npm run validate:rdfa

# Check accessibility compliance  
npm run test:a11y
For questions, issues, or contributions, please visit our GitHub repository or contact the development team.