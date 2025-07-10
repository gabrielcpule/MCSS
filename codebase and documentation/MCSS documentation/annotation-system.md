# Annotation System

The MCSS annotation system transforms HTML markup into a rich, machine-readable knowledge graph. This comprehensive guide covers the RDFa vocabulary, behavioral attributes, and validation strategies that make MCSS components semantically rich and AI-friendly.

## RDFa Vocabulary Reference

### Core Vocabulary Overview

The MCSS annotation system uses Resource Description Framework in Attributes (RDFa) to embed structured metadata directly into HTML. All components must declare the MCSS vocabulary namespace:

```html
<html lang="en" vocab="https://gabrielcpule.github.io/mcss-vocab/api/mcss/v1.rdf">
```

### Required Component Declaration

Every MCSS component must be properly identified and classified:

```html
<div 
    class="c-button"
    typeof="mcs:Component"
    property="mcs:taxonomyLevel" content="mcs:Atom">
    <!-- Component content -->
</div>
```

### Complete Property Reference

#### `mcs:componentName`
**Purpose**: Human-readable component identifier  
**Type**: String  
**Required**: No  
**Usage**: For component documentation and tooling

```html
<div 
    typeof="mcs:Component"
    property="mcs:componentName" content="Primary Call-to-Action Button">
    <!-- Component content -->
</div>
```

#### `mcs:purpose`
**Purpose**: Functional description of component's role  
**Type**: String  
**Required**: Yes for all components  
**Implementation**: Must be in hidden element to separate from presentation

```html
<button class="c-button">
    <span property="mcs:purpose" content="Submit the user registration form" class="u-hidden"></span>
    Create Account
</button>
```

#### `mcs:taxonomyLevel`
**Purpose**: Atomic Design classification  
**Type**: Controlled vocabulary  
**Required**: Yes for all components  
**Values**: `mcs:Atom`, `mcs:Molecule`, `mcs:Organism`

```html
<!-- Atom: Indivisible UI element -->
<button 
    typeof="mcs:Component"
    property="mcs:taxonomyLevel" content="mcs:Atom">
    Click Me
</button>

<!-- Molecule: Group of atoms -->
<div 
    typeof="mcs:Component"
    property="mcs:taxonomyLevel" content="mcs:Molecule">
    <!-- Contains multiple atoms -->
</div>

<!-- Organism: Complex UI section -->
<nav 
    typeof="mcs:Component"
    property="mcs:taxonomyLevel" content="mcs:Organism">
    <!-- Contains molecules and atoms -->
</nav>
```

#### `mcs:hasPart`
**Purpose**: Defines compositional relationships  
**Type**: Resource reference  
**Required**: For Molecules and Organisms  
**Usage**: Links parent components to their children

```html
<div 
    typeof="mcs:Component"
    property="mcs:taxonomyLevel" content="mcs:Molecule"
    id="search-form">
    
    <!-- Declare compositional relationships -->
    <div property="mcs:hasPart" resource="#search-input"></div>
    <div property="mcs:hasPart" resource="#search-button"></div>
    
    <!-- Actual component parts -->
    <input 
        id="search-input"
        typeof="mcs:Component"
        property="mcs:taxonomyLevel" content="mcs:Atom"
        class="c-input">
    
    <button 
        id="search-button"
        typeof="mcs:Component"
        property="mcs:taxonomyLevel" content="mcs:Atom"
        class="c-button">
        Search
    </button>
</div>
```

#### `mcs:part`
**Purpose**: Identifies component sub-elements  
**Type**: String  
**Usage**: Labels significant parts within a component

```html
<div class="c-card" typeof="mcs:Component">
    <header property="mcs:part" content="Header" class="c-card__header">
        <h2 property="mcs:part" content="Title" class="c-card__title">Card Title</h2>
    </header>
    <div property="mcs:part" content="Body" class="c-card__body">
        <p property="mcs:part" content="Description">Card description text.</p>
    </div>
</div>
```

#### `mcs:version`
**Purpose**: Component version tracking  
**Type**: Semantic version string (e.g., "1.2.0")  
**Usage**: For component lifecycle management

```html
<div 
    typeof="mcs:Component"
    property="mcs:version" content="2.1.0">
    <!-- Component content -->
</div>
```

#### `mcs:status`
**Purpose**: Development lifecycle indicator  
**Type**: Controlled vocabulary  
**Values**: `prototype`, `production`, `deprecated`

```html
<div 
    typeof="mcs:Component"
    property="mcs:status" content="production">
    <!-- Stable, production-ready component -->
</div>
```

#### `mcs:author`
**Purpose**: Component creator/maintainer  
**Type**: String  
**Usage**: Team attribution and responsibility tracking

```html
<div 
    typeof="mcs:Component"
    property="mcs:author" content="Design Systems Team">
    <!-- Component content -->
</div>
```

## Behavioral Attributes System

### Core Philosophy

The `data-mcs-*` attributes create a "headless UI" contract that describes component behavior independently of visual presentation or JavaScript framework. This enables:

- **Framework Agnostic**: Works with any JavaScript library
- **Automated Testing**: Clear behavioral contracts for testing tools
- **Analytics**: Semantic interaction tracking
- **AI Understanding**: Machine-readable behavior specification

### Complete Attribute Reference

#### `data-mcs-interaction-type`
**Purpose**: Categorizes the type of user interaction  
**Required**: Yes for interactive elements  
**Values**: Controlled vocabulary

| Value | Description | Use Cases |
|-------|-------------|-----------|
| `navigation` | Changes user's view or location | Links, menu items, pagination |
| `state-change` | Modifies UI component state | Toggle buttons, tabs, accordions |
| `submission` | Sends data to server | Form submits, save actions |
| `filter` | Reduces visible data set | Search filters, category filters |
| `sort` | Reorders visible data | Table headers, sort dropdowns |

```html
<!-- Navigation interaction -->
<a href="/products" 
   data-mcs-interaction-type="navigation"
   data-mcs-consequence="Navigate to products page">
   View Products
</a>

<!-- State change interaction -->
<button 
   data-mcs-interaction-type="state-change"
   data-mcs-consequence="Toggle navigation menu visibility"
   aria-expanded="false">
   Menu
</button>

<!-- Form submission -->
<button type="submit"
   data-mcs-interaction-type="submission"
   data-mcs-consequence="Create new user account">
   Sign Up
</button>
```

#### `data-mcs-consequence`
**Purpose**: Describes the primary result of interaction  
**Required**: Recommended for all interactive elements  
**Type**: Free-form descriptive text

```html
<button 
   data-mcs-interaction-type="state-change"
   data-mcs-consequence="Show additional product details in expanded card view">
   Show Details
</button>
```

#### `data-mcs-target`
**Purpose**: Identifies elements affected by the interaction  
**Type**: CSS selector  
**Usage**: Links controls to their targets

```html
<button 
   data-mcs-interaction-type="state-change"
   data-mcs-target="#sidebar-nav"
   data-mcs-consequence="Toggle sidebar navigation visibility">
   Toggle Sidebar
</button>

<nav id="sidebar-nav" class="c-sidebar">
   <!-- Navigation content -->
</nav>
```

#### `data-mcs-value`
**Purpose**: Payload data for interaction  
**Type**: String or JSON  
**Usage**: Passes data to event handlers

```html
<!-- Simple value -->
<button 
   data-mcs-interaction-type="filter"
   data-mcs-value="electronics"
   data-mcs-consequence="Filter products by electronics category">
   Electronics
</button>

<!-- Complex JSON data -->
<button 
   data-mcs-interaction-type="submission"
   data-mcs-value='{"action": "add-to-cart", "productId": "12345", "quantity": 1}'
   data-mcs-consequence="Add product to shopping cart">
   Add to Cart
</button>
```

#### `data-mcs-triggers-event`
**Purpose**: Specifies custom events dispatched on interaction  
**Type**: Event name (preferably namespaced)  
**Usage**: For cross-component communication

```html
<button 
   data-mcs-interaction-type="state-change"
   data-mcs-triggers-event="mcss:cart-updated"
   data-mcs-consequence="Update cart item quantity">
   Update Quantity
</button>
```

#### `data-mcs-controller`
**Purpose**: Identifies JavaScript controller managing the component  
**Type**: Controller name  
**Usage**: Framework integration and debugging

```html
<div 
   class="c-tabs"
   data-mcs-controller="TabsController"
   typeof="mcs:Component">
   <!-- Tabs content -->
</div>
```

## Atomic Design Taxonomy

### Classification System

MCSS uses Atomic Design methodology to organize components into a clear hierarchy:

#### Atoms (`mcs:Atom`)
**Definition**: Smallest functional units that cannot be broken down further  
**Examples**: Button, Input, Label, Icon  
**Composition Rule**: Contains no other MCSS components

```html
<button 
   class="c-button"
   typeof="mcs:Component"
   property="mcs:taxonomyLevel" content="mcs:Atom">
   <span property="mcs:purpose" content="Submit form data" class="u-hidden"></span>
   Submit
</button>
```

**Characteristics**:
- Self-contained and indivisible
- Generally stateless or simple UI state only
- No complex application logic
- Focused on single responsibility

#### Molecules (`mcs:Molecule`)
**Definition**: Groups of atoms that work together as a cohesive unit  
**Examples**: Search form, form field, navigation link with icon  
**Composition Rule**: Composed of atoms and/or other molecules

```html
<div 
   class="c-form-field"
   typeof="mcs:Component"
   property="mcs:taxonomyLevel" content="mcs:Molecule"
   id="email-field">
   
   <!-- Declare composition -->
   <div property="mcs:hasPart" resource="#email-label"></div>
   <div property="mcs:hasPart" resource="#email-input"></div>
   <div property="mcs:hasPart" resource="#email-error"></div>
   
   <!-- Component parts -->
   <label 
      id="email-label"
      typeof="mcs:Component"
      property="mcs:taxonomyLevel" content="mcs:Atom"
      for="email-input-field">
      Email Address
   </label>
   
   <input 
      id="email-input"
      type="email"
      typeof="mcs:Component"
      property="mcs:taxonomyLevel" content="mcs:Atom"
      class="c-input">
   
   <div 
      id="email-error"
      class="c-form-field__error"
      role="alert">
      Please enter a valid email address
   </div>
</div>
```

**Characteristics**:
- Combines multiple atoms for specific purpose
- May manage simple self-contained state
- Reusable across different contexts
- Clear single responsibility

#### Organisms (`mcs:Organism`)
**Definition**: Complex UI sections that form distinct interface areas  
**Examples**: Site header, product card, data table, modal dialog  
**Composition Rule**: Composed of atoms, molecules, and other organisms

```html
<header 
   class="c-site-header"
   typeof="mcs:Component"
   property="mcs:taxonomyLevel" content="mcs:Organism"
   id="main-header">
   
   <span property="mcs:purpose" content="Primary site navigation and branding" class="u-hidden"></span>
   
   <!-- Declare complex composition -->
   <div property="mcs:hasPart" resource="#site-logo"></div>
   <div property="mcs:hasPart" resource="#main-navigation"></div>
   <div property="mcs:hasPart" resource="#user-menu"></div>
   
   <!-- Logo (atom) -->
   <div id="site-logo" class="c-logo" typeof="mcs:Component">
      <img src="logo.svg" alt="Company Name">
   </div>
   
   <!-- Navigation (organism) -->
   <nav 
      id="main-navigation"
      class="c-navigation"
      typeof="mcs:Component"
      property="mcs:taxonomyLevel" content="mcs:Organism">
      <!-- Navigation content -->
   </nav>
   
   <!-- User menu (molecule) -->
   <div 
      id="user-menu"
      class="c-user-menu"
      typeof="mcs:Component"
      property="mcs:taxonomyLevel" content="mcs:Molecule">
      <!-- User menu content -->
   </div>
</header>
```

**Characteristics**:
- Complex state management and orchestration
- Often requires behavioral contracts (BEHAVIOR.md)
- May contain business logic
- Represents major interface sections

### Composition Validation Rules

#### Atom Constraints
```html
<!-- ✅ VALID: Atom with no component children -->
<button 
   typeof="mcs:Component"
   property="mcs:taxonomyLevel" content="mcs:Atom">
   Button Text
</button>

<!-- ❌ INVALID: Atom cannot contain other components -->
<button 
   typeof="mcs:Component"
   property="mcs:taxonomyLevel" content="mcs:Atom">
   <span typeof="mcs:Component">Icon</span> <!-- Violation! -->
</button>
```

#### Molecule/Organism Requirements
```html
<!-- ✅ VALID: Molecule declares its composition -->
<div 
   typeof="mcs:Component"
   property="mcs:taxonomyLevel" content="mcs:Molecule">
   <div property="mcs:hasPart" resource="#child-1"></div>
   <div property="mcs:hasPart" resource="#child-2"></div>
   <!-- Child components... -->
</div>

<!-- ❌ INVALID: Molecule without mcs:hasPart declarations -->
<div 
   typeof="mcs:Component"
   property="mcs:taxonomyLevel" content="mcs:Molecule">
   <!-- Contains components but doesn't declare them -->
</div>
```

## Behavioral Contracts

### When Behavioral Contracts Are Required

Complex interactive components (primarily Organisms) that involve keyboard navigation, focus management, or sophisticated user interactions **must** include a `BEHAVIOR.md` file that specifies their behavioral contract.

### Contract Components Required

#### Keyboard Interactions
Complete specification of all keyboard behaviors:

```markdown
| Key | Context | Action |
|-----|---------|--------|
| Tab | Any element | Move focus to next focusable element |
| Shift + Tab | Any element | Move focus to previous focusable element |
| Enter | Menu item | Activate item or open submenu |
| Escape | Open submenu | Close submenu and return focus to parent |
| Arrow Down | Menu bar | Open submenu or move to next item |
| Arrow Up | Menu bar | Open submenu or move to previous item |
| Arrow Right | Menu bar | Move to next top-level menu item |
| Arrow Left | Menu bar | Move to previous top-level menu item |
| Home | Any menu | Move focus to first menu item |
| End | Any menu | Move focus to last menu item |
```

#### Focus Management Rules
Explicit focus handling specifications:

- **Focus Entry**: How focus enters the component
- **Focus Trapping**: When and how focus is contained
- **Focus Restoration**: Where focus returns when component closes
- **Initial Focus**: Which element receives focus on activation

#### ARIA State Management
Mapping between component states and ARIA attributes:

```markdown
| Component State | ARIA Attributes | Example |
|----------------|-----------------|---------|
| Menu closed | aria-expanded="false" | `<button aria-expanded="false">Menu</button>` |
| Menu open | aria-expanded="true" | `<button aria-expanded="true">Menu</button>` |
| Item selected | aria-current="true" | `<a aria-current="true">Current Page</a>` |
| Item disabled | aria-disabled="true" | `<button aria-disabled="true">Disabled</button>` |
```

### Example Behavioral Contract

For a tabbed interface component:

```markdown
# Tabs Component Behavioral Contract

## Component: c-tabs
## APG Pattern: https://www.w3.org/WAI/ARIA/apg/patterns/tabs/

### Keyboard Interactions

| Key | Context | Action |
|-----|---------|---------|
| Tab | Tab panel | Move focus to next focusable element in tab panel |
| Shift + Tab | Tab panel | Move focus to previous focusable element |
| Right Arrow | Tab list | Move focus to next tab, wrapping to first |
| Left Arrow | Tab list | Move focus to previous tab, wrapping to last |
| Home | Tab list | Move focus to first tab |
| End | Tab list | Move focus to last tab |
| Space/Enter | Tab | Activate focused tab |

### Focus Management

- **Initial Focus**: First tab in tab list
- **Tab Activation**: Automatic on focus change
- **Panel Focus**: Tab key moves into active panel
- **Focus Restoration**: Return to previously focused tab when re-entering component

### ARIA State Management

- Tab elements: `role="tab"`, `aria-selected`, `aria-controls`
- Tab list: `role="tablist"`, `aria-label`
- Tab panels: `role="tabpanel"`, `aria-labelledby`
```

## Validation and Quality Assurance

### Static Linting Rules

The MCSS framework includes ESLint rules for automated validation:

#### Required Annotations
- `mcss/component-type-required`: Elements with `c-*` classes must have `typeof="mcs:Component"`
- `mcss/purpose-required`: All components must include `mcs:purpose` property
- `mcss/taxonomy-level-required`: All components must declare `mcs:taxonomyLevel`

#### Semantic Validation
- `mcss/invalid-taxonomy-value`: Validates taxonomy level values
- `mcss/dangling-has-part-reference`: Checks `mcs:hasPart` references resolve
- `mcss/behavioral-attribute-on-interactive-only`: Ensures behavioral attributes only on interactive elements

#### Documentation Requirements
- `mcss/missing-consequence`: Interactive elements should have `data-mcs-consequence`
- `mcss/missing-behavioral-contract`: Complex organisms should have `BEHAVIOR.md` files

### Semantic Graph Validation

Advanced validation using SPARQL queries against the generated RDF graph:

```sparql
# Validate component purpose cardinality
PREFIX mcs: <http://www.example.org/mcss/v1#>
ASK WHERE {
    {
        SELECT ?component (COUNT(?purpose) AS ?count) WHERE {
            ?component a mcs:Component.
            OPTIONAL { ?component mcs:purpose ?purpose. }
        } GROUP BY ?component
    }
    FILTER(?count != 1)
}
```

### Accessibility Validation

Automated checking of accessibility compliance:

- **Color Contrast**: Verify WCAG 2.2 AA compliance for all color combinations
- **Focus Management**: Validate focus order and keyboard navigation
- **ARIA Usage**: Check correct ARIA attribute usage and relationships
- **Semantic Structure**: Verify proper heading hierarchy and landmark usage

This comprehensive annotation system ensures that MCSS components are not just visually consistent, but semantically rich and machine-readable, enabling advanced tooling, testing, and AI integration.