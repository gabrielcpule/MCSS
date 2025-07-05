# MCSS-POC Customizations: Missing Classes, Components, and Styles

This document lists all classes, components, and styles that were custom-created for the login page because they were missing from the MCSS documentation or `mcss-poc.css`. Each entry includes an explanation of why the customization was necessary and the reasoning behind the chosen approach.

---

## 1. Custom Layout Styles (Inline `style={{ ... }}`)

### What was missing:
- No MCSS composition (`l-`) or utility (`u-`) classes for horizontal flex layouts, gap spacing, or responsive centering.
- No MCSS class for setting max-width, min-width, or flex-basis for responsive containers.
- No MCSS class for custom background colors (e.g., marketing background).

### Customizations Used:
- Inline styles for `display: flex`, `gap`, `alignItems`, `justifyContent`, `maxWidth`, `minWidth`, `flex`, and `background` on layout containers.

### Why:
- These are page-level layout needs not covered by MCSS. The MCSS framework currently only provides `l-stack` (vertical spacing) and `l-grid` (responsive grid), but not horizontal flex or centering utilities.
- Inline styles were used to avoid polluting the global CSS and to keep the MCSS block/component classes clean.
- This approach is compliant with the MCSS philosophy: custom styles are only for layout, not for component styling.

---

## 2. Social Login Button Styles

### What was missing:
- No MCSS modifier or utility class for circular, colored social login buttons (Google, LinkedIn, Facebook, GitHub).

### Customizations Used:
- Inline styles for `background`, `color`, `borderRadius: '50%'`, `width`, `height`, and flex centering on each social login button.

### Why:
- MCSS provides `c-button` and `c-button--primary/secondary`, but not social-specific or circular button modifiers.
- Inline styles allow for quick, isolated customization without altering the MCSS framework.
- This keeps the MCSS block/component structure intact and avoids introducing non-semantic classes.

---

## 3. Typography and Brand Highlights

### What was missing:
- No MCSS utility or modifier classes for large, bold, colored headings or brand highlights (e.g., "Sign On", "Social", "Networking").

### Customizations Used:
- Inline styles for `fontSize`, `fontWeight`, `color`, `background`, `padding`, `borderRadius`, `boxShadow`, and `margin` on heading spans.

### Why:
- MCSS provides base typography tokens but not utility classes for large, bold, or colored text.
- Inline styles allow for precise, one-off branding effects as shown in the reference image.

---

## 4. Password Visibility Icon

### What was missing:
- No MCSS utility or component for password visibility toggle icon placement.

### Customizations Used:
- Inline styles for `position: absolute`, `right`, `top`, `transform`, `color`, and `cursor` on the icon span.

### Why:
- MCSS does not provide a utility for absolute positioning of icons inside input fields.
- Inline styles ensure the icon is accessible and visually correct without affecting the MCSS component structure.

---

## Summary

All customizations were made only for layout, branding, or one-off UI needs not covered by the MCSS framework. No custom classes or styles were used for core component styling, in accordance with MCSS guidelines. If these patterns are needed elsewhere, consider adding new `l-` (composition) or `u-` (utility) classes to MCSS for future reuse.
