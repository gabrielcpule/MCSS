#!/usr/bin/env python3
"""
MCSS-BENCHMARK-V1 Runner
Sends benchmark prompts to Claude API, scores responses against gold standards.
"""
import json, os, time, re
from pathlib import Path
from datetime import datetime
from anthropic import Anthropic

BENCHMARK_DIR = Path("/home/gabrielp/Projects/MCSS/Benchmark/labs")
COMPENDIUM = Path("/home/gabrielp/Projects/MCSS/research/data/CONTEXT_COMPENDIUM_v2.md")
RESULTS_DIR = Path("/home/gabrielp/Projects/MCSS/research/data")
EXPERIMENT_DIR = Path("/home/gabrielp/Projects/MCSS/research/experiments/h1-baseline-reproduction")

class BenchmarkRunner:
    def __init__(self, model="claude-sonnet-4-6"):
        self.client = Anthropic()
        self.model = model
        self.system_prompt = COMPENDIUM.read_text()
        self.results = {
            "experiment": "H1",
            "model": model,
            "timestamp": datetime.now().isoformat(),
            "prompts_run": 0,
            "generation": {"passed": 0, "total": 0, "results": []},
            "modification": {"passed": 0, "total": 0, "results": []},
            "comprehension": {"passed": 0, "total": 0, "results": []},
        }

    def run_prompt(self, prompt_id, prompt_text, gold_standard="", task_type="generation"):
        """Send a single prompt to Claude and return the response."""
        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=4096,
                temperature=0.1,
                thinking={"type": "disabled"},
                system=self.system_prompt,
                messages=[{"role": "user", "content": prompt_text}]
            )
            # Handle thinking blocks — find the text response
            text_blocks = [b for b in response.content if b.type == 'text']
            output = text_blocks[0].text if text_blocks else response.content[0].text
            input_tokens = response.usage.input_tokens
            output_tokens = response.usage.output_tokens

            return {
                "prompt_id": prompt_id,
                "task_type": task_type,
                "prompt": prompt_text[:200],
                "output": output,
                "input_tokens": input_tokens,
                "output_tokens": output_tokens,
                "gold_standard": gold_standard[:200],
            }
        except Exception as e:
            return {
                "prompt_id": prompt_id,
                "task_type": task_type,
                "error": str(e),
            }

    def score_response(self, result):
        """Score a single response against validation rules."""
        if "error" in result:
            return False, f"API error: {result['error']}"

        output = result.get("output", "")
        task_type = result.get("task_type", "")

        checks = []

        # Check 1: Contains c-* class (component layer prefix)
        has_component = bool(re.search(r'\bc-[a-z]', output))
        checks.append(("Component class", has_component))

        # Check 2: Uses var(--token) for values (no magic numbers)
        has_tokens = bool(re.search(r'var\(--', output))
        has_magic = bool(re.search(r'(?<!var\()\b\d+px\b|\b\d+rem\b', output))
        checks.append(("Token usage", has_tokens))

        # Check 3: Uses data-state (not class modifiers for state)
        has_data_state = bool(re.search(r'data-state', output))
        has_class_state = bool(re.search(r'--(disabled|loading|error|active|checked|open|closed)', output))
        checks.append(("data-state usage", has_data_state or not has_class_state))

        # Check 4: Has RDFa annotations (generation tasks)
        if task_type == "generation":
            has_typeof = bool(re.search(r'typeof="mcs:Component"', output))
            has_taxonomy = bool(re.search(r'mcs:taxonomyLevel', output))
            has_purpose = bool(re.search(r'mcs:purpose', output))
            checks.append(("RDFa typeof", has_typeof))
            checks.append(("RDFa taxonomy", has_taxonomy))
            checks.append(("RDFa purpose", has_purpose))

        # Check 5: No margin on root c-* rules (Golden Rule)
        if task_type in ("generation", "modification"):
            # Strip CSS comments first
            output_no_comments = re.sub(r'/\*.*?\*/', '', output, flags=re.DOTALL)
            # Only match actual margin DECLARATIONS (margin: or margin-top: etc.), not comments
            # Only match root c-* selectors (no __ elements), not comments
            golden_violation = bool(re.search(r'\.c-[a-z][a-zA-Z]*\s*\{[^}]*\b(margin|margin-top|margin-bottom|margin-left|margin-right)\s*:', output_no_comments))
            checks.append(("Golden Rule (no margin)", not golden_violation))

        passed = all(p for _, p in checks)
        failed_checks = [name for name, p in checks if not p]

        return passed, failed_checks

    def run_benchmark(self, prompts, max_prompts=None):
        """Run a set of prompts through the benchmark."""
        if max_prompts:
            prompts = prompts[:max_prompts]

        for i, prompt in enumerate(prompts):
            print(f"[{i+1}/{len(prompts)}] {prompt['id']}...", end=" ", flush=True)

            result = self.run_prompt(
                prompt["id"],
                prompt["text"],
                prompt.get("gold_standard", ""),
                prompt["type"]
            )
            passed, details = self.score_response(result)
            result["passed"] = passed
            result["score_details"] = details

            category = prompt["type"]
            self.results[f"{category}"]["total"] += 1
            if passed:
                self.results[f"{category}"]["passed"] += 1
            self.results[f"{category}"]["results"].append(result)
            self.results["prompts_run"] += 1

            status = "PASS" if passed else f"FAIL ({', '.join(details[:2])})"
            print(status)

            # Rate limit: 1 request/sec
            time.sleep(1.5)

        return self.compute_score()

    def compute_score(self):
        """Compute weighted accuracy."""
        gen = self.results["generation"]
        mod = self.results["modification"]
        comp = self.results["comprehension"]

        gen_rate = gen["passed"] / max(gen["total"], 1)
        mod_rate = mod["passed"] / max(mod["total"], 1)
        comp_rate = comp["passed"] / max(comp["total"], 1)

        weighted = (gen_rate * 0.4) + (mod_rate * 0.4) + (comp_rate * 0.2)
        self.results["scores"] = {
            "generation_rate": round(gen_rate, 3),
            "modification_rate": round(mod_rate, 3),
            "comprehension_rate": round(comp_rate, 3),
            "weighted_accuracy": round(weighted, 3),
        }
        return self.results["scores"]

    def save_results(self):
        """Save results to disk."""
        out = RESULTS_DIR / f"h1_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        out.write_text(json.dumps(self.results, indent=2))
        print(f"\nResults saved to {out}")
        print(f"Weighted accuracy: {self.results['scores']['weighted_accuracy']:.1%}")
        return out


# Small validation subset (10 prompts: 4 gen, 4 mod, 2 comp)
VALIDATION_PROMPTS = [
    # Generation
    {"id": "G-001-01", "type": "generation", "text": "Generate a c-avatar component (mcs:Atom) that displays a user's profile image with fallback initials. Include proper RDFa annotations and support for small, medium, and large sizes via data-state."},
    {"id": "G-001-02", "type": "generation", "text": "Create a c-badge component (mcs:Atom) for displaying status indicators with semantic color states (success, warning, error, info)."},
    {"id": "G-001-03", "type": "generation", "text": "Generate a c-button component (mcs:Atom) with primary, secondary, outline, and ghost variants via data-variant. Include loading, disabled, and error states via data-state."},
    {"id": "G-002-01", "type": "generation", "text": "Generate a c-search-form molecule component that combines a text input, search button, and optional filter dropdown. Include proper composition annotations with mcs:hasPart."},
    # Modification
    {"id": "M-001-01", "type": "modification", "text": "Given a c-button component styled with var(--color-background-brand), modify it to add a 'loading' state that shows a spinner and disables interaction. Use data-state, not class modifiers."},
    {"id": "M-001-02", "type": "modification", "text": "Add an 'error' state to the c-input component. The error state should show a red border and red focus ring. Use data-state=\"error\"."},
    {"id": "M-002-01", "type": "modification", "text": "Modify the c-button--primary variant to use the semantic 'success' color tokens instead of the brand primary tokens. All values must use var()."},
    {"id": "M-003-01", "type": "modification", "text": "Enhance the c-navigation component with comprehensive ARIA labels and keyboard navigation support. Use aria-label, role=\"navigation\", and aria-current=\"page\"."},
    # Comprehension
    {"id": "C-001-01", "type": "comprehension", "text": "Given a c-card component with typeof=\"mcs:Component\", property=\"mcs:taxonomyLevel\" content=\"mcs:Molecule\", elements c-card__header, c-card__body, c-card__footer, all linked via mcs:hasPart — explain its purpose, constituent parts, and semantic annotations."},
    {"id": "C-002-01", "type": "comprehension", "text": "Examine a c-dropdown component with data-state=\"open\", aria-expanded, and data-mcs-triggers-event=\"mcss:dropdown:toggled\". Explain its complete interaction model including state management and accessibility."},
]

if __name__ == '__main__':
    print("MCSS Benchmark Runner — H1 Baseline Reproduction")
    print(f"Model: claude-sonnet-4-6")
    print(f"System prompt: {COMPENDIUM} ({COMPENDIUM.read_text().count(' ')} words)")
    print(f"Prompts: {len(VALIDATION_PROMPTS)} (validation subset)")
    print("-" * 50)

    runner = BenchmarkRunner()
    scores = runner.run_benchmark(VALIDATION_PROMPTS)
    runner.save_results()

    print(f"\n{'='*50}")
    print(f"H1 Baseline: {scores['weighted_accuracy']:.1%}")
    print(f"  Generation:     {scores['generation_rate']:.1%}")
    print(f"  Modification:   {scores['modification_rate']:.1%}")
    print(f"  Comprehension:  {scores['comprehension_rate']:.1%}")
