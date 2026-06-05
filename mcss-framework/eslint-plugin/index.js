const noMagicNumbers = require('./rules/no-magic-numbers');
const tokenDefined = require('./rules/token-defined');
const goldenRule = require('./rules/golden-rule');
const oncCompliance = require('./rules/onc-compliance');
const requireRdfa = require('./rules/require-rdfa');
const requireDataState = require('./rules/require-data-state');

module.exports = {
  rules: {
    'no-magic-numbers': noMagicNumbers,
    'token-defined': tokenDefined,
    'golden-rule': goldenRule,
    'onc-compliance': oncCompliance,
    'require-rdfa': requireRdfa,
    'require-data-state': requireDataState
  },
  configs: {
    recommended: {
      plugins: ['@mcss/framework'],
      rules: {
        '@mcss/no-magic-numbers': 'error',
        '@mcss/token-defined': 'warn',
        '@mcss/golden-rule': 'error',
        '@mcss/onc-compliance': 'error',
        '@mcss/require-rdfa': 'error',
        '@mcss/require-data-state': 'warn'
      }
    }
  }
};
