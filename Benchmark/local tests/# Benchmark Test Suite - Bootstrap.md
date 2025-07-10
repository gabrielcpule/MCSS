# Benchmark Test Suite - Bootstrap

These prompts focus on leveraging Bootstrap's pre-built components, extensive utility classes, and JavaScript plugins to rapidly build responsive and functional UIs to compare with MCSS benchmark results.

## Complexity Level 1 Tests

### Test 1.1: User Profile Card

**Prompt:** "Create a user profile card using Bootstrap. The card should display a user's avatar, name, and job title. It must also include a 'Contact' button styled as a primary action. Use Bootstrap's Card component and Grid system for layout. Ensure the HTML is semantic (e.g., `<img>`, `<h2>`, `<p>`) and responsive."

**Expected Output:** A single, responsive `.card` component containing a `.card-img-top`, `.card-body`, and a `.btn-primary`. The component should adapt gracefully to different screen sizes.

## Complexity Level 2 Tests

### Test 2.1: Modal Dialog with Form

**Prompt:** "Build a modal dialog that contains a simple contact form (Name, Email, and Message). The modal should be triggered by a button. Use Bootstrap's Modal JavaScript plugin to manage its state, backdrop, and focus. The form inside should be marked up with Bootstrap's form control classes. Ensure the modal is accessible, allowing closure via the Escape key and a close button."

**Expected Output:** A button that, when clicked, launches a fully functional modal (`.modal`). The modal must contain a form styled with `.form-control` and `.form-label`, and it must correctly trap focus and be dismissible as per Bootstrap's default behavior.

## Complexity Level 3 Tests

### Test 3.1: Advanced Tab Interface

**Prompt:** "Create a tabbed interface using Bootstrap's Navs and Tabs component. The interface must support at least three tabs. One of these tabs should contain a nested tab interface. Implement a 'loading' state by using JavaScript to simulate fetching content for a tab pane, displaying a Bootstrap Spinner for 2 seconds before showing the content. Ensure all tabs are keyboard-navigable."

**Expected Output:** A functional tab layout using Bootstrap's `.nav-tabs` and `.tab-content`. One `.tab-pane` must contain another complete tab component. The specified pane should correctly display a `.spinner-border` before revealing its content.

## Complexity Level 4 Tests

### Test 4.1: Dashboard Page Layout

**Prompt:** "Design a responsive dashboard page layout using Bootstrap. The layout must include a fixed-top Navbar, a vertical navigation sidebar, and a main content area. Use Bootstrap's Grid system to create the sidebar and main content columns. The main content area should contain at least three Card components acting as widgets. The layout must be fully responsive, collapsing the sidebar for smaller screens."

**Expected Output:** A full HTML page demonstrating a common dashboard structure. It should feature a `.navbar-fixed-top`, a sidebar column (`.col-md-3`), and a main content column (`.col-md-9`) that stack vertically on mobile screens.

## Complexity Level 5 Tests

### Test 5.1: Complete SaaS Application Page

**Prompt:** "Assemble a complete SaaS application page using Bootstrap components. The page must feature a main Navbar, a collapsible sidebar (built with the Grid and Collapse plugin), and a main workspace. The workspace should use the Grid system to feature multiple content panels (built with Cards). Implement a Toast component for notifications and a Modal component for a 'User Settings' overlay. A significant amount of custom JavaScript will be needed to coordinate the state between these components."

**Expected Output:** A complex, single-page layout that integrates a navbar, a collapsible sidebar, toasts, and a modal. The components must work together cohesively, demonstrating how to build an application shell with Bootstrap.