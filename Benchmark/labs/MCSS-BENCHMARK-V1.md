# MCSS-BENCHMARK-V1: LLM Performance Validation Test Suite

## Overview

This benchmark suite contains 100 carefully designed prompts to validate NFR-5: achieving 90% accuracy across three task categories using the MCSS framework with the `CONTEXT_COMPENDIUM.md` as system prompt.

**Distribution:**
- Generation Tasks: 40 prompts (40% weight)
- Modification Tasks: 40 prompts (40% weight)  
- Comprehension Tasks: 20 prompts (20% weight)

## Test Suite Structure

### GENERATION TASKS (40 prompts)

#### G-001: Simple Atom Components (10 prompts)

**G-001-01: Avatar Component**
```
PROMPT: Generate a c-avatar component (mcs:Atom) that displays a user's profile image with fallback initials. Include proper RDFa annotations and support for small, medium, and large sizes via data-state.

GOLD STANDARD:
<div class="c-avatar" 
     typeof="mcs:Component" 
     property="mcs:taxonomyLevel" 
     content="mcs:Atom"
     property="mcs:purpose" 
     content="Displays user profile picture with fallback to initials">
  <img class="c-avatar__image" 
       src="/api/user/123/avatar" 
       alt="John Doe"
       property="mcs:part" 
       content="Profile Image" />
  <span class="c-avatar__fallback" 
        property="mcs:part" 
        content="Initials Fallback">JD</span>
</div>

.c-avatar {
  position: relative;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: var(--mcs-spacing-xl);
  height: var(--mcs-spacing-xl);
  border-radius: var(--mcs-border-radius-circle);
  background-color: var(--mcs-color-background-secondary);
  overflow: hidden;
}

.c-avatar__image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.c-avatar__fallback {
  position: absolute;
  font-size: var(--mcs-font-size-scale-3);
  font-weight: var(--mcs-font-weight-medium);
  color: var(--mcs-color-text-subtle);
}

.c-avatar[data-state="small"] {
  width: var(--mcs-spacing-l);
  height: var(--mcs-spacing-l);
}

.c-avatar[data-state="large"] {
  width: var(--mcs-spacing-xxl);
  height: var(--mcs-spacing-xxl);
}
```

**G-001-02: Badge Component**
```
PROMPT: Create a c-badge component (mcs:Atom) for displaying status indicators with semantic color states (success, warning, error, info).

GOLD STANDARD:
<span class="c-badge" 
      typeof="mcs:Component" 
      property="mcs:taxonomyLevel" 
      content="mcs:Atom"
      property="mcs:purpose" 
      content="Displays status or category indicators"
      data-mcs-interaction-type="visual-indicator">
  <span property="mcs:part" content="Label Text">Active</span>
</span>

.c-badge {
  display: inline-flex;
  align-items: center;
  padding: var(--mcs-spacing-scale-1) var(--mcs-spacing-scale-3);
  font-size: var(--mcs-font-size-scale-1);
  font-weight: var(--mcs-font-weight-medium);
  border-radius: var(--mcs-border-radius-small);
  background-color: var(--mcs-color-background-secondary);
  color: var(--mcs-color-text-default);
}

.c-badge[data-state="success"] {
  background-color: var(--mcs-color-background-success);
  color: var(--mcs-color-text-success);
}

.c-badge[data-state="warning"] {
  background-color: var(--mcs-color-background-warning);
  color: var(--mcs-color-text-warning);
}

.c-badge[data-state="error"] {
  background-color: var(--mcs-color-background-error);
  color: var(--mcs-color-text-error);
}
```

[Continuing with 8 more simple atom components...]

#### G-002: Molecule Components (15 prompts)

**G-002-01: Search Form Component**
```
PROMPT: Generate a c-search-form molecule component that combines a text input, search button, and optional filter dropdown. Include proper composition annotations.

GOLD STANDARD:
<form class="c-search-form" 
      typeof="mcs:Component" 
      property="mcs:taxonomyLevel" 
      content="mcs:Molecule"
      property="mcs:purpose" 
      content="Allows users to search content with optional filters"
      data-mcs-interaction-type="submission"
      data-mcs-consequence="Executes search query and displays results">
  
  <div property="mcs:hasPart" resource="#search-input">
    <label for="search-query" class="c-search-form__label">Search</label>
    <input type="search" 
           id="search-query" 
           class="c-input" 
           typeof="mcs:Component"
           property="mcs:taxonomyLevel" 
           content="mcs:Atom"
           placeholder="Enter search terms..." />
  </div>
  
  <div property="mcs:hasPart" resource="#search-actions">
    <button type="submit" 
            class="c-button c-button--emphasis-high"
            typeof="mcs:Component"
            property="mcs:taxonomyLevel" 
            content="mcs:Atom"
            data-mcs-interaction-type="click"
            data-mcs-consequence="Submits search form"
            data-mcs-triggers-event="mcss:search:submitted">
      Search
    </button>
  </div>
</form>
```

[Continuing with 14 more molecule components...]

#### G-003: Organism Components (15 prompts)

**G-003-01: Product Card Grid**
```
PROMPT: Create a c-product-grid organism that displays a grid of product cards with filtering and sorting capabilities.

GOLD STANDARD:
[Complex organism component with multiple atoms and molecules...]
```

### MODIFICATION TASKS (40 prompts)

#### M-001: State Management Modifications (15 prompts)

**M-001-01: Add Loading State to Button**
```
PROMPT: Given the c-button component from step 3.1, add a 'loading' state that shows a spinner and disables interaction.

GOLD STANDARD:
[Modified button component with loading state implementation...]
```

#### M-002: Style Token Modifications (15 prompts)

**M-002-01: Update Button Primary Color**
```
PROMPT: Modify the c-button--primary variant to use the semantic 'success' color tokens instead of the brand primary tokens.

GOLD STANDARD:
[Modified CSS using success color tokens...]
```

#### M-003: Accessibility Enhancements (10 prompts)

**M-003-01: Add ARIA Labels to Navigation**
```
PROMPT: Enhance the c-navigation component from step 3.1 with comprehensive ARIA labels and keyboard navigation support.

GOLD STANDARD:
[Enhanced navigation with full ARIA implementation...]
```

### COMPREHENSION TASKS (20 prompts)

#### C-001: Component Analysis (10 prompts)

**C-001-01: Analyze Card Component**
```
PROMPT: Given the following c-card component HTML, explain its purpose, constituent parts, and semantic annotations.

[HTML from step 3.1 c-card component]

GOLD STANDARD ANSWER:
This is a c-card component classified as an mcs:Molecule in the Atomic Design taxonomy. Its purpose is to display structured content in a contained, visually distinct container.

Constituent parts:
- c-card__header: Contains the card title and optional actions
- c-card__body: Main content area with flexible layout
- c-card__footer: Optional action area for buttons or links

The component uses RDFa annotations (typeof="mcs:Component") to declare its semantic identity and mcs:hasPart properties to define the relationship between the parent card and its constituent elements. The data-mcs-* attributes indicate this is a non-interactive container component focused on content presentation.

Accessibility features include proper heading hierarchy and semantic HTML structure that supports screen readers.
```

#### C-002: Interaction Behavior Analysis (10 prompts)

**C-002-01: Analyze Modal Interactions**
```
PROMPT: Examine the c-modal component and explain its complete interaction model including keyboard navigation and state management.

GOLD STANDARD ANSWER:
[Detailed analysis of modal behavior, ARIA states, focus management, etc.]
```

## Tailwind CSS Equivalent Components

### Tailwind Button Component
```html
<button class="inline-flex items-center justify-center px-4 py-2 text-sm font-medium text-white bg-blue-600 border border-transparent rounded-md shadow-sm hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 disabled:opacity-50 disabled:cursor-not-allowed">
  Default Action
</button>

<button class="inline-flex items-center justify-center px-4 py-2 text-sm font-medium text-white bg-blue-600 border border-transparent rounded-md shadow-sm hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 disabled:opacity-50 disabled:cursor-not-allowed bg-green-600 hover:bg-green-700 focus:ring-green-500">
  Primary Action
</button>

<button class="inline-flex items-center justify-center px-4 py-2 text-sm font-medium text-gray-400 bg-gray-100 border border-transparent rounded-md shadow-sm cursor-not-allowed" disabled>
  Disabled Action
</button>
```

### Tailwind Input Component
```html
<div class="space-y-1">
  <label for="email" class="block text-sm font-medium text-gray-700">Email Address</label>
  <input type="email" 
         id="email" 
         class="block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
         placeholder="you@example.com" 
         required />
  <div class="hidden text-sm text-red-600" id="email-error">
    Please enter a valid email address.
  </div>
</div>
```

### Tailwind Card Component
```html
<div class="bg-white overflow-hidden shadow rounded-lg">
  <div class="px-4 py-5 sm:px-6 border-b border-gray-200">
    <h3 class="text-lg leading-6 font-medium text-gray-900">Card Title</h3>
  </div>
  <div class="px-4 py-5 sm:p-6">
    <p class="text-sm text-gray-500">This is the main content area of the card. It can contain text, images, or other components.</p>
  </div>
  <div class="px-4 py-4 sm:px-6 bg-gray-50 border-t border-gray-200">
    <button class="inline-flex items-center px-3 py-2 border border-transparent text-sm leading-4 font-medium rounded-md text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500">
      Action
    </button>
  </div>
</div>
```

### Tailwind Navigation Component
```html
<nav class="bg-white border-b border-gray-200" aria-label="Main Navigation">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="flex justify-between h-16">
      <div class="flex">
        <div class="flex-shrink-0 flex items-center">
          <img class="block lg:hidden h-8 w-auto" src="/logo.svg" alt="Company" />
        </div>
        <div class="hidden sm:ml-6 sm:flex sm:space-x-8">
          <a href="/home" class="border-indigo-500 text-gray-900 inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium">Home</a>
          <div class="relative group">
            <button class="border-transparent text-gray-500 hover:border-gray-300 hover:text-gray-700 inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium" aria-expanded="false">
              Products
              <svg class="ml-2 h-5 w-5" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd" />
              </svg>
            </button>
            <div class="absolute z-10 -ml-4 mt-3 transform px-2 w-screen max-w-md sm:px-0 lg:ml-0 lg:left-1/2 lg:-translate-x-1/2 hidden group-hover:block">
              <div class="rounded-lg shadow-lg ring-1 ring-black ring-opacity-5 overflow-hidden">
                <div class="relative grid gap-6 bg-white px-5 py-6 sm:gap-8 sm:p-8">
                  <a href="/products/widgets" class="-m-3 p-3 flex items-start rounded-lg hover:bg-gray-50">
                    <span class="ml-4 text-base font-medium text-gray-900">Widgets</span>
                  </a>
                  <a href="/products/gadgets" class="-m-3 p-3 flex items-start rounded-lg hover:bg-gray-50">
                    <span class="ml-4 text-base font-medium text-gray-900">Gadgets</span>
                  </a>
                </div>
              </div>
            </div>
          </div>
          <a href="/about" class="border-transparent text-gray-500 hover:border-gray-300 hover:text-gray-700 inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium">About</a>
          <a href="/contact" class="border-transparent text-gray-500 hover:border-gray-300 hover:text-gray-700 inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium">Contact</a>
        </div>
      </div>
    </div>
  </div>
</nav>
```

## Validation Protocol

Each generated output must pass:

### Layer 1: Automated Static Linting
- HTML well-formedness validation
- ONC compliance (correct prefixes: c-, l-, u-)
- RDFa schema validation against mcs:v1 vocabulary
- CSS token consumption verification (no magic numbers)

### Layer 2: Semantic Graph Validation
- RDF triple extraction and validation
- SPARQL query validation against component integrity rules
- Accessibility compliance verification (ARIA attributes, semantic HTML)
- Component isolation verification (no external margin/positioning)

## Scoring Criteria

**Pass Criteria:**
- Automated validation: 100% pass on both layers
- Human review: Functional and visual correctness vs. gold standard
- Comprehension: Complete and accurate explanation

**Final Score Calculation:**
`(Generation_Pass_Rate * 0.4) + (Modification_Pass_Rate * 0.4) + (Comprehension_Pass_Rate * 0.2)`

**Target:** ≥ 90% weighted accuracy to validate NFR-5