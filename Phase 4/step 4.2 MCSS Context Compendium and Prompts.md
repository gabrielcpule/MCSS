

# **Model Context Style Sheet (MCSS) Context Compendium and Prompting Guide**

This report presents the two key deliverables for the Model Context Style Sheet (MCSS) project: the CONTEXT\_COMPENDIUM.md knowledge base and the EXAMPLE\_PROMPTS.md usage guide. The compendium is a definitive, LLM-optimized knowledge base designed to be injected into a system prompt, enabling high-fidelity generation and analysis of MCSS components. The examples demonstrate its practical application.

---

### **CONTEXT\_COMPENDIUM.md**

# **1\. Core Philosophy: The Semantic Imperative**

The Model Context Style Sheet (MCSS) framework is governed by the **Semantic Imperative**: to transform HTML documents from human-readable displays into a structured, machine-readable knowledge graph.

The primary goal is to describe UI components as "things, not strings".1 Standard HTML relies on weak signals like class names, forcing a processing model to infer meaning. MCSS rejects this ambiguity. By embedding explicit, structured metadata directly into the markup using RDFa, the framework enables a model to understand a component's identity, composition, hierarchy, and purpose without inference.2 The HTML is no longer just for presentation; it is a serialized node in a queryable knowledge graph, where the

mcs:v1 vocabulary is the definitive source of truth.3

# **2\. The 5-Layer Architecture**

MCSS employs a 5-layer architecture to manage CSS cascade precedence and prevent specificity conflicts. This architecture maps directly to CSS Cascade Layers (@layer), where layer order always takes precedence over selector specificity.5 Styles in a higher layer will always override styles in a lower layer for the same property, regardless of selector complexity.

The layer order, from lowest to highest priority, is as follows:

1. **Global:** This layer contains foundational styles. It includes CSS resets, normalizations, and the global design token definitions (e.g., tokens.css).  
2. **Layout:** This layer contains layout-specific rules, identified by the l- prefix. These classes (l-grid, l-stack, etc.) are responsible for arranging components on the page.7  
3. **Component:** This layer contains the default styling for all reusable components, identified by the c- prefix. These are the core building blocks of the UI (c-button, c-card, etc.).7  
4. **Utility:** This layer contains high-specificity, single-purpose helper classes, identified by the u- prefix. These classes (u-text-center, u-margin-0, etc.) are used to override component or layout styles for specific instances.7  
5. **Exception:** This layer is reserved for temporary overrides, debugging styles, and third-party code that must take highest precedence.

# **3\. The Ontological Naming Convention (ONC)**

All CSS class names MUST follow the Ontological Naming Convention (ONC). The ONC provides a strict grammar that acts as a "type system" for CSS, allowing a model to instantly classify a class and understand its role within the 5-Layer Architecture.

The mandatory structure is \[prefix\]-.

### **Prefixes**

The prefix identifies the class's architectural layer and purpose 7:

* c-: **Component**. A self-contained, reusable UI pattern (e.g., c-button, c-card). Belongs to the **Component** layer.  
* l-: **Layout**. A rule that controls the positioning and spacing of components (e.g., l-grid, l-stack). Belongs to the **Layout** layer.  
* u-: **Utility**. A high-specificity helper class that applies a single, immutable style rule (e.g., u-text-align-center). Belongs to the **Utility** layer.

### **BEM Syntax**

The BEM (Block, Element, Modifier) syntax provides relational context within a component 8:

* **Block:** The root name of the component (e.g., c-card).  
* **\_\_Element:** A double underscore separates a descendant Element from its Block (e.g., c-card\_\_title). An Element is a constituent part of the Block and has no meaning on its own.  
* **\--Modifier:** A double hyphen separates a Modifier from its Block or Element (e.g., c-card--featured, c-card\_\_title--large). A Modifier represents a specific variant or state.

# **4\. The Full Annotation Schema**

The Annotation Schema is the vocabulary for the knowledge graph. It is divided into three orthogonal categories: semantic identity (mcs:v1), behavior (data-mcs-\*), and hierarchy (mcs:taxonomyLevel). This separation of concerns is mandatory.

### **The mcs:v1 RDFa Vocabulary**

These RDFa properties define the semantic identity and metadata of a component. The vocabulary URI is https://gabrielcpule.github.io/mcss-vocab/api/mcss/v1.rdf. All components MUST be declared with vocab="https://gabrielcpule.github.io/mcss-vocab/api/mcss/v1.rdf" and typeof="mcs:Component" on their root element.3

| Property | Description | Expected Value Type | Example Usage |
| :---- | :---- | :---- | :---- |
| mcs:componentName | The official, human-readable name of the component. | string | \<... property="mcs:componentName" content="Button"\> |
| mcs:version | The semantic version number of the component. | string (e.g., "1.0.0") | \<... property="mcs:version" content="1.2.1"\> |
| mcs:status | The development lifecycle status of the component. | string ('prototype', 'production', 'deprecated') | \<... property="mcs:status" content="production"\> |
| mcs:taxonomyLevel | The component's classification in the Atomic Design hierarchy. | string (See table below) | \<... property="mcs:taxonomyLevel" content="atom"\> |
| mcs:description | A brief explanation of the component's purpose and function. | string | \<... property="mcs:description" content="Used for primary user actions."\> |
| mcs:part | Identifies a constituent part or element within a component. | string | \<span property="mcs:part" content="Icon" class="c-button\_\_icon"\>\</span\> |
| mcs:author | The name or team responsible for the component. | string | \<... property="mcs:author" content="Design Systems Team"\> |

### **The data-mcs-\* Behavioral Attributes**

These data-\* attributes provide stable, framework-agnostic hooks for JavaScript-driven interactivity. They MUST be used for all dynamic behaviors, separating them from presentational class names.10

| Attribute | Purpose | Value Convention | Example Usage |
| :---- | :---- | :---- | :---- |
| data-mcs-action | Declares the action a user can trigger on an element. | string (e.g., 'toggle', 'open-modal', 'submit-form') | \<button data-mcs-action="toggle"\>Toggle\</button\> |
| data-mcs-target | A CSS selector pointing to the element(s) affected by an action. | string (CSS selector) | \<button... data-mcs-target="\#nav-menu"\> |
| data-mcs-value | A payload of data to be passed to the JavaScript handler. | string or JSON string | \<button... data-mcs-value='{"itemId": 123}'\> |
| data-mcs-controller | Identifies an element as the root of a component managed by a specific JS controller. | string (Controller name) | \<div data-mcs-controller="Tabs"\>...\</div\> |

### **The Atomic Design Taxonomy (mcs:taxonomyLevel)**

This taxonomy classifies components based on their complexity and composition, following the Atomic Design methodology. It governs how components can be composed.12

| Taxonomy Level | Definition | Composition Rule |
| :---- | :---- | :---- |
| atom | The smallest functional unit; an indivisible building block (e.g., Button, Input, Label). | Cannot be broken down further. Contains no other components. |
| molecule | A group of atoms bonded together to form a simple, reusable component (e.g., a search form composed of a label, input, and button). | Composed of atoms. Cannot contain organisms. |
| organism | A complex UI component composed of atoms, molecules, and/or other organisms that forms a distinct section of an interface (e.g., Header, Card, Data Grid). | Composed of atoms and molecules. Can be composed of other organisms. |

# **5\. Core Architectural Mandates**

The following rules are unbreakable system-wide mandates that ensure predictability, reusability, and maintainability.

* **The "Golden Rule" of Component Isolation:** Components (classes with a c- prefix) MUST NOT declare margin on their root element. External spacing is the sole responsibility of a parent layout container (an l- class) or a custom parent element. This ensures components are fully encapsulated and can be placed in any layout context without causing unexpected spacing issues.13  
* **State Management via data-state Attributes:** All component states (e.g., 'active', 'disabled', 'open', 'error', 'loading') MUST be managed via a data-state attribute on the relevant HTML element. CSS MUST use attribute selectors (e.g., .c-button\[data-state="loading"\]) to apply state-specific styles. This provides a single, predictable mechanism for state management, replacing ambiguous state-based class names like .is-active or .button-error.14

# **6\. Consuming Design Tokens**

All CSS property values that correspond to a defined value in the design system (e.g., colors, spacing units, font sizes, border radii) MUST be consumed from the global tokens.css file via CSS Custom Properties. Hard-coding "magic numbers" or hex codes is strictly forbidden. This decouples component styles from the theme, making the system maintainable and themeable.17css

/\* CORRECT: Values are semantic and sourced from tokens. \*/  
.c-alert {  
background-color: var(--color-background-critical-subtle);  
border: var(--border-width-thin) solid var(--color-border-critical);  
padding: var(--spacing-squish-medium);  
border-radius: var(--border-radius-medium);  
font-family: var(--font-family-body);  
}  
/\* INCORRECT: Values are hard-coded and non-semantic. \*/  
.c-alert {  
background-color: \#FEE2E2;  
border: 1px solid \#DC2626;  
padding: 8px 16px;  
border-radius: 6px;  
font-family: "Inter", sans-serif;  
}

\# 7\. The Behavioral Contract Pattern

For complex, interactive components, particularly those classified as \`organism\` (e.g., modals, dropdowns, tab systems), the full specification of behavior cannot be captured in attributes alone. For these components, a \`BEHAVIOR.md\` file is REQUIRED in the component's directory.

This file serves as a \*\*behavioral contract\*\* for the component's JavaScript implementation. It MUST detail all required behaviors, with the(https://www.w3.org/WAI/ARIA/apg/) serving as the normative source of truth.\[18\]

The \`BEHAVIOR.md\` file MUST specify:  
\- \*\*Keyboard Interactions:\*\* A complete list of required key presses and their resulting actions (e.g., "Pressing \`Escape\` while the modal is open must close the modal.").  
\- \*\*Focus Management:\*\* Explicit rules for how focus is handled (e.g., "When the modal opens, focus must be moved to the first focusable element inside it. Focus must be trapped within the modal.").  
\- \*\*ARIA Attribute Management:\*\* A mapping of component states to required ARIA attributes (e.g., "The trigger element must have \`aria-expanded\` set to \`true\` when the dropdown is open and \`false\` when it is closed.").

This pattern transforms the task from "build an accessible modal" to "implement this precise behavioral specification," ensuring compliance and testability.

---

### **EXAMPLE\_PROMPTS.md**

# **MCSS Prompting Examples**

This file contains three examples demonstrating how to use the CONTEXT\_COMPENDIUM.md to guide an LLM for component generation, modification, and analysis tasks. In a real application, the content of CONTEXT\_COMPENDIUM.md would be injected into the \`\` prompt.

---

## **Example 1: New Component Generation**

This prompt asks the model to generate a new, simple "Badge" component from scratch, ensuring it adheres to all MCSS rules.

# **1\. Core Philosophy: The Semantic Imperative**

The Model Context Style Sheet (MCSS) framework is governed by the **Semantic Imperative**: to transform HTML documents from human-readable displays into a structured, machine-readable knowledge graph.

The primary goal is to describe UI components as "things, not strings".1 Standard HTML relies on weak signals like class names, forcing a processing model to infer meaning. MCSS rejects this ambiguity. By embedding explicit, structured metadata directly into the markup using RDFa, the framework enables a model to understand a component's identity, composition, hierarchy, and purpose without inference.2 The HTML is no longer just for presentation; it is a serialized node in a queryable knowledge graph, where the

mcs:v1 vocabulary is the definitive source of truth.3

# **2\. The 5-Layer Architecture**

MCSS employs a 5-layer architecture to manage CSS cascade precedence and prevent specificity conflicts. This architecture maps directly to CSS Cascade Layers (@layer), where layer order always takes precedence over selector specificity.5 Styles in a higher layer will always override styles in a lower layer for the same property, regardless of selector complexity.

The layer order, from lowest to highest priority, is as follows:

1. **Global:** This layer contains foundational styles. It includes CSS resets, normalizations, and the global design token definitions (e.g., tokens.css).  
2. **Layout:** This layer contains layout-specific rules, identified by the l- prefix. These classes (l-grid, l-stack, etc.) are responsible for arranging components on the page.7  
3. **Component:** This layer contains the default styling for all reusable components, identified by the c- prefix. These are the core building blocks of the UI (c-button, c-card, etc.).7  
4. **Utility:** This layer contains high-specificity, single-purpose helper classes, identified by the u- prefix. These classes (u-text-center, u-margin-0, etc.) are used to override component or layout styles for specific instances.7  
5. **Exception:** This layer is reserved for temporary overrides, debugging styles, and third-party code that must take highest precedence.

# **3\. The Ontological Naming Convention (ONC)**

All CSS class names MUST follow the Ontological Naming Convention (ONC). The ONC provides a strict grammar that acts as a "type system" for CSS, allowing a model to instantly classify a class and understand its role within the 5-Layer Architecture.

The mandatory structure is \[prefix\]-.

### **Prefixes**

The prefix identifies the class's architectural layer and purpose 7:

* c-: **Component**. A self-contained, reusable UI pattern (e.g., c-button, c-card). Belongs to the **Component** layer.  
* l-: **Layout**. A rule that controls the positioning and spacing of components (e.g., l-grid, l-stack). Belongs to the **Layout** layer.  
* u-: **Utility**. A high-specificity helper class that applies a single, immutable style rule (e.g., u-text-align-center). Belongs to the **Utility** layer.

### **BEM Syntax**

The BEM (Block, Element, Modifier) syntax provides relational context within a component 8:

* **Block:** The root name of the component (e.g., c-card).  
* **\_\_Element:** A double underscore separates a descendant Element from its Block (e.g., c-card\_\_title). An Element is a constituent part of the Block and has no meaning on its own.  
* **\--Modifier:** A double hyphen separates a Modifier from its Block or Element (e.g., c-card--featured, c-card\_\_title--large). A Modifier represents a specific variant or state.

# **4\. The Full Annotation Schema**

The Annotation Schema is the vocabulary for the knowledge graph. It is divided into three orthogonal categories: semantic identity (mcs:v1), behavior (data-mcs-\*), and hierarchy (mcs:taxonomyLevel). This separation of concerns is mandatory.

### **The mcs:v1 RDFa Vocabulary**

These RDFa properties define the semantic identity and metadata of a component. The vocabulary URI is https://gabrielcpule.github.io/mcss-vocab/api/mcss/v1.rdf. All components MUST be declared with vocab="https://gabrielcpule.github.io/mcss-vocab/api/mcss/v1.rdf" and typeof="mcs:Component" on their root element.3

| Property | Description | Expected Value Type | Example Usage |
| :---- | :---- | :---- | :---- |
| mcs:componentName | The official, human-readable name of the component. | string | \<... property="mcs:componentName" content="Button"\> |
| mcs:version | The semantic version number of the component. | string (e.g., "1.0.0") | \<... property="mcs:version" content="1.2.1"\> |
| mcs:status | The development lifecycle status of the component. | string ('prototype', 'production', 'deprecated') | \<... property="mcs:status" content="production"\> |
| mcs:taxonomyLevel | The component's classification in the Atomic Design hierarchy. | string (See table below) | \<... property="mcs:taxonomyLevel" content="atom"\> |
| mcs:description | A brief explanation of the component's purpose and function. | string | \<... property="mcs:description" content="Used for primary user actions."\> |
| mcs:part | Identifies a constituent part or element within a component. | string | \<span property="mcs:part" content="Icon" class="c-button\_\_icon"\>\</span\> |
| mcs:author | The name or team responsible for the component. | string | \<... property="mcs:author" content="Design Systems Team"\> |

### **The data-mcs-\* Behavioral Attributes**

These data-\* attributes provide stable, framework-agnostic hooks for JavaScript-driven interactivity. They MUST be used for all dynamic behaviors, separating them from presentational class names.10

| Attribute | Purpose | Value Convention | Example Usage |
| :---- | :---- | :---- | :---- |
| data-mcs-action | Declares the action a user can trigger on an element. | string (e.g., 'toggle', 'open-modal', 'submit-form') | \<button data-mcs-action="toggle"\>Toggle\</button\> |
| data-mcs-target | A CSS selector pointing to the element(s) affected by an action. | string (CSS selector) | \<button... data-mcs-target="\#nav-menu"\> |
| data-mcs-value | A payload of data to be passed to the JavaScript handler. | string or JSON string | \<button... data-mcs-value='{"itemId": 123}'\> |
| data-mcs-controller | Identifies an element as the root of a component managed by a specific JS controller. | string (Controller name) | \<div data-mcs-controller="Tabs"\>...\</div\> |

### **The Atomic Design Taxonomy (mcs:taxonomyLevel)**

This taxonomy classifies components based on their complexity and composition, following the Atomic Design methodology. It governs how components can be composed.12

| Taxonomy Level | Definition | Composition Rule |
| :---- | :---- | :---- |
| atom | The smallest functional unit; an indivisible building block (e.g., Button, Input, Label). | Cannot be broken down further. Contains no other components. |
| molecule | A group of atoms bonded together to form a simple, reusable component (e.g., a search form composed of a label, input, and button). | Composed of atoms. Cannot contain organisms. |
| organism | A complex UI component composed of atoms, molecules, and/or other organisms that forms a distinct section of an interface (e.g., Header, Card, Data Grid). | Composed of atoms and molecules. Can be composed of other organisms. |

# **5\. Core Architectural Mandates**

The following rules are unbreakable system-wide mandates that ensure predictability, reusability, and maintainability.

* **The "Golden Rule" of Component Isolation:** Components (classes with a c- prefix) MUST NOT declare margin on their root element. External spacing is the sole responsibility of a parent layout container (an l- class) or a custom parent element. This ensures components are fully encapsulated and can be placed in any layout context without causing unexpected spacing issues.13  
* **State Management via data-state Attributes:** All component states (e.g., 'active', 'disabled', 'open', 'error', 'loading') MUST be managed via a data-state attribute on the relevant HTML element. CSS MUST use attribute selectors (e.g., .c-button\[data-state="loading"\]) to apply state-specific styles. This provides a single, predictable mechanism for state management, replacing ambiguous state-based class names like .is-active or .button-error.14

# **6\. Consuming Design Tokens**

All CSS property values that correspond to a defined value in the design system (e.g., colors, spacing units, font sizes, border radii) MUST be consumed from the global tokens.css file via CSS Custom Properties. Hard-coding "magic numbers" or hex codes is strictly forbidden. This decouples component styles from the theme, making the system maintainable and themeable.17

CSS

/\* CORRECT: Values are semantic and sourced from tokens. \*/  
.c-alert {  
  background-color: var(--color-background-critical-subtle);  
  border: var(--border-width-thin) solid var(--color-border-critical);  
  padding: var(--spacing-squish-medium);  
  border-radius: var(--border-radius-medium);  
  font-family: var(--font-family-body);  
}

/\* INCORRECT: Values are hard-coded and non-semantic. \*/  
.c-alert {  
  background-color: \#FEE2E2;  
  border: 1px solid \#DC2626;  
  padding: 8px 16px;  
  border-radius: 6px;  
  font-family: "Inter", sans-serif;  
}

# **7\. The Behavioral Contract Pattern**

For complex, interactive components, particularly those classified as organism (e.g., modals, dropdowns, tab systems), the full specification of behavior cannot be captured in attributes alone. For these components, a BEHAVIOR.md file is REQUIRED in the component's directory.

This file serves as a **behavioral contract** for the component's JavaScript implementation. It MUST detail all required behaviors, with the([https://www.w3.org/WAI/ARIA/apg/](https://www.w3.org/WAI/ARIA/apg/)) serving as the normative source of truth.18

The BEHAVIOR.md file MUST specify:

* **Keyboard Interactions:** A complete list of required key presses and their resulting actions (e.g., "Pressing Escape while the modal is open must close the modal.").  
* **Focus Management:** Explicit rules for how focus is handled (e.g., "When the modal opens, focus must be moved to the first focusable element inside it. Focus must be trapped within the modal.").  
* **ARIA Attribute Management:** A mapping of component states to required ARIA attributes (e.g., "The trigger element must have aria-expanded set to true when the dropdown is open and false when it is closed.").

This pattern transforms the task from "build an accessible modal" to "implement this precise behavioral specification," ensuring compliance and testability.

TASK: Generate a new MCSS component.

COMPONENT DETAILS:

* Name: Badge  
* Version: 1.0.0  
* Status: prototype  
* Taxonomy Level: atom  
* Description: A small, inline element used to display a count or a status.  
* States: A default state and a 'critical' state for attracting attention.

DELIVERABLES:

1. Fully annotated HTML for the c-badge component.  
2. CSS for the c-badge component, including the 'critical' state style. Place the CSS in a single code block.

\---

\#\# Example 2: Component Modification

This prompt asks the model to add a new \`error\` state to an existing \`c-input\` component. This tests the model's ability to perform a surgical modification according to the \`data-state\` mandate.

# **1\. Core Philosophy: The Semantic Imperative**

The Model Context Style Sheet (MCSS) framework is governed by the **Semantic Imperative**: to transform HTML documents from human-readable displays into a structured, machine-readable knowledge graph.

The primary goal is to describe UI components as "things, not strings".1 Standard HTML relies on weak signals like class names, forcing a processing model to infer meaning. MCSS rejects this ambiguity. By embedding explicit, structured metadata directly into the markup using RDFa, the framework enables a model to understand a component's identity, composition, hierarchy, and purpose without inference.2 The HTML is no longer just for presentation; it is a serialized node in a queryable knowledge graph, where the

mcs:v1 vocabulary is the definitive source of truth.3

# **2\. The 5-Layer Architecture**

MCSS employs a 5-layer architecture to manage CSS cascade precedence and prevent specificity conflicts. This architecture maps directly to CSS Cascade Layers (@layer), where layer order always takes precedence over selector specificity.5 Styles in a higher layer will always override styles in a lower layer for the same property, regardless of selector complexity.

The layer order, from lowest to highest priority, is as follows:

1. **Global:** This layer contains foundational styles. It includes CSS resets, normalizations, and the global design token definitions (e.g., tokens.css).  
2. **Layout:** This layer contains layout-specific rules, identified by the l- prefix. These classes (l-grid, l-stack, etc.) are responsible for arranging components on the page.7  
3. **Component:** This layer contains the default styling for all reusable components, identified by the c- prefix. These are the core building blocks of the UI (c-button, c-card, etc.).7  
4. **Utility:** This layer contains high-specificity, single-purpose helper classes, identified by the u- prefix. These classes (u-text-center, u-margin-0, etc.) are used to override component or layout styles for specific instances.7  
5. **Exception:** This layer is reserved for temporary overrides, debugging styles, and third-party code that must take highest precedence.

# **3\. The Ontological Naming Convention (ONC)**

All CSS class names MUST follow the Ontological Naming Convention (ONC). The ONC provides a strict grammar that acts as a "type system" for CSS, allowing a model to instantly classify a class and understand its role within the 5-Layer Architecture.

The mandatory structure is \[prefix\]-.

### **Prefixes**

The prefix identifies the class's architectural layer and purpose 7:

* c-: **Component**. A self-contained, reusable UI pattern (e.g., c-button, c-card). Belongs to the **Component** layer.  
* l-: **Layout**. A rule that controls the positioning and spacing of components (e.g., l-grid, l-stack). Belongs to the **Layout** layer.  
* u-: **Utility**. A high-specificity helper class that applies a single, immutable style rule (e.g., u-text-align-center). Belongs to the **Utility** layer.

### **BEM Syntax**

The BEM (Block, Element, Modifier) syntax provides relational context within a component 8:

* **Block:** The root name of the component (e.g., c-card).  
* **\_\_Element:** A double underscore separates a descendant Element from its Block (e.g., c-card\_\_title). An Element is a constituent part of the Block and has no meaning on its own.  
* **\--Modifier:** A double hyphen separates a Modifier from its Block or Element (e.g., c-card--featured, c-card\_\_title--large). A Modifier represents a specific variant or state.

# **4\. The Full Annotation Schema**

The Annotation Schema is the vocabulary for the knowledge graph. It is divided into three orthogonal categories: semantic identity (mcs:v1), behavior (data-mcs-\*), and hierarchy (mcs:taxonomyLevel). This separation of concerns is mandatory.

### **The mcs:v1 RDFa Vocabulary**

These RDFa properties define the semantic identity and metadata of a component. The vocabulary URI is https://gabrielcpule.github.io/mcss-vocab/api/mcss/v1.rdf. All components MUST be declared with vocab="https://gabrielcpule.github.io/mcss-vocab/api/mcss/v1.rdf" and typeof="mcs:Component" on their root element.3

| Property | Description | Expected Value Type | Example Usage |
| :---- | :---- | :---- | :---- |
| mcs:componentName | The official, human-readable name of the component. | string | \<... property="mcs:componentName" content="Button"\> |
| mcs:version | The semantic version number of the component. | string (e.g., "1.0.0") | \<... property="mcs:version" content="1.2.1"\> |
| mcs:status | The development lifecycle status of the component. | string ('prototype', 'production', 'deprecated') | \<... property="mcs:status" content="production"\> |
| mcs:taxonomyLevel | The component's classification in the Atomic Design hierarchy. | string (See table below) | \<... property="mcs:taxonomyLevel" content="atom"\> |
| mcs:description | A brief explanation of the component's purpose and function. | string | \<... property="mcs:description" content="Used for primary user actions."\> |
| mcs:part | Identifies a constituent part or element within a component. | string | \<span property="mcs:part" content="Icon" class="c-button\_\_icon"\>\</span\> |
| mcs:author | The name or team responsible for the component. | string | \<... property="mcs:author" content="Design Systems Team"\> |

### **The data-mcs-\* Behavioral Attributes**

These data-\* attributes provide stable, framework-agnostic hooks for JavaScript-driven interactivity. They MUST be used for all dynamic behaviors, separating them from presentational class names.10

| Attribute | Purpose | Value Convention | Example Usage |
| :---- | :---- | :---- | :---- |
| data-mcs-action | Declares the action a user can trigger on an element. | string (e.g., 'toggle', 'open-modal', 'submit-form') | \<button data-mcs-action="toggle"\>Toggle\</button\> |
| data-mcs-target | A CSS selector pointing to the element(s) affected by an action. | string (CSS selector) | \<button... data-mcs-target="\#nav-menu"\> |
| data-mcs-value | A payload of data to be passed to the JavaScript handler. | string or JSON string | \<button... data-mcs-value='{"itemId": 123}'\> |
| data-mcs-controller | Identifies an element as the root of a component managed by a specific JS controller. | string (Controller name) | \<div data-mcs-controller="Tabs"\>...\</div\> |

### **The Atomic Design Taxonomy (mcs:taxonomyLevel)**

This taxonomy classifies components based on their complexity and composition, following the Atomic Design methodology. It governs how components can be composed.12

| Taxonomy Level | Definition | Composition Rule |
| :---- | :---- | :---- |
| atom | The smallest functional unit; an indivisible building block (e.g., Button, Input, Label). | Cannot be broken down further. Contains no other components. |
| molecule | A group of atoms bonded together to form a simple, reusable component (e.g., a search form composed of a label, input, and button). | Composed of atoms. Cannot contain organisms. |
| organism | A complex UI component composed of atoms, molecules, and/or other organisms that forms a distinct section of an interface (e.g., Header, Card, Data Grid). | Composed of atoms and molecules. Can be composed of other organisms. |

# **5\. Core Architectural Mandates**

The following rules are unbreakable system-wide mandates that ensure predictability, reusability, and maintainability.

* **The "Golden Rule" of Component Isolation:** Components (classes with a c- prefix) MUST NOT declare margin on their root element. External spacing is the sole responsibility of a parent layout container (an l- class) or a custom parent element. This ensures components are fully encapsulated and can be placed in any layout context without causing unexpected spacing issues.13  
* **State Management via data-state Attributes:** All component states (e.g., 'active', 'disabled', 'open', 'error', 'loading') MUST be managed via a data-state attribute on the relevant HTML element. CSS MUST use attribute selectors (e.g., .c-button\[data-state="loading"\]) to apply state-specific styles. This provides a single, predictable mechanism for state management, replacing ambiguous state-based class names like .is-active or .button-error.14

# **6\. Consuming Design Tokens**

All CSS property values that correspond to a defined value in the design system (e.g., colors, spacing units, font sizes, border radii) MUST be consumed from the global tokens.css file via CSS Custom Properties. Hard-coding "magic numbers" or hex codes is strictly forbidden. This decouples component styles from the theme, making the system maintainable and themeable.17

CSS

/\* CORRECT: Values are semantic and sourced from tokens. \*/  
.c-alert {  
  background-color: var(--color-background-critical-subtle);  
  border: var(--border-width-thin) solid var(--color-border-critical);  
  padding: var(--spacing-squish-medium);  
  border-radius: var(--border-radius-medium);  
  font-family: var(--font-family-body);  
}

/\* INCORRECT: Values are hard-coded and non-semantic. \*/  
.c-alert {  
  background-color: \#FEE2E2;  
  border: 1px solid \#DC2626;  
  padding: 8px 16px;  
  border-radius: 6px;  
  font-family: "Inter", sans-serif;  
}

# **7\. The Behavioral Contract Pattern**

For complex, interactive components, particularly those classified as organism (e.g., modals, dropdowns, tab systems), the full specification of behavior cannot be captured in attributes alone. For these components, a BEHAVIOR.md file is REQUIRED in the component's directory.

This file serves as a **behavioral contract** for the component's JavaScript implementation. It MUST detail all required behaviors, with the([https://www.w3.org/WAI/ARIA/apg/](https://www.w3.org/WAI/ARIA/apg/)) serving as the normative source of truth.18

The BEHAVIOR.md file MUST specify:

* **Keyboard Interactions:** A complete list of required key presses and their resulting actions (e.g., "Pressing Escape while the modal is open must close the modal.").  
* **Focus Management:** Explicit rules for how focus is handled (e.g., "When the modal opens, focus must be moved to the first focusable element inside it. Focus must be trapped within the modal.").  
* **ARIA Attribute Management:** A mapping of component states to required ARIA attributes (e.g., "The trigger element must have aria-expanded set to true when the dropdown is open and false when it is closed.").

This pattern transforms the task from "build an accessible modal" to "implement this precise behavioral specification," ensuring compliance and testability.

TASK: Modify an existing MCSS component.

EXISTING COMPONENT HTML:

HTML

\<div vocab\="https://gabrielcpule.github.io/mcss-vocab/api/mcss/v1.rdf" typeof\="mcs:Component" class\="c-input" data-state\="default"\>  
  \<label property\="mcs:part" content\="Label" for\="input-id" class\="c-input\_\_label"\>Email Address\</label\>  
  \<input property\="mcs:part" content\="Control" type\="email" id\="input-id" class\="c-input\_\_control"\>  
\</div\>

EXISTING COMPONENT CSS:

CSS

.c-input\_\_control {  
  border: var(--border-width-thin) solid var(--color-border-default);  
  border-radius: var(--border-radius-medium);  
  padding: var(--spacing-squish-small);  
}

MODIFICATION REQUEST:

* Add a new 'error' state to the c-input component.  
* When the c-input element's data-state attribute is set to "error", its child element c-input\_\_control should have a border color that uses the color-border-critical design token.  
* Provide only the *new* CSS required for this change. Do not repeat existing CSS.

\---

\#\# Example 3: Component Explanation

This prompt asks the model to function as a knowledge graph query engine, analyzing a component's annotations to explain its purpose and behavior.

# **1\. Core Philosophy: The Semantic Imperative**

The Model Context Style Sheet (MCSS) framework is governed by the **Semantic Imperative**: to transform HTML documents from human-readable displays into a structured, machine-readable knowledge graph.

The primary goal is to describe UI components as "things, not strings".1 Standard HTML relies on weak signals like class names, forcing a processing model to infer meaning. MCSS rejects this ambiguity. By embedding explicit, structured metadata directly into the markup using RDFa, the framework enables a model to understand a component's identity, composition, hierarchy, and purpose without inference.2 The HTML is no longer just for presentation; it is a serialized node in a queryable knowledge graph, where the

mcs:v1 vocabulary is the definitive source of truth.3

# **2\. The 5-Layer Architecture**

MCSS employs a 5-layer architecture to manage CSS cascade precedence and prevent specificity conflicts. This architecture maps directly to CSS Cascade Layers (@layer), where layer order always takes precedence over selector specificity.5 Styles in a higher layer will always override styles in a lower layer for the same property, regardless of selector complexity.

The layer order, from lowest to highest priority, is as follows:

1. **Global:** This layer contains foundational styles. It includes CSS resets, normalizations, and the global design token definitions (e.g., tokens.css).  
2. **Layout:** This layer contains layout-specific rules, identified by the l- prefix. These classes (l-grid, l-stack, etc.) are responsible for arranging components on the page.7  
3. **Component:** This layer contains the default styling for all reusable components, identified by the c- prefix. These are the core building blocks of the UI (c-button, c-card, etc.).7  
4. **Utility:** This layer contains high-specificity, single-purpose helper classes, identified by the u- prefix. These classes (u-text-center, u-margin-0, etc.) are used to override component or layout styles for specific instances.7  
5. **Exception:** This layer is reserved for temporary overrides, debugging styles, and third-party code that must take highest precedence.

# **3\. The Ontological Naming Convention (ONC)**

All CSS class names MUST follow the Ontological Naming Convention (ONC). The ONC provides a strict grammar that acts as a "type system" for CSS, allowing a model to instantly classify a class and understand its role within the 5-Layer Architecture.

The mandatory structure is \[prefix\]-.

### **Prefixes**

The prefix identifies the class's architectural layer and purpose 7:

* c-: **Component**. A self-contained, reusable UI pattern (e.g., c-button, c-card). Belongs to the **Component** layer.  
* l-: **Layout**. A rule that controls the positioning and spacing of components (e.g., l-grid, l-stack). Belongs to the **Layout** layer.  
* u-: **Utility**. A high-specificity helper class that applies a single, immutable style rule (e.g., u-text-align-center). Belongs to the **Utility** layer.

### **BEM Syntax**

The BEM (Block, Element, Modifier) syntax provides relational context within a component 8:

* **Block:** The root name of the component (e.g., c-card).  
* **\_\_Element:** A double underscore separates a descendant Element from its Block (e.g., c-card\_\_title). An Element is a constituent part of the Block and has no meaning on its own.  
* **\--Modifier:** A double hyphen separates a Modifier from its Block or Element (e.g., c-card--featured, c-card\_\_title--large). A Modifier represents a specific variant or state.

# **4\. The Full Annotation Schema**

The Annotation Schema is the vocabulary for the knowledge graph. It is divided into three orthogonal categories: semantic identity (mcs:v1), behavior (data-mcs-\*), and hierarchy (mcs:taxonomyLevel). This separation of concerns is mandatory.

### **The mcs:v1 RDFa Vocabulary**

These RDFa properties define the semantic identity and metadata of a component. The vocabulary URI is https://gabrielcpule.github.io/mcss-vocab/api/mcss/v1.rdf. All components MUST be declared with vocab="https://gabrielcpule.github.io/mcss-vocab/api/mcss/v1.rdf" and typeof="mcs:Component" on their root element.3

| Property | Description | Expected Value Type | Example Usage |
| :---- | :---- | :---- | :---- |
| mcs:componentName | The official, human-readable name of the component. | string | \<... property="mcs:componentName" content="Button"\> |
| mcs:version | The semantic version number of the component. | string (e.g., "1.0.0") | \<... property="mcs:version" content="1.2.1"\> |
| mcs:status | The development lifecycle status of the component. | string ('prototype', 'production', 'deprecated') | \<... property="mcs:status" content="production"\> |
| mcs:taxonomyLevel | The component's classification in the Atomic Design hierarchy. | string (See table below) | \<... property="mcs:taxonomyLevel" content="atom"\> |
| mcs:description | A brief explanation of the component's purpose and function. | string | \<... property="mcs:description" content="Used for primary user actions."\> |
| mcs:part | Identifies a constituent part or element within a component. | string | \<span property="mcs:part" content="Icon" class="c-button\_\_icon"\>\</span\> |
| mcs:author | The name or team responsible for the component. | string | \<... property="mcs:author" content="Design Systems Team"\> |

### **The data-mcs-\* Behavioral Attributes**

These data-\* attributes provide stable, framework-agnostic hooks for JavaScript-driven interactivity. They MUST be used for all dynamic behaviors, separating them from presentational class names.10

| Attribute | Purpose | Value Convention | Example Usage |
| :---- | :---- | :---- | :---- |
| data-mcs-action | Declares the action a user can trigger on an element. | string (e.g., 'toggle', 'open-modal', 'submit-form') | \<button data-mcs-action="toggle"\>Toggle\</button\> |
| data-mcs-target | A CSS selector pointing to the element(s) affected by an action. | string (CSS selector) | \<button... data-mcs-target="\#nav-menu"\> |
| data-mcs-value | A payload of data to be passed to the JavaScript handler. | string or JSON string | \<button... data-mcs-value='{"itemId": 123}'\> |
| data-mcs-controller | Identifies an element as the root of a component managed by a specific JS controller. | string (Controller name) | \<div data-mcs-controller="Tabs"\>...\</div\> |

### **The Atomic Design Taxonomy (mcs:taxonomyLevel)**

This taxonomy classifies components based on their complexity and composition, following the Atomic Design methodology. It governs how components can be composed.12

| Taxonomy Level | Definition | Composition Rule |
| :---- | :---- | :---- |
| atom | The smallest functional unit; an indivisible building block (e.g., Button, Input, Label). | Cannot be broken down further. Contains no other components. |
| molecule | A group of atoms bonded together to form a simple, reusable component (e.g., a search form composed of a label, input, and button). | Composed of atoms. Cannot contain organisms. |
| organism | A complex UI component composed of atoms, molecules, and/or other organisms that forms a distinct section of an interface (e.g., Header, Card, Data Grid). | Composed of atoms and molecules. Can be composed of other organisms. |

# **5\. Core Architectural Mandates**

The following rules are unbreakable system-wide mandates that ensure predictability, reusability, and maintainability.

* **The "Golden Rule" of Component Isolation:** Components (classes with a c- prefix) MUST NOT declare margin on their root element. External spacing is the sole responsibility of a parent layout container (an l- class) or a custom parent element. This ensures components are fully encapsulated and can be placed in any layout context without causing unexpected spacing issues.13  
* **State Management via data-state Attributes:** All component states (e.g., 'active', 'disabled', 'open', 'error', 'loading') MUST be managed via a data-state attribute on the relevant HTML element. CSS MUST use attribute selectors (e.g., .c-button\[data-state="loading"\]) to apply state-specific styles. This provides a single, predictable mechanism for state management, replacing ambiguous state-based class names like .is-active or .button-error.14

# **6\. Consuming Design Tokens**

All CSS property values that correspond to a defined value in the design system (e.g., colors, spacing units, font sizes, border radii) MUST be consumed from the global tokens.css file via CSS Custom Properties. Hard-coding "magic numbers" or hex codes is strictly forbidden. This decouples component styles from the theme, making the system maintainable and themeable.17

CSS

/\* CORRECT: Values are semantic and sourced from tokens. \*/  
.c-alert {  
  background-color: var(--color-background-critical-subtle);  
  border: var(--border-width-thin) solid var(--color-border-critical);  
  padding: var(--spacing-squish-medium);  
  border-radius: var(--border-radius-medium);  
  font-family: var(--font-family-body);  
}

/\* INCORRECT: Values are hard-coded and non-semantic. \*/  
.c-alert {  
  background-color: \#FEE2E2;  
  border: 1px solid \#DC2626;  
  padding: 8px 16px;  
  border-radius: 6px;  
  font-family: "Inter", sans-serif;  
}

# **7\. The Behavioral Contract Pattern**

For complex, interactive components, particularly those classified as organism (e.g., modals, dropdowns, tab systems), the full specification of behavior cannot be captured in attributes alone. For these components, a BEHAVIOR.md file is REQUIRED in the component's directory.

This file serves as a **behavioral contract** for the component's JavaScript implementation. It MUST detail all required behaviors, with the([https://www.w3.org/WAI/ARIA/apg/](https://www.w3.org/WAI/ARIA/apg/)) serving as the normative source of truth.18

The BEHAVIOR.md file MUST specify:

* **Keyboard Interactions:** A complete list of required key presses and their resulting actions (e.g., "Pressing Escape while the modal is open must close the modal.").  
* **Focus Management:** Explicit rules for how focus is handled (e.g., "When the modal opens, focus must be moved to the first focusable element inside it. Focus must be trapped within the modal.").  
* **ARIA Attribute Management:** A mapping of component states to required ARIA attributes (e.g., "The trigger element must have aria-expanded set to true when the dropdown is open and false when it is closed.").

This pattern transforms the task from "build an accessible modal" to "implement this precise behavioral specification," ensuring compliance and testability.

TASK: Analyze the provided HTML and explain the component based *only* on its MCSS annotations.

COMPONENT HTML:

HTML

\<div vocab\="https://gabrielcpule.github.io/mcss-vocab/api/mcss/v1.rdf" typeof\="mcs:Component" class\="c-card"  
     property\="mcs:componentName" content\="ProfileCard"  
     property\="mcs:version" content\="1.2.0"  
     property\="mcs:status" content\="production"  
     property\="mcs:taxonomyLevel" content\="organism"  
     property\="mcs:description" content\="Displays a user's profile information."\>  
  \<img property\="mcs:part" content\="Avatar" class\="c-card\_\_avatar" src\="..." /\>  
  \<div class\="c-card\_\_body"\>  
    \<h3 property\="mcs:part" content\="Title" class\="c-card\_\_title"\>User Name\</h3\>  
    \<p property\="mcs:part" content\="Description" class\="c-card\_\_description"\>User bio goes here.\</p\>  
  \</div\>  
  \<button class\="c-button" data-mcs-action\="show-details" data-mcs-target\="\#details-modal"\>View Details\</button\>  
\</div\>

REQUEST:  
Provide a structured summary of this component covering the following points:

1. Its official name, version, and status.  
2. Its classification in the design system hierarchy.  
3. Its purpose.  
4. A list of its constituent parts.  
5. A description of its interactive behavior.

#### **Referências citadas**

1. What is a semantic knowledge graph? \- SciBite, acessado em julho 4, 2025, [https://scibite.com/knowledge-hub/news/what-is-a-semantic-knowledge-graph/](https://scibite.com/knowledge-hub/news/what-is-a-semantic-knowledge-graph/)  
2. RDFa \- Wikipedia, acessado em julho 4, 2025, [https://en.wikipedia.org/wiki/RDFa](https://en.wikipedia.org/wiki/RDFa)  
3. RDFa 1.1 Primer \- Third Edition \- W3C, acessado em julho 4, 2025, [https://www.w3.org/TR/rdfa-primer/](https://www.w3.org/TR/rdfa-primer/)  
4. Semantic Technologies (Knowledge Graphs and All That), acessado em julho 4, 2025, [https://titan.dcs.bbk.ac.uk/\~michael/sw15/sw15.html](https://titan.dcs.bbk.ac.uk/~michael/sw15/sw15.html)  
5. Cascade layers \- Learn web development | MDN, acessado em julho 4, 2025, [https://developer.mozilla.org/en-US/docs/Learn\_web\_development/Core/Styling\_basics/Cascade\_layers](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Cascade_layers)  
6. Cascade Layers Guide \- CSS-Tricks, acessado em julho 4, 2025, [https://css-tricks.com/css-cascade-layers/](https://css-tricks.com/css-cascade-layers/)  
7. CSS \- VA.gov Design System, acessado em julho 4, 2025, [https://design.va.gov/about/naming-conventions/css](https://design.va.gov/about/naming-conventions/css)  
8. BEM 101 \- CSS-Tricks, acessado em julho 4, 2025, [https://css-tricks.com/bem-101/](https://css-tricks.com/bem-101/)  
9. BEM: 4 Hang-Ups & How It Will Help Your CSS Organization \- Sparkbox, acessado em julho 4, 2025, [https://sparkbox.com/foundry/bem\_css\_organization](https://sparkbox.com/foundry/bem_css_organization)  
10. Using data attributes \- Learn web development | MDN, acessado em julho 4, 2025, [https://developer.mozilla.org/en-US/docs/Learn\_web\_development/Howto/Solve\_HTML\_problems/Use\_data\_attributes](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Solve_HTML_problems/Use_data_attributes)  
11. Understanding a Data Attribute Like a Pro Web Developer \- Designerly, acessado em julho 4, 2025, [https://designerly.com/data-attribute/](https://designerly.com/data-attribute/)  
12. Atomic Design Methodology | Atomic Design by Brad Frost, acessado em julho 4, 2025, [https://atomicdesign.bradfrost.com/chapter-2/](https://atomicdesign.bradfrost.com/chapter-2/)  
13. No Outer margin | Kyle Shevlin, acessado em julho 4, 2025, [https://kyleshevlin.com/no-outer-margin/](https://kyleshevlin.com/no-outer-margin/)  
14. CSS HTML Data Attributes \- DEV Community, acessado em julho 4, 2025, [https://dev.to/alserembani/css-html-data-attributes-43h5](https://dev.to/alserembani/css-html-data-attributes-43h5)  
15. Styling \- Bits UI, acessado em julho 4, 2025, [https://www.bits-ui.com/docs/styling](https://www.bits-ui.com/docs/styling)  
16. Use data attributes \- HTML | MDN, acessado em julho 4, 2025, [https://developer.mozilla.org/en-US/docs/Web/HTML/How\_to/Use\_data\_attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/How_to/Use_data_attributes)  
17. Using CSS Custom Properties \- Atlassian Developer, acessado em julho 4, 2025, [https://developer.atlassian.com/cloud/trello/power-ups/color-theme-compliance/using-css-custom-properties/](https://developer.atlassian.com/cloud/trello/power-ups/color-theme-compliance/using-css-custom-properties/)  
18. UI Blocks Documentation \- Tailwind Plus, acessado em julho 4, 2025, [https://tailwindcss.com/plus/ui-blocks/documentation](https://tailwindcss.com/plus/ui-blocks/documentation)