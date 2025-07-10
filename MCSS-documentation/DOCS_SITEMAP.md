# MCSS Documentation Website - Information Architecture

## Site Structure Overview

The MCSS documentation website is organized into six main sections, designed for progressive learning and easy reference access.

```
MCSS Documentation
├── Home / Landing Page
├── Getting Started
├── Core Concepts  
├── Annotation System
├── Design Tokens
└── Component Library
```

## Detailed Sitemap

### 1. Home / Landing Page (`index.html`)
**Purpose**: Introduction, value proposition, and quick navigation
**Content**:
- Hero section with MCSS overview
- Key benefits and features
- Quick start call-to-action
- Framework statistics (components, tokens, etc.)
- Links to main documentation sections

### 2. Getting Started (`/getting-started/`)
**Purpose**: Onboarding new developers
**Content**:
- **Installation** (`installation.html`)
  - NPM/CDN setup instructions
  - File structure overview
  - Basic project setup
- **Quick Start** (`quick-start.html`)
  - "Hello World" tutorial
  - Building your first page
  - Using tokens and components
- **Architecture Overview** (`architecture.html`)
  - High-level system overview
  - Understanding the 5 layers
  - Philosophy and benefits

### 3. Core Concepts (`/concepts/`)
**Purpose**: Deep dive into MCSS principles and architecture
**Content**:
- **The Semantic Imperative** (`semantic-imperative.html`)
  - Machine-readable HTML philosophy
  - Knowledge graph approach
- **5-Layer Architecture** (`layers.html`)
  - Global, Layout, Component, Utility, Exception layers
  - CSS cascade management
  - Layer precedence rules
- **Ontological Naming Convention** (`naming.html`)
  - Prefixes (c-, l-, u-)
  - BEM syntax integration
  - Naming patterns and examples
- **Component Isolation** (`isolation.html`)
  - The "Golden Rule" of no external margins
  - State management via data attributes
  - Encapsulation principles

### 4. Annotation System (`/annotations/`)
**Purpose**: Complete guide to semantic markup
**Content**:
- **RDFa Vocabulary** (`rdfa.html`)
  - mcs:v1 properties reference
  - Semantic identity markup
  - Machine-readable metadata
- **Behavioral Attributes** (`behavior.html`)
  - data-mcs-* attribute system
  - Interactive contracts
  - Framework-agnostic hooks
- **Atomic Design Taxonomy** (`taxonomy.html`)
  - Atom, Molecule, Organism classification
  - Composition rules
  - Hierarchy management
- **Validation Guide** (`validation.html`)
  - Linting rules
  - SPARQL validation
  - Quality assurance

### 5. Design Tokens (`/tokens/`)
**Purpose**: Complete token reference and usage guide
**Content**:
- **Token Overview** (`overview.html`)
  - Token philosophy
  - Single source of truth principle
  - Naming conventions
- **Color Tokens** (`colors.html`)
  - Color palette reference
  - Semantic color usage
  - Accessibility compliance
  - Interactive state colors
- **Typography Tokens** (`typography.html`)
  - Font families, sizes, weights
  - Line heights and spacing
  - Modular scale explanation
- **Spacing & Layout** (`spacing.html`)
  - Spacing scale system
  - Layout primitives
  - Grid system tokens
- **Effects & Transitions** (`effects.html`)
  - Shadow tokens
  - Animation timings
  - Z-index scale

### 6. Component Library (`/components/`)
**Purpose**: Interactive component showcase and documentation
**Content**:
- **Library Overview** (`index.html`)
  - Component philosophy
  - Usage guidelines
  - Contribution process
- **Atoms** (`/atoms/`)
  - **Button** (`button.html`)
  - **Input** (`input.html`)
  - **Label** (`label.html`)
  - **Icon** (`icon.html`)
- **Molecules** (`/molecules/`)
  - **Card** (`card.html`)
  - **Form Field** (`form-field.html`)
  - **Search Box** (`search-box.html`)
- **Organisms** (`/organisms/`)
  - **Navigation** (`navigation.html`)
  - **Header** (`header.html`)
  - **Modal** (`modal.html`)
  - **Data Table** (`data-table.html`)

## Content Structure Template

Each component page follows this structure:
1. **Overview** - Purpose and use cases
2. **Live Preview** - Interactive component demonstration
3. **HTML Code** - Fully annotated markup
4. **CSS Styles** - Token-driven styles
5. **Behavior Contract** - (For complex components) Keyboard interactions
6. **Accessibility Notes** - WCAG compliance details
7. **Usage Examples** - Common implementation patterns

## Navigation Design

### Primary Navigation
- Persistent header with main section links
- Breadcrumb navigation for deep pages
- Search functionality for quick access

### Secondary Navigation
- Section-specific sidebar navigation
- "On this page" table of contents
- Previous/Next page navigation

### Utility Navigation
- Theme toggle (light/dark mode)
- Version selector
- GitHub repository link
- Feedback/contribution links

## Content Strategy

### Progressive Disclosure
- Start with high-level concepts
- Provide detailed references
- Include practical examples
- Offer advanced implementation guides

### Accessibility Focus
- Screen reader friendly structure
- Keyboard navigation support
- High contrast compliance
- Clear heading hierarchy

### Developer Experience
- Copy-to-clipboard code examples
- Interactive token browser
- Live component playground
- Download/export capabilities

## Technical Implementation Notes

### Static Site Generation
- Use of semantic HTML5 structure
- Progressive enhancement approach
- Fast loading and SEO optimized

### Interactive Features
- Component preview sandboxes
- Token value browser with search/filter
- Code syntax highlighting
- Responsive design examples

### Content Management
- Markdown-based content system
- Automated component documentation generation
- Version-controlled documentation updates
- Community contribution workflow