# Semantic Component Architecture (SCA): A Requirements Specification for LLM-Optimized User Interfaces

## Section I: The Semantic Imperative in AI-Driven Development

The integration of Large Language Models (LLMs) into software development workflows represents a paradigm shift, moving from manual coding to AI-augmented and, ultimately, AI-driven creation. While the potential for accelerated development is immense, the practical realization of this potential is contingent upon a fundamental re-evaluation of how front-end code is architected. Current methodologies, optimized for human developer ergonomics, often create significant cognitive friction for AI systems, hindering their accuracy and reliability. This specification introduces the Semantic Component Architecture (SCA), a novel CSS framework designed from the ground up to be natively comprehensible to both human developers and LLMs. Its core mission is to establish a shared language of intent, structure, and behavior, thereby enabling a new class of highly accurate, maintainable, and accessible AI-driven user interfaces.

### 1.1 Analysis of Cognitive Friction Between LLMs and Contemporary CSS

The promise of LLMs in coding—from code assistants to autonomous agents generating entire projects—is rapidly advancing.1 Early benchmarks for code generation accuracy have become saturated, with models achieving near-perfect scores on isolated algorithmic tasks, such as 99.4% on HumanEval Pass@1.1 However, this proficiency masks a critical weakness. When confronted with the complexity of real-world web development projects that involve modern CSS frameworks, LLM performance plummets. On the Web-Bench benchmark, which simulates genuine development workflows involving web standards and frameworks, the state-of-the-art Claude 3.7 Sonnet model achieves only a 25.1% Pass@1 rate.1 This dramatic drop reveals a significant gap between algorithmic code generation and true architectural comprehension.

A primary source of this friction lies in the design of popular utility-first CSS frameworks like Tailwind CSS. While celebrated for improving developer experience by co-locating styling within HTML markup, this approach presents several challenges for LLMs.3 The proliferation of utility classes leads to verbose and "bloated" HTML, which increases the token count for LLM prompts, consequently impacting response time and cost.3 Furthermore, the framework-specific syntax, full of abbreviations like

`items-center` for `align-items: center`, introduces a steep learning curve that applies to both humans and machines.4 Developers report that even with AI assistance, configuration and usage of such frameworks can be problematic, especially when AI models are not trained on the latest versions.7

The most profound challenge, however, is the creation of a "semantic vacuum." A utility-first approach describes _what a component looks like_, not _what it is_. An LLM processing a `<div>` with classes like `flex items-center shadow-lg p-6` is forced to reverse-engineer the component's purpose from a list of atomic styles.6 It sees a collection of visual attributes, not a "user profile card" or a "primary action button." This lack of explicit semantic identity forces the LLM into a state of pattern-matching and inference, a process highly susceptible to error, misinterpretation, and hallucination.8 When using Retrieval-Augmented Generation (RAG) systems, this problem is compounded. Raw HTML documents are excessively noisy, with research showing that over 90% of tokens can be irrelevant CSS styles and JavaScript.9 Without a clear abstraction layer that isolates and defines semantic meaning, the LLM's ability to accurately interpret and manipulate the UI is fundamentally compromised.

### 1.2 The Accessibility Deficit: How Non-Semantic Code Impedes Human and Machine Understanding

The challenges that LLMs face in understanding non-semantic codebases mirror, with striking fidelity, the long-standing issues faced by Blind and Low Vision (BLV) developers who rely on screen readers. Research into the obstacles encountered by BLV developers reveals that both they and LLMs struggle with the same fundamental problems: difficulty gaining a holistic view of the codebase, comprehending structural information, and navigating interfaces that lack clear semantic context.8 This parallel is not a coincidence; it is a direct consequence of the fact that both screen readers and LLMs are "blind" to the visual presentation of a user interface. They depend entirely on the underlying semantic structure of the code to interpret its meaning and function.

A critical principle of web accessibility is that the Document Object Model (DOM) order must be logical and sequential, as this is the order in which a screen reader will announce content, regardless of its visual position determined by CSS properties like `position` or `float`.10 When developers create a visual layout that diverges from a coherent DOM order, the experience for a screen reader user becomes confusing and disorienting. LLMs, which process code as a linear sequence of tokens, are similarly confounded by such discrepancies.

Furthermore, foundational accessibility practices mandate the use of correct semantic HTML elements (`<nav>`, `<header>`, `<button>`) and a proper heading hierarchy (`<h1>` through `<h6>`) to structure content meaningfully.11 When visual styling is the only means used to convey structure—for instance, using a

`<div>` styled to look like a button—the semantic meaning is lost to assistive technologies. Similarly, ARIA (Accessible Rich Internet Applications) attributes are essential for communicating the roles, states, and properties of dynamic UI components that cannot be expressed with native HTML alone.12 These are precisely the kinds of structural, state-based, and relational nuances that an LLM must also comprehend to manipulate a UI accurately. The use of CSS to hide content also presents a parallel:

`display: none` removes content from the accessibility tree, making it invisible to screen readers, whereas other techniques may only hide it visually.14 An AI must understand this distinction to correctly assess a component's state.

This profound overlap leads to a powerful conclusion: a codebase that is inaccessible to a screen reader is also semantically opaque to an LLM. By elevating accessibility from a compliance-driven afterthought to a core architectural tenet, we create the most direct and robust pathway to achieving high-fidelity AI comprehension. A perfectly accessible component is, by definition, semantically explicit, state-aware, and machine-readable. Therefore, designing for accessibility is not merely a non-functional requirement; it is a primary engineering strategy for building the AI-optimized systems of the future.

### 1.3 Establishing the Business Case for a Semantically-Grounded Architecture

The adoption of a semantically-grounded architecture is not merely a technical exercise; it presents a compelling business case rooted in efficiency, risk mitigation, and future-readiness. The primary objective of integrating AI into development is to enhance productivity, yet this goal is undermined when the AI's output is inconsistent or incorrect. Such failures complicate developer workflows, requiring manual verification and correction that erodes the very efficiency gains the technology was intended to provide.8 A semantically explicit architecture directly addresses this by providing LLMs with clear, unambiguous instructions, reducing the likelihood of errors and costly rework.

Beyond immediate AI performance, a well-structured and predictable CSS architecture delivers significant long-term value for human-led development. It mitigates developer "decision fatigue" by providing clear standards for naming and structure, and it prevents the accumulation of bloated, fragile codebases filled with legacy styles that teams are hesitant to modify.4 This leads to improved maintainability and faster onboarding for new developers, lowering long-term engineering costs.17

Looking at the broader data ecosystem, the concept of a universal semantic layer offers a powerful model for this approach. A semantic layer allows business logic, metrics, and data definitions to be modeled once and then delivered consistently to any consuming application, whether it be a BI tool, a custom front-end, or an AI agent.18 This ensures that all actions, whether human or AI-driven, are consistent, compliant, and aligned with core business rules. The Semantic Component Architecture (SCA) applies this same principle to the user interface. It creates a "single source of truth" for UI component identity, behavior, and intent.

The initial investment in establishing this semantic foundation yields compounding returns on investment. First, it directly improves LLM accuracy, which reduces development costs and accelerates time-to-market. Second, its inherent focus on accessibility minimizes legal risks associated with non-compliance and expands the potential user base of the product. Third, it enhances the productivity and confidence of human developers, leading to a more robust and maintainable codebase. Finally, it establishes a future-proof foundation that can be readily consumed by the next generation of autonomous AI agents, automated testing suites, and design system management tools.

## Section II: Foundational Principles of the Semantic Component Architecture (SCA)

The Semantic Component Architecture (SCA) is built upon a set of foundational principles designed to maximize clarity, maintainability, and machine-readability. It synthesizes the most effective concepts from modern CSS methodologies, creating a layered, component-based system that is both powerful and predictable. SCA is not a reinvention of CSS; rather, it is an architectural framework that embraces the language's core strengths while providing the necessary structure to manage complexity at scale.

### 2.1 Adopting a CUBE CSS-Inspired Layered Model

SCA's structure is heavily inspired by CUBE CSS, a methodology oriented towards simplicity, pragmatism, and working _with_ the browser's cascade rather than against it.20 The central tenet of CUBE CSS is that a small amount of global styling can accomplish the majority of the work, with more specific styles applied only as contextual deviations. This "progressive enhancement" approach results in less code and greater efficiency.21 SCA formalizes this philosophy into a distinct, five-layer model:

- **1. CSS (The Global Layer):** This is the foundation of the entire system. It contains global style definitions such as CSS resets, `font-face` rules, and the definition of all design tokens as CSS Custom Properties. By leveraging the cascade, these foundational styles are inherited throughout the application, ensuring consistency and efficiency.
    
- **2. Composition Layer:** This layer defines the macro-structures and page-level layouts. It consists of content-agnostic layout primitives, such as grids, stacks, and wrappers (e.g., `.l-grid`, `.l-wrapper`). These classes are responsible for the flow and rhythm of the page, acting as skeletons into which components are placed.22
    
- **3. Utility Layer:** This layer provides a limited set of low-level, single-purpose helper classes for making minor, one-off adjustments to style. Utilities (e.g., `.u-text-center`, `.u-visually-hidden`) are to be used sparingly and should never be used to compose the entire visual appearance of a component.
    
- **4. Block Layer:** This is the core component layer of the architecture. A Block is a discrete, reusable piece of UI, such as a card, button, or modal (e.g., `.c-card`, `.c-button`). This is where the majority of application-specific styling resides.
    
- **5. Exception Layer:** This layer defines variations, states, or themes for Blocks. Following the CUBE CSS approach, exceptions are implemented using `data-*` attributes (e.g., `[data-state="error"]`, `[data-variant="reversed"]`). This provides a clear, semantic hook for both CSS and JavaScript to target, cleanly separating presentational variations from the core component structure.22
    

### 2.2 The Principle of Component Isolation and Predictable Specificity 

A core objective of SCA is to ensure that components are truly modular, reusable, and predictable. This is achieved through a strict principle of component isolation, drawing inspiration from the encapsulation goals of methodologies like BEM.17 The styles for a given Block must not affect any other element outside of that Block's scope.

To enforce this, SCA mandates the following rules:

- **No Nested Selectors:** All Block styles must be scoped directly to the Block's own class or one of its Element classes. Descendant or child selectors (e.g., `.c-card.c-button`) are strictly forbidden within Block definitions. This practice keeps CSS specificity consistently low and flat, which is a key strategy for preventing the "specificity wars" that plague large-scale CSS projects.16
    
- **Context Agnosticism:** Blocks must be styled to be independent of their container. A `.c-button` must look and behave identically whether it is placed within a `.c-modal__footer` or a `.c-hero__actions` element. All layout and spacing between components must be handled by the Composition layer, not by the Blocks themselves. This separation of concerns ensures that components are highly reusable and that the system remains predictable and maintainable.23
    

### 2.3 Embracing the Cascade for Global Styling and Token Management

SCA's most significant departure from utility-first frameworks and strict BEM implementations is its deliberate embrace of the CSS cascade for global styling and design token management. While utility-first frameworks like Tailwind CSS champion the use of design tokens to enforce consistency—a highly valuable principle—SCA implements this concept through native CSS capabilities.4

In SCA, all design tokens—colors, font families, font size scales, spacing units, border radii, etc.—shall be defined as global CSS Custom Properties on the `:root` selector. For example:

CSS

```
:root {
  --sca-color-brand-primary: #005A9C;
  --sca-font-size-base: 1rem;
  --sca-spacing-unit: 8px;
}
```

These tokens are then inherited throughout the document via the cascade. All other layers of the architecture (Composition, Utility, and Block) **must** consume these variables using the `var()` function. Raw, "magic" values are forbidden outside of the global token definition file.

This approach provides several key advantages. It creates a single, canonical source of truth for the entire design system's visual language. It makes Blocks themselves significantly more lightweight, as they do not need to redefine fundamental styles, a core benefit highlighted by the CUBE CSS methodology.20 Finally, it allows for powerful theming and dynamic style changes by simply updating the values of the custom properties at a higher level of the cascade, a capability that is native to the CSS platform.

## Section III: The Ontological Naming Convention (ONC)

To bridge the semantic gap between human intent and machine comprehension, a clear, consistent, and machine-parsable naming convention is paramount. The Ontological Naming Convention (ONC) is a hybrid system that fuses the layered clarity of CUBE CSS with the explicit relational structure of BEM. This multi-scale approach provides semantic signals at both the macro (architectural layer) and micro (component structure) levels, creating a rich informational context for LLMs and human developers alike.

### 3.1 Fusing BEM and CUBE: A Hybrid Approach

Methodologies like BEM, with its `Block__Element--Modifier` syntax, excel at providing a declarative language that explicitly describes the relationships between parts of a component.16 This relational information—knowing that

`.btn__icon` is a child of `.btn`—is invaluable for an LLM tasked with understanding or modifying a component's structure. However, a pure BEM approach can lead to overly verbose class names and can be rigid when minor customizations are needed.25 Conversely, CUBE CSS offers greater flexibility and embraces the cascade but lacks a prescriptive naming convention within its Blocks.26

The ONC addresses the limitations of each by combining their strengths. An LLM requires semantic context at multiple levels of abstraction. It needs to understand the high-level role of a class—is it a layout primitive, a reusable component, or a simple utility? It also needs to understand the low-level structure within a component. The ONC provides this multi-scale semantic system by mandating a prefix that indicates the CUBE layer (`l-`, `c-`, `u-`) and then using a BEM-like syntax for component (`c-`) classes to define their internal parts. This creates a deeply layered semantic signal that is optimized for machine parsing while remaining intuitive for human developers.

### 3.2 ONC Naming Rules

The ONC is governed by a strict set of rules to ensure absolute consistency across any project implementing the SCA.

- **Prefixes for Architectural Layers:** Every CSS class name must begin with a prefix indicating its role within the CUBE architecture. This prefix is followed by a hyphen.
    
    - `l-`: Denotes a **Compositional Layout**. These are macro-level, content-agnostic containers. Example: `l-grid`, `l-stack`.
        
    - `c-`: Denotes a **Component Block**. These are the primary, reusable building blocks of the UI. Example: `c-card`, `c-modal`.
        
    - `u-`: Denotes a **Utility**. These are single-purpose helper classes used for minor, specific overrides. Example: `u-text-center`.
        
- **Component Naming (`c-` prefix):** All component classes follow a modified BEM syntax.
    
    - **Block:** The root of a component. The name must be a meaningful, hyphen-separated string that describes the component's purpose or identity. Example: `c-main-navigation`, `c-user-profile-card`.
        
    - **Element:** A descendant part of a Block that is semantically tied to it. The Element name is appended to the full Block name, separated by two underscores (`__`). It should describe the Element's role within the Block. Example: `c-card__header`, `c-main-navigation__link`.
        
    - **Modifier:** A variation in the appearance or state of a Block or an Element. The Modifier name is appended to the Block or Element name it modifies, separated by two hyphens (`--`). It should describe the nature of the variation. Example: `c-button--primary`, `c-card--featured`, `c-card__header--large`.
        
- **State Handling:** Dynamic, interactive states (e.g., `:hover`, `:focus`, `aria-current`) are handled via CSS pseudo-classes or `data-*` attributes for exceptions, not through Modifier classes. A class like `.c-button--active` is forbidden; this state should be styled using the `:active` pseudo-class or a `data-state="active"` attribute selector.
    

### 3.3 Table: The Ontological Naming Convention (ONC) Guidelines

The following table serves as the canonical reference for the Ontological Naming Convention. It provides concrete, unambiguous examples to guide developers and serve as a training corpus for LLMs, ensuring consistent and correct implementation of the naming standard.

|Construct|Syntax|Purpose|Example (Correct)|Example (Incorrect) & Rationale|
|---|---|---|---|---|
|**Layout**|`l-[layout-name]`|A macro-level, content-agnostic container that controls the flow and arrangement of its children.|`l-grid`, `l-stack`, `l-wrapper`|`grid` (Missing `l-` prefix); `l-main-content-grid` (Overly specific; layouts should be generic).|
|**Component Block**|`c-[block-name]`|A standalone, encapsulated, and reusable UI component. The name should be semantic.|`c-media-object`, `c-site-header`, `c-form-field`|`.media-object` (Missing `c-` prefix); `c-red-button` (Non-semantic, presentational name).|
|**Component Element**|`c-[block-name]__[element-name]`|A child part of a Block that has no standalone meaning. It is structurally dependent on its parent Block.|`c-media-object__image`, `c-site-header__logo`|`c-media__image` (Incomplete block name); `c-site-header.logo` (Uses descendant selector, not BEM syntax).|
|**Component Modifier**|c-[block-name]--[modifier-name]<br><br>c-[block-name]__[element-name]--[modifier-name]|A flag on a Block or Element that defines a variation in appearance or behavior.|`c-button--primary`, `c-media-object--reversed`|`c-button-primary` (Incorrect separator); `c-button c-button--primary` (Redundant base class in selector logic).|
|**Utility**|`u-[utility-name]`|A low-level, single-purpose helper class for applying a specific, immutable style rule. Used sparingly.|`u-visually-hidden`, `u-text-center`|`text-center` (Missing `u-` prefix); `u-red-text` (Presentational; should use semantic tokens).|
|**Exception (State)**|[data-state="..."]<br><br>[data-variant="..."]|A hook for CSS to style a specific state or exceptional variation of a component, managed via attributes.|`[data-state="error"]`, `[data-state="is-loading"]`|`.c-button--error` (State should not be a modifier class; use an attribute selector for dynamic states).|

## Section IV: The Annotation Layer: Embedding Intent with RDFa

While the ONC provides structural semantics, achieving deep, unambiguous comprehension requires an additional layer of metadata that explicitly describes a component's purpose, behavior, and relationships. The SCA mandates the use of an in-situ annotation layer built with RDFa (Resource Description Framework in Attributes) to serve as a high-fidelity "hint" system for LLMs and a self-documentation mechanism for human developers.

### 4.1 Rationale for In-Situ Metadata: RDFa vs. Alternatives

The web provides several technologies for embedding structured data into documents, most notably JSON-LD, Microdata, and RDFa.27 While Google recommends JSON-LD for SEO purposes, its primary advantage—separating the metadata script from the HTML markup—is a distinct disadvantage for our use case.27 An LLM processing a specific UI component needs the relevant metadata to be co-located with the element it describes. This in-situ context is crucial for accurate interpretation and manipulation.

Between the two in-situ options, Microdata and RDFa, RDFa offers superior expressiveness and power. Microdata, while simpler, makes it difficult to mix different vocabularies and does not natively support advanced concepts like reverse properties, which are useful for describing complex relationships.29

RDFa, in contrast, is a formal W3C Recommendation designed as a core part of the Semantic Web initiative.30 It allows for the creation of rich, complex, and interoperable metadata by embedding RDF triples directly into HTML attributes. This capability allows us to transform a standard HTML document into a machine-readable knowledge graph.

This makes RDFa the ideal technology for SCA's annotation layer. It directly fulfills the dual requirements of creating self-documenting code and providing an explicit LLM hint system. By annotating a component with a property like `sca:purpose="Primary user authentication form"`, the code immediately becomes more transparent. An LLM can be prompted to "Read the RDFa annotations to understand this component's function," using the embedded metadata as a ground truth to guide its reasoning. This directly supports advanced human-AI interaction patterns like "Explainability," where the AI can cite the RDFa annotations as the source for its understanding of a component's role.32 The metadata is no longer just data; it is a machine-readable specification attached to every component in the UI.

### 4.2 Defining the SCA Namespace and Vocabulary

To ensure the uniqueness and authority of SCA's annotations, a custom RDFa vocabulary is required. This is achieved by defining a unique namespace. RDFa allows for custom vocabularies to be defined using prefixes that map to a URI.30

- **SCA Namespace Declaration:** The official prefix for the Semantic Component Architecture vocabulary shall be `sca`. This prefix will map to a canonical, versioned URI that hosts the schema definition. This declaration must be present on the `<html>` element of any document utilizing the SCA framework.
    
    Example Declaration:
    
    HTML
    
    ```
    <html lang="en" prefix="sca: http://schema.semantic-component.org/v1/">
    ```
    

### 4.3 Practical Implementation: Annotating a Component

The power of the SCA lies in the synergy between the Ontological Naming Convention (ONC) and the RDFa annotation layer. The following example demonstrates how these systems work together to describe a "Delete Confirmation" modal component, providing a rich semantic context for any system—human or machine—that processes it.

HTML

```
<div class="c-modal" typeof="sca:Modal" resource="#deleteConfirmationModal" property="sca:purpose" content="Confirms a destructive user action and warns of its consequences.">

  <h2 class="c-modal__title" property="sca:hasTitle">Confirm Deletion</h2>

  <div class="c-modal__body">
    <p>Are you sure you want to delete this item? This action cannot be undone.</p>
  </div>

  <div class="c-modal__footer">

    <button class="c-button c-button--secondary" 
            property="sca:hasAction" 
            typeof="sca:Action" 
            resource="#cancelDeleteAction"
            data-sca-interaction-type="dismisses-modal">
      Cancel
    </button>

    <button class="c-button c-button--danger"
            property="sca:hasAction"
            typeof="sca:Action"
            resource="#confirmDeleteAction"
            data-sca-interaction-type="triggers-event"
            data-sca-interaction-target="api.deleteItem"
            data-sca-consequence="Irreversible data loss. The associated item will be permanently removed from the database.">
      Delete
    </button>
  </div>
</div>
```

This annotated example transforms a simple piece of UI into a rich, self-describing document. An LLM can now parse this structure and understand not only that this is a modal with two buttons, but that its purpose is to confirm a destructive action, that one button is a "danger" action which triggers an API call (`api.deleteItem`), and that the consequence of this action is "irreversible data loss." This level of explicit detail is the key to unlocking high-accuracy AI interaction.

## Section V: The SCA Annotation Schema

This section provides the formal specification for the `sca` vocabulary. This schema is the canonical dictionary that defines the set of terms, their meanings, and their intended usage. It is the most critical artifact for enabling the LLM annotation system, transforming HTML from a simple presentation language into a structured knowledge graph that an AI can query and reason over. This approach is inspired by formal annotation systems used in complex enterprise software and game development engines.34

### 5.1 Table: Semantic Annotation Schema for UI Components (RDFa)

The following table details the core properties and types within the `sca:v1` namespace. This vocabulary provides the building blocks for describing the identity, purpose, structure, and behavior of any UI component.

| Property / Type                    | Expected Value Type | Description                                                                                                    | Usage Context                                                               | Example                                                                                                            |
| ---------------------------------- | ------------------- | -------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| **`sca:Component`**                | `typeof`            | A base type for all SCA components. Should be used as a parent class in an ontology.                           | Root element of any component Block (`c-` prefix).                          | `<div class="c-card" typeof="sca:Component sca:Card">`                                                             |
| **`sca:Action`**                   | `typeof`            | An entity representing an interactive element that initiates a process or navigation.                          | Applied to `button`, `a`, or other interactive elements.                    | `<button property="sca:hasAction" typeof="sca:Action">`                                                            |
| **`sca:purpose`**                  | String              | A human-readable description of the component's primary function within the user journey or business process.  | Root element of a Block. Use the `content` attribute.                       | `<form class="c-login-form" property="sca:purpose" content="Authenticates the user and establishes a session.">`   |
| **`sca:hasPart`**                  | URI / Resource      | A structural property linking a parent component to a child component or element.                              | Applied to a parent Block, pointing to a child Element's `resource`.        | `<div resource="#card1" property="sca:hasPart" href="#card1-header">`                                              |
| **`sca:dependency`**               | URI / Resource      | Specifies that this component's behavior or state depends on another component or data source.                 | Any component element. Value should be the `resource` ID of the dependency. | `<div property="sca:dependency" resource="#user-auth-status">`                                                     |
| **`sca:accessibilityRole`**        | String (ARIA Role)  | Explicitly states the intended ARIA role of the component, providing a hint for accessibility validation.      | Any element.                                                                | `<div class="c-tab-list" property="sca:accessibilityRole" content="tablist">`                                      |
| **`sca:accessibilityDescription`** | String              | A detailed description of the component's accessibility features or expected behavior for screen reader users. | Any component element.                                                      | `<div property="sca:accessibilityDescription" content="This chart is fully keyboard navigable using arrow keys.">` |

### 5.2 Annotating Component State, Behavior, and Interactions

To capture the dynamic nature of UI components, SCA extends the core RDFa vocabulary with a set of `data-sca-*` attributes. These attributes are designed to describe behavior, interactions, and state changes in a way that is easily parsable by both JavaScript and LLMs. While standard RDFa is excellent for describing static relationships, `data-*` attributes are the conventional and appropriate mechanism for custom, script-accessible data.22 This aligns with best practices for annotating component states (default, hover, error) and interactions (event triggers, consequences).13 Annotations are especially critical for behaviors that are not visually explicit, such as focus management or the content of error messages.38

The `data-sca-*` attributes provide a human- and machine-readable description of what _should_ happen in response to user input or application events.

- **State Change Descriptions:** `data-sca-state-on-[event]="description"`
    
    - Example: `data-sca-state-on-hover="Background color changes to --sca-color-neutral-100; a 2px border appears."`
        
- **Interaction Type:** `data-sca-interaction-type="[type]"`
    
    - Enum: `triggers-event`, `navigates`, `updates-data`, `dismisses-modal`, `reveals-content`
        
- **Interaction Target:** `data-sca-interaction-target="[target]"`
    
    - Describes the function, event name, or URL that is the target of the interaction.
        
    - Example: `data-sca-interaction-target="event:formSubmit"`, `data-sca-interaction-target="/dashboard"`
        
- **Interaction Consequence:** `data-sca-consequence="[description]"`
    
    - A plain-language description of the outcome of the interaction.
        
    - Example: `data-sca-consequence="The user's profile is updated and they are navigated to the success page."`
        

### 5.3 Table: Component State and Behavior Annotation Matrix

This matrix provides a practical, component-centric guide for applying the annotation schema to common UI states and behaviors. It serves as a template for developers and a clear learning resource for LLMs, bridging the gap between the abstract schema and concrete implementation. The example used is a standard form input field.

|State / Behavior|Annotation Attribute|Description Content (Example)|Accessibility Consideration|Example Snippet (`<input>`)|
|---|---|---|---|---|
|**Default**|`property="sca:state:default"`|"Accepts user text input for their email address. The associated label is 'Email Address'."|The `<label>` must be programmatically associated with the `<input>` using the `for` attribute.|`<input... property="sca:state:default" content="...">`|
|**Hover**|`data-sca-state-on-hover`|"The border color changes to `--sca-color-brand-primary`."|Visual change must not rely on color alone. A change in border thickness or style is recommended.|`<input... data-sca-state-on-hover="...">`|
|**Focus**|`data-sca-state-on-focus`|"A 2px solid outline using `--sca-color-focus` appears around the input."|The focus indicator must be clearly visible and have sufficient contrast against the background.|`<input... data-sca-state-on-focus="...">`|
|**Validation**|`data-sca-validation-rule`|"Input must be a valid email format (e.g., user@example.com)."|Use the `required` attribute for mandatory fields.|`<input type="email" required data-sca-validation-rule="...">`|
|**Error**|`data-sca-state-on-error`|"Border becomes 2px solid red (`--sca-color-error`). An error message appears below the input."|The error state must be conveyed programmatically using `aria-invalid="true"` and `aria-describedby` linking to the error message.|`<input... data-sca-state-on-error="..." aria-invalid="true" aria-describedby="email-error">`|
|**Disabled**|`data-sca-state-on-disabled`|"Input has a light gray background (`--sca-color-neutral-100`) and the cursor changes to 'not-allowed'."|The `disabled` attribute must be used, which removes the element from the tab order.|`<input... disabled data-sca-state-on-disabled="...">`|

## Section VI: Formal Requirements Specification

This section translates the architectural principles and schemas of the Semantic Component Architecture into a set of formal, testable requirements. These requirements will serve as the definitive guide for the implementation and validation of the framework.

### 6.1 Functional Requirements (FR)

- **FR-1 (Component Block Definition):** The system shall provide a mechanism for defining primary UI components as "Blocks" identified by a CSS class name starting with the `c-` prefix, as specified in the Ontological Naming Convention (ONC).
    
- **FR-2 (Component Element Definition):** The system shall allow for the definition of component sub-parts as "Elements," which are structurally dependent on a parent Block. Element class names must follow the `c-[block-name]__[element-name]` syntax of the ONC.
    
- **FR-3 (Component Modifier Definition):** The system shall support the definition of stylistic or behavioral variations of Blocks or Elements as "Modifiers." Modifier class names must follow the `c-[block-or-element]--[modifier-name]` syntax of the ONC.
    
- **FR-4 (Layout Primitive Definition):** The system shall provide a mechanism for defining content-agnostic layout structures, identified by a CSS class name starting with the `l-` prefix.
    
- **FR-5 (Utility Helper Definition):** The system shall provide a mechanism for defining single-purpose helper classes, identified by a CSS class name starting with the `u-` prefix.
    
- **FR-6 (Semantic Annotation - Identity and Purpose):** The system shall enable developers to embed semantic metadata describing a component's identity and purpose using the `typeof`, `resource`, and `property="sca:purpose"` RDFa attributes from the `sca` vocabulary.
    
- **FR-7 (Semantic Annotation - Structure and Dependency):** The system shall enable developers to describe a component's internal structure and external dependencies using the `sca:hasPart` and `sca:dependency` RDFa properties.
    
- **FR-8 (Behavioral Annotation - State):** The system shall enable developers to provide human- and machine-readable descriptions of component state changes using `data-sca-state-on-*` attributes.
    
- **FR-9 (Behavioral Annotation - Interaction):** The system shall enable developers to describe component interactions, targets, and consequences using the `data-sca-interaction-type`, `data-sca-interaction-target`, and `data-sca-consequence` attributes.
    
- **FR-10 (Global Tokenization):** All design tokens (e.g., colors, fonts, spacing) shall be defined as global CSS Custom Properties and consumed by all framework layers using the `var()` function.
    

### 6.2 Non-Functional Requirements (NFR)

- **NFR-1 (Performance):** The final, production-purged CSS asset for a representative reference application built with SCA shall not exceed the file size of the same application built with a baseline utility-first framework (e.g., Tailwind CSS) by more than 10%. The First Contentful Paint (FCP) and Largest Contentful Paint (LCP) metrics shall not show a regression of more than 5%.
    
- **NFR-2 (Accessibility):** All components built using the SCA framework must be perceivable, operable, understandable, and robust, achieving full compliance with the Web Content Accessibility Guidelines (WCAG) 2.2 at the AA level.13 This includes, but is not limited to, full keyboard navigability, logical focus order, sufficient color contrast, and compatibility with leading screen readers (JAWS, NVDA, VoiceOver).40
    
- **NFR-3 (Maintainability):** The architecture must be structured such that a developer with knowledge of the SCA specification can understand a component's purpose, structure, states, and variations solely by inspecting its HTML markup (class names and annotations), without reference to external documentation or the CSS source file.
    
- **NFR-4 (Self-Documentation):** The combination of ONC naming and the full suite of RDFa and `data-sca-*` annotations must provide sufficient structured information for an automated tool to parse a component's HTML and generate comprehensive, human-readable documentation detailing its properties, states, and interactions.
    
- **NFR-5 (LLM Accuracy):** A designated Large Language Model (e.g., GPT-4 Turbo, Claude 3.7 Sonnet), when prompted with the SCA specification as part of its system context, must be able to generate and correctly modify SCA-compliant components in response to natural language prompts with a minimum of 95% accuracy, as defined by the acceptance criteria in Section VII.
    
- **NFR-6 (Browser Compatibility):** All SCA features must be compatible with the latest two major versions of all evergreen browsers (Chrome, Firefox, Safari, Edge).
    
- **NFR-7 (Developer Experience):** The framework must be implementable using standard web technologies (HTML, CSS, PostCSS) without requiring a specific JavaScript framework. The learning curve for a developer familiar with CSS and BEM should not exceed 8 hours to reach proficiency.
    

## Section VII: Quality Assurance and Acceptance Criteria

This section establishes the formal protocols and measurable criteria for validating the Semantic Component Architecture. The successful fulfillment of these criteria will signify the achievement of the project's core objectives, particularly the ambitious 95% AI accuracy target.

### 7.1 Defining and Measuring the 95% AI Accuracy Target

The 95% accuracy target for LLM interaction is not a subjective measure but a quantifiable metric derived from a purpose-built benchmark suite. This approach is informed by academic practices in LLM evaluation, which rely on task-based benchmarks and Pass@1 rates.1

**Accuracy Definition:** LLM accuracy will be assessed across a weighted blend of three distinct task categories:

1. **Generation (40% weight):** Creating a new, fully compliant SCA component from a detailed natural language prompt that describes its appearance, content, and behavior.
    
2. **Modification (40% weight):** Correctly altering an existing SCA component based on a change request. This includes tasks like adding a new state, changing a style based on a design token, or modifying an interaction.
    
3. **Comprehension & Explanation (20% weight):** Accurately describing the purpose, states, interactions, and accessibility features of a given SCA component by reading its HTML markup and annotations.
    

A task is scored as a "Pass" (100% accurate) only if the LLM's output is fully compliant with the SCA specification (ONC, annotations, principles) and is functionally and visually correct without any need for manual correction. For comprehension tasks, the explanation must be complete and factually accurate based on the provided markup.

### 7.2 Protocols for LLM Comprehension and Generation Testing

The validation of NFR-5 requires a rigorous and repeatable testing protocol, mirroring methodologies used in formal AI research to assess model limitations and performance.41

**Test Protocol:**

1. **Benchmark Dataset Creation:** A benchmark suite, designated `SCA-Benchmark-v1`, will be created. It will consist of 100 prompts distributed across the three task categories (40 Generation, 40 Modification, 20 Comprehension). The prompts will cover a wide range of common UI components and complexity levels.
    
2. **Gold Standard Establishment:** For each prompt in `SCA-Benchmark-v1`, a team of senior front-end developers will create the canonical "gold standard" solution (i.e., the perfect SCA-compliant code or the definitive textual explanation).
    
3. **LLM Execution:** The 100 prompts will be executed via the API of the target LLM. The LLM will be provided with the complete SCA specification document in its system prompt or context to ensure it has access to the rules.
    
4. **Verification and Scoring:** The LLM's output for each prompt will be compared against the gold standard.
    
    - **Automated Validation:** A suite of validation scripts will perform initial checks:
        
        - An HTML linter will check for well-formed markup.
            
        - A custom linter will validate all class names against the ONC rules.
            
        - An RDFa parser will extract the semantic graph and validate it against the `sca` schema.
            
    - **Manual Review:** A human expert will perform a final review to assess functional correctness, visual fidelity (via screenshot comparison), and the semantic accuracy of explanations.
        
    - **Scoring:** Each prompt is given a binary score (Pass/Fail). The final accuracy is the weighted average of the pass rates across the three categories.
        

### 7.3 Validation of Semantic Clarity and Accessibility Compliance

- **Accessibility Audit (NFR-2):** All "gold standard" components within the `SCA-Benchmark-v1` suite, as well as any successfully generated components from the LLM tests, will undergo a formal accessibility audit. This will involve automated testing using tools like axe-core and manual testing with the latest versions of JAWS, NVDA, and VoiceOver to verify full WCAG 2.2 AA compliance.13
    
- **Semantic Validation (NFR-4):** To validate the self-documentation requirement, a script will be developed that uses an RDFa parser to consume the annotated HTML of a component and automatically generate a Markdown documentation file. The generated documentation for the benchmark components must be judged as "complete and accurate" by a human reviewer.
    

### 7.4 Considerations for Future Extensibility

The SCA is designed as an evolving standard. The `sca` vocabulary is explicitly versioned (e.g., `v1`). A formal process for proposing, reviewing, and accepting new terms into future versions of the vocabulary will be established, governed by a technical steering committee. This ensures that the framework can adapt to new UI patterns and technologies without introducing breaking changes to existing implementations.

### 7.5 Table: Measurable Acceptance Criteria and Testing Protocols

This table provides the definitive, measurable pass/fail conditions for the key requirements of the SCA project. It transforms the specification's goals into concrete tests, ensuring an objective evaluation of the final implemented framework.

|Requirement ID|Requirement Description|Acceptance Criterion|Test Method|Tooling|
|---|---|---|---|---|
|**NFR-5**|LLM must achieve 95% accuracy.|The target LLM must achieve a final weighted score of ≥ 95% on the `SCA-Benchmark-v1` test suite.|Execute the 100 prompts from `SCA-Benchmark-v1` and score outputs against the gold standard using the defined verification protocol.|`SCA-Benchmark-v1` prompt suite, Target LLM API, SCA Validation Scripts (Linter, RDFa Parser), Manual Review Checklist.|
|**NFR-2**|Components must meet WCAG 2.2 AA.|All components in the `SCA-Benchmark-v1` gold standard set must pass an accessibility audit with zero WCAG 2.2 AA violations.|Conduct automated scans with axe-core and perform manual testing with JAWS, NVDA, and VoiceOver covering keyboard navigation, focus management, and content announcement.|axe-core, JAWS, NVDA, VoiceOver, WCAG 2.2 AA Checklist.|
|**NFR-1**|Minimal performance overhead.|For the reference application, the production CSS bundle size is ≤ 110% of the baseline, and LCP/FCP regression is ≤ 5%.|Build the reference application using both SCA and the baseline framework. Measure production asset sizes and run performance tests using a tool like WebPageTest or Lighthouse.|Reference Application Code, Lighthouse, WebPageTest, Production Build Toolchain.|
|**NFR-3**|Code is understandable from markup.|A developer new to a component must be able to correctly answer 9 out of 10 questions about its structure, purpose, and states by only reading its HTML.|Conduct a "comprehension test" with 5 developers unfamiliar with the benchmark components. Present them with the HTML of 5 components and a questionnaire for each.|Component HTML from `SCA-Benchmark-v1`, Comprehension Questionnaire.|
|**NFR-4**|Framework enables self-documentation.|The auto-generated documentation for all benchmark components must be rated as "90% or more complete" by a technical writer.|Run the auto-documentation script on all `SCA-Benchmark-v1` gold standard components. A technical writer will review the output against a quality rubric.|Auto-documentation Script, RDFa Parser, Gold Standard Components, Documentation Quality Rubric.|

