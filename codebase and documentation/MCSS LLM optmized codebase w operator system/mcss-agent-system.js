/**
 * MCSS LLM Agent Implementation
 * Comprehensive agent system for understanding, generating, and validating MCSS components
 */

class MCSSAgentSystem {
  constructor() {
    this.coreConstraints = this.loadCoreConstraints();
    this.vocabularySchema = this.loadVocabularySchema();
    this.tokenDatabase = this.loadTokenDatabase();
    this.validationRules = this.loadValidationRules();
  }

  // ============================================================================
  // CORE CONSTRAINT VALIDATION
  // ============================================================================

  loadCoreConstraints() {
    return {
      // The Semantic Imperative - IMMUTABLE
      semanticRequirements: {
        typeofRequired: true,
        taxonomyLevelRequired: true,
        purposeRequired: true,
        vocabularyURI: "https://gabrielcpule.github.io/mcss-vocab/api/mcss/v1.rdf"
      },

      // 5-Layer Architecture - IMMUTABLE
      layerArchitecture: {
        layers: ["global", "layout", "component", "utility", "exception"],
        prefixes: { "layout": "l-", "component": "c-", "utility": "u-", "exception": "e-" },
        goldenRule: "Components MUST NOT declare external margins"
      },

      // Ontological Naming Convention - IMMUTABLE  
      namingConvention: {
        pattern: /^[lcue]-[a-z][a-z0-9]*(?:__[a-z][a-z0-9]*)?(?:--[a-z][a-z0-9]*)?$/,
        requirePrefix: true,
        semanticNaming: true,
        noAbbreviations: true
      },

      // Token System - IMMUTABLE
      tokenSystem: {
        tokenOnly: true,
        pattern: /^--mcs-[a-z]+-[a-z]+-[a-z]+$/,
        noMagicNumbers: true,
        singleSource: "tokens.css"
      }
    };
  }

  // ============================================================================
  // MCSS VALIDATOR AGENT
  // ============================================================================

  validateComponent(html, css) {
    const validation = {
      isValid: true,
      violations: [],
      suggestions: [],
      complianceScore: 100
    };

    // 1. Validate Semantic Annotations
    const semanticValidation = this.validateSemanticAnnotations(html);
    if (!semanticValidation.isValid) {
      validation.violations.push(...semanticValidation.violations);
      validation.isValid = false;
    }

    // 2. Validate Layer Architecture
    const layerValidation = this.validateLayerArchitecture(css);
    if (!layerValidation.isValid) {
      validation.violations.push(...layerValidation.violations);
      validation.isValid = false;
    }

    // 3. Validate Naming Convention
    const namingValidation = this.validateNamingConvention(html, css);
    if (!namingValidation.isValid) {
      validation.violations.push(...namingValidation.violations);
      validation.isValid = false;
    }

    // 4. Validate Token Usage
    const tokenValidation = this.validateTokenUsage(css);
    if (!tokenValidation.isValid) {
      validation.violations.push(...tokenValidation.violations);
      validation.isValid = false;
    }

    // Calculate compliance score
    validation.complianceScore = Math.max(0, 100 - (validation.violations.length * 10));

    return validation;
  }

  validateSemanticAnnotations(html) {
    const violations = [];
    
    // Parse HTML to check for required RDFa attributes
    const componentElements = this.parseComponentElements(html);
    
    for (const element of componentElements) {
      // Check for typeof="mcs:Component"
      if (!element.hasAttribute('typeof') || element.getAttribute('typeof') !== 'mcs:Component') {
        violations.push({
          type: "MISSING_TYPEOF",
          message: "Component missing typeof='mcs:Component' attribute",
          element: element.outerHTML,
          severity: "ERROR"
        });
      }

      // Check for vocab declaration
      if (!this.hasVocabDeclaration(html)) {
        violations.push({
          type: "MISSING_VOCAB",
          message: "Missing vocab declaration on html element",
          suggestion: `Add vocab="${this.coreConstraints.semanticRequirements.vocabularyURI}"`,
          severity: "ERROR"
        });
      }

      // Check for taxonomy level
      const taxonomyElement = element.querySelector('[property="mcs:taxonomyLevel"]');
      if (!taxonomyElement) {
        violations.push({
          type: "MISSING_TAXONOMY",
          message: "Component missing mcs:taxonomyLevel property",
          element: element.outerHTML,
          severity: "ERROR"
        });
      }

      // Check for purpose declaration
      const purposeElement = element.querySelector('[property="mcs:purpose"]');
      if (!purposeElement) {
        violations.push({
          type: "MISSING_PURPOSE",
          message: "Component missing mcs:purpose property",
          element: element.outerHTML,
          severity: "ERROR"
        });
      }
    }

    return {
      isValid: violations.length === 0,
      violations
    };
  }

  validateLayerArchitecture(css) {
    const violations = [];
    
    // Check for proper @layer declaration
    if (!css.includes('@layer global, layout, component, utility, exception')) {
      violations.push({
        type: "MISSING_LAYER_DECLARATION",
        message: "CSS missing proper @layer declaration",
        suggestion: "Add: @layer global, layout, component, utility, exception;",
        severity: "ERROR"
      });
    }

    // Check Golden Rule: components should not have external margins
    const componentRules = this.extractComponentRules(css);
    for (const rule of componentRules) {
      if (this.hasExternalMargin(rule)) {
        violations.push({
          type: "GOLDEN_RULE_VIOLATION",
          message: "Component declares external margin (violates Golden Rule)",
          rule: rule.selector,
          severity: "ERROR"
        });
      }
    }

    return {
      isValid: violations.length === 0,
      violations
    };
  }

  validateTokenUsage(css) {
    const violations = [];
    
    // Check for hardcoded values (magic numbers)
    const hardcodedValues = this.findHardcodedValues(css);
    for (const hardcoded of hardcodedValues) {
      violations.push({
        type: "HARDCODED_VALUE",
        message: "Hardcoded value found - must use design token",
        value: hardcoded.value,
        property: hardcoded.property,
        suggestion: this.suggestToken(hardcoded),
        severity: "ERROR"
      });
    }

    return {
      isValid: violations.length === 0,
      violations
    };
  }

  // ============================================================================
  // MCSS GENERATOR AGENT
  // ============================================================================

  generateComponent(request) {
    // Validate request against core constraints
    if (!this.isValidComponentRequest(request)) {
      throw new Error("Component request violates MCSS constraints");
    }

    const component = {
      html: this.generateSemanticHTML(request),
      css: this.generateTokenDrivenCSS(request),
      behaviorContract: this.generateBehaviorContract(request),
      tests: this.generateTests(request),
      documentation: this.generateDocumentation(request)
    };

    // Validate generated component
    const validation = this.validateComponent(component.html, component.css);
    if (!validation.isValid) {
      throw new Error(`Generated component failed validation: ${validation.violations.map(v => v.message).join(', ')}`);
    }

    return component;
  }

  generateSemanticHTML(request) {
    const { component_name, taxonomy_level, purpose, states, behaviors } = request;
    
    // Generate unique ID for component
    const componentId = this.generateComponentId(component_name);
    
    // Generate RDFa-annotated HTML
    let html = `<div
  vocab="${this.coreConstraints.semanticRequirements.vocabularyURI}"
  typeof="mcs:Component"
  class="${this.generateClassName(component_name, taxonomy_level)}"
  id="${componentId}"
  property="mcs:componentName" content="${component_name}"
  data-state="default"
>
  <span property="mcs:taxonomyLevel" content="mcs:${this.capitalizeFirst(taxonomy_level)}" class="u-hidden"></span>
  <span property="mcs:purpose" content="${purpose}" class="u-hidden"></span>
  <span property="mcs:version" content="1.0.0" class="u-hidden"></span>
  <span property="mcs:status" content="prototype" class="u-hidden"></span>
`;

    // Add component-specific content based on type
    html += this.generateComponentContent(request);
    
    // Add behavioral attributes if needed
    if (behaviors && behaviors.length > 0) {
      html = this.addBehavioralAttributes(html, behaviors);
    }
    
    html += `</div>`;
    
    return html;
  }

  generateTokenDrivenCSS(request) {
    const { component_name, taxonomy_level, states } = request;
    const className = this.generateClassName(component_name, taxonomy_level);
    
    let css = `/**
 * @component ${component_name}
 * @taxonomy ${taxonomy_level}
 * @layer component
 */

@layer component {
  .${className} {
    /* Box Model - using tokens only */
    display: var(--mcs-display-${this.getDefaultDisplay(taxonomy_level)});
    padding: var(--mcs-spacing-inset-medium);
    border: var(--mcs-border-width-default) solid var(--mcs-color-border-default);
    border-radius: var(--mcs-border-radius-medium);
    
    /* Typography - using tokens only */
    font-family: var(--mcs-typography-font-family-base);
    font-size: var(--mcs-typography-font-size-body-default);
    color: var(--mcs-color-text-primary);
    
    /* Visual - using tokens only */
    background-color: var(--mcs-color-background-surface);
    transition: var(--mcs-effect-transition-duration) var(--mcs-effect-transition-timing-function);
    
    /* GOLDEN RULE: No external margins */
    /* margin: FORBIDDEN - layout responsibility belongs to parent */
  }
`;

    // Add state variations
    if (states && states.length > 0) {
      for (const state of states) {
        if (state !== 'default') {
          css += this.generateStateCSS(className, state);
        }
      }
    }

    css += `}`;
    
    return css;
  }

  generateStateCSS(className, state) {
    const stateTokens = this.getStateTokens(state);
    
    return `
  
  .${className}[data-state="${state}"] {
    background-color: var(--mcs-color-background-${stateTokens.background});
    border-color: var(--mcs-color-border-${stateTokens.border});
    color: var(--mcs-color-text-${stateTokens.text});
  }`;
  }

  // ============================================================================
  // MCSS ANALYZER AGENT
  // ============================================================================

  analyzeCodebase(codebasePath, options = {}) {
    const analysis = {
      knowledgeGraph: this.buildKnowledgeGraph(codebasePath),
      componentInventory: this.inventoryComponents(codebasePath),
      tokenUsage: this.analyzeTokenUsage(codebasePath),
      architectureHealth: this.assessArchitectureHealth(codebasePath),
      recommendations: []
    };

    // Generate recommendations based on analysis
    analysis.recommendations = this.generateRecommendations(analysis);

    return analysis;
  }

  buildKnowledgeGraph(codebasePath) {
    const components = this.findAllComponents(codebasePath);
    const graph = {
      "@context": {
        "mcs": "https://gabrielcpule.github.io/mcss-vocab/api/mcss/v1.rdf",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#"
      },
      "@graph": []
    };

    for (const component of components) {
      const componentData = this.extractComponentMetadata(component);
      graph["@graph"].push({
        "@type": "mcs:Component",
        "@id": componentData.id,
        "mcs:componentName": componentData.name,
        "mcs:taxonomyLevel": componentData.taxonomyLevel,
        "mcs:purpose": componentData.purpose,
        "mcs:version": componentData.version,
        "mcs:status": componentData.status,
        "mcs:hasPart": componentData.parts || [],
        "mcs:usedBy": componentData.usedBy || []
      });
    }

    return graph;
  }

  // ============================================================================
  // MCSS OPTIMIZER AGENT
  // ============================================================================

  optimizeComponent(html, css, options = {}) {
    const optimizations = {
      cssOptimizations: [],
      tokenOptimizations: [],
      semanticImprovements: [],
      accessibilityImprovements: []
    };

    // Optimize CSS performance without changing semantics
    optimizations.cssOptimizations = this.optimizeCSS(css);
    
    // Suggest token consolidation
    optimizations.tokenOptimizations = this.optimizeTokens(css);
    
    // Improve semantic annotations
    optimizations.semanticImprovements = this.improveSemantic(html);
    
    // Enhance accessibility
    optimizations.accessibilityImprovements = this.improveAccessibility(html, css);

    return optimizations;
  }

  // ============================================================================
  // MCSS EDUCATOR AGENT
  // ============================================================================

  explainComponent(html, css) {
    const explanation = {
      overview: this.generateOverview(html, css),
      semanticBreakdown: this.explainSemantics(html),
      cssArchitecture: this.explainCSSArchitecture(css),
      designDecisions: this.explainDesignDecisions(html, css),
      bestPractices: this.identifyBestPractices(html, css),
      learningResources: this.suggestLearningResources(html, css)
    };

    return explanation;
  }

  generateTutorial(topic) {
    const tutorials = {
      "semantic-imperative": this.tutorialSemanticImperative(),
      "layer-architecture": this.tutorialLayerArchitecture(),
      "token-system": this.tutorialTokenSystem(),
      "component-creation": this.tutorialComponentCreation()
    };

    return tutorials[topic] || this.tutorialIndex();
  }

  // ============================================================================
  // UTILITY METHODS
  // ============================================================================

  parseComponentElements(html) {
    // Simple HTML parsing - in real implementation, use proper HTML parser
    const componentElements = [];
    const regex = /<[^>]*class="[^"]*c-[^"]*"[^>]*>/g;
    const matches = html.match(regex);
    
    if (matches) {
      for (const match of matches) {
        componentElements.push({
          outerHTML: match,
          hasAttribute: (attr) => match.includes(attr),
          getAttribute: (attr) => {
            const attrRegex = new RegExp(`${attr}="([^"]*)"`, 'i');
            const attrMatch = match.match(attrRegex);
            return attrMatch ? attrMatch[1] : null;
          },
          querySelector: () => null // Simplified for example
        });
      }
    }
    
    return componentElements;
  }

  generateClassName(componentName, taxonomyLevel) {
    const prefix = this.getTaxonomyPrefix(taxonomyLevel);
    const kebabName = this.toKebabCase(componentName);
    return `${prefix}${kebabName}`;
  }

  getTaxonomyPrefix(taxonomyLevel) {
    return taxonomyLevel === 'atom' || taxonomyLevel === 'molecule' || taxonomyLevel === 'organism' 
      ? 'c-' 
      : 'c-';
  }

  toKebabCase(str) {
    return str
      .replace(/([a-z])([A-Z])/g, '$1-$2')
      .toLowerCase();
  }

  capitalizeFirst(str) {
    return str.charAt(0).toUpperCase() + str.slice(1);
  }

  // ============================================================================
  // AGENT COORDINATION
  // ============================================================================

  async processRequest(request) {
    switch (request.type) {
      case 'generate':
        const generated = this.generateComponent(request.data);
        const validation = this.validateComponent(generated.html, generated.css);
        const optimization = this.optimizeComponent(generated.html, generated.css);
        const explanation = this.explainComponent(generated.html, generated.css);
        
        return {
          component: generated,
          validation,
          optimization,
          explanation
        };

      case 'validate':
        return this.validateComponent(request.data.html, request.data.css);

      case 'analyze':
        return this.analyzeCodebase(request.data.path, request.data.options);

      case 'optimize':
        return this.optimizeComponent(request.data.html, request.data.css, request.data.options);

      case 'explain':
        return this.explainComponent(request.data.html, request.data.css);

      default:
        throw new Error(`Unknown request type: ${request.type}`);
    }
  }
}

// ============================================================================
// EXAMPLE USAGE
// ============================================================================

// Initialize the MCSS Agent System
const mcssAgents = new MCSSAgentSystem();

// Example 1: Generate a new component
const componentRequest = {
  type: 'generate',
  data: {
    component_name: "SearchBox",
    taxonomy_level: "molecule",
    purpose: "Allow users to input search queries with autocomplete suggestions",
    required_props: ["placeholder", "value"],
    states: ["default", "focused", "error", "loading"],
    behaviors: ["submit-search", "clear-input", "show-suggestions"]
  }
};

// Example 2: Validate existing component
const validationRequest = {
  type: 'validate',
  data: {
    html: `<div class="c-button" typeof="mcs:Component">...</div>`,
    css: `.c-button { padding: var(--mcs-spacing-medium); }`
  }
};

// Example 3: Analyze codebase
const analysisRequest = {
  type: 'analyze',
  data: {
    path: './src/components',
    options: {
      includeTokenAnalysis: true,
      generateRecommendations: true
    }
  }
};

export default MCSSAgentSystem;