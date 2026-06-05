/**
 * ESLint rule: @mcss/require-data-state
 * Catches class-based state modifiers (.c-button--disabled) that should use data-state.
 */
module.exports = {
  meta: {
    type: 'warn',
    docs: {
      description: 'Prefer data-state attributes over class modifiers for component state',
      category: 'MCSS',
      recommended: true
    },
    schema: []
  },

  create(context) {
    const STATE_MODIFIERS = ['disabled', 'loading', 'error', 'active', 'checked', 'open', 'closed'];

    return {
      JSXAttribute(node) {
        if (node.name.name === 'className') {
          const value = node.value?.value || '';
          const classes = value.split(/\s+/);

          for (const cls of classes) {
            for (const state of STATE_MODIFIERS) {
              if (cls.match(new RegExp(`--${state}`))) {
                context.report({
                  node,
                  message: `Class modifier "${cls}" detected. Use data-state="${state}" instead of class modifiers for component state.`
                });
              }
            }
          }
        }
      }
    };
  }
};
