# MCSS-POC Customizations

This document lists all classes, components, and styles that were custom-created for the login page because they were missing from the MCSS documentation or `mcss.css` file. Each entry includes an explanation of why the customization was necessary and the reasoning behind the chosen approach.

## Custom Styles and Layouts

### 1. Notification Bar Layout (Top, Full-Width, Fixed)
- **Custom Inline Styles:**
  - `position: fixed; top: 0; left: 0; right: 0; z-index: 1000; box-shadow: var(--mcs-shadow-md); border-radius: 0; min-height: unset; height: 72px; display: flex; align-items: center; justify-content: center;`
- **Reason:**
  - MCSS does not provide a dedicated notification bar or utility classes for fixed, full-width, top-aligned notification containers. These styles were added inline to achieve the required layout for a dismissable notification at the top of the page.

### 2. Notification Dismiss Button Positioning
- **Custom Inline Style:**
  - `position: absolute; top: 12px; right: 24px;`
- **Reason:**
  - MCSS does not include a utility for absolutely positioning a button within a card. This was needed to visually separate the dismiss button from the notification content and make it easily accessible.

### 3. Login Card Right Alignment
- **Custom Inline Style:**
  - `display: flex; justify-content: flex-end; align-items: center; min-height: 100vh; padding-top: 80px;` (on `<main>`)
- **Reason:**
  - MCSS provides stack and grid composition classes, but does not have a utility for right-aligning a card within the viewport. This style was added to meet the design requirement.

### 4. Notification Image Sizing
- **Custom Inline Style:**
  - `width: 72px; height: 48px; object-fit: cover; border-radius: var(--mcs-border-radius-md); margin: auto;`
- **Reason:**
  - MCSS does not provide a utility for image sizing or object-fit. This was needed for consistent notification image appearance.

## Why These Options Were Chosen
- **Minimal Customization:** All custom styles are limited to layout and positioning, not component appearance, to preserve MCSS's design system integrity.
- **Inline Styles:** Used for page-specific layout needs, as recommended by the MCSS documentation when no utility class exists.
- **MCSS Classes Used Where Possible:** All component styling, spacing, and structure use MCSS-provided classes (`c-card`, `l-stack`, `u-margin-md`, etc.).
- **Semantic Annotations:** All custom and standard elements include full semantic annotations as per the MCSS guide.

## Summary
If MCSS adds new utilities for notification bars, absolute positioning, or image sizing, these custom styles can be replaced with framework classes for even better consistency.
