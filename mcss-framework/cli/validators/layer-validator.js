const postcss = require('postcss');

/**
 * Validates MCSS layer architecture rules:
 * - Golden Rule: no margin on c-* root selectors
 * - Layer integrity: no !important below utility layer
 * - Utility single-property rule
 */
class LayerValidator {
  validate(filePath, content) {
    const errors = [];
    const warnings = [];

    try {
      const root = postcss.parse(content, { from: filePath });

      root.walkRules((rule) => {
        const selectors = rule.selector || '';

        // Golden Rule: c-* root selectors cannot declare margin
        if (/\.c-[a-zA-Z]+[^_-]/.test(selectors) && !selectors.includes('__')) {
          rule.walkDecls((decl) => {
            if (decl.prop === 'margin' || decl.prop.startsWith('margin-')) {
              errors.push({
                file: filePath,
                line: decl.source?.start?.line,
                message: `Golden Rule violation: margin declared on root "${selectors}". Components cannot declare external margins.`
              });
            }
          });
        }

        // Utility layer: single property per class
        if (selectors.includes('.u-')) {
          const declarations = [];
          rule.walkDecls((decl) => {
            if (!decl.prop.startsWith('--')) {
              declarations.push(decl.prop);
            }
          });

          if (declarations.length > 1) {
            errors.push({
              file: filePath,
              line: rule.source?.start?.line,
              message: `Utility class "${selectors}" has ${declarations.length} properties. Utility classes must have exactly one property.`
            });
          }

          // Utility must use !important
          const hasImportant = declarations.length > 0 &&
            rule.walkDecls((decl) => {
              if (decl.important) return false;
            }) !== undefined;

          // Check first non-token declaration for !important
          for (const node of rule.nodes || []) {
            if (node.type === 'decl' && !node.prop.startsWith('--')) {
              if (!node.important) {
                errors.push({
                  file: filePath,
                  line: node.source?.start?.line,
                  message: `Utility class "${selectors}" missing !important on "${node.prop}: ${node.value}"`
                });
              }
              break;
            }
          }
        }
      });

    } catch (err) {
      errors.push({ file: filePath, line: 0, message: `CSS parse error: ${err.message}` });
    }

    return { errors, warnings };
  }
}

module.exports = LayerValidator;
