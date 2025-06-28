# MCSS Login Page: Custom Classes, Components, and Styles

This document lists all classes, components, and styles that were custom created for the login page because they were missing from the MCSS documentation or the provided `mcss-poc.css` file. Each entry includes an explanation of why a custom solution was necessary and the reasoning behind the chosen approach.

---

## Custom Classes

### 1. `.login-container`
- **Purpose:** Main flexbox layout for the login page, aligning the visual and form sections side by side (or stacked on mobile).
- **Reason for Customization:** No MCSS layout utility provided a full-page, centered flex container with responsive direction switching.
- **Design Choice:** Used modern CSS flexbox for alignment and responsiveness, with a fallback to column layout on small screens.

### 2. `.login-visual`
- **Purpose:** Container for branding, title, and description.
- **Reason for Customization:** No MCSS component for a visual/branding section with custom spacing and typography.
- **Design Choice:** Added margin, max-width, and text styling to match the provided image and ensure visual clarity.

### 3. `.login-card`
- **Purpose:** Card-style container for the login form.
- **Reason for Customization:** MCSS provides `c-card`, but additional padding, border-radius, and shadow were needed for the desired look.
- **Design Choice:** Extended the base card with extra spacing and visual enhancements for a modern, accessible appearance.

### 4. `.social-row`
- **Purpose:** Horizontal row for social login buttons.
- **Reason for Customization:** No MCSS utility for horizontal button grouping with spacing.
- **Design Choice:** Used flexbox for even spacing and alignment, matching the visual reference.

### 5. `.social-btn`
- **Purpose:** Circular social login buttons.
- **Reason for Customization:** MCSS does not provide circular button styles or icon button variants for social logins.
- **Design Choice:** Created a simple, accessible button with hover effect and color customization for each provider.

### 6. `.login-footer`
- **Purpose:** Footer area for the sign-up link.
- **Reason for Customization:** No MCSS footer utility for form footers with centered text and inline links.
- **Design Choice:** Added text alignment and spacing to match the design and improve usability.

### 7. `.forgot-link`
- **Purpose:** Right-aligned 'Forgot password?' link above the login button.
- **Reason for Customization:** No MCSS utility for floating or aligning help links within forms.
- **Design Choice:** Used float and margin for placement, with color matching the brand primary.

---

## Custom Styles

- **Background Gradient:**
  - **Reason:** MCSS does not provide a background utility for full-page gradients.
  - **Choice:** Used a linear gradient for a modern, soft background as seen in the reference image.

- **Responsive Layout (Media Query):**
  - **Reason:** MCSS does not include responsive flex direction utilities.
  - **Choice:** Added a media query to switch to column layout on small screens for accessibility and mobile usability.

- **Password Visibility Toggle (Inline Style):**
  - **Reason:** No MCSS component for password visibility toggles.
  - **Choice:** Used inline styles for positioning the toggle icon inside the password field.

---

## Summary

All custom classes and styles were created only where MCSS or the provided CSS did not offer a suitable utility or component. The customizations focus on layout, alignment, and minor visual enhancements to match the provided image and ensure accessibility, while all core components and semantics follow MCSS guidelines.

If MCSS adds these utilities in the future, the custom classes can be replaced with official MCSS classes for better maintainability.
