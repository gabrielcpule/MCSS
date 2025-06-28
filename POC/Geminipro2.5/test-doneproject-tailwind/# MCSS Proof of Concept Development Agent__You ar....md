# **MCSS: LLM Interaction & Documentation Guide**

This document provides the necessary context for a Large Language Model (LLM) to understand, interpret, and modify components built with the Model Context Style Sheet (MCSS) framework.

## **Core Philosophy for LLMs**

My structure is designed to be **semantically transparent**. Every class name, HTML tag, and attribute is chosen to be self-describing. Your goal is to parse this structure, understand the **purpose** and **relationships** of elements, and make modifications that respect the established architecture.

### **The 5 Architectural Layers**

When I ask you to create or modify something, understand which layer is most appropriate:

1. **Global Foundation (:root)**: Only modify this layer if I ask for a site-wide, thematic change (e.g., "Change the primary brand color to green"). You will target the CSS Custom Properties (--mcs-\*).  
2. **Composition (l- classes)**: Use these to arrange components. If I say "stack these cards vertically" or "arrange these items in a responsive grid," you should apply l-stack or l-grid to their parent container.  
3. **Utilities (u- classes)**: Apply these for simple, one-off styling needs. For example, if I say "hide this label from view but keep it for screen readers," you know to add the u-visually-hidden class.  
4. **Blocks (c- classes)**: This is for components. When I ask for a "new button" or a "card," you will assemble HTML with c- classes. Modifications to existing components will involve adding modifier classes (e.g., c-button--secondary) or adjusting the internal \_\_element structure.  
5. **Exceptions (data-mcs-\* attributes)**: Use these to represent a component's **state**. Do not create new classes for states. If I say "show the error state for this input field," you should add the attribute data-mcs-validation-state="invalid" to the c-form-group container.

## **Component Interaction Examples**

### **1\. Button (c-button)**

* **HTML Structure & Annotations:**  
  \<a href="\#" class="c-button c-button--primary"   
     typeof="mcs:Component"   
     property="mcs:purpose"   
     content="A primary action button to view the user's full profile."  
     data-mcs-interaction-type="navigation"  
     data-mcs-consequence="Navigates the user to the detailed profile page for 'Alex Doe'."\>  
     View Profile  
  \</a\>

* **LLM Interpretation:**  
  * typeof="mcs:Component": This is a button component.  
  * class="c-button c-button--primary": It's a button (c-button) with the primary visual style (--primary).  
  * property="mcs:purpose": Its function is to "view the user's full profile."  
  * data-mcs-interaction-type="navigation": The user interacts with it by navigating.  
  * data-mcs-consequence: Clicking it will take the user to a profile page.  
* **Example LLM Modification Prompts:**  
  * **User:** "Change the 'View Profile' button to a secondary style."  
  * **LLM Action:** Change c-button--primary to c-button--secondary.  
  * **User:** "There's a button that takes the user to a profile page. Add a new button next to it for deleting the profile. It should be styled like an error."  
  * **LLM Action:**  
    1. Recognize the need for a new modifier class: c-button--danger.  
    2. Add the corresponding CSS to the stylesheet, using the \--mcs-color-error token.  
    3. Generate the new button's HTML with complete annotations:  
       \<button class="c-button c-button--danger"  
               typeof="mcs:Component"  
               property="mcs:purpose"  
               content="A destructive action button to delete the user's profile."  
               data-mcs-interaction-type="action"  
               data-mcs-consequence="Opens a confirmation modal before permanently deleting the user's profile."\>  
           Delete Profile  
       \</button\>

### **2\. Form Input (c-form-group)**

* **HTML Structure & Annotations:**  
  \<div class="c-form-group"   
       typeof="mcs:Component"  
       data-mcs-validation-state="invalid"  
       id="form-group-email"\>  
      \<label for="email" class="c-form-group\_\_label"\>...\</label\>  
      \<input type="email" id="email" class="c-form-group\_\_input" aria-invalid="true"\>  
      \<p id="email-desc" class="c-form-group\_\_description"\>...\</p\>  
  \</div\>

* **LLM Interpretation:**  
  * typeof="mcs:Component": This is a form group component.  
  * data-mcs-validation-state="invalid": It is currently in an "invalid" state. The CSS handles the visual styling for this state.  
  * The label, input, and description are clearly identified by their BEM element classes (\_\_label, \_\_input).  
  * aria-invalid="true" directly supports accessibility by mirroring the visual state for assistive technologies.  
* **Example LLM Modification Prompts:**  
  * **User:** "Make the email input field valid."  
  * **LLM Action:** On the c-form-group div, change data-mcs-validation-state="invalid" to data-mcs-validation-state="valid". Also, change aria-invalid="true" to aria-invalid="false" on the input.  
  * **User:** "Add a new text input field for 'First Name' before the email field. It should be required."  
  * **LLM Action:** Duplicate the c-form-group structure, update all id, for, name, and aria-describedby attributes to "first-name", and change the property="mcs:purpose" content accordingly. Remove the data-mcs-validation-state attribute to render it in its default, neutral state.

## **Validation and Compliance**

* **WCAG 2.2 AA:** All generated markup must be compliant. This includes for attributes on labels, aria-\* attributes for states (aria-invalid), and providing text alternatives.  
* **Semantic Completeness:** Every component and interactive element you create **must** have a typeof="mcs:Component" and property="mcs:purpose" annotation. This is non-negotiable.

By following these guidelines, you will be able to interpret my requests accurately and generate code that is robust, accessible, and perfectly aligned with the MCSS framework.