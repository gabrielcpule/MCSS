/**
 * ESLint rule: @mcss/onc-compliance
 * Ensures classes use correct layer prefixes.
 * l-* for layout, c-* for components, u-* for utilities.
 */
const LAYER_PREFIXES = {
  layout: 'l-',
  component: 'c-',
  utility: 'u-'
};

module.exports = {
  meta: {
    type: 'problem',
    docs: {
      description: 'Enforce Ontological Naming Convention layer prefixes',
      category: 'MCSS',
      recommended: true
    },
    schema: []
  },

  create(context) {
    return {
      JSXAttribute(node) {
        if (node.name.name === 'className') {
          const value = node.value?.value || '';
          const classes = value.split(/\s+/);

          for (const cls of classes) {
            if (!cls) continue;

            // Check prefix validity
            const prefix = cls[0];
            if (prefix === 'l' && !cls.startsWith('l-')) {
              // Valid l- prefix
            } else if (prefix === 'c' && !cls.startsWith('c-')) {
              // Valid c- prefix
            } else if (prefix === 'u' && !cls.startsWith('u-')) {
              // Valid u- prefix
            } else if (['l', 'c', 'u'].includes(prefix) && cls.length > 2) {
              if (cls[1] !== '-') {
                context.report({
                  node,
                  message: `Class "${cls}" — invalid prefix. Use l- (layout), c- (component), or u- (utility).`
                });
              }
            }
          }
        }
      }
    };
  }
};
