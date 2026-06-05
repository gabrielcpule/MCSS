#!/usr/bin/env python3
"""Generate the full 100-prompt MCSS-BENCHMARK-V1 suite from section structure."""
import json, time
from pathlib import Path

# The benchmark spec defines these sections. Prompts are generated from section headers
# and follow the same pattern as the explicit prompts in the spec.

PROMPTS = []

# === GENERATION TASKS (40) ===

# G-001: Simple Atom Components (10)
atom_prompts = [
    ("G-001-01", "Generate a c-avatar component (mcs:Atom) that displays a user's profile image with fallback initials. Include proper RDFa annotations and support for small, medium, and large sizes via data-state."),
    ("G-001-02", "Create a c-badge component (mcs:Atom) for displaying status indicators with semantic color states (success, warning, error, info)."),
    ("G-001-03", "Generate a c-button component (mcs:Atom) with primary, secondary, outline, and ghost variants via data-variant. Include loading, disabled, and error states via data-state."),
    ("G-001-04", "Create a c-input component (mcs:Atom) for text entry with default, disabled, error, and focused states via data-state. Include proper placeholder styling."),
    ("G-001-05", "Generate a c-toggle component (mcs:Atom) — an on/off switch with on, off, and disabled states via data-state. Include an animated thumb element."),
    ("G-001-06", "Create a c-checkbox component (mcs:Atom) with checked, disabled, and indeterminate states via data-state. Include a custom checkmark indicator."),
    ("G-001-07", "Generate a c-spinner component (mcs:Atom) for loading indicators with small, medium, and large sizes via data-state. Use CSS animation for the spin effect."),
    ("G-001-08", "Create a c-tooltip component (mcs:Atom) that displays on hover with top, bottom, left, and right positioning via data-position. Include a subtle fade animation."),
    ("G-001-09", "Generate a c-progress component (mcs:Atom) for completion indicators with determinate (0-100%) and indeterminate states via data-state."),
    ("G-001-10", "Create a c-icon component (mcs:Atom) for displaying SVG icons with small, medium, and large sizes via data-state. Support currentColor inheritance."),
]
PROMPTS.extend((pid, "gen", text) for pid, text in atom_prompts)

# G-002: Molecule Components (15)
molecule_prompts = [
    ("G-002-01", "Generate a c-search-form molecule component that combines a text input, search button, and optional filter dropdown. Include proper composition annotations with mcs:hasPart."),
    ("G-002-02", "Create a c-login-form molecule (mcs:Molecule) with email field, password field, submit button, and a recovery link. Compose c-input, c-button, and c-link atoms."),
    ("G-002-03", "Generate a c-card molecule with header, body, footer, and optional image. Include an elevated variant via data-variant. Compose c-text and c-button atoms."),
    ("G-002-04", "Create a c-alert molecule for feedback messages with success, warning, error, and info states. Include an optional dismiss button. Compose c-icon and c-text."),
    ("G-002-05", "Generate a c-breadcrumb molecule showing navigation hierarchy with items separated by a visual separator. Include proper ARIA labeling."),
    ("G-002-06", "Create a c-pagination molecule for page navigation with numbered items, previous/next, and an ellipsis for truncated ranges. Support active and disabled states."),
    ("G-002-07", "Generate a c-dropdown molecule with a toggle trigger and a menu of action items. Support open/closed states via data-state and aria-expanded sync."),
    ("G-002-08", "Create a c-navigation molecule for primary site navigation with horizontal and vertical variants. Support active state on current page links."),
    ("G-002-09", "Generate a c-modal molecule with overlay backdrop, close button, title, body content area, and action footer. Support open/closed states and escape-key dismissal."),
    ("G-002-10", "Create a c-tabs molecule with tab list and tab panels. Support active tab state and keyboard navigation between tabs."),
    ("G-002-11", "Generate a c-accordion molecule with expandable sections. Support open/closed states per section and smooth height transitions."),
    ("G-002-12", "Create a c-table molecule with sortable headers, striped rows, and responsive scroll wrapper. Include proper caption and scope attributes."),
    ("G-002-13", "Generate a c-file-upload molecule with drag-and-drop zone, file list display, and upload progress indicator. Compose c-button and c-progress atoms."),
    ("G-002-14", "Create a c-date-picker molecule with calendar grid, month navigation, and date selection. Support disabled dates and today highlight states."),
    ("G-002-15", "Generate a c-combobox molecule combining a text input with a filtered dropdown list. Support keyboard navigation and selection state."),
]
PROMPTS.extend((pid, "gen", text) for pid, text in molecule_prompts)

# G-003: Organism Components (15)
organism_prompts = [
    ("G-003-01", "Create a c-product-grid organism that displays a grid of product cards with filtering and sorting capabilities. Compose c-card and c-search-form molecules."),
    ("G-003-02", "Generate a c-dashboard-header organism with logo, primary navigation, user menu dropdown, and notification badge. Compose c-navigation, c-dropdown, and c-badge."),
    ("G-003-03", "Create a c-data-table organism with search, column sorting, pagination, and row selection. Compose c-table, c-search-form, c-pagination molecules."),
    ("G-003-04", "Generate a c-article-feed organism with article cards, load-more pagination, and category filter sidebar. Compose c-card and c-pagination."),
    ("G-003-05", "Create a c-checkout-form organism with shipping fields, payment method selection, order summary card, and submit button. Multi-step with validation."),
    ("G-003-06", "Generate a c-user-profile organism with avatar, editable name/bio fields, settings toggles, and save/cancel actions. Compose c-avatar, c-input, c-toggle."),
    ("G-003-07", "Create a c-image-gallery organism with thumbnail grid, lightbox modal, and keyboard navigation between images. Compose c-image and c-modal."),
    ("G-003-08", "Generate a c-kanban-board organism with columns (todo/in-progress/done), draggable cards, and add-card buttons. Compose c-card and c-button."),
    ("G-003-09", "Create a c-chat-interface organism with message list, message bubbles, typing indicator, and message input with send button. Compose c-input and c-button."),
    ("G-003-10", "Generate a c-settings-page organism with sidebar navigation, grouped setting sections, and per-section save buttons. Compose c-navigation and c-toggle."),
    ("G-003-11", "Create a c-registration-form organism with personal info, account setup, and confirmation steps in a multi-step wizard. Progress indicator between steps."),
    ("G-003-12", "Generate a c-ecommerce-listing organism with product cards, price filters, sort dropdown, and category breadcrumbs. Compose c-card and c-breadcrumb."),
    ("G-003-13", "Create a c-notification-center organism with notification list grouped by time, mark-read actions, and an unread badge counter. Compose c-alert and c-badge."),
    ("G-003-14", "Generate a c-analytics-dashboard organism with metric cards, chart containers, date range picker, and export button. Grid layout with responsive cards."),
    ("G-003-15", "Create a c-footer organism with multi-column link sections, social icon links, copyright text, and newsletter signup. Compose c-input, c-button, c-link atoms."),
]
PROMPTS.extend((pid, "gen", text) for pid, text in organism_prompts)

# === MODIFICATION TASKS (40) ===

# M-001: State Management Modifications (15)
state_mod_prompts = [
    ("M-001-01", "Given a c-button component styled with var(--color-background-brand), modify it to add a 'loading' state that shows a spinner and disables interaction. Use data-state, not class modifiers."),
    ("M-001-02", "Add an 'error' state to the c-input component. The error state should show a red border and red focus ring. Use data-state=\"error\"."),
    ("M-001-03", "Modify the c-card component to add a 'hovered' state that elevates the shadow. Use data-state=\"hovered\" on the root element."),
    ("M-001-04", "Add a 'success' state to the c-badge component. The success state should use green background and text colors from the token system."),
    ("M-001-05", "Modify the c-toggle component to add a 'focused' state with a visible focus ring. Use :focus-visible and data-state sync."),
    ("M-001-06", "Add a 'readonly' state to the c-input component. The readonly state should show a muted background but remain focusable."),
    ("M-001-07", "Modify the c-dropdown to handle 'empty' state — when no menu items exist, show a subtle 'No options' message."),
    ("M-001-08", "Add keyboard Escape key handling state to the c-modal component. On Escape, the modal should transition to 'closing' then 'closed' state."),
    ("M-001-09", "Modify the c-pagination to disable previous/next buttons at boundaries. First page disables previous, last page disables next."),
    ("M-001-10", "Add 'sort-ascending' and 'sort-descending' states to c-table column headers with appropriate arrow indicators."),
    ("M-001-11", "Modify the c-alert to add a 'dismissing' animation state before removal. Use CSS transition triggered by data-state=\"dismissing\"."),
    ("M-001-12", "Add 'valid' and 'invalid' validation states to the c-input component. Invalid shows error styling, valid shows success indicator."),
    ("M-001-13", "Modify the c-tabs component to handle 'disabled' tabs that cannot be selected. Show muted styling and prevent click interaction."),
    ("M-001-14", "Add 'expanded' and 'collapsed' states to the c-accordion with smooth height transition animation between states."),
    ("M-001-15", "Modify the c-file-upload to show 'dragover' state when a file is dragged over the drop zone. Highlight the zone border."),
]
PROMPTS.extend((pid, "mod", text) for pid, text in state_mod_prompts)

# M-002: Style Token Modifications (15)
token_mod_prompts = [
    ("M-002-01", "Modify the c-button--primary variant to use the semantic 'success' color tokens instead of the brand primary tokens. All values must use var()."),
    ("M-002-02", "Update the c-card component to use --shadow-lg instead of the default border. Switch from border-based to shadow-based elevation."),
    ("M-002-03", "Change the c-input border-radius from --border-radius-md to --border-radius-lg for a pill-shaped input variant. Keep all other styles."),
    ("M-002-04", "Modify the c-alert success state to use a lighter green background (--color-green-100) with darker text (--color-green-800)."),
    ("M-002-05", "Update the c-navigation active link to use --color-background-brand with --color-text-on-brand instead of just coloring the text."),
    ("M-002-06", "Change the c-badge font from --font-size-overline to --font-size-caption with --font-weight-semibold for a larger badge variant."),
    ("M-002-07", "Modify the c-spinner to use --color-border-interactive for the track and --color-background-brand for the spin segment."),
    ("M-002-08", "Update all c-button variants to use --transition-base for hover effects instead of --transition-fast for smoother transitions."),
    ("M-002-09", "Change the c-card body padding from --space-5 to --space-6 for a more spacious card layout."),
    ("M-002-10", "Modify the c-tooltip to use --color-gray-800 for background and --color-text-on-brand for text, with --shadow-md elevation."),
    ("M-002-11", "Update the c-progress bar to use a gradient from --color-brand-400 to --color-brand-600 instead of a solid color."),
    ("M-002-12", "Change the c-breadcrumb separator color from default gray to --color-text-secondary for better visibility."),
    ("M-002-13", "Modify the c-pagination active item to use --font-weight-bold instead of just a background color change."),
    ("M-002-14", "Update the c-divider to use --space-2 for vertical margins and --color-border-default for the line color."),
    ("M-002-15", "Change the c-image border-radius from --border-radius-md to --border-radius-lg for a softer image presentation."),
]
PROMPTS.extend((pid, "mod", text) for pid, text in token_mod_prompts)

# M-003: Accessibility Enhancements (10)
a11y_prompts = [
    ("M-003-01", "Enhance the c-navigation component with comprehensive ARIA labels and keyboard navigation support. Use aria-label, role=\"navigation\", and aria-current=\"page\"."),
    ("M-003-02", "Add screen reader support to the c-alert component. Include role=\"alert\" for immediate announcements and aria-live=\"polite\" for updates."),
    ("M-003-03", "Enhance the c-modal with aria-modal=\"true\", aria-labelledby, aria-describedby, and focus trap behavior for keyboard users."),
    ("M-003-04", "Add accessible name computation to the c-button component. When used as icon-only, ensure aria-label is present."),
    ("M-003-05", "Enhance the c-tabs component with role=\"tablist\", role=\"tab\", role=\"tabpanel\", and arrow key navigation between tabs."),
    ("M-003-06", "Add form error association to c-input — when in error state, link aria-describedby to the error message element."),
    ("M-003-07", "Enhance the c-table with proper caption, scope attributes on headers, and role=\"table\" for screen reader navigation."),
    ("M-003-08", "Add skip-to-content link at the top of a c-navigation organism, visually hidden but focusable, linking to the main content area."),
    ("M-003-09", "Enhance the c-dropdown with aria-haspopup=\"true\", aria-expanded synced to open/closed state, and menuitem roles on items."),
    ("M-003-10", "Add reduced motion support throughout — wrap all transitions and animations in @media (prefers-reduced-motion: no-preference)."),
]
PROMPTS.extend((pid, "mod", text) for pid, text in a11y_prompts)

# === COMPREHENSION TASKS (20) ===

# C-001: Component Analysis (10)
analysis_prompts = [
    ("C-001-01", "Given a c-card component with typeof=\"mcs:Component\", property=\"mcs:taxonomyLevel\" content=\"mcs:Molecule\", elements c-card__header, c-card__body, c-card__footer, all linked via mcs:hasPart — explain its purpose, constituent parts, and semantic annotations."),
    ("C-001-02", "Analyze a c-button component with data-variant=\"primary\", data-state=\"loading\", typeof=\"mcs:Component\", and property=\"mcs:taxonomyLevel\" content=\"mcs:Atom\". Explain its taxonomy level, interaction model, and state handling."),
    ("C-001-03", "Examine a c-search-form with mcs:hasPart links to a c-input and c-button. Explain how molecular composition is expressed through RDFa annotations."),
    ("C-001-04", "Analyze a c-modal component marked as mcs:Organism containing c-button, c-input, and c-alert as children via mcs:hasPart. Explain the composition hierarchy."),
    ("C-001-05", "Given a c-data-table organism, explain how the semantic annotations enable automated accessibility auditing compared to a plain HTML table."),
    ("C-001-06", "Analyze a c-tabs component with role=\"tablist\", mcs:hasPart relationships, and data-state=\"active\" on the selected tab. Explain the semantic layering."),
    ("C-001-07", "Examine a c-accordion molecule and explain how data-state toggling (open/closed) should coordinate with aria-expanded for accessibility."),
    ("C-001-08", "Given a c-badge with data-state=\"success\" and data-mcs-interaction-type=\"visual-indicator\", explain the distinction between visual state and behavioral contracts."),
    ("C-001-09", "Analyze a c-pagination component and explain how active/disabled states should be communicated to both visual users and screen reader users."),
    ("C-001-10", "Examine a c-notification-center organism with multiple c-alert children and explain how mcs:hasPart creates a queryable component graph."),
]
PROMPTS.extend((pid, "comp", text) for pid, text in analysis_prompts)

# C-002: Interaction Behavior Analysis (10)
interaction_prompts = [
    ("C-002-01", "Examine a c-dropdown component with data-state=\"open\", aria-expanded, and data-mcs-triggers-event=\"mcss:dropdown:toggled\". Explain its complete interaction model including state management and accessibility."),
    ("C-002-02", "Analyze the keyboard navigation model of a c-combobox. Explain how Arrow keys, Enter, and Escape should interact with data-state and aria-expanded."),
    ("C-002-03", "Given a c-file-upload with drag-and-drop, explain how data-state changes (idle→dragover→uploading→complete→error) map to visual states and ARIA announcements."),
    ("C-002-04", "Examine a c-modal's focus management contract. Explain how focus should be trapped, restored on close, and how data-state='open'/'closed' drives this behavior."),
    ("C-002-05", "Analyze the interaction model of a c-date-picker. Explain how date selection, month navigation, and keyboard shortcuts should coordinate through data-state."),
    ("C-002-06", "Given a c-kanban-board organism, explain the drag-and-drop interaction model: how cards move between columns and how data-mcs-triggers-event communicates state changes."),
    ("C-002-07", "Examine the multi-step form wizard's interaction model. Explain how step transitions should manage data-state, validation, and browser history."),
    ("C-002-08", "Analyze a c-chat-interface and explain how optimistic updates, typing indicators, and message arrival should be expressed through data-state transitions."),
    ("C-002-09", "Given a c-table with sortable headers, explain the sort interaction model: how column click toggles sort direction and how data-state communicates sort state."),
    ("C-002-10", "Examine the c-ecommerce-listing organism and explain how filter changes should trigger loading states across the product grid via data-state propagation."),
]
PROMPTS.extend((pid, "comp", text) for pid, text in interaction_prompts)

if __name__ == '__main__':
    gen = sum(1 for _, t, _ in PROMPTS if t == "gen")
    mod = sum(1 for _, t, _ in PROMPTS if t == "mod")
    comp = sum(1 for _, t, _ in PROMPTS if t == "comp")
    print(f"Generated {len(PROMPTS)} prompts: {gen} gen, {mod} mod, {comp} comp")

    out = Path("/home/gabrielp/Projects/MCSS/research/data/benchmark_prompts_100.json")
    out.write_text(json.dumps(PROMPTS, indent=2))
    print(f"Saved to {out}")
