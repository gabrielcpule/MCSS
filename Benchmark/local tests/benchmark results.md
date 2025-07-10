Of course. That's an excellent question. Estimating token count is a great way to understand the complexity and verbosity of the generated code, especially with a semantically rich framework like MCSS.

Here is a rough estimation of the token count for each generated test file. Please note that this is an approximation, as the exact tokenization can vary between different language models. I'm using a general rule of thumb where 1 token is roughly equivalent to 4 characters of code.

Test 1.1: User Profile Card

Estimated Tokens: ~1,100
Rationale: This is a single, well-defined organism. The token count is substantial for a simple card due to the complete, self-contained CSS and the verbose semantic RDFa annotations, which are central to MCSS.
Test 2.1: Modal Dialog with Form

Estimated Tokens: ~1,900
Rationale: The complexity increases significantly with the introduction of a modal, a form, more intricate CSS for positioning and state, and a basic JavaScript controller for interactivity.
Test 3.1: Advanced Tab Interface

Estimated Tokens: ~2,200
Rationale: This test is token-heavy primarily because of the comprehensive, WAI-ARIA compliant JavaScript required for full keyboard navigation and focus management, in addition to the HTML and CSS.
Test 4.1: Dashboard Page Layout

Estimated Tokens: ~2,000
Rationale: This involves composing multiple organisms (c-header, c-sidebar) and molecules (c-card) within a complex layout (l-page-grid). The token count reflects the sheer volume of HTML elements and CSS rules needed to define the entire page structure.
Test 5.1: Complete SaaS Application Page

Estimated Tokens: ~3,100
Rationale: As the most complex example, this page combines multiple advanced layouts and organisms, including overlays like notifications and modals. The high token count is a direct result of the comprehensive nature of a full application shell, with extensive CSS and semantic markup for every part of the UI.
As you can see, the token count scales with the component's complexity and the level of semantic and behavioral detail required by the MCSS framework. The goal of MCSS is to be explicit and machine-readable, which naturally leads to a higher token count compared to more concise, but less semantic, code.
