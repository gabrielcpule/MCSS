#!/usr/bin/env python3
"""MCSS v2 refactor: self-contained modifiers, shorter attrs, expanded components."""
from pathlib import Path

FRAMEWORK = Path("/home/gabrielp/Projects/MCSS/mcss-framework")
SRC = FRAMEWORK / "src"

# ============================================================
# ATOM CSS — self-contained modifier classes
# Each variant carries full styles. No base+modifier pairs.
# ============================================================

BUTTON = """/* ============================================
 * Component: Button | Taxonomy: mcs:Atom
 * Purpose: Triggers user actions — submissions, navigation, toggles
 * States: default, loading, disabled, error (data-state)
 * Variants: primary, secondary, outline, ghost
 * ============================================ */

.c-button--primary,
.c-button--secondary,
.c-button--outline,
.c-button--ghost {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: var(--space-2);
  padding: var(--space-3) var(--space-5);
  font-size: var(--font-size-caption);
  font-weight: var(--font-weight-medium);
  line-height: var(--line-height-tight);
  border: 1px solid transparent;
  border-radius: var(--border-radius-md);
  cursor: pointer;
  transition: background-color var(--transition-fast), border-color var(--transition-fast), opacity var(--transition-fast);
  text-decoration: none;
}

.c-button--primary:focus-visible,
.c-button--secondary:focus-visible,
.c-button--outline:focus-visible,
.c-button--ghost:focus-visible {
  outline: 2px solid var(--color-border-focus);
  outline-offset: 2px;
}

.c-button--primary { background-color: var(--color-background-brand); color: var(--color-text-on-brand); }
.c-button--primary:hover { background-color: var(--color-background-brand-hover); }
.c-button--secondary { background-color: var(--color-background-secondary); color: var(--color-text-primary); border-color: var(--color-border-default); }
.c-button--secondary:hover { background-color: var(--color-gray-100); }
.c-button--outline { background-color: transparent; color: var(--color-brand-600); border-color: var(--color-border-interactive); }
.c-button--outline:hover { background-color: var(--color-brand-50); }
.c-button--ghost { background-color: transparent; color: var(--color-text-secondary); }
.c-button--ghost:hover { background-color: var(--color-background-secondary); color: var(--color-text-primary); }

.c-button--primary[data-state="loading"],
.c-button--secondary[data-state="loading"],
.c-button--outline[data-state="loading"],
.c-button--ghost[data-state="loading"] { opacity: 0.7; cursor: wait; pointer-events: none; }

.c-button--primary[data-state="disabled"],
.c-button--secondary[data-state="disabled"],
.c-button--outline[data-state="disabled"],
.c-button--ghost[data-state="disabled"] { opacity: 0.5; cursor: not-allowed; pointer-events: none; }

.c-button--primary[data-state="error"] { background-color: var(--color-red-500); border-color: var(--color-border-error); }
"""

INPUT = """/* ============================================
 * Component: Input | Taxonomy: mcs:Atom
 * Purpose: Text input fields for forms
 * States: default, disabled, error (data-state)
 * ============================================ */

.c-input {
  display: block;
  width: 100%;
  padding: var(--space-3) var(--space-4);
  font-size: var(--font-size-body);
  font-family: var(--font-family-sans);
  line-height: var(--line-height-base);
  color: var(--color-text-primary);
  background-color: var(--color-background-primary);
  border: 1px solid var(--color-border-default);
  border-radius: var(--border-radius-md);
  transition: border-color var(--transition-fast), box-shadow var(--transition-fast);
}
.c-input::placeholder { color: var(--color-gray-400); }
.c-input:focus { border-color: var(--color-border-interactive); box-shadow: 0 0 0 3px var(--color-brand-100); outline: none; }
.c-input[data-state="disabled"] { opacity: 0.5; cursor: not-allowed; background-color: var(--color-background-secondary); }
.c-input[data-state="error"] { border-color: var(--color-border-error); box-shadow: 0 0 0 3px var(--color-red-100); }
"""

BADGE = """/* ============================================
 * Component: Badge | Taxonomy: mcs:Atom
 * Purpose: Status indicators and category labels
 * States: success, warning, error, info, neutral (data-state)
 * ============================================ */

.c-badge--success,
.c-badge--warning,
.c-badge--error,
.c-badge--info,
.c-badge--neutral {
  display: inline-flex;
  align-items: center;
  padding: var(--space-1) var(--space-3);
  font-size: var(--font-size-overline);
  font-weight: var(--font-weight-semibold);
  line-height: var(--line-height-tight);
  border-radius: var(--border-radius-full);
  text-transform: uppercase;
  letter-spacing: 0.025em;
}

.c-badge--success { background-color: var(--color-background-success); color: var(--color-text-success); }
.c-badge--warning { background-color: var(--color-background-warning); color: var(--color-text-warning); }
.c-badge--error { background-color: var(--color-background-error); color: var(--color-text-error); }
.c-badge--info { background-color: var(--color-brand-100); color: var(--color-brand-700); }
.c-badge--neutral { background-color: var(--color-background-secondary); color: var(--color-text-secondary); }
"""

AVATAR = """/* ============================================
 * Component: Avatar | Taxonomy: mcs:Atom
 * Purpose: User profile image with fallback initials
 * States: small, medium (default), large (data-state)
 * ============================================ */

.c-avatar {
  position: relative; display: inline-flex; align-items: center; justify-content: center;
  width: 2.5rem; height: 2.5rem; border-radius: var(--border-radius-full);
  background-color: var(--color-brand-100); color: var(--color-brand-700);
  font-size: var(--font-size-caption); font-weight: var(--font-weight-semibold);
  overflow: hidden; flex-shrink: 0;
}
.c-avatar__image { width: 100%; height: 100%; object-fit: cover; }
.c-avatar__fallback { position: absolute; display: flex; align-items: center; justify-content: center; width: 100%; height: 100%; }
.c-avatar[data-state="small"] { width: 1.75rem; height: 1.75rem; font-size: var(--font-size-overline); }
.c-avatar[data-state="large"] { width: 3.5rem; height: 3.5rem; font-size: var(--font-size-subtitle); }
"""

ICON = """/* ============================================
 * Component: Icon | Taxonomy: mcs:Atom
 * Purpose: SVG icon wrapper at consistent sizes
 * States: small, medium (default), large (data-state)
 * ============================================ */

.c-icon { display: inline-flex; align-items: center; justify-content: center; width: 1.5rem; height: 1.5rem; color: inherit; flex-shrink: 0; }
.c-icon svg { width: 100%; height: 100%; }
.c-icon[data-state="small"] { width: 1rem; height: 1rem; }
.c-icon[data-state="large"] { width: 2rem; height: 2rem; }
"""

LABEL = """/* ============================================
 * Component: Label | Taxonomy: mcs:Atom
 * Purpose: Labels form inputs
 * ============================================ */

.c-label { display: block; font-size: var(--font-size-caption); font-weight: var(--font-weight-medium); color: var(--color-text-primary); margin-block-end: var(--space-2); }
"""

SPINNER = """/* ============================================
 * Component: Spinner | Taxonomy: mcs:Atom
 * Purpose: Loading indicator
 * States: small, medium (default), large (data-state)
 * ============================================ */

.c-spinner { display: inline-block; width: 1.5rem; height: 1.5rem; border: 2px solid var(--color-border-default); border-top-color: var(--color-background-brand); border-radius: var(--border-radius-full); animation: mcss-spin 0.6s linear infinite; }
.c-spinner[data-state="small"] { width: 1rem; height: 1rem; border-width: 1.5px; }
.c-spinner[data-state="large"] { width: 2.5rem; height: 2.5rem; border-width: 3px; }
@keyframes mcss-spin { to { transform: rotate(360deg); } }
"""

DIVIDER = """/* ============================================
 * Component: Divider | Taxonomy: mcs:Atom
 * Purpose: Visual separator
 * States: horizontal (default), vertical (data-state)
 * ============================================ */

.c-divider { border: none; width: 100%; height: 1px; background-color: var(--color-border-default); }
.c-divider[data-state="vertical"] { width: 1px; height: auto; align-self: stretch; }
"""

TEXT = """/* ============================================
 * Component: Text | Taxonomy: mcs:Atom
 * Purpose: Typographic styles
 * States: body (default), caption, overline, code (data-state)
 * ============================================ */

.c-text { font-size: var(--font-size-body); line-height: var(--line-height-base); color: var(--color-text-primary); }
.c-text[data-state="caption"] { font-size: var(--font-size-caption); color: var(--color-text-secondary); }
.c-text[data-state="overline"] { font-size: var(--font-size-overline); font-weight: var(--font-weight-semibold); text-transform: uppercase; letter-spacing: 0.05em; color: var(--color-text-secondary); }
.c-text[data-state="code"] { font-family: var(--font-family-mono); font-size: var(--font-size-caption); padding: 0.125em 0.375em; background-color: var(--color-background-secondary); border-radius: var(--border-radius-sm); }
"""

LINK = """/* ============================================
 * Component: Link | Taxonomy: mcs:Atom
 * Purpose: Navigational hyperlinks
 * Variants: default, subtle, external
 * ============================================ */

.c-link { color: var(--color-text-link); text-decoration: underline; text-underline-offset: 0.2em; cursor: pointer; transition: color var(--transition-fast); }
.c-link:hover { color: var(--color-text-link-hover); }
.c-link[data-variant="subtle"] { color: var(--color-text-secondary); text-decoration: none; }
.c-link[data-variant="subtle"]:hover { color: var(--color-text-primary); text-decoration: underline; }
.c-link[data-variant="external"]::after { content: " ↗"; font-size: var(--font-size-caption); }
"""

IMAGE = """/* ============================================
 * Component: Image | Taxonomy: mcs:Atom
 * Purpose: Responsive images with optional aspect ratios
 * Variants: responsive (default), 1:1, 4:3, 16:9 (data-variant)
 * ============================================ */

.c-image { display: block; max-width: 100%; height: auto; border-radius: var(--border-radius-md); }
.c-image[data-variant="1:1"] { aspect-ratio: 1 / 1; object-fit: cover; width: 100%; }
.c-image[data-variant="4:3"] { aspect-ratio: 4 / 3; object-fit: cover; width: 100%; }
.c-image[data-variant="16:9"] { aspect-ratio: 16 / 9; object-fit: cover; width: 100%; }
"""

CHECKBOX = """/* ============================================
 * Component: Checkbox | Taxonomy: mcs:Atom
 * Purpose: Binary selection control
 * States: checked, disabled, indeterminate (data-state)
 * ============================================ */

.c-checkbox { display: inline-flex; align-items: center; gap: var(--space-2); cursor: pointer; font-size: var(--font-size-caption); color: var(--color-text-primary); }
.c-checkbox__input { appearance: none; width: 1.125rem; height: 1.125rem; border: 2px solid var(--color-border-default); border-radius: var(--border-radius-sm); background-color: var(--color-background-primary); cursor: pointer; transition: background-color var(--transition-fast), border-color var(--transition-fast); flex-shrink: 0; display: grid; place-content: center; }
.c-checkbox__input::before { content: ""; width: 0.625rem; height: 0.625rem; transform: scale(0); transition: transform var(--transition-fast); background-color: var(--color-text-on-brand); clip-path: polygon(14% 44%, 0 65%, 50% 100%, 100% 16%, 80% 0%, 43% 62%); }
.c-checkbox__input:checked { background-color: var(--color-background-brand); border-color: var(--color-background-brand); }
.c-checkbox__input:checked::before { transform: scale(1); }
.c-checkbox__input:focus-visible { outline: 2px solid var(--color-border-focus); outline-offset: 2px; }
.c-checkbox[data-state="disabled"] { opacity: 0.5; cursor: not-allowed; }
.c-checkbox[data-state="disabled"] .c-checkbox__input { cursor: not-allowed; }
"""

TOGGLE = """/* ============================================
 * Component: Toggle | Taxonomy: mcs:Atom
 * Purpose: On/off switch control
 * States: on, off (default), disabled (data-state)
 * ============================================ */

.c-toggle { display: inline-flex; align-items: center; gap: var(--space-2); cursor: pointer; font-size: var(--font-size-caption); color: var(--color-text-primary); }
.c-toggle__track { width: 2.5rem; height: 1.375rem; border-radius: var(--border-radius-full); background-color: var(--color-gray-200); position: relative; transition: background-color var(--transition-fast); flex-shrink: 0; }
.c-toggle__thumb { position: absolute; top: 2px; left: 2px; width: 1.125rem; height: 1.125rem; border-radius: var(--border-radius-full); background-color: var(--color-white); box-shadow: var(--shadow-sm); transition: transform var(--transition-fast); }
.c-toggle[data-state="on"] .c-toggle__track { background-color: var(--color-background-brand); }
.c-toggle[data-state="on"] .c-toggle__thumb { transform: translateX(1.125rem); }
.c-toggle:focus-visible .c-toggle__track { outline: 2px solid var(--color-border-focus); outline-offset: 2px; }
.c-toggle[data-state="disabled"] { opacity: 0.5; cursor: not-allowed; }
"""

TOOLTIP = """/* ============================================
 * Component: Tooltip | Taxonomy: mcs:Atom
 * Purpose: Contextual hover tooltip
 * Positions: top (default), bottom, left, right (data-position)
 * ============================================ */

.c-tooltip { position: relative; display: inline-flex; }
.c-tooltip__content { position: absolute; bottom: calc(100% + var(--space-2)); left: 50%; transform: translateX(-50%); padding: var(--space-2) var(--space-3); font-size: var(--font-size-overline); font-weight: var(--font-weight-medium); color: var(--color-text-on-brand); background-color: var(--color-gray-800); border-radius: var(--border-radius-sm); white-space: nowrap; pointer-events: none; opacity: 0; transition: opacity var(--transition-fast); z-index: var(--z-index-dropdown); }
.c-tooltip[data-position="bottom"] .c-tooltip__content { bottom: auto; top: calc(100% + var(--space-2)); }
.c-tooltip[data-position="left"] .c-tooltip__content { left: auto; right: calc(100% + var(--space-2)); top: 50%; transform: translateY(-50%); }
.c-tooltip[data-position="right"] .c-tooltip__content { left: calc(100% + var(--space-2)); top: 50%; transform: translateY(-50%); }
.c-tooltip:hover .c-tooltip__content, .c-tooltip:focus-within .c-tooltip__content { opacity: 1; }
"""

PROGRESS = """/* ============================================
 * Component: Progress | Taxonomy: mcs:Atom
 * Purpose: Completion or loading progress indicator
 * States: indeterminate, determinate (data-state)
 * ============================================ */

.c-progress { width: 100%; height: 0.5rem; background-color: var(--color-background-secondary); border-radius: var(--border-radius-full); overflow: hidden; }
.c-progress__bar { height: 100%; background-color: var(--color-background-brand); border-radius: var(--border-radius-full); transition: width var(--transition-base); width: var(--mcss-progress-value, 0%); }
.c-progress[data-state="indeterminate"] .c-progress__bar { width: 40%; animation: mcss-progress-indeterminate 1.5s ease-in-out infinite; }
@keyframes mcss-progress-indeterminate { 0% { transform: translateX(-100%); } 100% { transform: translateX(250%); } }
"""

# ============================================================
# MOLECULE CSS
# ============================================================

CARD = """/* ============================================
 * Component: Card | Taxonomy: mcs:Molecule
 * Purpose: Structured content container
 * Variants: elevated (data-variant)
 * Elements: __header, __body, __footer, __image
 * ============================================ */

.c-card { display: flex; flex-direction: column; background-color: var(--color-background-primary); border: 1px solid var(--color-border-default); border-radius: var(--border-radius-lg); overflow: hidden; }
.c-card[data-variant="elevated"] { border: none; box-shadow: var(--shadow-md); }
.c-card__image { width: 100%; aspect-ratio: 16 / 9; object-fit: cover; }
.c-card__header { padding: var(--space-5) var(--space-5) 0; font-size: var(--font-size-subtitle); font-weight: var(--font-weight-semibold); color: var(--color-text-primary); }
.c-card__body { padding: var(--space-5); flex: 1; font-size: var(--font-size-body); color: var(--color-text-secondary); line-height: var(--line-height-base); }
.c-card__footer { padding: var(--space-4) var(--space-5); border-top: 1px solid var(--color-border-default); display: flex; align-items: center; gap: var(--space-3); }
"""

SEARCH_FORM = """/* ============================================
 * Component: Search Form | Taxonomy: mcs:Molecule
 * Purpose: Search input with submit button
 * Elements: __input, __button
 * ============================================ */

.c-search-form { display: flex; gap: var(--space-2); align-items: center; }
.c-search-form__input { flex: 1; }
.c-search-form__button { flex-shrink: 0; }
"""

LOGIN_FORM = """/* ============================================
 * Component: Login Form | Taxonomy: mcs:Molecule
 * Purpose: Email/password authentication form
 * Elements: __field, __submit, __recovery
 * ============================================ */

.c-login-form { display: flex; flex-direction: column; gap: var(--space-5); padding: var(--space-8); max-width: 28rem; margin-inline: auto; }
.c-login-form__field { display: flex; flex-direction: column; gap: var(--space-2); }
.c-login-form__submit { margin-block-start: var(--space-3); }
.c-login-form__recovery { text-align: center; font-size: var(--font-size-caption); }
"""

ALERT = """/* ============================================
 * Component: Alert | Taxonomy: mcs:Molecule
 * Purpose: Contextual feedback messages
 * States: info (default), success, warning, error (data-state)
 * Elements: __icon, __content, __dismiss
 * ============================================ */

.c-alert--info,
.c-alert--success,
.c-alert--warning,
.c-alert--error {
  display: flex; align-items: flex-start; gap: var(--space-3);
  padding: var(--space-4); border-radius: var(--border-radius-md);
  font-size: var(--font-size-caption); line-height: var(--line-height-base);
  border: 1px solid var(--color-border-default);
}

.c-alert--info { background-color: var(--color-background-secondary); color: var(--color-text-primary); border-color: var(--color-border-default); }
.c-alert--success { background-color: var(--color-background-success); color: var(--color-text-success); border-color: var(--color-border-success); }
.c-alert--warning { background-color: var(--color-background-warning); color: var(--color-text-warning); border-color: var(--color-yellow-500); }
.c-alert--error { background-color: var(--color-background-error); color: var(--color-text-error); border-color: var(--color-border-error); }

.c-alert__icon { flex-shrink: 0; }
.c-alert__content { flex: 1; }
.c-alert__dismiss { flex-shrink: 0; background: none; border: none; cursor: pointer; color: var(--color-text-secondary); padding: var(--space-1); }
"""

BREADCRUMB = """/* ============================================
 * Component: Breadcrumb | Taxonomy: mcs:Molecule
 * Purpose: Navigation trail showing page hierarchy
 * Elements: __list, __item, __separator
 * ============================================ */

.c-breadcrumb__list { display: flex; align-items: center; list-style: none; padding: 0; gap: var(--space-2); font-size: var(--font-size-caption); }
.c-breadcrumb__item { display: inline-flex; align-items: center; gap: var(--space-2); color: var(--color-text-secondary); }
.c-breadcrumb__separator { color: var(--color-gray-300); user-select: none; }
"""

PAGINATION = """/* ============================================
 * Component: Pagination | Taxonomy: mcs:Molecule
 * Purpose: Page navigation for paginated content
 * Elements: __list, __item, __ellipsis
 * ============================================ */

.c-pagination__list { display: flex; align-items: center; gap: var(--space-1); list-style: none; padding: 0; }
.c-pagination__item { min-width: 2.25rem; height: 2.25rem; display: flex; align-items: center; justify-content: center; font-size: var(--font-size-caption); border-radius: var(--border-radius-md); cursor: pointer; color: var(--color-text-primary); background-color: transparent; border: 1px solid transparent; transition: background-color var(--transition-fast); }
.c-pagination__item:hover { background-color: var(--color-background-secondary); }
.c-pagination__item[data-state="active"] { background-color: var(--color-background-brand); color: var(--color-text-on-brand); }
.c-pagination__item[data-state="disabled"] { opacity: 0.4; cursor: not-allowed; pointer-events: none; }
.c-pagination__ellipsis { min-width: 2.25rem; height: 2.25rem; display: flex; align-items: center; justify-content: center; color: var(--color-text-secondary); font-size: var(--font-size-caption); }
"""

DROPDOWN = """/* ============================================
 * Component: Dropdown | Taxonomy: mcs:Molecule
 * Purpose: Toggleable menu of actions
 * States: open, closed (data-state)
 * Elements: __trigger, __menu, __item
 * ============================================ */

.c-dropdown { position: relative; display: inline-block; }
.c-dropdown__trigger { cursor: pointer; }
.c-dropdown__menu { position: absolute; top: calc(100% + var(--space-1)); left: 0; min-width: 12rem; background-color: var(--color-background-primary); border: 1px solid var(--color-border-default); border-radius: var(--border-radius-md); box-shadow: var(--shadow-lg); padding: var(--space-1); z-index: var(--z-index-dropdown); display: none; }
.c-dropdown[data-state="open"] > .c-dropdown__menu { display: block; }
.c-dropdown__item { display: block; width: 100%; padding: var(--space-2) var(--space-3); font-size: var(--font-size-caption); color: var(--color-text-primary); text-decoration: none; border-radius: var(--border-radius-sm); cursor: pointer; background: none; border: none; text-align: left; }
.c-dropdown__item:hover { background-color: var(--color-background-secondary); }
"""

NAVIGATION = """/* ============================================
 * Component: Navigation | Taxonomy: mcs:Molecule
 * Purpose: Primary site navigation
 * Variants: horizontal (default), vertical (data-variant)
 * Elements: __list, __item, __link
 * ============================================ */

.c-navigation__list { display: flex; list-style: none; padding: 0; gap: var(--space-1); }
.c-navigation__link { display: block; padding: var(--space-2) var(--space-3); font-size: var(--font-size-caption); font-weight: var(--font-weight-medium); color: var(--color-text-secondary); text-decoration: none; border-radius: var(--border-radius-md); transition: color var(--transition-fast), background-color var(--transition-fast); }
.c-navigation__link:hover { color: var(--color-text-primary); background-color: var(--color-background-secondary); }
.c-navigation__link[data-state="active"] { color: var(--color-background-brand); background-color: var(--color-brand-50); }
.c-navigation[data-variant="vertical"] .c-navigation__list { flex-direction: column; gap: var(--space-1); }
.c-navigation[data-variant="vertical"] .c-navigation__link { width: 100%; }
"""

# ============================================================
# NEW ATOMS (5)
# ============================================================

TABLE = """/* ============================================
 * Component: Table | Taxonomy: mcs:Atom
 * Purpose: Data table with sortable headers and striped rows
 * States: default, loading, empty (data-state)
 * ============================================ */

.c-table { width: 100%; border-collapse: collapse; font-size: var(--font-size-caption); }
.c-table th { text-align: left; font-weight: var(--font-weight-semibold); color: var(--color-text-secondary); padding: var(--space-3) var(--space-4); border-bottom: 2px solid var(--color-border-default); }
.c-table td { padding: var(--space-3) var(--space-4); border-bottom: 1px solid var(--color-border-default); color: var(--color-text-primary); }
.c-table tr:nth-child(even) td { background-color: var(--color-background-secondary); }
.c-table[data-state="loading"] { opacity: 0.6; pointer-events: none; }
"""

SELECT = """/* ============================================
 * Component: Select | Taxonomy: mcs:Atom
 * Purpose: Dropdown selection control
 * States: default, disabled, error (data-state)
 * ============================================ */

.c-select { display: block; width: 100%; padding: var(--space-3) var(--space-4); font-size: var(--font-size-body); font-family: var(--font-family-sans); color: var(--color-text-primary); background-color: var(--color-background-primary); border: 1px solid var(--color-border-default); border-radius: var(--border-radius-md); appearance: none; background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='8'%3E%3Cpath d='M1 1l5 5 5-5' stroke='%236c757d' stroke-width='1.5' fill='none'/%3E%3C/svg%3E"); background-repeat: no-repeat; background-position: right var(--space-3) center; padding-right: var(--space-10); cursor: pointer; }
.c-select:focus { border-color: var(--color-border-interactive); box-shadow: 0 0 0 3px var(--color-brand-100); outline: none; }
.c-select[data-state="disabled"] { opacity: 0.5; cursor: not-allowed; background-color: var(--color-background-secondary); }
.c-select[data-state="error"] { border-color: var(--color-border-error); }
"""

TEXTAREA = """/* ============================================
 * Component: Textarea | Taxonomy: mcs:Atom
 * Purpose: Multi-line text input
 * States: default, disabled, error (data-state)
 * ============================================ */

.c-textarea { display: block; width: 100%; min-height: 6rem; padding: var(--space-3) var(--space-4); font-size: var(--font-size-body); font-family: var(--font-family-sans); line-height: var(--line-height-base); color: var(--color-text-primary); background-color: var(--color-background-primary); border: 1px solid var(--color-border-default); border-radius: var(--border-radius-md); resize: vertical; }
.c-textarea:focus { border-color: var(--color-border-interactive); box-shadow: 0 0 0 3px var(--color-brand-100); outline: none; }
.c-textarea[data-state="disabled"] { opacity: 0.5; cursor: not-allowed; background-color: var(--color-background-secondary); }
.c-textarea[data-state="error"] { border-color: var(--color-border-error); }
"""

RADIO = """/* ============================================
 * Component: Radio | Taxonomy: mcs:Atom
 * Purpose: Single-select radio button
 * States: checked, disabled (data-state)
 * ============================================ */

.c-radio { display: inline-flex; align-items: center; gap: var(--space-2); cursor: pointer; font-size: var(--font-size-caption); color: var(--color-text-primary); }
.c-radio__input { appearance: none; width: 1.125rem; height: 1.125rem; border: 2px solid var(--color-border-default); border-radius: var(--border-radius-full); background-color: var(--color-background-primary); cursor: pointer; transition: border-color var(--transition-fast); flex-shrink: 0; display: grid; place-content: center; }
.c-radio__input::before { content: ""; width: 0.5rem; height: 0.5rem; border-radius: var(--border-radius-full); transform: scale(0); transition: transform var(--transition-fast); background-color: var(--color-background-brand); }
.c-radio__input:checked { border-color: var(--color-background-brand); }
.c-radio__input:checked::before { transform: scale(1); }
.c-radio[data-state="disabled"] { opacity: 0.5; cursor: not-allowed; }
"""

FILE_INPUT = """/* ============================================
 * Component: File Input | Taxonomy: mcs:Atom
 * Purpose: File upload trigger
 * States: default, disabled (data-state)
 * ============================================ */

.c-file-input { display: inline-flex; align-items: center; gap: var(--space-3); }
.c-file-input__trigger { display: inline-flex; align-items: center; padding: var(--space-2) var(--space-4); font-size: var(--font-size-caption); font-weight: var(--font-weight-medium); border: 1px solid var(--color-border-default); border-radius: var(--border-radius-md); background-color: var(--color-background-secondary); color: var(--color-text-primary); cursor: pointer; }
.c-file-input__trigger:hover { background-color: var(--color-gray-100); }
.c-file-input__name { font-size: var(--font-size-caption); color: var(--color-text-secondary); }
.c-file-input__input { display: none; }
.c-file-input[data-state="disabled"] .c-file-input__trigger { opacity: 0.5; cursor: not-allowed; }
"""

# ============================================================
# NEW MOLECULES (7)
# ============================================================

MODAL = """/* ============================================
 * Component: Modal | Taxonomy: mcs:Molecule
 * Purpose: Overlay dialog for focused interactions
 * States: open, closed (data-state)
 * Elements: __overlay, __content, __header, __body, __footer
 * ============================================ */

.c-modal__overlay { position: fixed; inset: 0; background-color: rgba(0,0,0,0.5); display: flex; align-items: center; justify-content: center; z-index: var(--z-index-modal); padding: var(--space-4); }
.c-modal__content { background-color: var(--color-background-primary); border-radius: var(--border-radius-lg); box-shadow: var(--shadow-lg); width: 100%; max-width: 32rem; }
.c-modal__header { padding: var(--space-5) var(--space-5) 0; font-size: var(--font-size-subtitle); font-weight: var(--font-weight-semibold); }
.c-modal__body { padding: var(--space-5); color: var(--color-text-secondary); line-height: var(--line-height-base); }
.c-modal__footer { padding: var(--space-4) var(--space-5); display: flex; justify-content: flex-end; gap: var(--space-3); border-top: 1px solid var(--color-border-default); }
"""

TABS = """/* ============================================
 * Component: Tabs | Taxonomy: mcs:Molecule
 * Purpose: Tabbed content panels
 * Elements: __list, __tab, __panel
 * ============================================ */

.c-tabs__list { display: flex; border-bottom: 2px solid var(--color-border-default); gap: 0; }
.c-tabs__tab { padding: var(--space-3) var(--space-5); font-size: var(--font-size-caption); font-weight: var(--font-weight-medium); color: var(--color-text-secondary); cursor: pointer; border-bottom: 2px solid transparent; margin-bottom: -2px; transition: color var(--transition-fast), border-color var(--transition-fast); background: none; border-top: none; border-left: none; border-right: none; }
.c-tabs__tab:hover { color: var(--color-text-primary); }
.c-tabs__tab[data-state="active"] { color: var(--color-background-brand); border-bottom-color: var(--color-background-brand); }
.c-tabs__panel { padding: var(--space-5) 0; }
.c-tabs__panel[data-state="hidden"] { display: none; }
"""

ACCORDION = """/* ============================================
 * Component: Accordion | Taxonomy: mcs:Molecule
 * Purpose: Expandable content sections
 * States: open, closed (data-state)
 * Elements: __item, __trigger, __panel
 * ============================================ */

.c-accordion__item { border-bottom: 1px solid var(--color-border-default); }
.c-accordion__trigger { display: flex; align-items: center; justify-content: space-between; width: 100%; padding: var(--space-4) 0; font-size: var(--font-size-body); font-weight: var(--font-weight-medium); color: var(--color-text-primary); background: none; border: none; cursor: pointer; text-align: left; }
.c-accordion__trigger::after { content: "+"; font-size: 1.25rem; transition: transform var(--transition-fast); }
.c-accordion__item[data-state="open"] .c-accordion__trigger::after { content: "-"; }
.c-accordion__panel { padding: 0 0 var(--space-4); color: var(--color-text-secondary); line-height: var(--line-height-base); }
.c-accordion__item:not([data-state="open"]) .c-accordion__panel { display: none; }
"""

TOAST = """/* ============================================
 * Component: Toast | Taxonomy: mcs:Molecule
 * Purpose: Transient notification
 * States: visible, hidden (data-state)
 * Variants: success, error, warning, info (data-variant)
 * ============================================ */

.c-toast { position: fixed; top: var(--space-4); right: var(--space-4); z-index: var(--z-index-toast); padding: var(--space-4); border-radius: var(--border-radius-md); box-shadow: var(--shadow-lg); display: flex; align-items: flex-start; gap: var(--space-3); min-width: 18rem; max-width: 24rem; animation: mcss-toast-in 0.3s ease; background-color: var(--color-background-primary); border: 1px solid var(--color-border-default); }
.c-toast[data-variant="success"] { border-color: var(--color-border-success); }
.c-toast[data-variant="error"] { border-color: var(--color-border-error); }
.c-toast__close { flex-shrink: 0; background: none; border: none; cursor: pointer; color: var(--color-text-secondary); font-size: 1.25rem; line-height: 1; }
@keyframes mcss-toast-in { from { transform: translateX(100%); opacity: 0; } to { transform: translateX(0); opacity: 1; } }
"""

COMBOBOX = """/* ============================================
 * Component: Combobox | Taxonomy: mcs:Molecule
 * Purpose: Text input with filtered dropdown
 * States: open, closed (data-state)
 * Elements: __input, __menu, __option
 * ============================================ */

.c-combobox { position: relative; }
.c-combobox__input { width: 100%; }
.c-combobox__menu { position: absolute; top: 100%; left: 0; right: 0; background-color: var(--color-background-primary); border: 1px solid var(--color-border-default); border-radius: var(--border-radius-md); box-shadow: var(--shadow-md); z-index: var(--z-index-dropdown); max-height: 12rem; overflow-y: auto; display: none; }
.c-combobox[data-state="open"] .c-combobox__menu { display: block; }
.c-combobox__option { padding: var(--space-2) var(--space-4); font-size: var(--font-size-caption); cursor: pointer; color: var(--color-text-primary); }
.c-combobox__option:hover { background-color: var(--color-background-secondary); }
.c-combobox__option[data-state="active"] { background-color: var(--color-brand-50); }
"""

DATE_PICKER = """/* ============================================
 * Component: Date Picker | Taxonomy: mcs:Molecule
 * Purpose: Calendar date selection
 * Elements: __header, __grid, __day
 * ============================================ */

.c-date-picker { background-color: var(--color-background-primary); border: 1px solid var(--color-border-default); border-radius: var(--border-radius-lg); padding: var(--space-4); width: 17.5rem; }
.c-date-picker__header { display: flex; justify-content: space-between; align-items: center; margin-bottom: var(--space-3); font-weight: var(--font-weight-semibold); font-size: var(--font-size-caption); }
.c-date-picker__grid { display: grid; grid-template-columns: repeat(7, 1fr); gap: 2px; text-align: center; }
.c-date-picker__day { padding: var(--space-2); font-size: var(--font-size-caption); border-radius: var(--border-radius-sm); cursor: pointer; color: var(--color-text-primary); }
.c-date-picker__day:hover { background-color: var(--color-background-secondary); }
.c-date-picker__day[data-state="selected"] { background-color: var(--color-background-brand); color: var(--color-text-on-brand); }
.c-date-picker__day[data-state="disabled"] { color: var(--color-gray-300); cursor: not-allowed; pointer-events: none; }
"""

FILE_UPLOAD = """/* ============================================
 * Component: File Upload | Taxonomy: mcs:Molecule
 * Purpose: Drag-and-drop file upload area
 * States: default, dragover, uploading, complete, error (data-state)
 * Elements: __zone, __icon, __text, __list
 * ============================================ */

.c-file-upload__zone { display: flex; flex-direction: column; align-items: center; justify-content: center; gap: var(--space-3); padding: var(--space-10); border: 2px dashed var(--color-border-default); border-radius: var(--border-radius-lg); background-color: var(--color-background-secondary); cursor: pointer; transition: border-color var(--transition-fast), background-color var(--transition-fast); text-align: center; }
.c-file-upload__zone:hover { border-color: var(--color-border-interactive); background-color: var(--color-brand-50); }
.c-file-upload[data-state="dragover"] .c-file-upload__zone { border-color: var(--color-background-brand); background-color: var(--color-brand-50); }
.c-file-upload__icon { color: var(--color-gray-400); }
.c-file-upload__text { font-size: var(--font-size-caption); color: var(--color-text-secondary); }
.c-file-upload__list { margin-top: var(--space-4); }
"""

# ============================================================
# NEW ORGANISMS (5)
# ============================================================

DASHBOARD_HEADER = """/* ============================================
 * Component: Dashboard Header | Taxonomy: mcs:Organism
 * Purpose: Application header with logo, nav, user menu, and notifications
 * Elements: __logo, __nav, __actions, __user-menu, __notification-badge
 * ============================================ */

.c-dashboard-header { display: flex; align-items: center; justify-content: space-between; padding: var(--space-3) var(--space-6); background-color: var(--color-background-primary); border-bottom: 1px solid var(--color-border-default); }
.c-dashboard-header__logo { font-size: var(--font-size-subtitle); font-weight: var(--font-weight-bold); color: var(--color-text-primary); }
.c-dashboard-header__nav { display: flex; gap: var(--space-4); }
.c-dashboard-header__actions { display: flex; align-items: center; gap: var(--space-3); }
"""

SETTINGS_PANEL = """/* ============================================
 * Component: Settings Panel | Taxonomy: mcs:Organism
 * Purpose: Grouped settings with sidebar navigation
 * Elements: __sidebar, __sections, __section, __save
 * ============================================ */

.c-settings-panel { display: flex; min-height: 100%; }
.c-settings-panel__sidebar { width: 14rem; padding: var(--space-6) var(--space-4); border-right: 1px solid var(--color-border-default); display: flex; flex-direction: column; gap: var(--space-1); flex-shrink: 0; }
.c-settings-panel__sections { flex: 1; padding: var(--space-6); overflow-y: auto; }
.c-settings-panel__section { margin-bottom: var(--space-8); }
.c-settings-panel__save { margin-top: var(--space-4); }
"""

REGISTRATION_WIZARD = """/* ============================================
 * Component: Registration Wizard | Taxonomy: mcs:Organism
 * Purpose: Multi-step registration form
 * Elements: __steps, __step, __content, __actions
 * ============================================ */

.c-registration-wizard__steps { display: flex; justify-content: center; gap: var(--space-2); margin-bottom: var(--space-8); }
.c-registration-wizard__step { width: 2rem; height: 2rem; border-radius: var(--border-radius-full); display: flex; align-items: center; justify-content: center; font-size: var(--font-size-caption); font-weight: var(--font-weight-semibold); background-color: var(--color-background-secondary); color: var(--color-text-secondary); }
.c-registration-wizard__step[data-state="active"] { background-color: var(--color-background-brand); color: var(--color-text-on-brand); }
.c-registration-wizard__step[data-state="complete"] { background-color: var(--color-green-500); color: var(--color-white); }
.c-registration-wizard__content { max-width: 32rem; margin: 0 auto; }
.c-registration-wizard__actions { display: flex; justify-content: space-between; margin-top: var(--space-6); }
"""

DATA_TABLE_O = """/* ============================================
 * Component: DataTable | Taxonomy: mcs:Organism
 * Purpose: Full-featured data table with search, sort, pagination
 * Elements: __toolbar, __search, __table, __pagination
 * ============================================ */

.c-datatable__toolbar { display: flex; justify-content: space-between; align-items: center; padding: var(--space-4) 0; }
.c-datatable__search { width: 18rem; }
.c-datatable__table { width: 100%; }
.c-datatable__pagination { display: flex; justify-content: center; padding: var(--space-4) 0; }
"""

KANBAN_BOARD = """/* ============================================
 * Component: Kanban Board | Taxonomy: mcs:Organism
 * Purpose: Draggable task board with columns
 * Elements: __column, __card, __add-button
 * ============================================ */

.c-kanban-board { display: flex; gap: var(--space-4); overflow-x: auto; padding: var(--space-4); min-height: 60vh; }
.c-kanban-board__column { flex: 0 0 18rem; background-color: var(--color-background-secondary); border-radius: var(--border-radius-lg); padding: var(--space-3); display: flex; flex-direction: column; gap: var(--space-2); }
.c-kanban-board__card { background-color: var(--color-background-primary); border: 1px solid var(--color-border-default); border-radius: var(--border-radius-md); padding: var(--space-3); cursor: grab; box-shadow: var(--shadow-sm); }
.c-kanban-board__card:hover { box-shadow: var(--shadow-md); }
.c-kanban-board__add-button { width: 100%; padding: var(--space-2); background: none; border: 1px dashed var(--color-border-default); border-radius: var(--border-radius-md); color: var(--color-text-secondary); cursor: pointer; font-size: var(--font-size-caption); }
"""

# ============================================================
# WRITE ALL FILES
# ============================================================

atoms = {
    "button.css": BUTTON, "input.css": INPUT, "badge.css": BADGE, "avatar.css": AVATAR,
    "icon.css": ICON, "label.css": LABEL, "spinner.css": SPINNER, "divider.css": DIVIDER,
    "text.css": TEXT, "link.css": LINK, "image.css": IMAGE, "checkbox.css": CHECKBOX,
    "toggle.css": TOGGLE, "tooltip.css": TOOLTIP, "progress.css": PROGRESS,
    "table.css": TABLE, "select.css": SELECT, "textarea.css": TEXTAREA,
    "radio.css": RADIO, "file-input.css": FILE_INPUT,
}

molecules = {
    "card.css": CARD, "search-form.css": SEARCH_FORM, "login-form.css": LOGIN_FORM,
    "alert.css": ALERT, "breadcrumb.css": BREADCRUMB, "pagination.css": PAGINATION,
    "dropdown.css": DROPDOWN, "navigation.css": NAVIGATION,
    "modal.css": MODAL, "tabs.css": TABS, "accordion.css": ACCORDION,
    "toast.css": TOAST, "combobox.css": COMBOBOX, "date-picker.css": DATE_PICKER,
    "file-upload.css": FILE_UPLOAD,
}

organisms = {
    "dashboard-header.css": DASHBOARD_HEADER, "settings-panel.css": SETTINGS_PANEL,
    "registration-wizard.css": REGISTRATION_WIZARD, "datatable.css": DATA_TABLE_O,
    "kanban-board.css": KANBAN_BOARD,
}

# Create organisms directory first
(SRC / "components" / "organisms").mkdir(exist_ok=True)

for name, css in {**atoms, **molecules, **organisms}.items():
    subdir = "atoms" if name in atoms else ("molecules" if name in molecules else "organisms")
    path = SRC / "components" / subdir / name
    path.write_text(css.strip() + "\n")
    existed = "U" if path.exists() else "NEW"
    print(f"  {existed}: components/{subdir}/{name}")

# ============================================================
# UPDATE COMPONENT AGGREGATOR
# ============================================================

aggregator = """/* Layer 3: Component — Aggregated c-* components */

/* Atoms */
"""
for name in atoms:
    aggregator += f'@import "../components/atoms/{name}";\n'
aggregator += "\n/* Molecules */\n"
for name in molecules:
    aggregator += f'@import "../components/molecules/{name}";\n'
aggregator += "\n/* Organisms */\n"
for name in organisms:
    aggregator += f'@import "../components/organisms/{name}";\n'

(SRC / "layers" / "component.css").write_text(aggregator)
print(f"\n  Updated: layers/component.css ({len(atoms)} atoms + {len(molecules)} molecules + {len(organisms)} organisms)")

print(f"\nTotal components: {len(atoms)} atoms + {len(molecules)} molecules + {len(organisms)} organisms = {len(atoms)+len(molecules)+len(organisms)}")
