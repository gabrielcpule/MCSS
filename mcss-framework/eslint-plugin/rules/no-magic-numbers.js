/**
 * ESLint rule: @mcss/no-magic-numbers
 * Catches hard-coded CSS values (px, rem, em, hex, rgb) not using var() tokens.
 * Applies to CSS files and inline style objects in JSX/TSX.
 */
const MAGIC_PATTERNS = [
  /\d+px\b/,
  /\d+rem\b/,
  /\d+em\b/,
  /#[0-9a-fA-F]{3,8}\b/,
  /rgb\(\s*\d+/,
  /rgba\(\s*\d+/,
  /hsl\(\s*\d+/
];

const ALLOWED_PLAIN = ['0', 'none', 'auto', 'inherit', 'initial', 'unset', 'transparent', 'currentColor'];

module.exports = {
  meta: {
    type: 'problem',
    docs: {
      description: 'Disallow magic numbers in CSS — all values must use var() tokens',
      category: 'MCSS',
      recommended: true
    },
    schema: []
  },

  create(context) {
    return {
      // CSS-in-JS template literals
      TaggedTemplateExpression(node) {
        if (node.tag.name === 'css' || node.tag.name === 'styled') {
          for (const quasi of node.quasi.quasis) {
            for (const pattern of MAGIC_PATTERNS) {
              if (pattern.test(quasi.value.raw) && !quasi.value.raw.includes('var(')) {
                context.report({
                  node,
                  message: `Magic number found. Use var(--token) instead.`
                });
              }
            }
          }
        }
      },

      // Inline style objects
      Property(node) {
        if (node.value?.type === 'Literal' && typeof node.value.value === 'string') {
          for (const pattern of MAGIC_PATTERNS) {
            if (pattern.test(node.value.value)) {
              context.report({
                node,
                message: `Magic number "${node.value.value}" in style. Use var(--token).`
              });
            }
          }
        }
      }
    };
  }
};
