# Component Documentation
Auto-Generated Documentation from RDFa Annotations
Based on the RDFa annotations in the HTML, here's the auto-generated component documentation:

Button Component
Purpose: Primary action trigger for main user flows

Interaction Type: click

Consequence: form-submission, navigation, confirmation, data-deletion

Variants: primary, secondary, success, danger

Sizes: small, medium, large

States: normal, disabled, loading

Card Component
Purpose: Content container with structured information display

Structure: header, content, footer

Interaction Type: hover, click

Consequence: visual-feedback, detailed-view

Elements:

Header: Card title and metadata container

Content: Main card content area

Footer: Card actions and secondary information

Form Field Component
Purpose: User information collection with validation feedback

Input Types: text, email

Validation States: normal, error, success

Elements:

Label: Describes the input field

Input: Data entry element

Help Text: Guidance for users

Error Text: Validation feedback

LLM Interaction Examples
Example 1: Creating a New Button Variant
Prompt: "Create a warning button variant using the MCSS framework"

Expected LLM Response:

css
.c-button--warning {
  background-color: var(--mcs-color-warning);
  color: var(--mcs-color-neutral-900);
}

.c-button--warning:hover {
  background-color: #e0a800;
}
HTML Usage:

xml
<button class="c-button c-button--warning" 
        typeof="mcs:Button"
        property="mcs:purpose" 
        content="Warning action requiring user attention"
        data-mcs-interaction-type="click"
        data-mcs-consequence="warning-display">
    Warning Action
</button>
Example 2: Modifying Form Component
Prompt: "Add a password input field with strength indicator to the form"

Expected LLM Response:

xml
<div class="c-form-field" 
     typeof="mcs:FormField"
     property="mcs:input-type" 
     content="password"
     property="mcs:validation-rule" 
     content="strength-check">
    <label for="password" class="c-form-field__label">Password *</label>
    <input type="password" 
           id="password" 
           name="password"
           class="c-form-field__input"
           required
           typeof="mcs:PasswordInput"
           property="mcs:purpose" 
           content="Secure password for account protection"
           aria-describedby="password-help">
    <div class="c-password-strength" 
         typeof="mcs:PasswordStrength"
         property="mcs:purpose" 
         content="Visual password strength indicator">
        <div class="c-password-strength__bar"></div>
    </div>
    <span id="password-help" 
          class="c-form-field__help"
          typeof="mcs:HelpText">
        Password should be at least 8 characters with mixed case, numbers, and symbols
    </span>
</div>