

# **Model Context Style Sheet (MCSS) Official Documentation**

## **ANNOTATION\_REFERENCE.MD**

### **1.0 Introduction**

#### **1.1 Purpose**

This document provides the canonical technical specification for the Model Context Style Sheet (MCSS) Annotation System, Version 1 (mcs:v1). It is the single source of truth for all semantic annotations within the project's component library. Adherence to this specification is mandatory for all new and existing components to ensure consistency, machine-readability, and system integrity.

#### **1.2 Core Principle**

The fundamental goal of the MCSS system is to embed a rich, machine-readable semantic layer directly into the HTML of UI components. This layer transforms the component library from a purely presentational system into a structured, queryable knowledge graph. This transformation is the cornerstone of achieving the project's non-functional requirement (NFR-5) of enabling high-fidelity understanding and interaction by automated agents, particularly Large Language Models (LLMs), with a target accuracy of 90% or higher. The system leverages Resource Description Framework in Attributes (RDFa) to achieve this, embedding linked data within HTML without duplicating content, which is a core principle of modern semantic web practices.1

#### **1.3 Governing Sources**

This reference is a formal synthesis of the vocabulary definitions established in the project's constitutional document, **step 1.2 v3 LLM-Optimized System Design Requirements.md**, and the gold-standard implementation patterns demonstrated in **step 3.1 MCSS Component Generation Agent.md**. It serves as the definitive guide for developers, architects, and automated systems.

#### **1.4 The mcs: Namespace**

The official namespace for this vocabulary is an Internationalized Resource Identifier (IRI) that uniquely identifies all terms.

* **Namespace IRI:** http://www.example.org/mcss/v1\#

In all normative examples throughout this document, the prefix mcs: is assumed to be bound to this namespace IRI, typically declared on the \<html\> element. The principles for publishing and versioning this vocabulary are detailed in the VALIDATION\_STRATEGY.md document, drawing upon established W3C best practices for vocabulary management.3

### **2.0 The mcs:v1 RDFa Vocabulary Reference**

#### **2.1 Overview**

This section defines the core classes and properties of the mcs:v1 vocabulary. The system utilizes RDFa 1.1 to structure the data, chosen for its capacity to embed rich, linked data directly within existing HTML5 markup.2 This approach avoids the need for separate, sidecar metadata files and ensures that the semantic description is co-located with the component it describes.

The vocabulary is designed to create a data model based on subject-predicate-object triples, forming a directed graph from the HTML structure.6 Each component becomes a subject, and its characteristics and relationships are defined by predicates (properties) pointing to objects (values or other components).

#### **2.2 Decoupling Semantics from Presentation**

A core architectural pattern within MCSS is the separation of semantic metadata from visible, presentational content. For properties whose values are not intended for direct display to the user (such as mcs:purpose or mcs:taxonomyLevel), the value MUST be contained within a dedicated, non-presentational element. The recommended element is a \<span\> that is hidden from visual rendering using a utility class (e.g., u-hidden).

This pattern is deliberate and crucial for system robustness. It decouples the semantic layer from the presentation layer. If a UI designer changes the text of a button or alters the DOM structure for stylistic reasons, the underlying semantic data remains untouched and valid. This prevents UI modifications from inadvertently corrupting the knowledge graph, a common pitfall in systems where semantic data is mixed with display content. This practice aligns with the general guidance to not store content that should be accessible *only* in metadata attributes, by providing a clear distinction between what is for the machine versus what is for the human user.7

#### **2.3 mcs:v1 Vocabulary Table**

The following table provides the formal definition for every class and property in the mcs:v1 vocabulary. Each entry includes its type, a precise definition, the expected value format, and a normative HTML example demonstrating its correct usage.

| Term | Type | Definition | Expected Value | Normative HTML Example |
| :---- | :---- | :---- | :---- | :---- |
| mcs:Component | Class | The fundamental, addressable building block of the UI. Represents a self-contained entity that encapsulates presentation, behavior, and a distinct semantic purpose. | Applied to the root element of a component using the typeof attribute. | \<div class="c-button" typeof="mcs:Component"\>...\</div\> |
| mcs:purpose | Property | A human-readable, concise statement describing the primary function or goal of the component from a user's perspective. This text is intended for machine consumption to understand intent. | Plain text content. MUST be enclosed within a hidden element (e.g., \<span class="u-hidden"\>) marked with property="mcs:purpose". | \<div typeof="mcs:Component"\>...\<span property="mcs:purpose" class="u-hidden"\>To submit the user registration form.\</span\>\</div\> |
| mcs:hasPart | Property | A relationship property indicating that the subject component (a Molecule or Organism) is composed of, and contains, the object component. This property is the primary mechanism for defining the structural hierarchy of the application. | An IRI referencing the id of the child component. MUST be applied via the property="mcs:hasPart" and resource attributes. | \<div typeof="mcs:Molecule" id="user-auth"\>\<div property="mcs:hasPart" resource="\#username-field"\>\</div\>...\</div\> |
| mcs:taxonomyLevel | Property | A mandatory property that classifies a component within the Atomic Design methodology, providing context on its complexity and compositional role. | A single IRI from the controlled vocabulary: mcs:Atom, mcs:Molecule, or mcs:Organism. MUST be applied via property="mcs:taxonomyLevel" and the content attribute on a hidden \<span\>. | \<div typeof="mcs:Component"\>\<span property="mcs:taxonomyLevel" content="mcs:Atom" class="u-hidden"\>\</span\>...\</div\> |
| mcs:state | Property | Describes a specific, named state that the component can be in (e.g., "disabled", "expanded", "error"). This complements ARIA states by providing a hook for LLM understanding and custom styling. | Plain text content. Applied via property="mcs:state". The value should correspond to a defined state in the component's documentation. | \<button property="mcs:state" content="disabled" class="c-button is-disabled"\>Submit\</button\> |
| mcs:version | Property | The semantic version number of the component's definition and implementation. | A string conforming to the SemVer (Semantic Versioning) 2.0.0 specification (e.g., "1.0.0"). Applied via property="mcs:version" and the content attribute. | \<div typeof="mcs:Component" property="mcs:version" content="1.2.0"\>...\</div\> |

### **3.0 The data-mcs-\* Behavioral Attribute Reference**

#### **3.1 Overview**

While the mcs:v1 RDFa vocabulary describes a component's identity, structure, and classification, the data-mcs-\* attributes describe its *interactive contract*. These attributes, based on the standard HTML data-\* attribute mechanism 8, provide a declarative and machine-readable way to specify the intended behavior and consequences of user interactions.

This approach creates a "headless UI" contract directly within the HTML.10 It separates the component's behavioral logic from its visual presentation and underlying JavaScript implementation. An LLM can understand that "clicking this button submits the form" purely by reading these attributes, without needing to parse complex event listeners or framework-specific code. This is analogous to how headless UI libraries like Headless UI use

data-\* attributes (e.g., data-focus, data-active) to expose internal state for styling purposes 12; here, we expose the

*behavioral contract* for semantic interpretation.

#### **3.2 data-mcs-\* Attribute Table**

These attributes MUST only be applied to interactive elements, such as \<button\>, \<a\>, \<input\>, or elements with an appropriate ARIA role.

| Attribute | Purpose | Allowed Values (Controlled Vocabulary) | Normative HTML Example |
| :---- | :---- | :---- | :---- |
| data-mcs-interaction-type | Describes the high-level category of the user interaction. It specifies the *kind* of action being performed. | navigation: Changes the user's view or location (e.g., loading a new page). state-change: Modifies the state of the component or another part of the UI (e.g., toggling a panel, showing a modal). submission: Sends data to a server (e.g., submitting a form). filter: Reduces or refines a visible set of data. sort: Reorders a visible set of data. | \<button data-mcs-interaction-type="state-change" aria-expanded="false"\>Toggle Details\</button\> |
| data-mcs-consequence | A human-readable description of the primary, user-visible result of the interaction. It answers the question, "What happens when I interact with this?" | Free-form text. The description MUST be concise, written in the present tense, and clearly state the outcome. | \<a href="/home" data-mcs-interaction-type="navigation" data-mcs-consequence="Navigates to the main dashboard."\>Home\</a\> |
| data-mcs-triggers-event | (Optional) Specifies the name of a custom JavaScript event that is dispatched to the window or a parent element upon successful interaction. This provides a formal hook for cross-component communication. | A valid JavaScript custom event name, preferably namespaced (e.g., mcss:cart-updated, mcss:filter-applied). | \<button data-mcs-interaction-type="submission" data-mcs-consequence="Adds the selected item to the shopping cart." data-mcs-triggers-event="mcss:item-added"\>Add to Cart\</button\> |

### **4.0 The Atomic Design Taxonomy (mcs:taxonomyLevel)**

#### **4.1 Overview**

The mcs:taxonomyLevel property is a mandatory property for every mcs:Component instance. It classifies the component according to a strict Atomic Design hierarchy, providing crucial context about its complexity, composition, and role within the system's design. This classification is fundamental to building a coherent and navigable knowledge graph.

#### **4.2 Taxonomy Level Definitions**

While Atomic Design is a well-known methodology, its terms can be interpreted loosely. For a machine to use this information reliably, the definitions must be strict and prescriptive. The following table formalizes the project's specific interpretation of each level, defining its responsibilities regarding composition and state.

| Value | Definition | Core Responsibilities & Constraints |
| :---- | :---- | :---- |
| mcs:Atom | The smallest, indivisible functional unit of the user interface. Atoms are the fundamental building blocks of the system. Examples include a button, an input field, a label, or an icon. | Composition: MUST NOT be composed of other mcs:Components. An Atom cannot be broken down into smaller functional parts. State: Generally stateless, or may contain only trivial UI state (e.g., a hover effect). It does not manage application data. |
| mcs:Molecule | A grouping of two or more Atoms bound together to form a simple, reusable component that serves a single, discrete purpose. Examples include a search form (input \+ button), a navigation link with an icon, or an input field with its label and validation message. | Composition: MUST be composed of one or more mcs:Atoms or other mcs:Molecules. The compositional relationship MUST be defined using the mcs:hasPart property. State: May manage its own simple, self-contained state (e.g., the value of an input field). It does not typically manage complex application-wide state. |
| mcs:Organism | A complex, distinct section of an interface, composed of a group of Molecules and/or Atoms to form a relatively standalone part of the UI. Examples include a site header, a product card, a data table, or a tabbed interface. | Composition: MUST be composed of one or more mcs:Molecules and/or mcs:Atoms. Relationships MUST be defined via mcs:hasPart. State: Often manages complex state, orchestrating interactions between its constituent parts. Stateful, interactive Organisms frequently require a formal Behavioral Contract. |

### **5.0 The Behavioral Contract Specification**

#### **5.1 Overview and Mandate**

For mcs:Organism level components that are stateful and involve complex user interactions (e.g., accordions, tab panels, carousels, menubars), the HTML annotations alone are insufficient to describe the full user experience contract. An LLM cannot infer the expected keyboard navigation for a tab panel just from its structure.

Therefore, any directory containing a complex, interactive mcs:Organism **MUST** include a BEHAVIOR.md file adjacent to its primary source file. This file must contain a markdown table detailing the keyboard interactions for the component. The presence of this file is a mandatory part of the component's definition.

#### **5.2 Standardization with WAI-ARIA Authoring Practices Guide (APG)**

The keyboard interactions specified in the BEHAVIOR.md file are not arbitrary. They **MUST** adhere to the design patterns and keyboard interaction models defined in the **W3C WAI-ARIA Authoring Practices Guide (APG)**.13 The APG is the industry standard for building accessible rich internet applications and provides detailed, user-tested patterns for common widgets.15

Mandating APG compliance provides a powerful dual benefit:

1. **For Machine Understanding:** It provides a predictable, standardized set of interaction rules that an LLM can use to understand *how to operate* a complex component. The LLM does not need to guess; it can refer to a known, public standard.  
2. **For Human Accessibility:** It ensures that our components are not only semantically rich but also highly accessible to users of assistive technologies (e.g., screen readers, keyboard-only users). This aligns the project with best-in-class accessibility practices from the ground up.17

#### **5.3 Behavioral Contract Template (Example: Tab Interface)**

The following table serves as a normative template for a Behavioral Contract. This example is for a c-tabs organism and is directly derived from the APG pattern for Tabs.16 Developers creating new complex organisms MUST consult the relevant APG pattern and create a corresponding table.

Component: c-tabs  
APG Pattern:(https://www.w3.org/WAI/ARIA/apg/patterns/tabs/)

| Key(s) | Action |
| :---- | :---- |
| Tab | When focus is on a tab, moves focus to the associated tab panel. When focus is within a tab panel, it moves focus to the next focusable element inside the panel. If focus is on the last focusable element in the panel, it moves focus to the next focusable element in the page tab order. |
| Shift \+ Tab | Moves focus to the previous focusable element, following the reverse of the Tab key logic. |
| Right Arrow | When focus is on a tab, moves focus to the next tab in the tab list. If focus is on the last tab, it wraps to the first tab. Activates the newly focused tab. |
| Left Arrow | When focus is on a tab, moves focus to the previous tab in the tab list. If focus is on the first tab, it wraps to the last tab. Activates the newly focused tab. |
| Home | (Optional) When focus is on a tab, moves focus to the first tab in the tab list. Activates the newly focused tab. |
| End | (Optional) When focus is on a tab, moves focus to the last tab in the tab list. Activates the newly focused tab. |

---

## **VALIDATION\_STRATEGY.MD**

### **1.0 Introduction to the Two-Layer Validation Protocol**

#### **1.1 Purpose**

This document specifies the complete, mandatory validation strategy for the Model Context Style Sheet (MCSS) Annotation System. Its purpose is to programmatically enforce 100% compliance with the schema defined in ANNOTATION\_REFERENCE.md. The successful execution of this strategy is critical to guaranteeing the structural and semantic integrity of the project's knowledge graph, which is the foundation for achieving the 90% accuracy goal for LLM interactions (NFR-5).

#### **1.2 Strategy Overview**

A two-layer validation protocol is mandated to provide both immediate developer feedback and deep, systemic integrity checks. This layered approach ensures that errors are caught as early and efficiently as possible.

* **Layer 1: Automated Static Linting:** This layer consists of fast, automated checks integrated directly into the development environment (IDE) and pre-commit hooks. Its function is to catch common structural and syntactical errors in real-time as a developer writes code. This is the developer's first line of defense against non-compliance.18  
* **Layer 2: Semantic Graph Validation:** This layer performs deep, build-time validation. It moves beyond syntax by parsing a component's annotations into an actual RDF graph and then querying that graph for semantic and relational integrity. This is the ultimate gatekeeper of quality and MUST be integrated as a blocking step in the project's Continuous Integration (CI) pipeline.

### **2.0 Layer 1: Automated Linting with Custom Static Analysis Rules**

#### **2.1 Overview and Technology**

This layer uses a static analysis tool, or "linter," to parse the HTML source code of components and report on patterns that violate the MCSS schema. Linting is an established practice for improving code quality and enforcing standards.18

* **Recommended Technology:** **html-eslint**.20 This ESLint plugin is chosen for its ability to parse HTML into an Abstract Syntax Tree (AST) and apply rules that are context-aware, understanding the document's structure. This is superior to simple regex-based checks as it can understand element nesting, attributes, and content distinctly.22 The  
  html-eslint plugin provides a robust foundation for creating the custom rules required by the MCSS system.  
* **Implementation:** A custom ESLint plugin, to be named **eslint-plugin-mcss**, MUST be developed to house the rules specified below. This plugin MUST be configured as a mandatory part of the project's core ESLint configuration and integrated into a pre-commit hook using a tool like Husky.23 This ensures that no non-compliant code can be committed to the repository.

#### **2.2 MCSS Linting Rules Specification**

The following table provides the formal specification for the initial set of custom linting rules. Each rule is designed to enforce a specific constraint from the ANNOTATION\_REFERENCE.md. The Rule ID is the identifier to be used in ESLint configuration files.

| Rule ID | Severity | Description | Rationale | Autofixable |
| :---- | :---- | :---- | :---- | :---- |
| mcss/component-type-required | Error | An element with a BEM class starting with c-\* is missing the required typeof="mcs:Component" attribute. | Ensures that every element designated as a component is correctly typed and discoverable as a node in the knowledge graph. | Yes |
| mcss/purpose-required | Error | An mcs:Component is missing a child element with the property="mcs:purpose" attribute. | The purpose property is fundamental to the LLM's ability to understand a component's function. Its absence is a critical semantic failure. | No |
| mcss/taxonomy-level-required | Error | An mcs:Component is missing a child element with the property="mcs:taxonomyLevel" attribute. | Enforces the mandatory Atomic Design classification for all components, which is crucial for understanding component complexity and structure. | No |
| mcss/invalid-taxonomy-value | Error | The content attribute for mcs:taxonomyLevel is not one of the allowed values: mcs:Atom, mcs:Molecule, or mcs:Organism. | Maintains the integrity of the controlled vocabulary for the Atomic Design taxonomy. Prevents typos and invalid classifications. | No |
| mcss/dangling-has-part-reference | Warning | The resource attribute of an mcs:hasPart property points to an id that does not exist within the current document scope. | Catches broken links in the component hierarchy, which can result from typos or refactoring. This is a Warning because dynamic content may affect this. | No |
| mcss/behavioral-attribute-on-interactive-only | Warning | A data-mcs-\* attribute was found on a non-interactive element (e.g., div, span) that does not have an interactive ARIA role. | Behavioral contracts are only meaningful on elements that a user can interact with. Applying them elsewhere is likely a developer error. | No |
| mcss/missing-consequence | Warning | An interactive element (button, a, etc.) with a data-mcs-interaction-type is missing the data-mcs-consequence attribute. | While interaction-type provides a category, consequence provides the specific detail needed for full understanding. Its absence is a documentation gap. | No |
| mcss/missing-behavioral-contract | Warning | An mcs:Organism with a class name suggesting complex interactivity (e.g., c-tabs, c-accordion, c-carousel) is missing its corresponding BEHAVIOR.md file in the same directory. | Enforces the rule that complex components must be fully documented with their keyboard interaction patterns according to the specification. | No |

### **3.0 Layer 2: Semantic Graph Validation**

#### **3.1 Overview**

This layer moves beyond syntactic checks to validate the semantic meaning and relational integrity of the annotations. It treats the component's HTML as a source for an RDF graph and runs formal queries to verify its correctness according to the mcs:v1 ontology. This process provides a guarantee that the generated graph is logically sound. This validation MUST be integrated as a mandatory, blocking step in the project's Continuous Integration (CI) build pipeline, failing the build if any validation check does not pass.24

#### **3.2 Process Definition**

The semantic validation process for each component follows three distinct steps:

1. **Parse:** Use a spec-compliant RDFa 1.1 parser to extract all RDF triples from the component's rendered HTML source. The recommended tool for this is the Node.js library **rdfa-streaming-parser**.25 Its streaming nature is highly performant and suitable for CI environments, as it can process documents larger than available memory.25  
2. **Load:** Load the extracted triples into a temporary, in-memory RDF graph store. In a Node.js environment, this can be achieved with any RDF/JS-compliant library. For a Python-based pipeline, RDFLib is the standard choice.26  
3. **Query:** Execute the SPARQL Validation Query Suite (defined below) against the in-memory graph. SPARQL is the standard query language for RDF and is designed specifically for this type of graph pattern matching.27  
4. **Report:** If any ASK query returns false or any SELECT query returns one or more rows, the validation fails. The build MUST be terminated, and the results of the failing query, including the query ID and any returned rows, MUST be logged to the build output to facilitate debugging.

#### **3.3 Shadow DOM and Relational Integrity**

A critical consideration for this validation layer is the impact of the Shadow DOM, a core feature of Web Components.28 The Shadow DOM encapsulates a DOM subtree, and crucially, it scopes

id attributes within that subtree's boundary.29

The mcs:hasPart property relies on an IRI that references a document-local id (e.g., resource="\#my-atom"). If a parent component (e.g., a Molecule) exists in the light DOM, and its child part (e.g., an Atom) is rendered inside a separate Shadow DOM, the id of the child will not be visible from the parent's scope. This breaks the mcs:hasPart relationship, creating a "dangling" or unresolved link in the RDF graph.

The semantic validation process is designed to catch this. The SPARQL queries will fail if a resource reference cannot be resolved to a valid node within the graph. This enforces an implicit architectural rule: **a component and the parts it references via mcs:hasPart MUST exist within the same DOM tree scope (either all in the light DOM or all within the same single shadow root).**

#### **3.4 SPARQL Validation Query Suite**

The following table defines a suite of SPARQL 1.1 queries that serve as executable test cases for the semantic integrity of a component's knowledge graph. ASK queries are preferred where possible as they return a simple boolean and are often more performant for validation checks.

| Query ID | Query Type | Description | SPARQL 1.1 Query |
| :---- | :---- | :---- | :---- |
| mcs-validate-purpose-cardinality | ASK | Verifies that every mcs:Component has **exactly one** mcs:purpose property. Fails if a component has zero or more than one. | PREFIX mcs: \<http://www.example.org/mcss/v1\#\> PREFIX rdf: \<http://www.w3.org/1999/02/22-rdf-syntax-ns\#\> ASK WHERE { { SELECT?component (COUNT(?purpose) AS?count) WHERE {?component a mcs:Component. OPTIONAL {?component mcs:purpose?purpose. } } GROUP BY?component } FILTER(?count\!= 1\) } |
| mcs-validate-taxonomy-cardinality | ASK | Verifies that every mcs:Component has **exactly one** mcs:taxonomyLevel property. | PREFIX mcs: \<http://www.example.org/mcss/v1\#\> PREFIX rdf: \<http://www.w3.org/1999/02/22-rdf-syntax-ns\#\> ASK WHERE { { SELECT?component (COUNT(?level) AS?count) WHERE {?component a mcs:Component. OPTIONAL {?component mcs:taxonomyLevel?level. } } GROUP BY?component } FILTER(?count\!= 1\) } |
| mcs-validate-hasPart-object-is-component | ASK | Verifies that every resource referenced by an mcs:hasPart property is itself typed as an mcs:Component. This prevents linking to non-component elements. | PREFIX mcs: \<http://www.example.org/mcss/v1\#\> PREFIX rdf: \<http://www.w3.org/1999/02/22-rdf-syntax-ns\#\> ASK WHERE {?component mcs:hasPart?part. FILTER NOT EXISTS {?part a mcs:Component. } } |
| mcs-validate-atom-composition | ASK | Verifies that no component classified as an mcs:Atom incorrectly contains another component via mcs:hasPart. Atoms must be indivisible. | PREFIX mcs: \<http://www.example.org/mcss/v1\#\> ASK WHERE {?atom mcs:taxonomyLevel "mcs:Atom" ; mcs:hasPart?anyPart. } |
| mcs-validate-molecule-organism-composition | SELECT | Finds any mcs:Molecule or mcs:Organism that does not declare at least one mcs:hasPart relationship. Returns the non-compliant components. | PREFIX mcs: \<http://www.example.org/mcss/v1\#\> PREFIX rdf: \<http://www.w3.org/1999/02/22-rdf-syntax-ns\#\> SELECT?component WHERE {?component a mcs:Component.?component mcs:taxonomyLevel?level. FILTER(?level IN ("mcs:Molecule", "mcs:Organism")) FILTER NOT EXISTS {?component mcs:hasPart?part. } } |
| mcs-validate-version-format | ASK | Verifies that the value of mcs:version conforms to a basic SemVer pattern (e.g., X.Y.Z). This is a basic check; full SemVer validation is complex for SPARQL. | PREFIX mcs: \<http://www.example.org/mcss/v1\#\> PREFIX xsd: \<http://www.w3.org/2001/XMLSchema\#\> ASK WHERE {?component mcs:version?version. FILTER(\!REGEX(STR(?version), "^\[0-9\]+\\\\.\[0-9\]+\\\\.\[0-9\]+(-\[0-9A-Za-z-\]+(\\\\.\[0-9A-Za-z-\]+)\*)?(\\\\+\[0-9A-Za-z-\]+(\\\\.\[0-9A-Za-z-\]+)\*)?$")) } |

### **4.0 Expert Recommendation: Evolving to a Declarative Validation Framework with SHACL**

#### **4.1 The Limitation of Imperative Validation**

While the SPARQL query suite provides robust and essential validation coverage, it represents an *imperative* approach to data validation. Each new constraint requires a new, custom-written query designed to *find* violations. As the mcs:v1 vocabulary evolves and grows in complexity, this approach can become cumbersome to maintain and scale. Writing and debugging complex SPARQL queries for every possible validation case is inefficient and error-prone.31

#### **4.2 The Power of Declarative Validation with SHACL**

A more mature and scalable approach is to adopt a *declarative* validation framework. The **Shapes Constraint Language (SHACL)** is the official W3C standard specifically designed for this purpose.33 Instead of writing queries to find bad data, SHACL allows you to create a "shapes graph" that declaratively defines the

*shape* that valid data must have. The SHACL engine then compares the data graph against the shapes graph and produces a detailed validation report.35

This approach is more concise, more readable, and aligns better with the principles of semantic data modeling. The validation rules themselves become a formal, reusable artifact.

#### **4.3 A Comparative Example**

Consider the validation rule that every mcs:Component must have exactly one mcs:purpose.

* **SPARQL Approach (Imperative):**  
  Snippet de código  
  PREFIX mcs: \<http://www.example.org/mcss/v1\#\>  
  ASK WHERE {  
    { SELECT?c (COUNT(?p) AS?count)  
      WHERE {?c a mcs:Component. OPTIONAL {?c mcs:purpose?p} }  
      GROUP BY?c }  
    FILTER(?count\!= 1\)  
  }

* **SHACL Approach (Declarative):**  
  Snippet de código  
  @prefix mcs: \<http://www.example.org/mcss/v1\#\>.  
  @prefix sh: \<http://www.w3.org/ns/shacl\#\>.

  mcs:ComponentShape  
      a sh:NodeShape ;  
      sh:targetClass mcs:Component ;  
      sh:property \[  
          sh:path mcs:purpose ;  
          sh:minCount 1 ;  
          sh:maxCount 1 ;  
          sh:message "Every mcs:Component must have exactly one mcs:purpose property."  
      \].

The SHACL shape is not a query to find errors; it is a clear, human-readable definition of correctness. It is far easier to write, understand, and maintain.24

#### **4.4 Proposed Strategic Roadmap**

To ensure the long-term health and maintainability of the MCSS ecosystem, the adoption of SHACL is strongly recommended. The following phased roadmap is proposed:

1. **Phase 1 \- Implementation (Current):** Implement the two-layer validation strategy as specified in this document, using html-eslint and the SPARQL query suite. This provides immediate and comprehensive validation coverage.  
2. **Phase 2 \- Formalization (Next 3-6 Months):** Develop a comprehensive SHACL shapes graph (mcss-shapes.ttl) that formally and declaratively defines all constraints on the mcs:v1 vocabulary. This includes all cardinality, datatype, value range, and relational constraints.  
3. **Phase 3 \- Migration (6-9 Months):** Replace the SPARQL query suite in the CI/CD pipeline with a call to a standard SHACL validation engine. The engine will validate the parsed RDF data against the mcss-shapes.ttl graph. Numerous open-source tools are available for this, such as pySHACL for Python environments or shacl-js for JavaScript-based pipelines.38

Adopting this roadmap will transition the project from a custom validation scripting approach to a standards-based, enterprise-grade data governance framework. The vocabulary (mcs.ttl), the component data (HTML with RDFa), and the validation rules (mcss-shapes.ttl) will all be expressed as interoperable RDF, creating a fully self-describing and self-validating system. This represents the pinnacle of semantic system design and ensures the MCSS framework is robust, scalable, and built for the future.

#### **Referências citadas**

1. RDFa, acessado em julho 4, 2025, [https://rdfa.info/](https://rdfa.info/)  
2. RDFa in XHTML: Syntax and Processing \- W3C, acessado em julho 4, 2025, [https://www.w3.org/TR/rdfa-syntax/rdfa-syntax-diff.html](https://www.w3.org/TR/rdfa-syntax/rdfa-syntax-diff.html)  
3. Best Practices for Publishing Linked Data \- W3C, acessado em julho 4, 2025, [https://www.w3.org/TR/ld-bp/](https://www.w3.org/TR/ld-bp/)  
4. Best Practice Recipes for Publishing RDF Vocabularies \- W3C, acessado em julho 4, 2025, [https://www.w3.org/TR/swbp-vocab-pub/](https://www.w3.org/TR/swbp-vocab-pub/)  
5. RDFa Core 1.1 \- Third Edition \- W3C, acessado em julho 4, 2025, [https://www.w3.org/TR/rdfa-core/](https://www.w3.org/TR/rdfa-core/)  
6. Resource Description Framework \- Wikipedia, acessado em julho 4, 2025, [https://en.wikipedia.org/wiki/Resource\_Description\_Framework](https://en.wikipedia.org/wiki/Resource_Description_Framework)  
7. HTML Data Attributes Guide \- CSS-Tricks, acessado em julho 4, 2025, [https://css-tricks.com/a-complete-guide-to-data-attributes/](https://css-tricks.com/a-complete-guide-to-data-attributes/)  
8. Using data attributes \- Learn web development | MDN, acessado em julho 4, 2025, [https://developer.mozilla.org/en-US/docs/Learn\_web\_development/Howto/Solve\_HTML\_problems/Use\_data\_attributes](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Solve_HTML_problems/Use_data_attributes)  
9. HTML Data Attribute: Syntax, Usage, and Examples \- Mimo, acessado em julho 4, 2025, [https://mimo.org/glossary/html/data-attribute](https://mimo.org/glossary/html/data-attribute)  
10. Rise of Headless UI Components: Why Separation of Concerns is Revolutionising Frontend Development \- Stackademic, acessado em julho 4, 2025, [https://blog.stackademic.com/rise-of-headless-ui-components-why-separation-of-concerns-is-revolutionising-frontend-development-3a899194773f](https://blog.stackademic.com/rise-of-headless-ui-components-why-separation-of-concerns-is-revolutionising-frontend-development-3a899194773f)  
11. What is Headless UI?: Unlocking Flexibility and Accessibility | by Jill Chang | Medium, acessado em julho 4, 2025, [https://medium.com/@jill6666/what-is-headless-ui-unlocking-flexibility-and-accessibility-3c7f9bec5a23](https://medium.com/@jill6666/what-is-headless-ui-unlocking-flexibility-and-accessibility-3c7f9bec5a23)  
12. Dropdown Menu \- Headless UI, acessado em julho 4, 2025, [https://headlessui.com/react/menu](https://headlessui.com/react/menu)  
13. Authoring Practices Guide (APG) Examples & Rules in 2025 \- Elementor, acessado em julho 4, 2025, [https://elementor.com/blog/apg-explained/](https://elementor.com/blog/apg-explained/)  
14. ARIA Authoring Practices Guide | APG | WAI | W3C, acessado em julho 4, 2025, [https://www.w3.org/WAI/ARIA/apg/](https://www.w3.org/WAI/ARIA/apg/)  
15. Accessibility information for web authors \- MDN Web Docs, acessado em julho 4, 2025, [https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Information\_for\_Web\_authors](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Information_for_Web_authors)  
16. WAI-ARIA Authoring Practices 1.2 \- W3C, acessado em julho 4, 2025, [https://www.w3.org/TR/2021/NOTE-wai-aria-practices-1.2-20211129/](https://www.w3.org/TR/2021/NOTE-wai-aria-practices-1.2-20211129/)  
17. WAI-ARIA Secrets: Master Authoring Practices NOW\! \- Hurix Digital, acessado em julho 4, 2025, [https://www.hurix.com/blogs/the-future-of-aria-authoring-practices-emerging-trends-and-innovations/](https://www.hurix.com/blogs/the-future-of-aria-authoring-practices-emerging-trends-and-innovations/)  
18. What is Linting and how to use a Linter tool \- DEV Community, acessado em julho 4, 2025, [https://dev.to/aryan\_shourie/what-is-linting-and-how-to-use-a-linter-tool-524l](https://dev.to/aryan_shourie/what-is-linting-and-how-to-use-a-linter-tool-524l)  
19. HTML-Lint | A code quality bookmarklet and command-line tool \- GitHub Pages, acessado em julho 4, 2025, [https://curtisj44.github.io/HTML-Lint/](https://curtisj44.github.io/HTML-Lint/)  
20. ESLint can now lint HTML using the html-eslint language plugin, acessado em julho 4, 2025, [https://eslint.org/blog/2025/05/eslint-html-plugin/](https://eslint.org/blog/2025/05/eslint-html-plugin/)  
21. html-eslint, acessado em julho 4, 2025, [https://html-eslint.org/](https://html-eslint.org/)  
22. An Introduction to Writing HTML ESLint Rules in Angular | Bits and Pieces, acessado em julho 4, 2025, [https://blog.bitsrc.io/an-introduction-to-writing-html-eslint-rules-in-angular-51be8d8c4cfc](https://blog.bitsrc.io/an-introduction-to-writing-html-eslint-rules-in-angular-51be8d8c4cfc)  
23. CI/CD Pipeline in React.js Project with Github Workflows using Eslint Prettier Pre-commit and Husky \- YouTube, acessado em julho 4, 2025, [https://www.youtube.com/watch?v=T1sV7D418dY](https://www.youtube.com/watch?v=T1sV7D418dY)  
24. Design reusable SHACL shapes and implement a linked data validation pipeline, acessado em julho 4, 2025, [https://journal.code4lib.org/articles/14711](https://journal.code4lib.org/articles/14711)  
25. rdfa-streaming-parser \- npm, acessado em julho 4, 2025, [https://www.npmjs.com/package/rdfa-streaming-parser](https://www.npmjs.com/package/rdfa-streaming-parser)  
26. RDFLib/pyrdfa3: RDFa 1.1 distiller/parser library: can extract RDFa 1.1 (and RDFa 1.0, if properly set via a @version attribute) from (X)HTML, SVG, or XML in general. The module can be used to produce serialized versions of the extracted graph, or simply an RDFLib Graph \- GitHub, acessado em julho 4, 2025, [https://github.com/RDFLib/pyrdfa3](https://github.com/RDFLib/pyrdfa3)  
27. SPARQL Query Language for RDF \- W3C, acessado em julho 4, 2025, [https://www.w3.org/TR/rdf-sparql-query/](https://www.w3.org/TR/rdf-sparql-query/)  
28. Using shadow DOM \- Web APIs | MDN, acessado em julho 4, 2025, [https://developer.mozilla.org/en-US/docs/Web/API/Web\_components/Using\_shadow\_DOM](https://developer.mozilla.org/en-US/docs/Web/API/Web_components/Using_shadow_DOM)  
29. Accessibility with ID Referencing and Shadow DOM \- Cory Rylan, acessado em julho 4, 2025, [https://coryrylan.com/blog/accessibility-with-id-referencing-and-shadow-dom](https://coryrylan.com/blog/accessibility-with-id-referencing-and-shadow-dom)  
30. Shadow DOM and accessibility: the trouble with ARIA \- Nolan Lawson, acessado em julho 4, 2025, [https://nolanlawson.com/2022/11/28/shadow-dom-and-accessibility-the-trouble-with-aria/](https://nolanlawson.com/2022/11/28/shadow-dom-and-accessibility-the-trouble-with-aria/)  
31. Validating Data Integrity with SQL Queries | by Vishnu TR \- Medium, acessado em julho 4, 2025, [https://vishnutr.medium.com/validating-data-integrity-with-sql-queries-5ccc000d2b0a](https://vishnutr.medium.com/validating-data-integrity-with-sql-queries-5ccc000d2b0a)  
32. Knowledge graph training offers, RDF, OWL, SPARQL, SHACL \- Sparna, acessado em julho 4, 2025, [https://www.sparna.fr/en/formations/](https://www.sparna.fr/en/formations/)  
33. How to create and validate SHACL rules for your RDF data, acessado em julho 4, 2025, [https://shacl.dev/article/How\_to\_create\_and\_validate\_SHACL\_rules\_for\_your\_RDF\_data.html](https://shacl.dev/article/How_to_create_and_validate_SHACL_rules_for_your_RDF_data.html)  
34. Shapes Constraint Language (SHACL) \- W3C, acessado em julho 4, 2025, [https://www.w3.org/TR/shacl/](https://www.w3.org/TR/shacl/)  
35. Validation With SHACL \- Eclipse RDF4J, acessado em julho 4, 2025, [https://rdf4j.org/documentation/programming/shacl/](https://rdf4j.org/documentation/programming/shacl/)  
36. What is SHACL? (With Examples). SHACL is a critical tool for anyone… | by Kevin Doubleday | Fluree PBC | Medium, acessado em julho 4, 2025, [https://medium.com/fluree/what-is-shacl-with-examples-2697f659d465](https://medium.com/fluree/what-is-shacl-with-examples-2697f659d465)  
37. Validating RDF data with SHACL \- Bob DuCharme, acessado em julho 4, 2025, [https://www.bobdc.com/blog/validating-rdf-data-with-shacl/](https://www.bobdc.com/blog/validating-rdf-data-with-shacl/)  
38. Top 10 tools for working with SHACL, acessado em julho 4, 2025, [https://shacl.dev/article/Top\_10\_tools\_for\_working\_with\_SHACL.html](https://shacl.dev/article/Top_10_tools_for_working_with_SHACL.html)  
39. RDFLib/pySHACL: A Python validator for SHACL \- GitHub, acessado em julho 4, 2025, [https://github.com/RDFLib/pySHACL](https://github.com/RDFLib/pySHACL)