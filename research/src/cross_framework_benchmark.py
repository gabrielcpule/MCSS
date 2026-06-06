#!/usr/bin/env python3
"""Cross-framework benchmark: MCSS vs Tailwind on the same 100 prompts."""
import json, re, time
from pathlib import Path
from anthropic import Anthropic

BASE = Path("/home/gabrielp/Projects/MCSS/research")
PROMPTS_FILE = BASE / "data/benchmark_prompts_100.json"
MCSS_COMPENDIUM = BASE / "data/CONTEXT_COMPENDIUM_v2_minimal.md"
TAILWIND_COMPENDIUM = BASE / "data/CONTEXT_COMPENDIUM_tailwind.md"
RESULTS_DIR = BASE / "data"

def score_mcss(output, task_type):
    """MCSS scoring (from established benchmark)."""
    checks = []
    checks.append(("c-class", bool(re.search(r'\bc-[a-z]', output))))
    checks.append(("var-tokens", bool(re.search(r'var\(--', output))))
    checks.append(("data-state", bool(re.search(r'data-state', output))))
    if task_type == "gen":
        checks.append(("typeof", bool(re.search(r'typeof="mcs:Component"', output))))
        checks.append(("taxonomy", bool(re.search(r'mcs:taxonomyLevel', output))))
    if task_type in ("gen", "mod"):
        clean = re.sub(r'/\*.*?\*/', '', output, flags=re.DOTALL)
        violation = bool(re.search(r'\.c-[a-z][a-zA-Z]*\s*\{[^}]*\b(margin|margin-top|margin-bottom|margin-left|margin-right)\s*:', clean))
        checks.append(("golden-rule", not violation))
    return all(p for _, p in checks), [n for n, p in checks if not p]

def score_tailwind(output, task_type):
    """Tailwind scoring — utility-first criteria."""
    checks = []
    # Uses Tailwind utility classes (at least 3 distinct ones)
    tw_classes = re.findall(r'\b(flex|grid|block|inline|hidden|p-\d|px-\d|py-\d|m-\d|mt-\d|mb-\d|w-|h-|bg-|text-|font-|rounded|shadow|border|gap-|space-|items-|justify-|max-w|ring-|outline-|opacity|transition|duration|hover:|focus:|disabled:|sm:|md:|lg:|xl:)', output)
    has_utilities = len(set(tw_classes)) >= 3
    checks.append(("utility-classes", has_utilities))

    # No bare CSS declarations (should use utilities, not raw CSS)
    has_raw_css = bool(re.search(r'\b[\w-]+\s*:\s*[^;]+;', output))
    checks.append(("no-raw-css", not has_raw_css or "class=" in output))

    # Semantic HTML elements
    has_semantic = bool(re.search(r'<(button|nav|main|header|footer|section|article|form|label|input)', output))
    checks.append(("semantic-html", has_semantic))

    # Responsive prefixes for layout
    if task_type == "gen":
        has_responsive = bool(re.search(r'(sm|md|lg|xl):', output))
        checks.append(("responsive", has_responsive or "container" in output or "mx-auto" in output))

    # Interactive states
    has_states = bool(re.search(r'(hover|focus|disabled|active):', output))
    checks.append(("state-variants", has_states or task_type != "gen"))

    # Accessibility basics
    has_a11y = bool(re.search(r'(aria-|role=|alt=|sr-only|focus-visible)', output))
    checks.append(("accessibility", has_a11y))

    return all(p for _, p in checks), [n for n, p in checks if not p]

def run_framework(name, compendium_path, score_fn, model="claude-sonnet-4-6"):
    client = Anthropic()
    system = compendium_path.read_text()
    prompts = json.loads(PROMPTS_FILE.read_text())
    prompts = [(pid, cat, text) for pid, cat, text in prompts]

    print(f"\n{'='*55}")
    print(f"{name} — {len(prompts)} prompts")
    print(f"Compendium: {compendium_path.name} ({len(system.split())} words)")
    print(f"{'='*55}")

    results = {"gen": [0, 0, []], "mod": [0, 0, []], "comp": [0, 0, []]}
    total_tok = 0
    start = time.time()

    for i, (pid, cat, ptext) in enumerate(prompts):
        resp = client.messages.create(
            model=model, max_tokens=4096, temperature=0.1,
            thinking={"type": "disabled"}, system=system,
            messages=[{"role": "user", "content": ptext}]
        )
        output = "".join(b.text for b in resp.content if b.type == 'text')
        passed, failures = score_fn(output, cat)

        results[cat][1] += 1
        if passed: results[cat][0] += 1
        else: results[cat][2].append({"id": pid, "failures": failures})
        total_tok += resp.usage.input_tokens + resp.usage.output_tokens

        elapsed = time.time() - start
        pct = (i+1)/len(prompts)*100
        status = "PASS" if passed else f"FAIL({','.join(failures[:2])})"
        print(f"[{i+1:3d}/100 {pct:3.0f}%] {pid} {status} | {elapsed:.0f}s")

        time.sleep(1.0)

    gen_r = results["gen"][0] / results["gen"][1]
    mod_r = results["mod"][0] / results["mod"][1]
    comp_r = results["comp"][0] / results["comp"][1]
    w = gen_r * 0.4 + mod_r * 0.4 + comp_r * 0.2

    print(f"\n{name} RESULTS:")
    print(f"  Gen={gen_r:.1%} ({results['gen'][0]}/{results['gen'][1]})")
    print(f"  Mod={mod_r:.1%} ({results['mod'][0]}/{results['mod'][1]})")
    print(f"  Comp={comp_r:.1%} ({results['comp'][0]}/{results['comp'][1]})")
    print(f"  Weighted={w:.1%}")
    print(f"  Tokens={total_tok:,} ({total_tok/100:.0f}/prompt)")

    return {"name": name, "gen": gen_r, "mod": mod_r, "comp": comp_r,
            "weighted": w, "total_tokens": total_tok, "results": results}

if __name__ == '__main__':
    # MCSS already done — load from saved
    import glob
    mcss_files = sorted(glob.glob(str(RESULTS_DIR / "full_benchmark_100_*.json")))
    if mcss_files:
        mcss = json.loads(Path(mcss_files[-1]).read_text())
        mcss_result = {
            "name": "MCSS",
            "gen": mcss["generation"]["rate"],
            "mod": mcss["modification"]["rate"],
            "comp": mcss["comprehension"]["rate"],
            "weighted": mcss["weighted_accuracy"],
            "total_tokens": mcss["total_tokens"],
        }
        print(f"Loaded MCSS results: {mcss_result['weighted']:.1%}")
    else:
        print("No MCSS results found — run full benchmark first")

    # Run Tailwind
    tw = run_framework("Tailwind CSS", TAILWIND_COMPENDIUM, score_tailwind)

    # Comparison
    print(f"\n{'='*65}")
    print(f"CROSS-FRAMEWORK COMPARISON")
    print(f"{'='*65}")
    print(f"{'Metric':<22} {'MCSS':>10} {'Tailwind':>10} {'Delta':>10}")
    print(f"{'-'*52}")
    for metric in ["weighted", "gen", "mod", "comp"]:
        if metric in mcss_result:
            m = mcss_result[metric]
            t = tw[metric]
            d = t - m
            print(f"{metric:<22} {m:>10.1%} {t:>10.1%} {d:>+10.1%}")
    print(f"total_tokens        {mcss_result['total_tokens']:>10,} {tw['total_tokens']:>10,} {tw['total_tokens']-mcss_result['total_tokens']:>+10,}")

    out = {"experiment": "CROSS_FRAMEWORK", "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
           "mcss": mcss_result, "tailwind": tw}
    out_path = RESULTS_DIR / f"cross_framework_{time.strftime('%Y%m%d_%H%M%S')}.json"
    Path(out_path).write_text(json.dumps(out, indent=2))
    print(f"\nSaved: {out_path}")
