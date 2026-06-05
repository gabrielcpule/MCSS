/**
 * ESLint rule: @mcss/token-defined
 * Catches var() calls referencing tokens not in token-schema.json.
 */
const fs = require('fs');
const path = require('path');

let tokenSet = null;

function loadTokens() {
  if (tokenSet) return tokenSet;
  try {
    const schemaPath = path.resolve('src/tokens/token-schema.json');
    const schema = JSON.parse(fs.readFileSync(schemaPath, 'utf8'));
    tokenSet = new Set();

    for (const [category, config] of Object.entries(schema.categories)) {
      for (const value of config.values || []) {
        tokenSet.add(`--${config.prefix}-${value}`);
      }
    }

    // Color tokens
    for (const [color, config] of Object.entries(schema.tokens.color)) {
      if (config.scale) {
        for (const step of config.scale) {
          tokenSet.add(`--color-${color}-${step}`);
        }
      } else {
        tokenSet.add(`--color-${color}`);
      }
    }

    // Semantic aliases
    ['text', 'background', 'border'].forEach(group => {
      Object.keys(schema.tokens[group] || {}).forEach(key => {
        tokenSet.add(`--color-${group}-${key}`);
      });
    });

  } catch {
    tokenSet = new Set();
  }
  return tokenSet;
}

module.exports = {
  meta: {
    type: 'warn',
    docs: {
      description: 'Ensure var() references only defined MCSS tokens',
      category: 'MCSS',
      recommended: true
    },
    schema: []
  },

  create(context) {
    const tokens = loadTokens();

    return {
      CallExpression(node) {
        if (node.callee.name === 'var') {
          const arg = node.arguments[0]?.value;
          if (arg && arg.startsWith('--') && !tokens.has(arg) && !arg.startsWith('--mcss-')) {
            context.report({
              node,
              message: `Token "${arg}" is not defined in token-schema.json`
            });
          }
        }
      }
    };
  }
};
