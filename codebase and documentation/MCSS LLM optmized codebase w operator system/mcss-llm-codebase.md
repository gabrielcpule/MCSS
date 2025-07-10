# MCSS LLM-Optimized Codebase

## Overview

This codebase provides a comprehensive, LLM-friendly implementation of the Model Context Style Sheet (MCSS) framework. It is designed to enable Large Language Models to understand, generate, validate, and improve MCSS code while strictly preserving core architectural principles.

## Core Philosophy

**The Semantic Imperative**: Transform HTML documents from human-readable displays into machine-readable knowledge graphs through explicit RDFa metadata.

## Directory Structure

```
mcss-llm/
├── core/                     # Immutable MCSS principles and constants
│   ├── principles.json       # Core principles and rules
│   ├── constraints.json      # Immutable architectural constraints
│   └── vocabulary.ttl        # RDFa vocabulary definition
├── agents/                   # LLM agent system
│   ├── validator/           # Validation agent
│   ├── generator/           # Code generation agent
│   ├── analyzer/            # Analysis agent
│   ├── optimizer/           # Optimization agent
│   └── educator/            # Teaching agent
├── tokens/                   # Design token system
│   ├── tokens.css           # Master token definitions
│   ├── token-schema.json    # Token structure validation
│   └── token-tools/         # Token management utilities
├── layers/                   # 5-Layer Architecture implementation
│   ├── 1-global/            # Global layer styles
│   ├── 2-layout/            # Layout layer utilities
│   ├── 3-component/         # Component layer library
│   ├── 4-utility/           # Utility layer classes
│   └── 5-exception/         # Exception layer overrides
├── components/               # Semantic component library
│   ├── atoms/               # Atomic components
│   ├── molecules/           # Molecular components
│   ├── organisms/           # Organism components
│   └── templates/           # Component generation templates
├── validation/               # Validation and linting tools
│   ├── rules/               # ESLint and SPARQL rules
│   ├── schemas/             # JSON schemas for validation
│   └── tests/               # Automated test suites
├── generation/               # Code generation utilities
│   ├── templates/           # Code generation templates
│   ├── parsers/             # RDFa and CSS parsers
│   └── builders/            # Component builders
├── docs/                     # Machine-readable documentation
│   ├── api/                 # API documentation
│   ├── examples/            # Working examples
│   └── tutorials/           # Step-by-step guides
└── tools/                    # Development and build tools
    ├── cli/                 # Command-line interface
    ├── build/               # Build system
    └── dev/                 # Development utilities
```

## Core Principles (Immutable)

### 1. The Semantic Imperative

Transform HTML from human-readable displays into machine-readable knowledge graphs through explicit semantic metadata.

**Constraints:**
- All components MUST have `typeof="mcs:Component"`
- All components MUST declare their `taxonomyLevel`
- All components MUST have a semantic purpose declaration

### 2. Five-Layer Architecture

Systematic CSS organization using CSS Cascade Layers:

1. **Global** (no prefix): Foundational styles, resets, tokens
2. **Layout** (`l-`): Component arrangement and positioning  
3. **Component** (`c-`): Default styling for reusable UI patterns
4. **Utility** (`u-`): Single-purpose override classes
5. **Exception** (`e-`): Temporary overrides and debugging

**Immutable Rules:**
- Higher layer always overrides lower layer regardless of specificity
- Components (`c-`) MUST NOT declare external margins (Golden Rule)
- Each layer has exactly one designated prefix

### 3. Ontological Naming Convention (ONC)

Strict grammar: `[prefix]-[block]__[element]--[modifier]`

**Rules:**
- Every class MUST have a layer prefix
- Follow BEM syntax after prefix
- Names MUST describe purpose, not appearance
- Use full words for clarity

### 4. Design Token System

Single source of truth for all design values:

- All CSS values MUST come from tokens via `var()` function
- No magic numbers or hardcoded values permitted
- Tokens MUST follow semantic naming: `--mcs-[category]-[property]-[variant]`

### 5. Atomic Design Taxonomy

Component classification system:

- **Atom**: Smallest indivisible functional unit
- **Molecule**: Group of atoms forming simple reusable component
- **Organism**: Complex component forming distinct interface section

## LLM Agent System

### Available Agents

1. **Validator Agent**: Validates all MCSS code against core principles
2. **Generator Agent**: Creates new MCSS components following all conventions
3. **Analyzer Agent**: Analyzes and understands existing MCSS codebases
4. **Optimizer Agent**: Improves MCSS code while preserving semantics
5. **Educator Agent**: Teaches MCSS principles and assists developers

### Agent Constraints

All agents MUST:
- Preserve MCSS core principles
- Never violate immutable rules
- Maintain semantic integrity
- Follow validation pipelines

## Usage Examples

### 1. Component Generation

```javascript
// Request new component
const request = {
  component_name: "SearchBox",
  taxonomy_level: "molecule",
  purpose: "Allow users to input search queries",
  required_props: ["placeholder", "value"],
  states: ["default", "focused", "error"],
  behaviors: ["submit-search", "clear-input"]
};

// Generator agent creates complete component package
const output = await mcssGenerator.createComponent(request);
```

### 2. Code Validation

```javascript
// Validate existing code
const validation = await mcssValidator.validate({
  html_content: htmlString,
  css_content: cssString,
  validation_level: "strict"
});

console.log(validation.compliance_score); // 0-100
console.log(validation.violations); // Array of issues
```

### 3. Codebase Analysis

```javascript
// Analyze entire codebase
const analysis = await mcssAnalyzer.analyze({
  codebase_path: "./src",
  analysis_type: "full",
  output_format: "json"
});

console.log(analysis.knowledge_graph); // RDF representation
console.log(analysis.component_inventory); // All components
```

## Extension Guidelines

### Adding New Patterns

1. **Validate against core principles**: Ensure new patterns don't violate immutable rules
2. **Document semantic rationale**: Explain why the pattern preserves semantic meaning
3. **Create validation rules**: Add lint rules to enforce the new pattern
4. **Generate examples**: Provide working examples and documentation

### Customizing for Projects

1. **Extend token system**: Add project-specific tokens following naming convention
2. **Create custom components**: Build components using MCSS foundation
3. **Add validation rules**: Create project-specific validation extensions
4. **Train agents**: Feed project patterns to adaptive learning system

## Validation and Quality Assurance

### Automated Validation

- **ESLint Plugin**: Real-time validation of HTML and CSS
- **SPARQL Queries**: Semantic validation of RDFa annotations
- **CSS Analysis**: Token usage and layer compliance checking
- **Accessibility Testing**: WCAG 2.2 AA compliance verification

### Manual Review

- **Architecture Review**: Ensure layer separation and component isolation
- **Semantic Review**: Verify RDFa annotations convey correct meaning
- **Performance Review**: Check token usage and CSS efficiency
- **Accessibility Review**: Manual testing with assistive technologies

## Contributing

### For Developers

1. Study core principles and immutable rules
2. Follow validation pipelines for all contributions
3. Ensure comprehensive semantic annotations
4. Test with automated validation tools

### For LLM Systems

1. Load core principles as immutable constraints
2. Use agent validation pipeline before output
3. Preserve semantic meaning in all modifications
4. Learn from validation feedback loops

## Integration with Build Systems

### npm/yarn Integration

```bash
npm install @mcss/framework
npm install @mcss/eslint-plugin
npm install @mcss/validation-tools
```

### Build Pipeline Integration

```javascript
// webpack.config.js
module.exports = {
  plugins: [
    new MCSSValidationPlugin({
      strictMode: true,
      validateTokens: true,
      validateSemantics: true
    })
  ]
};
```

### CI/CD Integration

```yaml
# .github/workflows/mcss-validation.yml
- name: Validate MCSS Compliance
  run: |
    npx mcss-validate --strict
    npx mcss-semantic-check --format junit
```

## Performance Considerations

### CSS Performance

- Layer-based architecture minimizes specificity conflicts
- Token system enables efficient CSS custom property usage
- Component isolation prevents cascade leakage

### Build Performance

- Semantic validation can be resource-intensive
- Use caching for repeated validation tasks
- Consider progressive validation in development

### Runtime Performance

- Semantic annotations add minimal HTML overhead
- CSS layers provide optimal cascade performance
- Token system enables efficient theming

## Accessibility Features

### Built-in Accessibility

- WCAG 2.2 AA compliance by design
- Semantic HTML structure from RDFa annotations
- Keyboard navigation patterns in behavioral contracts
- Screen reader optimization through proper markup

### Validation

- Automated contrast ratio checking
- Semantic structure validation
- Interactive element accessibility verification
- Focus management testing

---

This codebase provides a complete foundation for LLM-driven MCSS development while maintaining strict adherence to core architectural principles. All agents and tools are designed to preserve semantic integrity and enforce best practices automatically.