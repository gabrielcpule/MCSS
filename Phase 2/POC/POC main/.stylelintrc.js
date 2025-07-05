// Stylelint configuration to enforce MCSS Ontological Naming Convention (ONC)
module.exports = {
  plugins: ['stylelint-selector-bem-pattern'], // [13]
  rules: {
    // Enforces the c-, l-, u- prefixes and BEM syntax [14]
    'plugin/selector-bem-pattern': {
      preset: 'bem',
      componentSelectors: {
        initial: '^\\.(?:[clu])-{1,2}[a-zA-Z0-9]+(?:-[a-zA-Z0-9]+)*(?:__[a-zA-Z0-9]+(?:-[a-zA-Z0-9]+)*)?(?:--[a-zA-Z0-9]+(?:-[a-zA-Z0-9]+)*)?$',
        combined: '.*',
      },
      utilitySelectors: '^\\.u-[a-z0-9]+(?:-[a-z0-9]+)*$',
      message: 'Expected class selector to follow MCSS ONC rules (e.g., c-card__title--primary, l-stack, u-text-center)'
    },
    // Rule to forbid external margins on components (Block Layer)
    // This would require a custom plugin, but we can enforce it via code reviews and team standards.
    // 'mcss/no-external-margin': true, 
  },
};
