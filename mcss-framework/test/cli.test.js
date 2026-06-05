const HtmlValidator = require('../cli/validators/html-validator');
const CssValidator = require('../cli/validators/css-validator');
const LayerValidator = require('../cli/validators/layer-validator');
const SemanticValidator = require('../cli/validators/semantic-validator');
const fs = require('fs');
const path = require('path');

const schema = JSON.parse(
  fs.readFileSync(path.join(__dirname, '..', 'src', 'tokens', 'token-schema.json'), 'utf8')
);

describe('HTML Validator', () => {
  const validator = new HtmlValidator(schema);

  it('validates a well-formed component', () => {
    const html = fs.readFileSync(
      path.join(__dirname, 'fixtures', 'valid-component.html'), 'utf8'
    );
    const result = validator.validate('test.html', html);
    expect(result.errors.filter(e => !e.message.includes('hasPart'))).toHaveLength(0);
  });

  it('detects missing RDFa properties', () => {
    const html = '<div class="c-button" typeof="mcs:Component">Click</div>';
    const result = validator.validate('test.html', html);
    expect(result.errors.length).toBeGreaterThan(0);
    expect(result.errors.some(e => e.message.includes('mcs:purpose'))).toBe(true);
  });
});

describe('CSS Validator', () => {
  const validator = new CssValidator(schema);

  it('validates token-compliant CSS', () => {
    const css = fs.readFileSync(
      path.join(__dirname, 'fixtures', 'valid-component.css'), 'utf8'
    );
    const result = validator.validate('test.css', css);
    expect(result.errors).toHaveLength(0);
  });

  it('detects magic numbers', () => {
    const css = fs.readFileSync(
      path.join(__dirname, 'fixtures', 'invalid-magic-number.css'), 'utf8'
    );
    const result = validator.validate('test.css', css);
    expect(result.errors.length).toBeGreaterThan(0);
    expect(result.errors.some(e => e.message.includes('Magic'))).toBe(true);
  });
});

describe('Layer Validator', () => {
  const validator = new LayerValidator();

  it('detects Golden Rule violation', () => {
    const css = '.c-button { margin: 8px; padding: var(--space-4); }';
    const result = validator.validate('test.css', css);
    expect(result.errors.some(e => e.message.includes('Golden Rule'))).toBe(true);
  });

  it('passes compliant component', () => {
    const css = fs.readFileSync(
      path.join(__dirname, 'fixtures', 'valid-component.css'), 'utf8'
    );
    const result = validator.validate('test.css', css);
    expect(result.errors).toHaveLength(0);
  });
});

describe('Semantic Validator', () => {
  const validator = new SemanticValidator();

  it('detects broken hasPart reference', () => {
    const html = '<div property="mcs:hasPart" resource="#missing">...</div>';
    const result = validator.validate('test.html', html);
    expect(result.errors.length).toBeGreaterThan(0);
  });
});
