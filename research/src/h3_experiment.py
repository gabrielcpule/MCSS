#!/usr/bin/env python3
"""H3: Annotation density — test 3 compendium variants."""
import json, re, time
from pathlib import Path
from anthropic import Anthropic

BASE = Path("/home/gabrielp/Projects/MCSS/research")
COMPENDIUM_V2 = BASE / "data/CONTEXT_COMPENDIUM_v2.md"
RESULTS_DIR = BASE / "data"

PROMPTS = [
    {"id": "G-001-01", "type": "generation", "text": "Generate a c-avatar component (mcs:Atom) that displays a user's profile image with fallback initials. Include proper RDFa annotations and support for small, medium, and large sizes via data-state."},
    {"id": "G-001-02", "type": "generation", "text": "Create a c-badge component (mcs:Atom) for displaying status indicators with semantic color states (success, warning, error, info)."},
    {"id": "G-001-03", "type": "generation", "text": "Generate a c-button component (mcs:Atom) with primary, secondary, outline, and ghost variants via data-variant. Include loading, disabled, and error states via data-state."},
    {"id": "G-002-01", "type": "generation", "text": "Generate a c-search-form molecule component that combines a text input, search button, and optional filter dropdown. Include proper composition annotations with mcs:hasPart."},
    {"id": "M-001-01", "type": "modification", "text": "Given a c-button component styled with var(--color-background-brand), modify it to add a 'loading' state that shows a spinner and disables interaction. Use data-state, not class modifiers."},
    {"id": "M-001-02", "type": "modification", "text": "Add an 'error' state to the c-input component. The error state should show a red border and red focus ring. Use data-state=\"error\"."},
    {"id": "M-002-01", "type": "modification", "text": "Modify the c-button--primary variant to use the semantic 'success' color tokens instead of the brand primary tokens. All values must use var()."},
    {"id": "M-003-01", "type": "modification", "text": "Enhance the c-navigation component with comprehensive ARIA labels and keyboard navigation support. Use aria-label, role=\"navigation\", and aria-current=\"page\"."},
    {"id": "C-001-01", "type": "comprehension", "text": "Given a c-card component with typeof=\"mcs:Component\", property=\"mcs:taxonomyLevel\" content=\"mcs:Molecule\", elements c-card__header, c-card__body, c-card__footer, all linked via mcs:hasPart — explain its purpose, constituent parts, and semantic annotations."},
    {"id": "C-002-01", "type": "comprehension", "text": "Examine a c-dropdown component with data-state=\"open\", aria-expanded, and data-mcs-triggers-event=\"mcss:dropdown:toggled\". Explain its complete interaction model including state management and accessibility."},
]
TYPE_MAP = {"generation": "gen", "modification": "mod", "comprehension": "comp"}

def build_variants():
    """Build minimal, standard, and verbose compendiums from the v2 base."""
    base_text = COMPENDIUM_V2.read_text()

    # Minimal: Remove purpose requirement, hasPart, behavioral attrs
    minimal = base_text.replace(
        '- property="mcs:purpose" content="description"',
        '- property="mcs:purpose" content="description" (OPTIONAL — not required)')
    minimal = re.sub(r'### Molecular Composition.*?(?=###|\Z)', '', minimal, flags=re.DOTALL)
    minimal = re.sub(r'### Behavioral Attributes.*?(?=###|\Z)', '', minimal, flags=re.DOTALL)
    minimal = re.sub(r'5\. Every component has typeof.*?\n', '5. Every component has typeof and taxonomyLevel\n', minimal)

    # Verbose: Strengthen requirements
    verbose = base_text.replace(
        'Every component MUST have:',
        'Every component MUST have ALL of the following (all required, none optional):')
    verbose += """
## Additional Required Annotations (ALL mandatory)

In addition to typeof, taxonomyLevel, and purpose, every component MUST include:

1. property="mcs:componentName" content="human-readable name"
2. data-mcs-interaction-type — one of: click, hover, submission, toggle, drag, focus, input, visual-indicator
3. data-mcs-consequence — what happens when activated
4. ARIA attributes synced with data-state (e.g., aria-disabled when data-state="disabled")
5. For molecules: every child MUST have property="mcs:hasPart" resource="#unique-id"

Components missing ANY of these will fail validation.
"""

    variants = {
        "minimal": minimal,
        "standard": base_text,
        "verbose": verbose
    }

    for name, text in variants.items():
        path = RESULTS_DIR / f"CONTEXT_COMPENDIUM_v2_{name}.md"
        path.write_text(text)
        print(f"  {name}: {len(text.split())} words (~{len(text.split())*2.5:.0f} tokens)")

    return variants

def score(output, task_type, variant):
    """Score with variant-appropriate checks."""
    checks = []

    # Universal checks
    has_component = bool(re.search(r'\bc-[a-z]', output))
    checks.append(("Component class", has_component))
    has_tokens = bool(re.search(r'var\(--', output))
    checks.append(("Token usage", has_tokens))
    has_data_state = bool(re.search(r'data-state', output))
    checks.append(("data-state usage", has_data_state))

    # RDFa checks — variant-dependent
    if task_type == "generation":
        checks.append(("RDFa typeof", bool(re.search(r'typeof="mcs:Component"', output))))
        checks.append(("RDFa taxonomy", bool(re.search(r'mcs:taxonomyLevel', output))))

        if variant == "standard" or variant == "verbose":
            checks.append(("RDFa purpose", bool(re.search(r'mcs:purpose', output))))

        if variant == "verbose":
            checks.append(("RDFa componentName", bool(re.search(r'mcs:componentName', output))))
            checks.append(("Behavioral attrs", bool(re.search(r'data-mcs-interaction-type', output))))
            checks.append(("ARIA sync", bool(re.search(r'aria-', output))))

    # Comprehension checks — does the LLM discuss annotations?
    if task_type == "comprehension" and variant == "verbose":
        checks.append(("Discusses annotations", bool(re.search(r'(annotation|RDFa|metadata|semantic)', output, re.IGNORECASE))))

    # Golden Rule (all variants)
    if task_type in ("generation", "modification"):
        output_clean = re.sub(r'/\*.*?\*/', '', output, flags=re.DOTALL)
        golden_violation = bool(re.search(r'\.c-[a-z][a-zA-Z]*\s*\{[^}]*\b(margin|margin-top|margin-bottom|margin-left|margin-right)\s*:', output_clean))
        checks.append(("Golden Rule (no margin)", not golden_violation))

    passed = all(p for _, p in checks)
    return passed, [name for name, p in checks if not p]

def run_variant(name, variant_text, model="claude-sonnet-4-6"):
    client = Anthropic()
    results = {"gen": {"pass": 0, "total": 0}, "mod": {"pass": 0, "total": 0}, "comp": {"pass": 0, "total": 0}}
    total_in, total_out = 0, 0

    print(f"\n{'='*50}")
    print(f"H3: {name.upper()} annotations ({len(variant_text.split())} words)")
    print(f"{'='*50}")

    for i, p in enumerate(PROMPTS):
        response = client.messages.create(
            model=model, max_tokens=4096, temperature=0.1,
            thinking={"type": "disabled"},
            system=variant_text,
            messages=[{"role": "user", "content": p["text"]}]
        )
        text_blocks = [b for b in response.content if b.type == 'text']
        output = text_blocks[0].text if text_blocks else ""
        passed, fails = score(output, p["type"], name)

        cat = TYPE_MAP[p["type"]]
        results[cat]["total"] += 1
        if passed: results[cat]["pass"] += 1
        total_in += response.usage.input_tokens
        total_out += response.usage.output_tokens

        status = "PASS" if passed else f"FAIL ({', '.join(fails[:2])})"
        print(f"[{i+1}/10] {p['id']} {status}")
        time.sleep(1.2)

    gen = results["gen"]["pass"] / results["gen"]["total"]
    mod = results["mod"]["pass"] / results["mod"]["total"]
    comp = results["comp"]["pass"] / results["comp"]["total"]
    weighted = gen * 0.4 + mod * 0.4 + comp * 0.2

    print(f"  Gen={gen:.0%} Mod={mod:.0%} Comp={comp:.0%} | Weighted={weighted:.0%} | Tokens={total_in+total_out}")
    return {"variant": name, "weighted": weighted, "gen": gen, "mod": mod, "comp": comp,
            "input_tokens": total_in, "output_tokens": total_out, "total_tokens": total_in + total_out}

if __name__ == '__main__':
    print("Building 3 compendium variants...")
    variants = build_variants()

    print("\nRunning experiments...")
    results = []
    for name in ["minimal", "standard", "verbose"]:
        r = run_variant(name, variants[name])
        results.append(r)
        time.sleep(2)

    print(f"\n{'='*65}")
    print("H3 RESULTS: Annotation Density Impact")
    print(f"{'='*65}")
    print(f"{'Metric':<25} {'Minimal':<13} {'Standard':<13} {'Verbose':<13}")
    print(f"{'-'*64}")
    print(f"{'Weighted Accuracy':<25} {results[0]['weighted']:<13.0%} {results[1]['weighted']:<13.0%} {results[2]['weighted']:<13.0%}")
    print(f"{'Generation':<25} {results[0]['gen']:<13.0%} {results[1]['gen']:<13.0%} {results[2]['gen']:<13.0%}")
    print(f"{'Modification':<25} {results[0]['mod']:<13.0%} {results[1]['mod']:<13.0%} {results[2]['mod']:<13.0%}")
    print(f"{'Comprehension':<25} {results[0]['comp']:<13.0%} {results[1]['comp']:<13.0%} {results[2]['comp']:<13.0%}")
    print(f"{'Total Tokens':<25} {results[0]['total_tokens']:<13} {results[1]['total_tokens']:<13} {results[2]['total_tokens']:<13}")

    out = {"experiment": "H3", "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"), "results": results}
    out_path = RESULTS_DIR / f"h3_results_{time.strftime('%Y%m%d_%H%M%S')}.json"
    Path(out_path).write_text(json.dumps(out, indent=2))
    print(f"\nSaved: {out_path}")
