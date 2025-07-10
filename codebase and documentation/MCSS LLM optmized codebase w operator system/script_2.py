# Create the LLM Agent Framework for MCSS
llm_agent_framework = {
    "mcss_agent_system": {
        "description": "Multi-agent system for MCSS understanding, generation, and validation",
        "core_constraint": "All agents MUST preserve MCSS core principles and never violate immutable rules",
        
        "agents": {
            "mcss_validator_agent": {
                "purpose": "Validate all MCSS code against core principles",
                "responsibilities": [
                    "Check semantic annotation completeness",
                    "Validate layer architecture compliance", 
                    "Verify ontological naming convention",
                    "Ensure token-only CSS values",
                    "Validate atomic design taxonomy"
                ],
                "tools": ["eslint-plugin-mcss", "sparql-validator", "css-analyzer"],
                "constraints": [
                    "REJECT any code violating MCSS immutable rules",
                    "NEVER approve hardcoded CSS values",
                    "ENFORCE RDFa annotation completeness"
                ]
            },
            
            "mcss_generator_agent": {
                "purpose": "Generate new MCSS components following all conventions",
                "responsibilities": [
                    "Create semantic HTML with full RDFa annotations",
                    "Generate token-driven CSS",
                    "Ensure proper layer assignment",
                    "Follow atomic design taxonomy",
                    "Create accessibility compliant code"
                ],
                "tools": ["component-templates", "token-database", "rdfa-schema"],
                "constraints": [
                    "ALWAYS use tokens for CSS values",
                    "NEVER violate Golden Rule (no external margins on components)",
                    "REQUIRE full semantic annotation on all components"
                ]
            },
            
            "mcss_analyzer_agent": {
                "purpose": "Analyze and understand existing MCSS codebases",
                "responsibilities": [
                    "Parse semantic annotations into knowledge graph",
                    "Identify component relationships and dependencies",
                    "Extract design patterns and conventions",
                    "Map component hierarchy via RDFa",
                    "Generate component documentation"
                ],
                "tools": ["rdfa-parser", "sparql-query-engine", "graph-analyzer"],
                "output_formats": ["knowledge-graph", "component-map", "dependency-tree"]
            },
            
            "mcss_optimizer_agent": {
                "purpose": "Improve MCSS code while preserving semantics",
                "responsibilities": [
                    "Optimize CSS performance without changing semantics",
                    "Suggest token consolidation opportunities",
                    "Identify redundant or unused styles",
                    "Propose accessibility improvements",
                    "Recommend component composition refinements"
                ],
                "tools": ["css-optimizer", "token-analyzer", "accessibility-checker"],
                "constraints": [
                    "NEVER change semantic meaning",
                    "PRESERVE all RDFa annotations",
                    "MAINTAIN layer architecture integrity"
                ]
            },
            
            "mcss_educator_agent": {
                "purpose": "Teach MCSS principles and assist developers",
                "responsibilities": [
                    "Explain MCSS concepts and rationale",
                    "Provide examples and tutorials",
                    "Guide developers through best practices",
                    "Answer questions about implementation",
                    "Generate learning materials"
                ],
                "tools": ["example-database", "tutorial-generator", "concept-explainer"],
                "knowledge_areas": [
                    "semantic_imperative",
                    "rdfa_annotations", 
                    "layer_architecture",
                    "token_system",
                    "atomic_design"
                ]
            }
        },
        
        "agent_coordination": {
            "validation_pipeline": [
                "generator_agent creates component",
                "validator_agent checks compliance", 
                "optimizer_agent suggests improvements",
                "validator_agent re-checks optimized version",
                "educator_agent documents rationale"
            ],
            
            "analysis_pipeline": [
                "analyzer_agent parses existing code",
                "analyzer_agent builds knowledge graph",
                "educator_agent explains patterns found",
                "optimizer_agent suggests improvements",
                "validator_agent ensures improvements are valid"
            ]
        }
    },
    
    "llm_interface_protocols": {
        "description": "Standardized interfaces for LLM interaction with MCSS",
        
        "input_formats": {
            "component_request": {
                "schema": {
                    "component_name": "string",
                    "taxonomy_level": "atom|molecule|organism", 
                    "purpose": "string",
                    "required_props": "array",
                    "states": "array",
                    "behaviors": "array"
                },
                "example": {
                    "component_name": "SearchBox",
                    "taxonomy_level": "molecule",
                    "purpose": "Allow users to input search queries",
                    "required_props": ["placeholder", "value"],
                    "states": ["default", "focused", "error"],
                    "behaviors": ["submit-search", "clear-input"]
                }
            },
            
            "validation_request": {
                "schema": {
                    "html_content": "string",
                    "css_content": "string", 
                    "validation_level": "strict|standard|lenient"
                }
            },
            
            "analysis_request": {
                "schema": {
                    "codebase_path": "string",
                    "analysis_type": "full|components|tokens|layers",
                    "output_format": "json|rdf|markdown"
                }
            }
        },
        
        "output_formats": {
            "component_output": {
                "html": "Fully annotated HTML with RDFa",
                "css": "Token-driven CSS with layer assignment",
                "behavior_contract": "Markdown file for complex interactions",
                "tests": "Accessibility and validation tests",
                "documentation": "Usage examples and rationale"
            },
            
            "validation_output": {
                "is_valid": "boolean",
                "violations": "array of violation objects",
                "suggestions": "array of improvement suggestions",
                "compliance_score": "0-100 numeric score"
            },
            
            "analysis_output": {
                "knowledge_graph": "RDF/JSON-LD representation",
                "component_inventory": "List of all components with metadata",
                "token_usage": "Token usage statistics and optimization opportunities",
                "architecture_health": "Assessment of layer architecture compliance"
            }
        }
    },
    
    "adaptive_learning_system": {
        "description": "System for LLMs to learn and adapt MCSS usage patterns",
        
        "learning_mechanisms": {
            "pattern_recognition": "Identify successful MCSS patterns from codebases",
            "best_practice_extraction": "Learn optimal implementations from validated code", 
            "error_prevention": "Build knowledge of common mistakes and how to avoid them",
            "context_adaptation": "Adapt recommendations based on project context"
        },
        
        "knowledge_accumulation": {
            "validated_patterns": "Library of proven MCSS implementations",
            "anti_patterns": "Documented bad practices to avoid",
            "context_rules": "When to apply specific patterns or exceptions",
            "optimization_strategies": "Performance and maintainability improvements"
        },
        
        "feedback_loops": {
            "validation_feedback": "Learn from validation successes and failures",
            "user_feedback": "Incorporate developer preferences and constraints",
            "performance_feedback": "Learn from real-world performance data",
            "accessibility_feedback": "Improve based on accessibility testing results"
        }
    }
}

print("MCSS LLM Agent Framework")
print("========================")
print(json.dumps(llm_agent_framework, indent=2))