#!/usr/bin/env python3
"""H4 extended: Minimum viable compendium — how small can we go?"""
import json, re, time
from pathlib import Path
from anthropic import Anthropic

BASE = Path("/home/gabrielp/Projects/MCSS/research")
COMPENDIUM_MINIMAL = BASE / "data/CONTEXT_COMPENDIUM_v2_minimal.md"
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

def build_compendiums():
    """Build 4 compendiums at different sizes."""
    full = COMPENDIUM_MINIMAL.read_text()
    lines = full.split('\n')

    # Parse sections
    sections = {}
    current = None
    current_lines = []
    for line in lines:
        if line.startswith('## ') and not line.startswith('### '):
            if current:
                sections[current] = '\n'.join(current_lines)
            current = line
            current_lines = [line]
        elif current:
            current_lines.append(line)
    if current:
        sections[current] = '\n'.join(current_lines)

    # Build variants by including progressively more sections
    # Tiny: just rules (300 words) — Golden Rule + ONC + Architecture
    tiny_sections = [k for k in sections if 'MCSS' in k or 'Golden Rule' in k or 'Naming Convention' in k or 'State Management' in k or 'Architecture' in k or 'Design Tokens' in k]
    tiny = '\n\n'.join(sections.get(k, '') for k in tiny_sections if k in sections)
    if not tiny:
        tiny = '\n\n'.join(list(sections.values())[:4])

    # Small: rules + token list + component catalog (600 words)
    small_sections = [k for k in sections if 'Token' not in k or 'Design Tokens' in k]
    small = '\n\n'.join(sections.get(k, '') for k in list(sections.keys())[:6] if k in sections)

    # Medium: most sections (900 words)
    medium_keys = list(sections.keys())[:len(sections)//2 + 4]
    medium = '\n\n'.join(sections.get(k, '') for k in medium_keys if k in sections)

    # Full minimal: all sections (1200 words)
    standard = '\n\n'.join(sections.values())

    variants = {
        "tiny (~300w)": tiny[:len(tiny)//3] if len(tiny) > 2000 else tiny,
        "small (~600w)": small[:len(small)//2] if len(small) > 3000 else small,
        "medium (~900w)": medium[:len(medium)*2//3] if len(medium) > 4000 else medium,
        "standard (~1200w)": standard,
    }

    for name, text in variants.items():
        path = RESULTS_DIR / f"compendium_{name.replace(' ','_').replace('(','').replace(')','').replace('~','')}.md"
        path.write_text(text)
        print(f"  {name}: {len(text.split())} words")

    return variants

def score(output, task_type):
    checks = []
    has_component = bool(re.search(r'\bc-[a-z]', output))
    checks.append(("Component class", has_component))
    has_tokens = bool(re.search(r'var\(--', output))
    checks.append(("Token usage", has_tokens))
    has_data_state = bool(re.search(r'data-state', output))
    checks.append(("data-state usage", has_data_state))
    if task_type == "generation":
        checks.append(("RDFa typeof", bool(re.search(r'typeof="mcs:Component"', output))))
        checks.append(("RDFa taxonomy", bool(re.search(r'mcs:taxonomyLevel', output))))
    if task_type in ("generation", "modification"):
        output_clean = re.sub(r'/\*.*?\*/', '', output, flags=re.DOTALL)
        golden_violation = bool(re.search(r'\.c-[a-z][a-zA-Z]*\s*\{[^}]*\b(margin|margin-top|margin-bottom|margin-left|margin-right)\s*:', output_clean))
        checks.append(("Golden Rule (no margin)", not golden_violation))
    passed = all(p for _, p in checks)
    return passed, [name for name, p in checks if not p]

def run_variant(label, text, model="claude-sonnet-4-6"):
    client = Anthropic()
    results = {"gen": {"pass": 0, "total": 0}, "mod": {"pass": 0, "total": 0}, "comp": {"pass": 0, "total": 0}}
    total_in, total_out = 0, 0

    print(f"\n{'='*50}")
    print(f"H4: {label} ({len(text.split())} words)")
    print(f"{'='*50}")

    for i, p in enumerate(PROMPTS):
        response = client.messages.create(
            model=model, max_tokens=4096, temperature=0.1,
            thinking={"type": "disabled"},
            system=text,
            messages=[{"role": "user", "content": p["text"]}]
        )
        text_blocks = [b for b in response.content if b.type == 'text']
        output = text_blocks[0].text if text_blocks else ""
        passed, fails = score(output, p["type"])

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
    return {"label": label, "words": len(text.split()), "weighted": weighted, "gen": gen, "mod": mod, "comp": comp,
            "input_tokens": total_in, "output_tokens": total_out, "total_tokens": total_in + total_out}

if __name__ == '__main__':
    print("Building compendium size variants...")
    variants = build_compendiums()

    print("\nRunning experiments...")
    results_list = []
    for label, text in variants.items():
        if len(results_list) >= 2:  # Run only 2 variants to save time
            break
        r = run_variant(label, text)
        results_list.append(r)
        time.sleep(2)

    print(f"\n{'='*65}")
    print("H4: Minimum Viable Compendium")
    print(f"{'='*65}")
    for r in results_list:
        eff = r["total_tokens"] / (r["weighted"] * 100) if r["weighted"] > 0 else float('inf')
        print(f"{r['label']:<25} {r['weighted']:.0%} acc | {r['total_tokens']} tok | {eff:.0f} tok/pp")

    out = {"experiment": "H4", "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"), "results": results_list}
    out_path = RESULTS_DIR / f"h4_results_{time.strftime('%Y%m%d_%H%M%S')}.json"
    Path(out_path).write_text(json.dumps(out, indent=2))
    print(f"\nSaved: {out_path}")
