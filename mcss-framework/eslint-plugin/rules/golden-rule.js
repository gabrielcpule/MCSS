/**
 * ESLint rule: @mcss/golden-rule
 * Ensures c-* component classes never declare margin on their root selector.
 */
module.exports = {
  meta: {
    type: 'problem',
    docs: {
      description: 'Disallow margin on c-* component root selectors',
      category: 'MCSS',
      recommended: true
    },
    schema: []
  },

  create(context) {
    return {
      // CSS-in-JS: detect margin in component styles
      TaggedTemplateExpression(node) {
        if (node.tag.name === 'css' || node.tag.name === 'styled') {
          for (const quasi of node.quasi.quasis) {
            const text = quasi.value.raw;

            // Check for .c-something { ... margin ... } pattern (no BEM element)
            const componentPattern = /\.c-([a-zA-Z]+)\s*\{[^}]*\b(margin|margin-top|margin-bottom|margin-left|margin-right)\s*:/s;
            const match = text.match(componentPattern);

            if (match && !text.includes('__')) {
              context.report({
                node,
                message: `Golden Rule violation: .c-${match[1]} declares ${match[2]}. Components cannot set external margins.`
              });
            }
          }
        }
      }
    };
  }
};
