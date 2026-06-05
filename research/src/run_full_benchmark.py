"""Run the full 100-prompt benchmark."""
import json, re, time
from pathlib import Path
from anthropic import Anthropic

COMPENDIUM = Path("/home/gabrielp/Projects/MCSS/research/data/CONTEXT_COMPENDIUM_v2_minimal.md")
PROMPTS_FILE = Path("/home/gabrielp/Projects/MCSS/research/data/benchmark_prompts_100.json")
RESULTS_DIR = Path("/home/gabrielp/Projects/MCSS/research/data")

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
    failures = [n for n, p in checks if not p]
    return passed, failures

if __name__ == '__main__':
    prompts = json.loads(PROMPTS_FILE.read_text())
    prompts = [(pid, cat, text) for pid, cat, text in prompts]

    client = Anthropic()
    system = COMPENDIUM.read_text()

    print(f"Full 100-Prompt Benchmark")
    print(f"Compendium: {len(system.split())} words")
    print(f"Prompts: {len(prompts)}")
    print("=" * 55)

    results = {"gen": [0, 0, []], "mod": [0, 0, []], "comp": [0, 0, []]}
    total_tok = 0
    start = time.time()

    for i, (pid, cat, ptext) in enumerate(prompts):
        try:
            resp = client.messages.create(
                model="claude-sonnet-4-6", max_tokens=4096, temperature=0.1,
                thinking={"type": "disabled"}, system=system,
                messages=[{"role": "user", "content": ptext}]
            )
            text_blocks = [b for b in resp.content if b.type == 'text']
            output = text_blocks[0].text if text_blocks else ""
            passed, failures = score(output, cat)

            results[cat][1] += 1
            if passed:
                results[cat][0] += 1
            else:
                results[cat][2].append({"id": pid, "failures": failures})
            total_tok += resp.usage.input_tokens + resp.usage.output_tokens

            elapsed = time.time() - start
            rate = (i + 1) / elapsed * 60
            pct = (i + 1) / len(prompts) * 100
            status = "PASS" if passed else f"FAIL({','.join(failures[:2])})"
            print(f"[{i+1:3d}/100 {pct:3.0f}%] {pid} {status} | {rate:.0f}/min")

        except Exception as e:
            print(f"[{i+1:3d}/100] {pid} ERROR: {e}")
            results[cat][1] += 1
            results[cat][2].append({"id": pid, "failures": [str(e)]})

        time.sleep(1.0)

    elapsed = time.time() - start
    gen_r = results["gen"][0] / results["gen"][1]
    mod_r = results["mod"][0] / results["mod"][1]
    comp_r = results["comp"][0] / results["comp"][1]
    w = gen_r * 0.4 + mod_r * 0.4 + comp_r * 0.2

    print(f"\n{'='*55}")
    print(f"FULL 100-PROMPT BENCHMARK RESULTS")
    print(f"{'='*55}")
    print(f"Generation:     {gen_r:.1%} ({results['gen'][0]}/{results['gen'][1]})")
    print(f"Modification:   {mod_r:.1%} ({results['mod'][0]}/{results['mod'][1]})")
    print(f"Comprehension:  {comp_r:.1%} ({results['comp'][0]}/{results['comp'][1]})")
    print(f"{'-'*45}")
    print(f"WEIGHTED ACC:   {w:.1%}")
    print(f"Total tokens:   {total_tok:,}")
    print(f"Time:           {elapsed:.0f}s ({elapsed/60:.1f}m)")
    print(f"Avg tok/prompt: {total_tok/100:.0f}")

    out = {
        "experiment": "FULL_BENCHMARK",
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "compendium": "minimal (607 words)",
        "model": "claude-sonnet-4-6",
        "weighted_accuracy": w,
        "generation": {"rate": gen_r, "pass": results["gen"][0], "total": results["gen"][1], "failures": results["gen"][2]},
        "modification": {"rate": mod_r, "pass": results["mod"][0], "total": results["mod"][1], "failures": results["mod"][2]},
        "comprehension": {"rate": comp_r, "pass": results["comp"][0], "total": results["comp"][1], "failures": results["comp"][2]},
        "total_tokens": total_tok,
        "elapsed_seconds": elapsed,
    }
    out_path = RESULTS_DIR / f"full_benchmark_100_{time.strftime('%Y%m%d_%H%M%S')}.json"
    Path(out_path).write_text(json.dumps(out, indent=2))
    print(f"\nSaved: {out_path}")
