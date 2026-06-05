/**
 * ESLint rule: @mcss/require-rdfa
 * Ensures MCSS components declare typeof="mcs:Component" and taxonomyLevel.
 */
module.exports = {
  meta: {
    type: 'problem',
    docs: {
      description: 'Require RDFa annotations on MCSS components',
      category: 'MCSS',
      recommended: true
    },
    schema: []
  },

  create(context) {
    return {
      JSXOpeningElement(node) {
        const classNameAttr = node.attributes.find(
          a => a.name?.name === 'className'
        );
        const classValue = classNameAttr?.value?.value || '';

        if (classValue.match(/\bc-[a-z]/)) {
          // Check for typeof
          const hasTypeof = node.attributes.some(
            a => a.name?.name === 'typeof' && a.value?.value === 'mcs:Component'
          );
          if (!hasTypeof) {
            context.report({
              node,
              message: `Component with class "${classValue}" missing typeof="mcs:Component"`
            });
          }

          // Check for taxonomyLevel
          const hasTaxonomy = node.attributes.some(
            a => a.name?.name === 'property' && a.value?.value?.includes('mcs:taxonomyLevel')
          );
          if (!hasTaxonomy) {
            context.report({
              node,
              message: `Component with class "${classValue}" missing property="mcs:taxonomyLevel"`
            });
          }
        }
      }
    };
  }
};
