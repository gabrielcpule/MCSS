# MCSS vs Tailwind: Missing Classes, Components, and Custom Styles

This document lists the classes, components, and styles that were missing from the MCSS framework or documentation, which required custom creation or adaptation when substituting for Tailwind CSS. It also explains the rationale for each custom addition or adaptation.

---

## 1. Responsive Layout Utilities

**Missing in MCSS:**
- Tailwind provides responsive utility classes (e.g., `lg:flex-row`, `sm:max-w-sm`, `hidden`, `block`, etc.) for controlling layout and visibility at different breakpoints.
- MCSS, as provided, does not include responsive utility classes or breakpoint-based composition helpers.

**Custom Solution:**
- Used inline styles and the `l-grid`/`l-stack` composition classes to approximate two-column layouts and vertical stacking.
- For hiding/showing elements at breakpoints, no direct MCSS equivalent was available, so no responsive visibility was implemented.

**Reasoning:**
- MCSS focuses on semantic, component-based, and utility classes, but lacks a built-in responsive system. Inline styles and composition classes were the closest available tools.

---

## 2. Image Container / Media Block

**Missing in MCSS:**
- Tailwind's `object-contain`, `max-h-full`, `max-w-full`, and responsive sizing utilities for images.
- MCSS does not provide a dedicated media/image block or utility classes for image sizing and object-fit.

**Custom Solution:**
- Used inline styles: `object-fit: contain; max-height: 90vh; max-width: 100%` on the `<img>` element.
- Optionally, a custom class like `c-card__media` could be introduced for future MCSS versions.

**Reasoning:**
- To visually match the Tailwind layout, these styles were necessary for the placeholder image. Inline styles were used to avoid polluting the MCSS class namespace.

---

## 3. Button and Link Variants

**Missing in MCSS:**
- Tailwind provides many button variants and link styles (e.g., `font-semibold`, `text-indigo-600`, `hover:text-indigo-500`).
- MCSS provides `c-button`, `c-button--primary`, and `c-button--secondary`, but not all color/text/hover variants.

**Custom Solution:**
- Used MCSS button classes where possible.
- For the "Forgot password?" link, used a `c-button c-button--secondary` with additional inline styles to mimic a text link (font size, color, underline, no background/border).

**Reasoning:**
- MCSS does not have a dedicated link or text-button style. Inline styles were used to visually match the Tailwind design while maintaining semantic annotations.

---

## 4. Spacing and Sizing Utilities

**Missing in MCSS:**
- Tailwind's granular spacing utilities (e.g., `px-3`, `py-1.5`, `mt-10`, `w-full`, `h-10`, etc.).
- MCSS provides spacing tokens and some composition classes, but not the same level of utility granularity.

**Custom Solution:**
- Used MCSS spacing tokens in inline styles and composition classes (e.g., `--stack-space: var(--mcs-spacing-md);`).
- For precise spacing, inline styles were sometimes necessary.

**Reasoning:**
- To achieve similar visual rhythm and alignment as Tailwind, direct spacing values were needed.

---

## 5. Responsive Card Widths

**Missing in MCSS:**
- Tailwind's `max-w-sm`, `w-full`, and responsive width utilities.
- MCSS does not provide responsive width helpers.

**Custom Solution:**
- Used inline styles: `max-width: 24rem; width: 100%; margin: auto;` on the card container.

**Reasoning:**
- To center and size the card similarly to Tailwind's responsive card, inline styles were required.

---

## Summary Table

| Feature/Utility         | Tailwind Class Example      | MCSS Equivalent | Custom/Inline Used? | Reasoning |
|------------------------|----------------------------|-----------------|--------------------|-----------|
| Responsive layout      | `lg:flex-row`              | None            | Yes                | No MCSS responsive utilities |
| Image sizing           | `object-contain`           | None            | Yes                | No MCSS image/media block |
| Button/link variants   | `text-indigo-600`          | Partial         | Yes                | No MCSS text-link style |
| Spacing utilities      | `px-3`, `mt-10`            | Partial         | Yes                | MCSS less granular |
| Card width             | `max-w-sm`, `w-full`       | None            | Yes                | No MCSS width helpers |

---

## Conclusion

MCSS provides a strong semantic and component-based foundation, but lacks many of the utility and responsive features found in Tailwind CSS. Where MCSS was missing a feature, inline styles or minimal custom classes were used to achieve visual and functional parity, always prioritizing semantic clarity and MCSS architectural guidelines.
