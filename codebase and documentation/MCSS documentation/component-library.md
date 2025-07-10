# Component Library

The MCSS Component Library provides a comprehensive set of production-ready, accessible, and semantically rich UI components built on Atomic Design principles. Each component follows the MCSS architectural guidelines and includes full semantic annotations.

## Library Overview

### Design Philosophy

MCSS components are built with three core principles:

1. **Semantic Richness**: Every component includes machine-readable metadata that describes its purpose, composition, and behavior
2. **Accessibility First**: All components meet or exceed WCAG 2.2 AA standards with proper ARIA implementation
3. **Composability**: Components follow strict isolation rules allowing them to be combined and reused in any context

### Component Architecture

Components are organized using Atomic Design methodology:

- **Atoms**: Indivisible UI building blocks (buttons, inputs, labels)
- **Molecules**: Simple combinations of atoms (form fields, cards)
- **Organisms**: Complex interface sections (navigation, headers, modals)

### Usage Guidelines

#### Import Required Files

```html
<!-- Required MCSS files -->
<link rel="stylesheet" href="css/tokens.css">
<link rel="stylesheet" href="css/global.css">
<link rel="stylesheet" href="css/components.css">

<!-- RDFa vocabulary declaration -->
<html vocab="https://gabrielcpule.github.io/mcss-vocab/api/mcss/v1.rdf">
```

#### Basic Component Usage

Every MCSS component follows this pattern:

```html
<element 
    class="c-component-name"
    typeof="mcs:Component"
    property="mcs:taxonomyLevel" content="mcs:Level">
    <span property="mcs:purpose" content="Component description" class="u-hidden"></span>
    <!-- Component content -->
</element>
```

## Atoms

### Button

A fundamental interactive element for user actions.

**Usage**: Primary actions, form submissions, navigation triggers

```html
<!-- Primary button -->
<button 
    class="c-button c-button--primary"
    typeof="mcs:Component"
    property="mcs:taxonomyLevel" content="mcs:Atom"
    data-mcs-interaction-type="submission"
    data-mcs-consequence="Submit the user registration form">
    <span property="mcs:purpose" content="Submit form data to create new user account" class="u-hidden"></span>
    Create Account
</button>

<!-- Secondary button -->
<button 
    class="c-button c-button--secondary"
    typeof="mcs:Component"
    property="mcs:taxonomyLevel" content="mcs:Atom"
    data-mcs-interaction-type="navigation"
    data-mcs-consequence="Navigate to previous page">
    <span property="mcs:purpose" content="Return to previous page in workflow" class="u-hidden"></span>
    Go Back
</button>

<!-- Disabled state -->
<button 
    class="c-button"
    typeof="mcs:Component"
    property="mcs:taxonomyLevel" content="mcs:Atom"
    data-state="disabled"
    aria-disabled="true">
    <span property="mcs:purpose" content="Action currently unavailable to user" class="u-hidden"></span>
    Unavailable
</button>
```

**Available Variants**:
- `c-button--primary`: Primary call-to-action styling
- `c-button--secondary`: Secondary action styling
- `c-button--ghost`: Minimal styling for subtle actions

**States**: `default`, `hover`, `active`, `disabled`, `loading`

### Input

Text input field for user data entry with validation support.

**Usage**: Forms, search fields, data collection

```html
<div class="c-input-group">
    <label for="user-email" class="c-input-label">Email Address</label>
    <input 
        type="email"
        id="user-email"
        class="c-input"
        typeof="mcs:Component"
        property="mcs:taxonomyLevel" content="mcs:Atom"
        aria-required="true"
        aria-invalid="false"
        aria-describedby="email-error">
    <span property="mcs:purpose" content="Collect user's email address for account creation" class="u-hidden"></span>
    
    <!-- Error message (shown when data-state="error") -->
    <div id="email-error" class="c-input-error" role="alert">
        Please enter a valid email address
    </div>
</div>
```

**States**: `default`, `focus`, `error`, `success`, `disabled`

### Label

Accessible form labels that associate with input elements.

```html
<label 
    for="username"
    class="c-label"
    typeof="mcs:Component"
    property="mcs:taxonomyLevel" content="mcs:Atom">
    <span property="mcs:purpose" content="Identify the username input field for users" class="u-hidden"></span>
    Username
</label>
```

### Icon

Scalable vector icons for visual communication.

```html
<svg 
    class="c-icon c-icon--small"
    typeof="mcs:Component"
    property="mcs:taxonomyLevel" content="mcs:Atom"
    aria-hidden="true"
    focusable="false">
    <span property="mcs:purpose" content="Visual indicator for search functionality" class="u-hidden"></span>
    <use href="#icon-search"></use>
</svg>
```

**Sizes**: `c-icon--small`, `c-icon--medium`, `c-icon--large`

## Molecules

### Card

A flexible content container with header, body, and footer sections.

**Usage**: Content organization, product displays, information grouping

```html
<div 
    class="c-card"
    typeof="mcs:Component"
    property="mcs:taxonomyLevel" content="mcs:Molecule"
    property="mcs:componentName" content="Product Card"
    id="product-card-1">
    
    <span property="mcs:purpose" content="Display product information with actions" class="u-hidden"></span>
    
    <!-- Declare composition -->
    <div property="mcs:hasPart" resource="#card-header-1"></div>
    <div property="mcs:hasPart" resource="#card-body-1"></div>
    <div property="mcs:hasPart" resource="#card-footer-1"></div>
    
    <header id="card-header-1" class="c-card__header">
        <h3 property="mcs:part" content="Title" class="c-card__title">
            Product Name
        </h3>
    </header>
    
    <div id="card-body-1" class="c-card__body">
        <p property="mcs:part" content="Description">
            Detailed product description and features.
        </p>
        <div property="mcs:part" content="Price" class="c-card__price">
            $29.99
        </div>
    </div>
    
    <footer id="card-footer-1" class="c-card__footer">
        <button class="c-button c-button--primary">
            Add to Cart
        </button>
    </footer>
</div>
```

**Variants**: 
- `c-card--elevated`: Enhanced shadow for prominence
- `c-card--bordered`: Subtle border styling
- `c-card--interactive`: Hover effects for clickable cards

### Form Field

Complete form input with label, validation, and help text.

```html
<div 
    class="c-form-field"
    typeof="mcs:Component"
    property="mcs:taxonomyLevel" content="mcs:Molecule"
    id="email-field">
    
    <span property="mcs:purpose" content="Complete email input with validation feedback" class="u-hidden"></span>
    
    <!-- Composition declaration -->
    <div property="mcs:hasPart" resource="#email-label"></div>
    <div property="mcs:hasPart" resource="#email-input"></div>
    <div property="mcs:hasPart" resource="#email-help"></div>
    
    <label 
        id="email-label"
        for="email-field-input"
        class="c-form-field__label">
        Email Address
    </label>
    
    <input 
        id="email-input"
        type="email"
        class="c-form-field__input"
        required
        aria-describedby="email-help email-error">
    
    <div id="email-help" class="c-form-field__help">
        We'll never share your email with anyone else.
    </div>
    
    <div id="email-error" class="c-form-field__error" role="alert">
        <!-- Error message appears here -->
    </div>
</div>
```

### Search Box

Input field optimized for search functionality.

```html
<div 
    class="c-search-box"
    typeof="mcs:Component"
    property="mcs:taxonomyLevel" content="mcs:Molecule"
    role="search">
    
    <span property="mcs:purpose" content="Enable users to search through content" class="u-hidden"></span>
    
    <label for="search-input" class="c-search-box__label u-hidden">
        Search
    </label>
    
    <div class="c-search-box__input-wrapper">
        <input 
            id="search-input"
            type="search"
            class="c-search-box__input"
            placeholder="Search..."
            aria-label="Search">
        
        <button 
            type="submit"
            class="c-search-box__button"
            aria-label="Submit search">
            <svg class="c-icon" aria-hidden="true">
                <use href="#icon-search"></use>
            </svg>
        </button>
    </div>
</div>
```

## Organisms

### Navigation

Accessible navigation menubar with dropdown support.

**Usage**: Site navigation, application menus

```html
<nav 
    class="c-navigation"
    typeof="mcs:Component"
    property="mcs:taxonomyLevel" content="mcs:Organism"
    aria-label="Main navigation">
    
    <span property="mcs:purpose" content="Primary site navigation with hierarchical menu structure" class="u-hidden"></span>
    
    <ul class="c-navigation__menu" role="menubar">
        <li class="c-navigation__item" role="none">
            <a 
                href="/"
                class="c-navigation__link"
                role="menuitem"
                tabindex="0">
                Home
            </a>
        </li>
        
        <li class="c-navigation__item" role="none">
            <a 
                href="/products"
                class="c-navigation__link"
                role="menuitem"
                tabindex="-1"
                aria-haspopup="true"
                aria-expanded="false">
                Products
            </a>
            
            <!-- Submenu -->
            <ul class="c-navigation__submenu" role="menu" aria-label="Products">
                <li role="none">
                    <a href="/products/widgets" role="menuitem" tabindex="-1">
                        Widgets
                    </a>
                </li>
                <li role="none">
                    <a href="/products/gadgets" role="menuitem" tabindex="-1">
                        Gadgets
                    </a>
                </li>
            </ul>
        </li>
        
        <li class="c-navigation__item" role="none">
            <a 
                href="/about"
                class="c-navigation__link"
                role="menuitem"
                tabindex="-1">
                About
            </a>
        </li>
    </ul>
</nav>
```

**Required Behavior**: See [Navigation Behavioral Contract](#navigation-behavior)

### Site Header

Complete page header with branding and navigation.

```html
<header 
    class="c-site-header"
    typeof="mcs:Component"
    property="mcs:taxonomyLevel" content="mcs:Organism"
    role="banner">
    
    <span property="mcs:purpose" content="Site branding and primary navigation container" class="u-hidden"></span>
    
    <div class="c-site-header__container">
        <div class="c-site-header__brand">
            <a href="/" class="c-site-header__logo">
                <img src="logo.svg" alt="Company Name" width="120" height="40">
            </a>
        </div>
        
        <div class="c-site-header__nav">
            <!-- Navigation component -->
            <nav class="c-navigation" aria-label="Main navigation">
                <!-- Navigation content -->
            </nav>
        </div>
        
        <div class="c-site-header__actions">
            <button class="c-button c-button--secondary">
                Sign In
            </button>
            <button class="c-button c-button--primary">
                Sign Up
            </button>
        </div>
    </div>
</header>
```

### Modal Dialog

Accessible modal overlay for focused interactions.

```html
<div 
    class="c-modal"
    typeof="mcs:Component"
    property="mcs:taxonomyLevel" content="mcs:Organism"
    role="dialog"
    aria-modal="true"
    aria-labelledby="modal-title"
    aria-describedby="modal-description"
    data-state="closed">
    
    <span property="mcs:purpose" content="Display focused content that requires user attention" class="u-hidden"></span>
    
    <div class="c-modal__backdrop" data-mcs-action="close-modal"></div>
    
    <div class="c-modal__container">
        <div class="c-modal__header">
            <h2 id="modal-title" class="c-modal__title">
                Confirm Action
            </h2>
            <button 
                class="c-modal__close"
                aria-label="Close dialog"
                data-mcs-action="close-modal">
                <svg class="c-icon" aria-hidden="true">
                    <use href="#icon-close"></use>
                </svg>
            </button>
        </div>
        
        <div class="c-modal__body">
            <p id="modal-description">
                Are you sure you want to delete this item? This action cannot be undone.
            </p>
        </div>
        
        <div class="c-modal__footer">
            <button class="c-button c-button--secondary" data-mcs-action="close-modal">
                Cancel
            </button>
            <button class="c-button c-button--primary" data-mcs-action="confirm-delete">
                Delete
            </button>
        </div>
    </div>
</div>
```

**Required Behavior**: Focus trapping, escape key handling, backdrop clicks

## Behavioral Contracts

### Navigation Behavior

Complex interactive components require behavioral contracts that specify keyboard interactions and ARIA state management.

#### Keyboard Interactions

| Key | Context | Action |
|-----|---------|--------|
| **Tab** | Any element | Move focus out of navigation to next page element |
| **Shift + Tab** | Any element | Move focus out of navigation to previous page element |
| **Right Arrow** | Menu bar | Move focus to next menu item (wraps to first) |
| **Left Arrow** | Menu bar | Move focus to previous menu item (wraps to last) |
| **Down Arrow** | Menu bar | Open submenu and focus first item |
| **Up Arrow** | Menu bar | Open submenu and focus last item |
| **Enter/Space** | Menu item | Activate link or open submenu |
| **Escape** | Submenu | Close submenu and return focus to parent |
| **Home** | Any menu | Focus first item in current menu level |
| **End** | Any menu | Focus last item in current menu level |

#### Focus Management

- **Initial Focus**: First menu item has `tabindex="0"`, others have `tabindex="-1"`
- **Roving Tabindex**: Focus moves between items using arrow keys, updating tabindex values
- **Submenu Focus**: When submenu opens, focus moves to first item inside
- **Focus Restoration**: When submenu closes, focus returns to triggering menu item

#### ARIA State Management

- **Menu Structure**: `role="menubar"` on main list, `role="menu"` on submenus
- **Menu Items**: `role="menuitem"` on links, `role="none"` on list items
- **Submenu Indicators**: `aria-haspopup="true"` and `aria-expanded` on parent items
- **Accessible Names**: `aria-label` on submenus for context

## Component Customization

### CSS Custom Properties

Many components expose CSS custom properties for easy customization:

```css
.c-button {
    /* Customizable properties */
    --button-padding: var(--space-3) var(--space-5);
    --button-border-radius: var(--border-radius-md);
    --button-font-weight: var(--font-weight-medium);
    
    /* Usage */
    padding: var(--button-padding);
    border-radius: var(--button-border-radius);
    font-weight: var(--button-font-weight);
}

/* Custom button variant */
.c-button--large {
    --button-padding: var(--space-4) var(--space-8);
    --button-font-size: var(--font-size-lg);
}
```

### Creating Custom Components

Follow MCSS patterns when creating new components:

```css
/* New component following MCSS patterns */
.c-alert {
    /* Use design tokens */
    padding: var(--space-4);
    border-radius: var(--border-radius-md);
    border: 1px solid var(--color-border-default);
    
    /* No external margins (Golden Rule) */
    margin: 0;
    
    /* State management via data attributes */
}

.c-alert[data-state="error"] {
    background-color: var(--color-background-error);
    border-color: var(--color-border-error);
    color: var(--color-text-error);
}
```

```html
<!-- Properly annotated custom component -->
<div 
    class="c-alert"
    typeof="mcs:Component"
    property="mcs:taxonomyLevel" content="mcs:Atom"
    data-state="error"
    role="alert">
    <span property="mcs:purpose" content="Display important error message to user" class="u-hidden"></span>
    Error: Please check your input and try again.
</div>
```

## Contributing to the Library

### Component Proposal Process

1. **Research**: Verify the component doesn't already exist
2. **Design**: Create designs following MCSS token system
3. **Specification**: Write behavioral contracts for complex components
4. **Implementation**: Build component following architectural guidelines
5. **Testing**: Verify accessibility and semantic compliance
6. **Documentation**: Create comprehensive usage examples

### Quality Standards

All components must meet these standards:

- **Accessibility**: WCAG 2.2 AA compliance minimum
- **Semantic Annotations**: Complete RDFa vocabulary implementation
- **Token Usage**: No hard-coded values, tokens only
- **Isolation**: No external margins, proper encapsulation
- **Documentation**: Clear usage examples and behavioral contracts

The MCSS Component Library provides a solid foundation for building consistent, accessible, and semantically rich user interfaces. Each component is designed to work independently while composing seamlessly with others, following the established architectural patterns that make MCSS unique.