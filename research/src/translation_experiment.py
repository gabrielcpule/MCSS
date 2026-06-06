#!/usr/bin/env python3
"""H6: Framework translation ability — Tailwind/Bootstrap → MCSS."""
import json, re, time
from pathlib import Path
from anthropic import Anthropic

BASE = Path("/home/gabrielp/Projects/MCSS/research")
MCSS_COMPENDIUM = BASE / "data/CONTEXT_COMPENDIUM_v2_minimal.md"
RESULTS_DIR = BASE / "data"

# Real Tailwind components from the project's POC files
TAILWIND_COMPONENTS = [
    {
        "id": "T-001",
        "name": "Login Form",
        "source": "Tailwind CSS",
        "component": """<div class="flex min-h-full flex-col justify-center px-6 py-12 lg:px-8">
  <div class="sm:mx-auto sm:w-full sm:max-w-sm">
    <h2 class="mt-10 text-center text-2xl/9 font-bold tracking-tight text-gray-900">Sign in to your account</h2>
  </div>
  <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
    <form class="space-y-6">
      <div>
        <label for="email" class="block text-sm/6 font-medium text-gray-900">Email address</label>
        <input type="email" id="email" class="block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:outline-indigo-600 sm:text-sm/6" required>
      </div>
      <div>
        <label for="password" class="block text-sm/6 font-medium text-gray-900">Password</label>
        <input type="password" id="password" class="block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:outline-indigo-600 sm:text-sm/6" required>
      </div>
      <div class="flex items-center justify-between">
        <div>
          <a href="#" class="font-semibold text-indigo-600 hover:text-indigo-500">Forgot password?</a>
        </div>
      </div>
      <button type="submit" class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm/6 font-semibold text-white shadow-xs hover:bg-indigo-500 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Sign in</button>
    </form>
  </div>
</div>"""
    },
    {
        "id": "T-002",
        "name": "Card Component",
        "source": "Tailwind CSS",
        "component": """<div class="bg-white overflow-hidden shadow rounded-lg">
  <div class="px-4 py-5 sm:px-6 border-b border-gray-200">
    <h3 class="text-lg leading-6 font-medium text-gray-900">Card Title</h3>
  </div>
  <div class="px-4 py-5 sm:p-6">
    <p class="text-sm text-gray-500">This is the main content area of the card. It can contain text, images, or other components.</p>
  </div>
  <div class="px-4 py-4 sm:px-6 bg-gray-50 border-t border-gray-200">
    <button class="inline-flex items-center px-3 py-2 border border-transparent text-sm leading-4 font-medium rounded-md text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500">Action</button>
  </div>
</div>"""
    },
    {
        "id": "T-003",
        "name": "Navigation Bar",
        "source": "Tailwind CSS",
        "component": """<nav class="bg-white border-b border-gray-200" aria-label="Main Navigation">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="flex justify-between h-16">
      <div class="flex">
        <div class="flex-shrink-0 flex items-center">
          <img class="block lg:hidden h-8 w-auto" src="/logo.svg" alt="Company">
        </div>
        <div class="hidden sm:ml-6 sm:flex sm:space-x-8">
          <a href="/home" class="border-indigo-500 text-gray-900 inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium">Home</a>
          <a href="/about" class="border-transparent text-gray-500 hover:border-gray-300 hover:text-gray-700 inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium">About</a>
          <a href="/contact" class="border-transparent text-gray-500 hover:border-gray-300 hover:text-gray-700 inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium">Contact</a>
        </div>
      </div>
    </div>
  </div>
</nav>"""
    },
    {
        "id": "T-004",
        "name": "Data Table",
        "source": "Tailwind CSS",
        "component": """<div class="overflow-hidden shadow ring-1 ring-black ring-opacity-5 rounded-lg">
  <table class="min-w-full divide-y divide-gray-300">
    <thead class="bg-gray-50">
      <tr>
        <th scope="col" class="py-3.5 pl-4 pr-3 text-left text-sm font-semibold text-gray-900 sm:pl-6">Name</th>
        <th scope="col" class="px-3 py-3.5 text-left text-sm font-semibold text-gray-900">Title</th>
        <th scope="col" class="px-3 py-3.5 text-left text-sm font-semibold text-gray-900">Status</th>
        <th scope="col" class="relative py-3.5 pl-3 pr-4 sm:pr-6"><span class="sr-only">Edit</span></th>
      </tr>
    </thead>
    <tbody class="divide-y divide-gray-200 bg-white">
      <tr>
        <td class="whitespace-nowrap py-4 pl-4 pr-3 text-sm font-medium text-gray-900 sm:pl-6">Lindsay Walton</td>
        <td class="whitespace-nowrap px-3 py-4 text-sm text-gray-500">Front-end Developer</td>
        <td class="whitespace-nowrap px-3 py-4 text-sm text-gray-500"><span class="inline-flex items-center rounded-full bg-green-100 px-2 py-1 text-xs font-medium text-green-700">Active</span></td>
        <td class="relative whitespace-nowrap py-4 pl-3 pr-4 text-right text-sm font-medium sm:pr-6"><a href="#" class="text-indigo-600 hover:text-indigo-900">Edit</a></td>
      </tr>
    </tbody>
  </table>
</div>"""
    },
    {
        "id": "T-005",
        "name": "Alert Message",
        "source": "Tailwind CSS",
        "component": """<div class="rounded-md bg-green-50 p-4">
  <div class="flex">
    <div class="flex-shrink-0">
      <svg class="h-5 w-5 text-green-400" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>
    </div>
    <div class="ml-3">
      <p class="text-sm font-medium text-green-800">Successfully saved</p>
      <p class="mt-2 text-sm text-green-700">Your changes have been saved successfully.</p>
    </div>
    <div class="ml-auto pl-3">
      <button type="button" class="inline-flex rounded-md bg-green-50 p-1.5 text-green-500 hover:bg-green-100 focus:outline-none focus:ring-2 focus:ring-green-600 focus:ring-offset-2 focus:ring-offset-green-50">
        <span class="sr-only">Dismiss</span>
        <svg class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor"><path d="M6.28 5.22a.75.75 0 00-1.06 1.06L8.94 10l-3.72 3.72a.75.75 0 101.06 1.06L10 11.06l3.72 3.72a.75.75 0 101.06-1.06L11.06 10l3.72-3.72a.75.75 0 00-1.06-1.06L10 8.94 6.28 5.22z"/></svg>
      </button>
    </div>
  </div>
</div>"""
    },
]

def score_translation(output, original_name):
    """Score MCSS translation quality."""
    checks = []

    # Structural checks (must pass)
    checks.append(("c-prefix", bool(re.search(r'\bc-[a-z]', output))))
    checks.append(("var-tokens", bool(re.search(r'var\(--', output))))
    checks.append(("data-state", bool(re.search(r'data-state', output))))
    checks.append(("typeof", bool(re.search(r'typeof="mcs:Component"', output))))
    checks.append(("taxonomy", bool(re.search(r'mcs:taxonomyLevel', output))))

    # Quality checks
    clean = re.sub(r'/\*.*?\*/', '', output, flags=re.DOTALL)
    golden_ok = not bool(re.search(r'\.c-[a-z][a-zA-Z]*\s*\{[^}]*\b(margin|margin-top|margin-bottom|margin-left|margin-right)\s*:', clean))
    checks.append(("golden-rule", golden_ok))

    # BEM structure (elements use __)
    has_bem = bool(re.search(r'\bc-\w+__\w+', output))
    checks.append(("bem-elements", has_bem or "mcs:Atom" in output))  # Atoms don't need BEM elements

    # No Tailwind remnants
    has_tailwind = bool(re.search(r'\b(bg-\w+-\d+|text-\w+-\d+|px-\d|py-\d|mt-\d|space-y-|sm:|md:|lg:|hover:bg-)', output))
    checks.append(("no-tailwind-remnants", not has_tailwind))

    # CSS included (not just HTML)
    has_css = bool(re.search(r'[{]\s*[\w-]+\s*:', output) or '/*' in output)
    checks.append(("includes-css", has_css))

    return all(p for _, p in checks), [n for n, p in checks if not p]

if __name__ == '__main__':
    client = Anthropic()
    system = MCSS_COMPENDIUM.read_text()

    print(f"Framework Translation Experiment")
    print(f"Translating {len(TAILWIND_COMPONENTS)} Tailwind components → MCSS")
    print(f"{'='*55}")

    results = []
    total_tok = 0
    for comp in TAILWIND_COMPONENTS:
        prompt = f"""Translate this {comp['source']} component to MCSS (Model Context Style Sheet).

Original {comp['source']} {comp['name']}:
```html
{comp['component']}
```

Generate the equivalent MCSS component with:
1. HTML using c-* classes with BEM naming (c-block__element--modifier)
2. RDFa annotations (typeof="mcs:Component", mcs:taxonomyLevel, mcs:purpose)
3. CSS using var(--tokens) for all values, no magic numbers
4. data-state attributes for all states (not class modifiers)
5. No external margins on root component selectors (Golden Rule)
6. For molecules: use mcs:hasPart for composition relationships"""

        print(f"\n[{comp['id']}] {comp['name']}...", end=" ", flush=True)

        resp = client.messages.create(
            model="claude-sonnet-4-6", max_tokens=4096, temperature=0.1,
            thinking={"type": "disabled"}, system=system,
            messages=[{"role": "user", "content": prompt}]
        )
        output = "".join(b.text for b in resp.content if b.type == 'text')
        passed, failures = score_translation(output, comp['name'])
        total_tok += resp.usage.input_tokens + resp.usage.output_tokens

        status = "PASS" if passed else f"FAIL({','.join(failures[:3])})"
        print(status)

        results.append({
            "id": comp["id"], "name": comp["name"], "source": comp["source"],
            "passed": passed, "failures": failures,
            "input_tokens": resp.usage.input_tokens,
            "output_tokens": resp.usage.output_tokens,
            "output": output[:500]  # Save first 500 chars for analysis
        })

        time.sleep(1.2)

    passed = sum(1 for r in results if r["passed"])
    rate = passed / len(results)
    print(f"\n{'='*55}")
    print(f"TRANSLATION RESULTS: {rate:.0%} ({passed}/{len(results)})")
    print(f"{'='*55}")
    for r in results:
        s = "✓" if r["passed"] else f"✗ ({', '.join(r['failures'][:2])})"
        print(f"  {r['id']} {r['name']}: {s}")

    out = {"experiment": "TRANSLATION", "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
           "pass_rate": rate, "total": len(results), "passed": passed,
           "total_tokens": total_tok, "results": results}
    out_path = RESULTS_DIR / f"translation_{time.strftime('%Y%m%d_%H%M%S')}.json"
    Path(out_path).write_text(json.dumps(out, indent=2))
    print(f"\nSaved: {out_path}")
