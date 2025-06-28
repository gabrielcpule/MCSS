# MCSS-POC: Custom Classes, Components, and Styles Used

This document lists all classes, components, and styles that were custom-created for the login page and notification bar, due to their absence in the MCSS documentation or the `mcss-poc.css` file. Each entry includes an explanation of why it was needed and the rationale for the chosen implementation.

---

## 1. `.notification-bar`
**Type:** Custom composition/layout class

**Why created:**
- The MCSS-POC framework provides `l-stack` and `l-grid` for layout, but does not include a full-width, fixed-height, visually distinct notification bar component for page-level alerts.
- The notification needed to span the top of the page, be visually separated, and support a dismiss action.

**Design rationale:**
- Used `c-card` for base styling, but added `.notification-bar` for width, margin, border-radius, and box-shadow to create a visually distinct, horizontally full-width alert area.
- Chose flexbox for vertical centering and responsiveness.
- Kept the style minimal and compositional, in line with MCSS philosophy.

---

## 2. `.login-container`
**Type:** Custom layout class

**Why created:**
- MCSS-POC does not provide a class for right-aligning a card on the page or for page-level container alignment.
- Needed to position the login card on the right side of the viewport, with responsive fallback for mobile.

**Design rationale:**
- Used flexbox and margin utilities to align the card right on desktop, and center on mobile.
- Kept the class focused on layout only, not component styling.

---

## 3. Inline Styles for Spacing and Alignment
**Type:** Custom inline style attributes (e.g., `style="--stack-space: ..."`)

**Why created:**
- MCSS-POC supports custom properties for spacing, but some spacing and alignment (e.g., padding-right, margin-top) required direct inline control for this specific layout.

**Design rationale:**
- Used inline custom properties to leverage MCSS tokens while achieving the exact layout needed for the login and notification components.

---

## 4. Responsive Media Queries
**Type:** Custom CSS in `<style>` block

**Why created:**
- MCSS-POC does not provide built-in responsive container classes for page-level layout changes (e.g., switching from right-aligned to centered on mobile).

**Design rationale:**
- Added a media query to adjust `.login-container` and `.notification-bar` for mobile screens, ensuring accessibility and usability.

---

## 5. Notification Dismiss Script
**Type:** Custom JavaScript

**Why created:**
- MCSS-POC does not provide a built-in dismissable notification component or JS utility for this behavior.

**Design rationale:**
- Added a simple script to show/hide the notification, keeping logic minimal and focused on accessibility.

---

## Summary
All custom classes and styles were created to fill gaps in the MCSS-POC framework for page-level layout, notification bar, and responsive design. The approach was to:
- Use MCSS tokens and philosophy wherever possible
- Keep custom code minimal, compositional, and non-intrusive
- Clearly separate layout/composition from component styling

If these features are needed in future MCSS versions, they could be formalized as new `l-` (layout/composition) or `c-` (component) classes.
