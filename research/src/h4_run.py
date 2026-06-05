"""H4: Minimum viable compendium — micro (148w) vs minimal (607w)"""
import json, re, time
from pathlib import Path
from anthropic import Anthropic

RESEARCH = Path("/home/gabrielp/Projects/MCSS/research")
MICRO = RESEARCH / "data/CONTEXT_COMPENDIUM_v2_micro.md"
MINIMAL = RESEARCH / "data/CONTEXT_COMPENDIUM_v2_minimal.md"
RESULTS = RESEARCH / "data"

PROMPTS = [
    ("G-001-01", "gen", "Generate a c-avatar component (mcs:Atom) that displays a user's profile image with fallback initials. Include proper RDFa annotations and support for small, medium, and large sizes via data-state."),
    ("G-001-02", "gen", "Create a c-badge component (mcs:Atom) for displaying status indicators with semantic color states (success, warning, error, info)."),
    ("G-001-03", "gen", "Generate a c-button component (mcs:Atom) with primary, secondary, outline, and ghost variants via data-variant. Include loading, disabled, and error states via data-state."),
    ("G-002-01", "gen", "Generate a c-search-form molecule component that combines a text input, search button, and optional filter dropdown. Include proper composition annotations with mcs:hasPart."),
    ("M-001-01", "mod", "Given a c-button component styled with var(--color-background-brand), modify it to add a 'loading' state that shows a spinner and disables interaction. Use data-state, not class modifiers."),
    ("M-001-02", "mod", "Add an 'error' state to the c-input component. The error state should show a red border and red focus ring. Use data-state=\"error\"."),
    ("M-002-01", "mod", "Modify the c-button--primary variant to use the semantic 'success' color tokens instead of the brand primary tokens. All values must use var()."),
    ("M-003-01", "mod", "Enhance the c-navigation component with comprehensive ARIA labels and keyboard navigation support. Use aria-label, role=\"navigation\", and aria-current=\"page\"."),
    ("C-001-01", "comp", "Given a c-card component with typeof=\"mcs:Component\", property=\"mcs:taxonomyLevel\" content=\"mcs:Molecule\", elements c-card__header, c-card__body, c-card__footer, all linked via mcs:hasPart — explain its purpose, constituent parts, and semantic annotations."),
    ("C-002-01", "comp", "Examine a c-dropdown component with data-state=\"open\", aria-expanded, and data-mcs-triggers-event=\"mcss:dropdown:toggled\". Explain its complete interaction model including state management and accessibility."),
]

def score(output, task_type):
    checks = []
    checks.append(("comp-class", bool(re.search(r'\bc-[a-z]', output))))
    checks.append(("tokens", bool(re.search(r'var\(--', output))))
    checks.append(("data-state", bool(re.search(r'data-state', output))))
    if task_type == "gen":
        checks.append(("typeof", bool(re.search(r'typeof="mcs:Component"', output))))
        checks.append(("taxonomy", bool(re.search(r'mcs:taxonomyLevel', output))))
    if task_type in ("gen", "mod"):
        clean = re.sub(r'/\*.*?\*/', '', output, flags=re.DOTALL)
        violation = bool(re.search(r'\.c-[a-z][a-zA-Z]*\s*\{[^}]*\b(margin|margin-top|margin-bottom|margin-left|margin-right)\s*:', clean))
        checks.append(("golden-rule", not violation))
    passed = all(p for _, p in checks)
    return passed

def run(name, compendium_path, model="claude-sonnet-4-6"):
    client = Anthropic()
    system = compendium_path.read_text()
    results = {"gen": [0, 0], "mod": [0, 0], "comp": [0, 0]}
    total_tok = 0

    print(f"\n{'='*50}")
    print(f"H4: {name} ({len(system.split())} words)")
    print(f"{'='*50}")

    for pid, cat, ptext in PROMPTS:
        resp = client.messages.create(
            model=model, max_tokens=4096, temperature=0.1,
            thinking={"type": "disabled"}, system=system,
            messages=[{"role": "user", "content": ptext}]
        )
        text_blocks = [b for b in resp.content if b.type == 'text']
        output = text_blocks[0].text if text_blocks else ""
        passed = score(output, cat)

        results[cat][1] += 1
        if passed: results[cat][0] += 1
        total_tok += resp.usage.input_tokens + resp.usage.output_tokens

        print(f"  [{pid}] {'PASS' if passed else 'FAIL'}")
        time.sleep(1.2)

    gen = results["gen"][0] / results["gen"][1]
    mod = results["mod"][0] / results["mod"][1]
    comp = results["comp"][0] / results["comp"][1]
    w = gen * 0.4 + mod * 0.4 + comp * 0.2
    print(f"  Gen={gen:.0%} Mod={mod:.0%} Comp={comp:.0%} | W={w:.0%} | {total_tok} tok")
    return {"name": name, "words": len(system.split()), "weighted": w, "gen": gen, "mod": mod, "comp": comp, "total_tokens": total_tok}

if __name__ == '__main__':
    a = run("Micro (148w)", MICRO)
    time.sleep(2)
    b = run("Minimal (607w)", MINIMAL)

    print(f"\n{'='*55}")
    print("H4 RESULTS: Minimum Viable Compendium")
    print(f"{'='*55}")
    print(f"{'':<22} {'Micro':>10} {'Minimal':>10} {'Delta':>10}")
    print(f"{'Weighted':<22} {a['weighted']:>10.0%} {b['weighted']:>10.0%} {b['weighted']-a['weighted']:>+10.0%}")
    print(f"{'Generation':<22} {a['gen']:>10.0%} {b['gen']:>10.0%} {b['gen']-a['gen']:>+10.0%}")
    print(f"{'Modification':<22} {a['mod']:>10.0%} {b['mod']:>10.0%} {b['mod']-a['mod']:>+10.0%}")
    print(f"{'Comprehension':<22} {a['comp']:>10.0%} {b['comp']:>10.0%} {b['comp']-a['comp']:>+10.0%}")
    print(f"{'Total Tokens':<22} {a['total_tokens']:>10} {b['total_tokens']:>10} {b['total_tokens']-a['total_tokens']:>+10}")

    out = {"experiment": "H4", "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"), "results": [a, b]}
    out_path = RESULTS / f"h4_results_{time.strftime('%Y%m%d_%H%M%S')}.json"
    Path(out_path).write_text(json.dumps(out, indent=2))
    print(f"\nSaved: {out_path}")
