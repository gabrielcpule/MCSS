"""Run full 100-prompt MCSS-BENCHMARK-V1 against minimal compendium."""
import json, re, time
from pathlib import Path
from anthropic import Anthropic

BENCHMARK = Path("/home/gabrielp/Projects/MCSS/Benchmark/labs/MCSS-BENCHMARK-V1.md")
COMPENDIUM = Path("/home/gabrielp/Projects/MCSS/research/data/CONTEXT_COMPENDIUM_v2_minimal.md")
RESULTS_DIR = Path("/home/gabrielp/Projects/MCSS/research/data")

def extract_prompts():
    """Extract all PROMPT: lines from the benchmark file."""
    text = BENCHMARK.read_text()
    prompts = []

    # Find all PROMPT: patterns with their task IDs
    pattern = re.compile(r'\*\*(G-\d+-\d+|M-\d+-\d+|C-\d+-\d+):.*?\*\*\n```\nPROMPT: (.*?)(?:\n\nGOLD STANDARD:|```)', re.DOTALL)
    matches = pattern.findall(text)

    for task_id, prompt_text in matches:
        prompt_text = prompt_text.strip()
        # Determine task type
        if task_id.startswith('G-'):
            task_type = 'gen'
        elif task_id.startswith('M-'):
            task_type = 'mod'
        else:
            task_type = 'comp'
        prompts.append((task_id, task_type, prompt_text))

    # Also try simpler extraction for prompts without gold standards
    simple_pattern = re.compile(r'\*\*(G-\d+-\d+|M-\d+-\d+|C-\d+-\d+):.*?\*\*\n```\nPROMPT: (.*?)```', re.DOTALL)
    simple_matches = simple_pattern.findall(text)

    # Merge using task_id to deduplicate
    seen = set()
    all_prompts = []
    for task_id, task_type, prompt_text in prompts:
        if task_id not in seen:
            seen.add(task_id)
            all_prompts.append((task_id, task_type, prompt_text))

    # Add any from simple extraction not already captured
    for task_id, prompt_text in simple_matches:
        if task_id not in seen:
            seen.add(task_id)
            if task_id.startswith('G-'):
                task_type = 'gen'
            elif task_id.startswith('M-'):
                task_type = 'mod'
            else:
                task_type = 'comp'
            all_prompts.append((task_id, task_type, prompt_text.strip()))

    # Sort by ID
    all_prompts.sort(key=lambda x: x[0])

    gen_count = sum(1 for _, t, _ in all_prompts if t == 'gen')
    mod_count = sum(1 for _, t, _ in all_prompts if t == 'mod')
    comp_count = sum(1 for _, t, _ in all_prompts if t == 'comp')

    print(f"Extracted {len(all_prompts)} prompts: {gen_count} gen, {mod_count} mod, {comp_count} comp")
    return all_prompts

def score(output, task_type):
    """Minimal annotation scoring (H3-optimized)."""
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
    failures = [n for n, p in checks if not p]
    return passed, failures

def run_full_benchmark(prompts, model="claude-sonnet-4-6"):
    client = Anthropic()
    system = COMPENDIUM.read_text()
    print(f"Compendium: {COMPENDIUM.name} ({len(system.split())} words)")
    print(f"Model: {model}")
    print(f"Prompts: {len(prompts)}")
    print("-" * 50)

    results = {"gen": {"pass": 0, "total": 0, "failures": []},
               "mod": {"pass": 0, "total": 0, "failures": []},
               "comp": {"pass": 0, "total": 0, "failures": []}}
    total_in, total_out = 0, 0

    for i, (pid, cat, ptext) in enumerate(prompts):
        try:
            resp = client.messages.create(
                model=model, max_tokens=4096, temperature=0.1,
                thinking={"type": "disabled"}, system=system,
                messages=[{"role": "user", "content": ptext}]
            )
            text_blocks = [b for b in resp.content if b.type == 'text']
            output = text_blocks[0].text if text_blocks else ""
            passed, failures = score(output, cat)

            results[cat]["total"] += 1
            if passed:
                results[cat]["pass"] += 1
            else:
                results[cat]["failures"].append({"id": pid, "failures": failures})
            total_in += resp.usage.input_tokens
            total_out += resp.usage.output_tokens

            status = "PASS" if passed else f"FAIL({','.join(failures[:2])})"
            pct = (i + 1) / len(prompts) * 100
            print(f"[{i+1:3d}/100 {pct:3.0f}%] {pid} {status}")

        except Exception as e:
            print(f"[{i+1:3d}/100] {pid} ERROR: {e}")
            results[cat]["total"] += 1
            results[cat]["failures"].append({"id": pid, "failures": [str(e)]})

        time.sleep(1.1)  # ~55 req/min to stay under rate limits

    gen = results["gen"]["pass"] / max(results["gen"]["total"], 1)
    mod = results["mod"]["pass"] / max(results["mod"]["total"], 1)
    comp = results["comp"]["pass"] / max(results["comp"]["total"], 1)
    weighted = gen * 0.4 + mod * 0.4 + comp * 0.2

    return {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "model": model,
        "compendium": str(COMPENDIUM),
        "prompts_total": len(prompts),
        "generation": {"rate": gen, "pass": results["gen"]["pass"], "total": results["gen"]["total"],
                       "failures": results["gen"]["failures"]},
        "modification": {"rate": mod, "pass": results["mod"]["pass"], "total": results["mod"]["total"],
                         "failures": results["mod"]["failures"]},
        "comprehension": {"rate": comp, "pass": results["comp"]["pass"], "total": results["comp"]["total"],
                          "failures": results["comp"]["failures"]},
        "weighted_accuracy": weighted,
        "input_tokens": total_in,
        "output_tokens": total_out,
        "total_tokens": total_in + total_out,
    }

if __name__ == '__main__':
    print("MCSS Full Benchmark — 100 Prompts")
    print("=" * 50)

    prompts = extract_prompts()
    if len(prompts) < 50:
        print(f"WARNING: Only {len(prompts)} prompts extracted. Expected 100.")
        print("Check regex patterns in the benchmark file.")
        # Fallback: manually list known prompts
        pass

    result = run_full_benchmark(prompts)

    print(f"\n{'='*50}")
    print("FULL BENCHMARK RESULTS")
    print(f"{'='*50}")
    print(f"Generation:     {result['generation']['rate']:.1%} ({result['generation']['pass']}/{result['generation']['total']})")
    print(f"Modification:   {result['modification']['rate']:.1%} ({result['modification']['pass']}/{result['modification']['total']})")
    print(f"Comprehension:  {result['comprehension']['rate']:.1%} ({result['comprehension']['pass']}/{result['comprehension']['total']})")
    print(f"{'-'*40}")
    print(f"WEIGHTED:       {result['weighted_accuracy']:.1%}")
    print(f"Total tokens:   {result['total_tokens']:,}")
    print(f"Avg tok/prompt: {result['total_tokens'] / result['prompts_total']:.0f}")

    out_path = RESULTS_DIR / f"full_benchmark_{time.strftime('%Y%m%d_%H%M%S')}.json"
    Path(out_path).write_text(json.dumps(result, indent=2))
    print(f"\nSaved: {out_path}")
