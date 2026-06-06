#!/usr/bin/env python3
"""Fair cross-framework comparison + bidirectional translation."""
import json, re, time
from pathlib import Path
from anthropic import Anthropic

BASE = Path("/home/gabrielp/Projects/MCSS/research")
MCSS_COMPENDIUM = BASE / "data/CONTEXT_COMPENDIUM_v2_minimal.md"
TW_COMPENDIUM = BASE / "data/CONTEXT_COMPENDIUM_tailwind.md"
RESULTS_DIR = BASE / "data"

# Framework-agnostic prompts — what a real developer would ask
DEV_PROMPTS = [
    ("P01", "Build a login form with email field, password field, a 'Forgot password?' link, and a Sign In button."),
    ("P02", "Create a card component with a title, description text, and an action button at the bottom."),
    ("P03", "Build a navigation bar with a logo on the left, and Home/About/Contact links on the right."),
    ("P04", "Create an alert message for success notifications. Include a dismiss button."),
    ("P05", "Build a pagination component showing page numbers with previous/next buttons."),
    ("P06", "Create a dropdown menu that opens on click with a list of action items."),
    ("P07", "Build a data table with Name, Title, and Status columns. Include a header row and one data row."),
    ("P08", "Create a breadcrumb navigation showing Home > Products > Category > Item."),
    ("P09", "Build a search form with a text input and a Search button side by side."),
    ("P10", "Create a modal dialog with a title, body text, Cancel and Confirm buttons."),
    ("P11", "Build a toggle switch component for settings on/off."),
    ("P12", "Create a progress bar showing 60% completion with a label."),
    ("P13", "Build a badge/tag component for displaying status labels like 'Active', 'Pending', 'Closed'."),
    ("P14", "Create a user avatar component showing a profile picture with the user's name below it."),
    ("P15", "Build a set of tabs with three tab headers and corresponding content panels."),
    ("P16", "Create a tooltip that appears on hover above an element."),
    ("P17", "Build a file upload area with a drop zone and a 'Choose File' button."),
    ("P18", "Create a loading spinner with a 'Loading...' text below it."),
    ("P19", "Build a notification toast that slides in from the top-right corner."),
    ("P20", "Create a sidebar layout with navigation links on the left and main content on the right."),
]

# MCSS scoring (framework's own rules)
def score_mcss(output):
    checks = []
    checks.append(("c-classes", bool(re.search(r'\bc-[a-z]', output))))
    checks.append(("var-tokens", bool(re.search(r'var\(--', output))))
    checks.append(("data-state", bool(re.search(r'data-state', output))))
    checks.append(("typeof", bool(re.search(r'typeof="mcs:Component"', output))))
    checks.append(("taxonomy", bool(re.search(r'mcs:taxonomyLevel', output))))
    clean = re.sub(r'/\*.*?\*/', '', output, flags=re.DOTALL)
    golden = not bool(re.search(r'\.c-[a-z][a-zA-Z]*\s*\{[^}]*\b(margin|margin-top|margin-bottom|margin-left|margin-right)\s*:', clean))
    checks.append(("golden-rule", golden))
    has_css = bool(re.search(r'[{]\s*[\w-]+\s*:', output))
    checks.append(("includes-css", has_css))
    has_bem = bool(re.search(r'\bc-\w+__\w+', output))
    checks.append(("bem-elements", has_bem or "mcs:Atom" in output))
    return all(p for _, p in checks), [n for n, p in checks if not p], checks

# Tailwind scoring (framework's own rules)
def score_tailwind(output):
    checks = []
    tw_classes = re.findall(r'\b(flex|grid|block|inline|hidden|p-\d|px-\d|py-\d|m-\d|mt-\d|mb-\d|ml-\d|mr-\d|w-|h-|bg-|text-|font-|rounded|shadow|border|gap-|space-|items-|justify-|max-w|ring-|outline-|opacity|transition|duration|hover:|focus:|disabled:|active:|sm:|md:|lg:|xl:|divide-|whitespace-|leading-|tracking-)', output)
    checks.append(("utility-classes", len(set(tw_classes)) >= 4))
    checks.append(("semantic-html", bool(re.search(r'<(button|nav|main|header|footer|section|article|form|label|input|table)', output))))
    checks.append(("state-variants", bool(re.search(r'(hover:|focus:|disabled:|active:|focus-visible:)', output))))
    checks.append(("responsive", bool(re.search(r'(sm:|md:|lg:|xl:)', output)) or "container" in output or "mx-auto" in output))
    checks.append(("accessibility", bool(re.search(r'(aria-|role=|alt=|sr-only|focus-visible:)', output))))
    # No bare CSS (should use utilities)
    raw_css = bool(re.search(r'\b[\w-]+\s*:\s*[^;]+;', output))
    checks.append(("utility-first", not raw_css or "class=" in output))
    # No inline styles
    inline = bool(re.search(r'style="[^"]*:\s*[^"]*"', output))
    checks.append(("no-inline-styles", not inline))
    return all(p for _, p in checks), [n for n, p in checks if not p], checks

# MCSS→Tailwind translation components (from our framework)
MCSS_COMPONENTS = [
    {
        "id": "R-001", "name": "Login Form",
        "component": """<form class="c-login-form" typeof="mcs:Component" property="mcs:taxonomyLevel" content="mcs:Molecule" property="mcs:purpose" content="User authentication form">
  <div class="c-login-form__field">
    <label class="c-label" for="email">Email</label>
    <input class="c-input" type="email" id="email" data-state="default">
  </div>
  <div class="c-login-form__field">
    <label class="c-label" for="password">Password</label>
    <input class="c-input" type="password" id="password" data-state="default">
  </div>
  <a class="c-link" href="#" data-variant="subtle">Forgot password?</a>
  <button class="c-button c-login-form__submit" data-variant="primary" data-state="default">Sign In</button>
</form>"""
    },
    {
        "id": "R-002", "name": "Card",
        "component": """<div class="c-card" typeof="mcs:Component" property="mcs:taxonomyLevel" content="mcs:Molecule" property="mcs:purpose" content="Content container">
  <header class="c-card__header"><h3 class="c-text c-text--heading">Card Title</h3></header>
  <div class="c-card__body"><p class="c-text" data-state="body">Card description text goes here.</p></div>
  <footer class="c-card__footer"><button class="c-button" data-variant="primary">Action</button></footer>
</div>"""
    },
    {
        "id": "R-003", "name": "Alert",
        "component": """<div class="c-alert" typeof="mcs:Component" property="mcs:taxonomyLevel" content="mcs:Molecule" property="mcs:purpose" content="Success feedback" data-state="success">
  <span class="c-alert__icon"><svg class="c-icon" data-state="small">...</svg></span>
  <span class="c-alert__content">Successfully saved!</span>
  <button class="c-alert__dismiss" aria-label="Dismiss">×</button>
</div>"""
    },
]

if __name__ == '__main__':
    client = Anthropic()
    mcss_system = MCSS_COMPENDIUM.read_text()
    tw_system = TW_COMPENDIUM.read_text()

    print("="*60)
    print("FAIR CROSS-FRAMEWORK COMPARISON")
    print(f"20 framework-agnostic prompts × 2 frameworks")
    print(f"Scoring: each framework scored against its OWN rules")
    print("="*60)

    # Part 1: Cross-framework
    fw_results = {"MCSS": {"pass": 0, "total": 0, "tokens": 0, "scores": []},
                  "Tailwind": {"pass": 0, "total": 0, "tokens": 0, "scores": []}}

    for pid, prompt in DEV_PROMPTS:
        # MCSS
        resp = client.messages.create(
            model="claude-sonnet-4-6", max_tokens=4096, temperature=0.1,
            thinking={"type": "disabled"}, system=mcss_system,
            messages=[{"role": "user", "content": prompt}]
        )
        mcss_out = "".join(b.text for b in resp.content if b.type == 'text')
        mcss_pass, mcss_fails, mcss_checks = score_mcss(mcss_out)
        fw_results["MCSS"]["total"] += 1
        if mcss_pass: fw_results["MCSS"]["pass"] += 1
        fw_results["MCSS"]["tokens"] += resp.usage.input_tokens + resp.usage.output_tokens
        fw_results["MCSS"]["scores"].append({"id": pid, "pass": mcss_pass, "checks": mcss_checks})

        time.sleep(0.8)

        # Tailwind
        resp = client.messages.create(
            model="claude-sonnet-4-6", max_tokens=4096, temperature=0.1,
            thinking={"type": "disabled"}, system=tw_system,
            messages=[{"role": "user", "content": prompt}]
        )
        tw_out = "".join(b.text for b in resp.content if b.type == 'text')
        tw_pass, tw_fails, tw_checks = score_tailwind(tw_out)
        fw_results["Tailwind"]["total"] += 1
        if tw_pass: fw_results["Tailwind"]["pass"] += 1
        fw_results["Tailwind"]["tokens"] += resp.usage.input_tokens + resp.usage.output_tokens
        fw_results["Tailwind"]["scores"].append({"id": pid, "pass": tw_pass, "checks": tw_checks})

        print(f"[{pid}] MCSS={'✓' if mcss_pass else '✗'} Tailwind={'✓' if tw_pass else '✗'}")
        time.sleep(0.8)

    mcss_rate = fw_results["MCSS"]["pass"] / 20
    tw_rate = fw_results["Tailwind"]["pass"] / 20

    print(f"\n{'='*50}")
    print(f"CROSS-FRAMEWORK RESULTS (Framework Compliance Rate)")
    print(f"{'='*50}")
    print(f"MCSS:     {mcss_rate:.0%} ({fw_results['MCSS']['pass']}/20) | {fw_results['MCSS']['tokens']:,} tok")
    print(f"Tailwind: {tw_rate:.0%} ({fw_results['Tailwind']['pass']}/20) | {fw_results['Tailwind']['tokens']:,} tok")

    # Analyze which checks failed most
    for fw, name in [("MCSS", "MCSS"), ("Tailwind", "Tailwind")]:
        fail_counts = {}
        for s in fw_results[fw]["scores"]:
            if not s["pass"]:
                for check_name, check_pass in s["checks"]:
                    if not check_pass:
                        fail_counts[check_name] = fail_counts.get(check_name, 0) + 1
        if fail_counts:
            print(f"\n{name} failure modes:")
            for k, v in sorted(fail_counts.items(), key=lambda x: -x[1]):
                print(f"  {k}: {v}")

    # Part 2: Reverse Translation (MCSS → Tailwind)
    print(f"\n{'='*60}")
    print(f"REVERSE TRANSLATION: MCSS → Tailwind")
    print(f"{'='*60}")

    trans_results = []
    for comp in MCSS_COMPONENTS:
        prompt = f"""Translate this MCSS component to Tailwind CSS.

MCSS {comp['name']}:
```html
{comp['component']}
```

Generate the equivalent Tailwind CSS component using utility classes. Include:
- Proper Tailwind utility classes for layout, spacing, colors, typography
- Semantic HTML elements
- Responsive variants where appropriate
- Hover/focus states for interactive elements
- Accessibility attributes (aria-*, role, alt)"""

        resp = client.messages.create(
            model="claude-sonnet-4-6", max_tokens=4096, temperature=0.1,
            thinking={"type": "disabled"}, system=tw_system,
            messages=[{"role": "user", "content": prompt}]
        )
        output = "".join(b.text for b in resp.content if b.type == 'text')
        passed, fails, checks = score_tailwind(output)

        trans_results.append({"id": comp["id"], "name": comp["name"], "passed": passed, "fails": fails})
        print(f"[{comp['id']}] {comp['name']}: {'✓' if passed else '✗ (' + ','.join(fails) + ')'}")
        time.sleep(1.0)

    trans_pass = sum(1 for r in trans_results if r["passed"])
    trans_rate = trans_pass / len(trans_results)
    print(f"\nMCSS→Tailwind Translation: {trans_rate:.0%} ({trans_pass}/{len(trans_results)})")

    # Summary
    print(f"\n{'='*60}")
    print(f"SUMMARY")
    print(f"{'='*60}")
    print(f"Framework Compliance: MCSS={mcss_rate:.0%} Tailwind={tw_rate:.0%}")
    print(f"Tailwind→MCSS Translation: 80% (from previous experiment)")
    print(f"MCSS→Tailwind Translation: {trans_rate:.0%}")
    print(f"Bidirectional avg: {(0.80 + trans_rate) / 2:.0%}")

    out = {
        "experiment": "FAIR_COMPARISON",
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "cross_framework": fw_results,
        "reverse_translation": {
            "rate": trans_rate, "passed": trans_pass, "total": len(trans_results),
            "results": trans_results
        }
    }
    out_path = RESULTS_DIR / f"fair_comparison_{time.strftime('%Y%m%d_%H%M%S')}.json"
    Path(out_path).write_text(json.dumps(out, indent=2, default=str))
    print(f"\nSaved: {out_path}")
