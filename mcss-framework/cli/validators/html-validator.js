const { parseDocument } = require('htmlparser2');
const { DomUtils } = require('htmlparser2');

/**
 * Validates HTML files for MCSS compliance:
 * - Well-formedness
 * - RDFa completeness (typeof="mcs:Component", taxonomyLevel, purpose)
 * - Valid RDFa vocabulary usage
 * - hasPart relationship integrity
 * - Basic accessibility (labels, alt text)
 */
class HtmlValidator {
  constructor(schema) {
    this.schema = schema;
    this.errors = [];
    this.warnings = [];
  }

  validate(filePath, content) {
    this.errors = [];
    this.warnings = [];

    try {
      const dom = parseDocument(content);
      const components = DomUtils.findAll(
        (el) => el.attribs && el.attribs['typeof'] === 'mcs:Component',
        [dom]
      );

      for (const el of components) {
        this._checkRdfaCompleteness(el, filePath);
        this._checkRdfaVocabulary(el, filePath);
        this._checkHasPartRelations(el, content, filePath);
      }

      this._checkAccessibility(dom, filePath);

    } catch (err) {
      this.errors.push({
        file: filePath,
        line: 0,
        message: `HTML parse error: ${err.message}`
      });
    }

    return { errors: this.errors, warnings: this.warnings };
  }

  _checkRdfaCompleteness(el, filePath) {
    const required = this.schema.rdfa.requiredProperties;
    for (const prop of required) {
      if (prop === 'typeof') continue; // already verified

      const hasProp = Object.entries(el.attribs || {}).some(([k, v]) =>
        k === 'property' && v === prop
      ) || el.attribs?.[prop] !== undefined;

      if (!hasProp) {
        this.errors.push({
          file: filePath,
          message: `Component "${el.attribs?.class || el.name}" missing required RDFa property: ${prop}`
        });
      }
    }

    // Check taxonomy level is valid
    const taxonomyProp = Object.entries(el.attribs || {}).find(
      ([k, v]) => k === 'property' && v === 'mcs:taxonomyLevel'
    );
    if (taxonomyProp) {
      const contentAttr = el.attribs['content'];
      if (contentAttr && !this.schema.rdfa.validTaxonomyLevels.includes(contentAttr)) {
        this.errors.push({
          file: filePath,
          message: `Invalid taxonomy level "${contentAttr}" on component "${el.attribs?.class || el.name}". Valid: ${this.schema.rdfa.validTaxonomyLevels.join(', ')}`
        });
      }
    }
  }

  _checkRdfaVocabulary(el, filePath) {
    const allowedAttrs = [
      'typeof', 'property', 'content', 'resource', 'vocab',
      'class', 'id', 'style', 'data-state', 'data-variant', 'data-position',
      ...this.schema.rdfa.behavioralAttributes
    ];

    for (const attr of Object.keys(el.attribs || {})) {
      if (attr.startsWith('data-mcs-')) {
        const value = el.attribs[attr];
        const allowedValues = this.schema.rdfa.allowedValues?.[attr];
        if (allowedValues && !allowedValues.includes(value)) {
          this.warnings.push({
            file: filePath,
            message: `Attribute ${attr} has value "${value}". Allowed: ${allowedValues.join(', ')}`
          });
        }
      }
    }
  }

  _checkHasPartRelations(el, content, filePath) {
    const hasPartProps = Object.entries(el.attribs || {}).filter(
      ([k, v]) => k === 'property' && v === 'mcs:hasPart'
    );

    for (const [,] of hasPartProps) {
      const resourceId = el.attribs['resource'];
      if (resourceId) {
        const idRef = resourceId.startsWith('#') ? resourceId.slice(1) : resourceId;
        if (!content.includes(`id="${idRef}"`)) {
          this.errors.push({
            file: filePath,
            message: `hasPart references resource="${resourceId}" but no element with id="${idRef}" found`
          });
        }
      }
    }
  }

  _checkAccessibility(dom, filePath) {
    // Inputs need associated labels
    const inputs = DomUtils.findAll(
      (el) => el.name === 'input' && el.attribs?.type !== 'hidden',
      [dom]
    );

    for (const input of inputs) {
      const hasLabel = input.attribs?.['aria-label'] ||
                       input.attribs?.['aria-labelledby'];
      const id = input.attribs?.id;
      const hasLabelFor = id && DomUtils.findOne(
        (el) => el.name === 'label' && el.attribs?.for === id,
        [dom]
      );

      if (!hasLabel && !hasLabelFor) {
        this.warnings.push({
          file: filePath,
          message: `Input "${input.attribs?.name || input.attribs?.id || '(unnamed)'}" has no associated label`
        });
      }
    }

    // Images need alt text
    const images = DomUtils.findAll((el) => el.name === 'img', [dom]);
    for (const img of images) {
      if (!img.attribs?.alt && img.attribs?.role !== 'presentation') {
        this.warnings.push({
          file: filePath,
          message: `Image "${img.attribs?.src || '(no src)'}" missing alt text`
        });
      }
    }
  }
}

module.exports = HtmlValidator;
