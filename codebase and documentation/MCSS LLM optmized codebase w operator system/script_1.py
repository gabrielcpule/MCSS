# Create the core MCSS principles and immutable rules
core_principles = {
    "semantic_imperative": {
        "description": "Transform HTML documents from human-readable displays into machine-readable knowledge graphs",
        "goal": "Describe UI components as 'things, not strings'",
        "implementation": "Explicit RDFa metadata embedded directly in markup",
        "constraints": [
            "All components MUST have typeof='mcs:Component'",
            "All components MUST declare their taxonomyLevel",
            "All components MUST have a semantic purpose declaration"
        ]
    },
    
    "five_layer_architecture": {
        "description": "Systematic CSS organization using CSS Cascade Layers",
        "layers": {
            "1_global": {
                "name": "Global", 
                "purpose": "Foundational styles, resets, token definitions",
                "prefix": "none (direct element selectors)",
                "examples": ["body", "h1-h6", "* (resets)"]
            },
            "2_layout": {
                "name": "Layout",
                "purpose": "Arrangement and positioning of components", 
                "prefix": "l-",
                "examples": ["l-grid", "l-stack", "l-container"]
            },
            "3_component": {
                "name": "Component",
                "purpose": "Default styling for reusable UI patterns",
                "prefix": "c-", 
                "examples": ["c-button", "c-card", "c-navigation"]
            },
            "4_utility": {
                "name": "Utility",
                "purpose": "Single-purpose override classes",
                "prefix": "u-",
                "examples": ["u-text-center", "u-margin-0", "u-font-bold"]
            },
            "5_exception": {
                "name": "Exception", 
                "purpose": "Temporary overrides and debugging",
                "prefix": "e-",
                "examples": ["e-debug", "e-temp-fix"]
            }
        },
        "immutable_rules": [
            "Higher layer always overrides lower layer regardless of specificity",
            "Components (c-) MUST NOT declare external margins (Golden Rule)",
            "Each layer has exactly one designated prefix",
            "CSS @layer declaration MUST reflect this exact order"
        ]
    },
    
    "ontological_naming_convention": {
        "description": "Strict grammar for CSS class names acting as a type system",
        "pattern": "[prefix]-[block]__[element]--[modifier]",
        "rules": {
            "prefix_required": "Every class MUST have a layer prefix (c-, l-, u-, e-)",
            "bem_syntax": "Follow Block__Element--Modifier pattern after prefix",
            "semantic_naming": "Names MUST describe purpose, not appearance",
            "no_abbreviations": "Use full words for clarity (button not btn)"
        },
        "examples": {
            "valid": ["c-button", "c-card__header", "c-button--primary", "l-grid__item"],
            "invalid": ["button", "btn-primary", "red-text", "big-font"]
        }
    },
    
    "semantic_annotation_schema": {
        "description": "RDFa vocabulary for machine-readable component metadata",
        "vocabulary_uri": "https://gabrielcpule.github.io/mcss-vocab/api/mcss/v1.rdf",
        "required_properties": {
            "mcs:componentName": "Human-readable component name",
            "mcs:taxonomyLevel": "Atomic Design classification (atom|molecule|organism)",
            "mcs:purpose": "Semantic description of component function",
            "mcs:version": "SemVer version string",
            "mcs:status": "Development status (prototype|production|deprecated)"
        },
        "behavioral_attributes": {
            "data-mcs-interaction-type": "Category of user interaction",
            "data-mcs-consequence": "What happens when interacted with",
            "data-mcs-triggers-event": "Custom event dispatched on interaction"
        },
        "state_management": {
            "mechanism": "data-state attribute",
            "rule": "All component states MUST use data-state, never classes",
            "examples": ["data-state='disabled'", "data-state='error'", "data-state='loading'"]
        }
    },
    
    "design_token_system": {
        "description": "Single source of truth for all design values",
        "principles": [
            "All CSS values MUST come from tokens via var() function",
            "No magic numbers or hardcoded values permitted",
            "Tokens MUST follow semantic naming: --mcs-[category]-[property]-[variant]",
            "All tokens defined in tokens.css file"
        ],
        "token_categories": {
            "color": "All color values including states and feedback",
            "typography": "Font families, sizes, weights, line heights",
            "spacing": "Margins, padding, gaps based on 4px/8px grid", 
            "dimensions": "Border widths, radii, shadows",
            "effects": "Transitions, animations, z-index"
        }
    },
    
    "atomic_design_taxonomy": {
        "description": "Component classification system governing composition",
        "levels": {
            "atom": {
                "definition": "Smallest indivisible functional unit",
                "composition_rule": "Cannot contain other components",
                "examples": ["Button", "Input", "Label", "Icon"]
            },
            "molecule": {
                "definition": "Group of atoms forming simple reusable component",
                "composition_rule": "Composed of atoms only, cannot contain organisms",
                "examples": ["Search Form", "Card", "Navigation Link"]
            },
            "organism": {
                "definition": "Complex component forming distinct interface section",
                "composition_rule": "Can contain atoms, molecules, and other organisms",
                "examples": ["Header", "Data Grid", "Modal", "Sidebar"]
            }
        }
    }
}

print("MCSS Core Principles (Immutable Foundation)")
print("==========================================")
print(json.dumps(core_principles, indent=2))