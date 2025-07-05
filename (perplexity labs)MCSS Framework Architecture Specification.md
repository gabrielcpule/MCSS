<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" class="logo" width="120"/>

# MCSS Framework Architecture Specification

This document establishes the foundational architecture for the Model Context Style Sheet (MCSS) framework, designed to maximize both human developer productivity and Large Language Model comprehension [^1_1]. The architecture addresses critical gaps in current CSS methodologies, which achieve only 30% first-attempt success rates with LLMs, by implementing semantic transparency and hierarchical clarity throughout the system [^1_1].

## Executive Summary

The MCSS framework introduces a revolutionary approach to CSS architecture that bridges human intent and machine understanding through systematic semantic enhancement [^1_2][^1_3]. Unlike traditional utility-first frameworks that create semantic vacuums, MCSS prioritizes explicit component identity and purpose-driven naming conventions [^1_4][^1_5]. This architecture enables LLMs to achieve the target 80% comprehension rate while maintaining excellent developer experience and maintainability.

## 6-Layer Hierarchical Architecture

The MCSS framework employs a six-layer inverted triangle architecture that progresses from generic foundational elements to highly specific semantic annotations [^1_6][^1_7]. This structure draws inspiration from ITCSS (Inverted Triangle CSS) while incorporating semantic web principles and machine-readable documentation standards [^1_6][^1_8].

![MCSS Framework 6-Layer Architecture: An inverted triangle structure optimized for both human understanding and LLM comprehension](https://pplx-res.cloudinary.com/image/upload/v1751140863/pplx_code_interpreter/aa6796d9_xzugpf.jpg)

MCSS Framework 6-Layer Architecture: An inverted triangle structure optimized for both human understanding and LLM comprehension

### Layer 1: Foundation Layer (Design Tokens)

**Prefix**: `f-` (CSS Custom Properties)
**Purpose**: Global design tokens that establish the visual language foundation [^1_9][^1_10]
**Specificity**: Lowest (0,0,0,1)

The Foundation Layer contains all primitive design decisions as CSS Custom Properties, following the three-tiered token architecture recommended by leading design systems [^1_11][^1_9]. These tokens serve as the single source of truth for all visual styling throughout the framework:

```css
:root {
  /* Primitive Color Tokens */
  --mcs-color-blue-500: #3b82f6;
  --mcs-color-red-500: #ef4444;
  --mcs-color-gray-100: #f3f4f6;
  
  /* Primitive Spacing Tokens */
  --mcs-space-xs: 0.25rem;
  --mcs-space-sm: 0.5rem;
  --mcs-space-md: 1rem;
  --mcs-space-lg: 1.5rem;
  
  /* Primitive Typography Tokens */
  --mcs-font-size-sm: 0.875rem;
  --mcs-font-size-base: 1rem;
  --mcs-font-size-lg: 1.125rem;
  --mcs-font-weight-normal: 400;
  --mcs-font-weight-semibold: 600;
}
```


### Layer 2: Layout Layer (Compositional)

**Prefix**: `l-`
**Purpose**: Content-agnostic layout primitives and spatial arrangements [^1_7]
**Specificity**: Low (0,0,1,0)

The Layout Layer provides macro-level structural patterns that establish page rhythm and content flow [^1_7]. These classes focus purely on arrangement without imposing visual styling:

```css
.l-grid {
  display: grid;
  gap: var(--mcs-space-md);
}

.l-stack {
  display: flex;
  flex-direction: column;
  gap: var(--mcs-space-sm);
}

.l-wrapper {
  max-width: var(--mcs-layout-max-width);
  margin-inline: auto;
  padding-inline: var(--mcs-space-md);
}
```


### Layer 3: Utility Layer

**Prefix**: `u-`
**Purpose**: Single-purpose helper classes for specific adjustments [^1_7]
**Specificity**: Medium (0,0,1,0)

Utility classes provide targeted style adjustments while maintaining semantic clarity [^1_12][^1_7]. Unlike traditional utility frameworks, MCSS utilities use descriptive names that clearly communicate intent:

```css
.u-text-center { text-align: center; }
.u-visually-hidden { 
  position: absolute !important;
  width: 1px !important;
  height: 1px !important;
  overflow: hidden !important;
  clip: rect(1px, 1px, 1px, 1px) !important;
}
.u-margin-top-large { margin-top: var(--mcs-space-lg); }
```


### Layer 4: Component Layer (Blocks)

**Prefix**: `c-`
**Purpose**: Reusable UI components with explicit semantic meaning [^1_2][^1_3]
**Specificity**: Medium (0,0,1,0)

The Component Layer implements the core BEM methodology enhanced with semantic naming conventions [^1_2][^1_3]. Each component follows the `c-[component-name]__[element-name]--[modifier-name]` pattern:

```css
.c-button {
  display: inline-flex;
  align-items: center;
  padding: var(--mcs-button-padding);
  border: var(--mcs-button-border);
  border-radius: var(--mcs-button-radius);
  background: var(--mcs-button-background);
  color: var(--mcs-button-color);
  font-size: var(--mcs-button-font-size);
}

.c-button__icon {
  margin-inline-end: var(--mcs-space-xs);
}

.c-button--primary {
  --mcs-button-background: var(--mcs-color-primary);
  --mcs-button-color: var(--mcs-color-on-primary);
}
```


### Layer 5: Exception Layer (States \& Variants)

**Prefix**: `[data-*]`
**Purpose**: Dynamic states and contextual variations [^1_7]
**Specificity**: High (0,1,0,0)

The Exception Layer handles component states and variations through data attributes, providing clear hooks for both CSS and JavaScript while maintaining semantic clarity [^1_7]:

```css
.c-button[data-state="loading"] {
  pointer-events: none;
  opacity: 0.7;
}

.c-button[data-state="loading"]::after {
  content: "";
  display: inline-block;
  width: 1em;
  height: 1em;
  border: 2px solid currentColor;
  border-radius: 50%;
  border-top-color: transparent;
  animation: spin 1s linear infinite;
}

.c-card[data-variant="elevated"] {
  box-shadow: var(--mcs-shadow-large);
}

.c-modal[data-context="error"] {
  --mcs-modal-accent-color: var(--mcs-color-error);
}
```


### Layer 6: Annotation Layer (Semantic Metadata)

**Prefix**: `mcs:`
**Purpose**: RDFa annotations for machine readability and AI comprehension [^1_8][^1_13]
**Specificity**: No CSS impact (attribute-based)

The Annotation Layer provides semantic metadata through RDFa attributes, enabling LLMs to understand component purpose, relationships, and behavior [^1_8][^1_13]. This layer implements W3C standards for semantic web technologies:

```html
<button class="c-button c-button--primary"
        typeof="mcs:Action"
        property="mcs:purpose"
        content="Submits the user registration form and creates new account"
        data-mcs-interaction-type="triggers-event"
        data-mcs-interaction-target="api.user.register"
        data-mcs-consequence="User account created and welcome email sent">
  Create Account
</button>
```


## Design Token System Architecture

The MCSS design token system implements a three-tiered hierarchy that provides clear inheritance patterns and semantic relationships [^1_11][^1_9]. This approach ensures consistency while enabling flexible customization and efficient maintenance.

![MCSS Design Token Hierarchy: Three-tier architecture showing token inheritance and semantic relationships](https://pplx-res.cloudinary.com/image/upload/v1751140963/pplx_code_interpreter/c217c229_yconu5.jpg)

MCSS Design Token Hierarchy: Three-tier architecture showing token inheritance and semantic relationships

### Primitive Tokens (Tier 1)

Primitive tokens represent raw design values without contextual meaning [^1_11]. These context-agnostic tokens form the foundation of the design system:

```css
/* Color Primitives */
--mcs-color-blue-100: #dbeafe;
--mcs-color-blue-500: #3b82f6;
--mcs-color-blue-900: #1e3a8a;

/* Spacing Primitives */
--mcs-space-1: 0.25rem;  /* 4px */
--mcs-space-2: 0.5rem;   /* 8px */
--mcs-space-4: 1rem;     /* 16px */
--mcs-space-8: 2rem;     /* 32px */

/* Typography Primitives */
--mcs-font-size-12: 0.75rem;
--mcs-font-size-14: 0.875rem;
--mcs-font-size-16: 1rem;
--mcs-font-size-18: 1.125rem;
```


### Semantic Tokens (Tier 2)

Semantic tokens add contextual meaning by referencing primitive tokens with purpose-driven names [^1_11][^1_9]:

```css
/* Semantic Color Tokens */
--mcs-color-primary: var(--mcs-color-blue-500);
--mcs-color-primary-hover: var(--mcs-color-blue-600);
--mcs-color-on-primary: var(--mcs-color-white);
--mcs-color-error: var(--mcs-color-red-500);
--mcs-color-success: var(--mcs-color-green-500);

/* Semantic Spacing Tokens */
--mcs-space-component-padding: var(--mcs-space-4);
--mcs-space-section-gap: var(--mcs-space-8);
--mcs-space-inline-gap: var(--mcs-space-2);

/* Semantic Typography Tokens */
--mcs-font-size-body: var(--mcs-font-size-16);
--mcs-font-size-caption: var(--mcs-font-size-14);
--mcs-font-size-heading: var(--mcs-font-size-18);
```


### Component Tokens (Tier 3)

Component tokens provide component-specific design decisions while maintaining inheritance from semantic tokens [^1_11]:

```css
/* Button Component Tokens */
--mcs-button-padding: var(--mcs-space-component-padding);
--mcs-button-background: var(--mcs-color-primary);
--mcs-button-color: var(--mcs-color-on-primary);
--mcs-button-border-radius: var(--mcs-radius-default);
--mcs-button-font-size: var(--mcs-font-size-body);

/* Card Component Tokens */
--mcs-card-padding: var(--mcs-space-component-padding);
--mcs-card-background: var(--mcs-color-surface);
--mcs-card-border: 1px solid var(--mcs-color-border);
--mcs-card-shadow: var(--mcs-shadow-default);
```


## Component Taxonomy and Relationship Mapping

The MCSS component taxonomy organizes UI components into logical categories that reflect both functionality and semantic relationships [^1_14][^1_15]. This systematic approach enables LLMs to understand component purposes and appropriate usage contexts.

### Form Components

Form components handle user input and data collection with clear semantic roles:


| Component | Base Class | Elements | Modifiers | Purpose |
| :-- | :-- | :-- | :-- | :-- |
| Input | `c-input` | `c-input__label`, `c-input__help`, `c-input__error` | `--large`, `--small`, `--inline` | Text and data input |
| Button | `c-button` | `c-button__icon`, `c-button__text` | `--primary`, `--secondary`, `--danger` | User actions |
| Select | `c-select` | `c-select__option`, `c-select__group` | `--multiple`, `--searchable` | Option selection |
| Checkbox | `c-checkbox` | `c-checkbox__label`, `c-checkbox__description` | `--indeterminate` | Boolean input |

### Layout Components

Layout components structure content and establish visual hierarchy:


| Component | Base Class | Elements | Modifiers | Purpose |
| :-- | :-- | :-- | :-- | :-- |
| Card | `c-card` | `c-card__header`, `c-card__body`, `c-card__footer` | `--elevated`, `--outlined` | Content grouping |
| Modal | `c-modal` | `c-modal__overlay`, `c-modal__content`, `c-modal__close` | `--large`, `--fullscreen` | Overlay content |
| Navigation | `c-nav` | `c-nav__item`, `c-nav__link`, `c-nav__submenu` | `--horizontal`, `--vertical` | Site navigation |
| Tabs | `c-tabs` | `c-tabs__list`, `c-tabs__tab`, `c-tabs__panel` | `--vertical` | Content switching |

### Content Components

Content components display and organize information:


| Component | Base Class | Elements | Modifiers | Purpose |
| :-- | :-- | :-- | :-- | :-- |
| Media | `c-media` | `c-media__object`, `c-media__content` | `--reverse`, `--center` | Media with text |
| Hero | `c-hero` | `c-hero__title`, `c-hero__subtitle`, `c-hero__actions` | `--large`, `--centered` | Prominent sections |
| Alert | `c-alert` | `c-alert__icon`, `c-alert__content`, `c-alert__close` | `--error`, `--warning`, `--success` | Status messages |
| Badge | `c-badge` | `c-badge__text`, `c-badge__icon` | `--large`, `--outline` | Status indicators |

## Documentation Standards and Templates

The MCSS documentation architecture implements machine-readable standards that serve both human developers and AI systems [^1_16][^1_17]. Documentation follows structured templates that embed semantic metadata throughout.

### Component Documentation Template

Each component requires comprehensive documentation following this standardized template [^1_17][^1_18]:

```markdown
# Component Name

## Purpose
[mcs:purpose content]

## Usage Context
[When and where to use this component]

## Accessibility Features
[WCAG compliance details and screen reader support]

## API Reference
### HTML Structure
[Required markup with RDFa annotations]

### CSS Classes
[All available classes with descriptions]

### States and Variants
[Data attributes and their effects]

### Design Tokens
[Related tokens and customization options]

## Examples
[Code examples with explanations]

## Related Components
[Dependencies and relationships]
```


### RDFa Annotation Standards

All components must include comprehensive RDFa annotations using the `mcs:` vocabulary [^1_8][^1_13]:

```html
<!-- Component Identity -->
typeof="mcs:Component mcs:Button"
resource="#unique-component-id"

<!-- Purpose and Context -->
property="mcs:purpose" 
content="Clear description of component function"

<!-- Relationships -->
property="mcs:hasPart" href="#child-element-id"
property="mcs:dependency" resource="#required-component-id"

<!-- Interaction Metadata -->
data-mcs-interaction-type="[action-type]"
data-mcs-interaction-target="[target-specification]"
data-mcs-consequence="[outcome-description]"
```


### Quality Assurance Documentation

Each component documentation includes automated validation criteria [^1_19]:

- **Semantic Validation**: RDFa markup validation using W3C tools
- **Accessibility Testing**: WCAG 2.2 AA compliance verification
- **LLM Comprehension**: Automated testing for AI understanding
- **Performance Impact**: Bundle size and rendering performance metrics


## Dependency Management Strategy

The MCSS framework implements a sophisticated dependency management system that tracks component relationships and ensures architectural integrity [^1_20][^1_21].

### Dependency Types

1. **Inheritance Dependencies**: Components that extend base patterns
2. **Composition Dependencies**: Components that include other components
3. **Token Dependencies**: Components that rely on specific design tokens
4. **Layout Dependencies**: Components that require specific layout contexts

### Dependency Matrix

The framework maintains a Dependency Structure Matrix (DSM) that visualizes component relationships and identifies architectural violations [^1_20][^1_21]:

```css
/* Example: Button component dependencies */
.c-button {
  /* Token Dependencies */
  padding: var(--mcs-button-padding);          /* → Foundation Layer */
  background: var(--mcs-button-background);    /* → Foundation Layer */
  
  /* Layout Dependencies (Optional) */
  /* Can be used within: l-grid, l-stack, l-cluster */
  
  /* Composition Dependencies */
  /* Can contain: c-icon, text content */
}

/* Dependency Validation Rules */
.c-button .c-modal {          /* ❌ Invalid - architectural violation */
.c-button .c-icon {           /* ✅ Valid - allowed composition */
.l-grid .c-button {           /* ✅ Valid - layout context */
```


### Dependency Validation

Automated tools validate dependencies during development [^1_20]:

1. **Static Analysis**: CSS parsing to detect invalid nesting patterns
2. **Token Usage Tracking**: Verification that components use appropriate tokens
3. **Circular Dependency Detection**: Prevention of component dependency loops
4. **Architecture Conformance**: Enforcement of layer separation rules

## Quality Assurance Guidelines

The MCSS framework establishes comprehensive quality assurance processes that ensure both human usability and AI comprehension [^1_19].

### LLM Comprehension Testing

Automated testing validates that components achieve the 80% LLM comprehension target:

1. **Semantic Clarity Tests**: LLM interpretation of component purpose and usage
2. **Relationship Understanding**: AI comprehension of component hierarchies
3. **State Management Tests**: LLM recognition of component states and transitions
4. **Documentation Parsing**: Automated extraction of component metadata

### Performance Benchmarks

All components must meet strict performance criteria:

- **Bundle Size**: Maximum 10% increase over utility-first frameworks
- **Runtime Performance**: No measurable impact on rendering speed
- **Memory Usage**: Efficient CSS custom property utilization
- **Load Time**: Optimal critical path CSS delivery


### Accessibility Validation

Comprehensive accessibility testing ensures WCAG 2.2 AA compliance [^1_22]:

- **Automated Testing**: Integration with axe-core and similar tools
- **Manual Testing**: Screen reader compatibility verification
- **Keyboard Navigation**: Complete keyboard accessibility validation
- **Color Contrast**: Automated contrast ratio verification for all tokens


### Documentation Quality

Documentation undergoes rigorous quality assurance [^1_16][^1_17]:

- **Completeness**: All required sections and metadata present
- **Accuracy**: Technical information verified through testing
- **Machine Readability**: RDFa validation and semantic consistency
- **Human Usability**: Clear explanations and practical examples


## Implementation Roadmap

The MCSS architecture supports phased implementation that minimizes disruption while maximizing benefits:

### Phase 1: Foundation (Weeks 1-4)

- Establish design token system and CSS custom properties
- Implement core layout primitives and utility classes
- Create documentation templates and quality assurance processes


### Phase 2: Core Components (Weeks 5-12)

- Develop essential form and navigation components
- Implement RDFa annotation system and semantic metadata
- Establish dependency management and validation tools


### Phase 3: Advanced Features (Weeks 13-20)

- Complete component library with complex interactions
- Optimize LLM comprehension through iterative testing
- Finalize performance optimization and accessibility features


### Phase 4: Validation and Optimization (Weeks 21-24)

- Comprehensive testing across multiple LLM providers
- Performance benchmarking and optimization
- Documentation completion and adoption support

This architectural foundation establishes the MCSS framework as a revolutionary approach to CSS development that successfully bridges human creativity and machine understanding, enabling unprecedented levels of AI-assisted development while maintaining excellent developer experience and accessibility standards.

<div style="text-align: center">⁂</div>

[^1_1]: README.md

[^1_2]: step-1.2-v2-LLM-Optimized-System-Design-Requirements.md

[^1_3]: step-1.1-LLM-Performance-Assessment.md

[^1_4]: https://s-lib.com/en/issues/smc_2024_07_a6/

[^1_5]: https://www.scitepress.org/DigitalLibrary/Link.aspx?doi=10.5220/0010441307150725

[^1_6]: https://www.civilejournal.org/index.php/cej/article/view/944

[^1_7]: https://dl.acm.org/doi/10.1145/3643660.3643942

[^1_8]: https://ieeexplore.ieee.org/document/10305966/

[^1_9]: https://www.nature.com/articles/s41598-022-24522-w

[^1_10]: https://accscience.com/journal/JCAU/0/0/10.36922/jcau.1335

[^1_11]: https://www.arekibo.com/news/blog/2021/05/05/popular-css-methodologies-for-scaling-web-projects

[^1_12]: https://www.valoremreply.com/resources/insights/blog/2020/november/5-methodologies-for-architecting-css/

[^1_13]: https://snipcart.com/blog/organize-css-modular-architecture

[^1_14]: https://www.webfx.com/blog/web-design/css-methodologies/

[^1_15]: https://dev.to/teclearn/web-theory-part-2-the-magic-of-css-architectures-48m3

[^1_16]: https://codedamn.com/news/css/efficient-css-architectures-bem-smacss-itcss

[^1_17]: https://rangle.io/blog/developing-your-token-structure

[^1_18]: https://github.com/CosmoMyzrailGorynych/css-naming-guide

[^1_19]: https://blog.logrocket.com/bem-vs-smacss-comparing-css-methodologies/

[^1_20]: https://www.semanticscholar.org/paper/7ac4d029111d0f215a9576f73b541b652ed7ab98

[^1_21]: https://dl.acm.org/doi/10.1145/3494106.3528685

[^1_22]: https://dl.acm.org/doi/10.1145/3620666.3651352

[^1_23]: https://arxiv.org/abs/2208.02592

[^1_24]: https://arxiv.org/abs/2405.17741

[^1_25]: https://www.ewadirect.com/proceedings/ace/article/view/4671

[^1_26]: https://ieeexplore.ieee.org/document/10249563/

[^1_27]: https://arxiv.org/abs/2502.04180

[^1_28]: https://journals.sagepub.com/doi/full/10.3233/JIFS-189172

[^1_29]: https://martinfowler.com/articles/design-token-based-ui-architecture.html

[^1_30]: https://m3.material.io/foundations/design-tokens/overview

[^1_31]: https://www.contentful.com/blog/design-token-system/

[^1_32]: https://atlassian.design/foundations/design-tokens

[^1_33]: https://blog.prototypr.io/understanding-the-parts-of-a-design-system-tokens-assets-components-and-patterns-80b22c67a0a8?gi=84464a32c4fe

[^1_34]: https://other.media/itcss-the-inverted-triangle-css-the-right-way-up/

[^1_35]: https://www.somethingsblog.com/2024/10/22/mastering-cube-css-a-scalable-approach-to-web-development/

[^1_36]: https://blogs.sw.siemens.com/electronic-systems-design/2014/09/29/defining-the-perfect-taxonomy/

[^1_37]: https://ieeexplore.ieee.org/document/10986069/

[^1_38]: https://www.mdpi.com/1424-8220/20/18/5103

[^1_39]: https://ijicis.journals.ekb.eg/article_305267.html

[^1_40]: https://www.scitepress.org/DigitalLibrary/Link.aspx?doi=10.5220/0011852300003467

[^1_41]: https://www.semanticscholar.org/paper/c5e06397d64e86369dea1371361300737c49eec8

[^1_42]: http://www.sciedu.ca/journal/index.php/ijhe/article/view/15469

[^1_43]: https://www.figma.com/blog/design-systems-103-documentation-that-drives-adoption/

[^1_44]: https://www.uxpin.com/studio/blog/design-system-documentation-guide/

[^1_45]: https://backlight.dev/mastery/the-best-design-system-documentation-sites

[^1_46]: https://uxdesign.cc/design-systems-simplifying-documentation-writing-5ec240c484fe

[^1_47]: https://www.designrush.com/best-designs/print/trends/design-system-documentation

[^1_48]: https://citeseerx.ist.psu.edu/document?doi=31d4ff95152dc8e5a0cbd321dfae92b19bdf2af8\&repid=rep1\&type=pdf

[^1_49]: https://student.cs.uwaterloo.ca/~cs338/slides/13 ER to Rel.pdf

[^1_50]: https://design-encyclopedia.com/?E=458464\&I=Q

[^1_51]: https://appmaster.io/blog/documenting-software-architecture

[^1_52]: https://groups.csail.mit.edu/sdg/pubs/2005/oopsla05-dsm.pdf

[^1_53]: http://radiotec.ru/en/journal/Information-measuring_and_Control_Systems/number/2024-4/article/24500

[^1_54]: https://arxiv.org/abs/2406.18211

[^1_55]: https://biss.pensoft.net/article/35297/

[^1_56]: https://dl.acm.org/doi/10.1145/3308560.3317073

[^1_57]: https://scholarworks.iu.edu/journals/index.php/sdh/article/view/23330

[^1_58]: https://arxiv.org/abs/2501.10391

[^1_59]: https://journals.uni-lj.si/jezikinslovstvo/article/view/17271

[^1_60]: https://en.wikipedia.org/wiki/Machine-readable_document

[^1_61]: https://www.icao.int/publications/Documents/9303_p3_cons_en.pdf

[^1_62]: https://www.ibm.com/docs/en/zvm/7.2?topic=identification-guidelines-machine-readable-documentation

[^1_63]: https://www.icao.int/publications/Documents/9303_p7_cons_en.pdf

[^1_64]: https://github.com/ISO-TC211/AutomatedDocumentation

[^1_65]: https://arxiv.org/html/2411.12357v1

[^1_66]: https://ercim-news.ercim.eu/en72/special/bridging-the-clickable-and-semantic-webs-with-rdfa

[^1_67]: https://montanab.com/2025/03/accessible-design-systems-building-components-for-everyone/

[^1_68]: https://labelyourdata.com/articles/llm-architecture

[^1_69]: https://dl.acm.org/doi/10.1145/3593663.3593670

[^1_70]: https://www.semanticscholar.org/paper/1a1e8536cda05e6a3f7b037764a2f9d646bcae28

[^1_71]: https://link.springer.com/10.1007/s00500-022-07737-x

[^1_72]: https://dev.to/vyckes/css-methodology-and-architecture-3b34

[^1_73]: http://link.springer.com/10.1007/978-1-4419-5567-8_3

[^1_74]: https://spectrum.adobe.com/page/design-tokens/

[^1_75]: https://www.designsociety.org/publication/45137/Design+Decisions+in+the+Architecture+Development+of+Advanced+Systems%3A+Towards+traceable+and+sustainable+Documentation+and+Communication

[^1_76]: https://www.semanticscholar.org/paper/b4d019d93c1e17d1c8e6b797959c1563f48be04a

[^1_77]: https://www.semanticscholar.org/paper/e8e89580641200e6eef45b9fdb8c14396579b526

[^1_78]: http://link.springer.com/10.1007/978-0-387-35563-4_1

[^1_79]: https://www.semanticscholar.org/paper/d19921afd30a1eeafc745c5407c6506b26f9f2de

[^1_80]: https://www.semanticscholar.org/paper/6095f77afc93019b6dcee03f6d52dc2021d83354

[^1_81]: https://www.semanticscholar.org/paper/21c36e192703710c4b1c901b85b1831bb57921e8

[^1_82]: https://textmine.com/post/an-introduction-to-machine-readable-documents

