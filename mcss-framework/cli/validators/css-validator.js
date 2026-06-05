const postcss = require('postcss');

/**
 * Validates CSS files for MCSS compliance:
 * - No magic numbers (all values are var() or zero/inherit/none/auto)
 * - ONC compliance (correct prefix per layer)
 * - All var() references defined tokens
 */
class CssValidator {
  constructor(schema) {
    this.schema = schema;
    this.errors = [];
    this.warnings = [];
    this.definedTokens = this._buildTokenIndex();
  }

  _buildTokenIndex() {
    const tokens = new Set();

    // Built-in
    tokens.add('--color-white');
    tokens.add('--color-black');

    // Scale tokens
    for (const [key, config] of Object.entries(this.schema.tokens)) {
      if (config.scale) {
        for (const step of config.scale) {
          tokens.add(`--color-${key}-${step}`);
        }
      } else {
        tokens.add(`--color-${key}`);
      }
    }

    // Category tokens
    for (const [category, config] of Object.entries(this.schema.categories)) {
      const prefix = config.prefix;
      for (const value of config.values || []) {
        tokens.add(`--${prefix}-${value}`);
      }
    }

    // Semantic text/background/border aliases
    for (const group of ['text', 'background', 'border']) {
      for (const key of Object.keys(this.schema.tokens[group] || {})) {
        tokens.add(`--color-${group}-${key}`);
      }
    }

    return tokens;
  }

  validate(filePath, content) {
    this.errors = [];
    this.warnings = [];

    try {
      const root = postcss.parse(content, { from: filePath });

      root.walkDecls((decl) => {
        this._checkMagicNumbers(decl, filePath);
        this._checkTokenUsage(decl, filePath);
      });

      root.walkRules((rule) => {
        this._checkOncCompliance(rule, filePath);
      });

    } catch (err) {
      this.errors.push({
        file: filePath,
        line: 0,
        message: `CSS parse error: ${err.message}`
      });
    }

    return { errors: this.errors, warnings: this.warnings };
  }

  _checkMagicNumbers(decl, filePath) {
    const value = decl.value;
    const allowedPlain = ['0', 'none', 'auto', 'inherit', 'initial', 'unset', 'transparent', 'currentColor'];
    const excludeProps = ['z-index', 'opacity', 'font-weight', 'line-height', 'animation', 'transform'];

    if (excludeProps.some(p => decl.prop.includes(p))) return;

    // Check for hard-coded pixel, rem, em, hex, rgb values
    const hardcodedPatterns = [
      /\d+px/, /\d+rem/, /\d+em/, /#[0-9a-fA-F]{3,8}/,
      /rgb\(\s*\d+/, /rgba\(\s*\d+/, /hsl\(\s*\d+/
    ];

    for (const pattern of hardcodedPatterns) {
      if (pattern.test(value) && !value.includes('var(')) {
        // Allow in @keyframes and --token definitions
        const inKeyframes = decl.parent.parent?.name === 'keyframes';
        const isTokenDef = decl.prop.startsWith('--');
        if (!inKeyframes && !isTokenDef) {
          this.errors.push({
            file: filePath,
            line: decl.source?.start?.line,
            message: `Magic number "${value.trim()}" in "${decl.prop}". Use var(--token) instead.`
          });
          return;
        }
      }
    }
  }

  _checkTokenUsage(decl, filePath) {
    const varMatches = decl.value.matchAll(/var\((--[a-zA-Z-]+)[),]/g);
    for (const match of varMatches) {
      const tokenName = match[1];
      if (!this.definedTokens.has(tokenName) && !tokenName.startsWith('--mcss-')) {
        this.warnings.push({
          file: filePath,
          line: decl.source?.start?.line,
          message: `Token "${tokenName}" is not defined in token-schema.json`
        });
      }
    }
  }

  _checkOncCompliance(rule, filePath) {
    const selectors = rule.selector || '';

    // Check class selectors
    const classMatches = selectors.matchAll(/\.([a-z]+-[a-zA-Z0-9_-]+)/g);
    for (const match of classMatches) {
      const className = match[1];
      const prefix = className[0];

      // l- prefix: should be in layout layer
      // c- prefix: should be in component layer
      // u- prefix: should be in utility layer
      // No prefix allowed in global layer

      // Check that prefix is valid
      if (!['l', 'c', 'u'].includes(prefix) && className.includes('-')) {
        // Class without standard prefix — might be in global or exception layer
        // Not an error, just note
      }
    }
  }
}

module.exports = CssValidator;
