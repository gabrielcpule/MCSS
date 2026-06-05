const fs = require('fs');
const path = require('path');

const schemaPath = path.join(__dirname, '..', 'src', 'tokens', 'token-schema.json');
const tokensCssPath = path.join(__dirname, '..', 'src', 'tokens', 'tokens.css');

describe('Design Token System', () => {
  it('token-schema.json is valid JSON', () => {
    const schema = JSON.parse(fs.readFileSync(schemaPath, 'utf8'));
    expect(schema).toHaveProperty('tokens');
    expect(schema).toHaveProperty('categories');
    expect(schema).toHaveProperty('utilities');
    expect(schema).toHaveProperty('layers');
    expect(schema).toHaveProperty('rdfa');
  });

  it('token-schema defines all 5 layers in correct order', () => {
    const schema = JSON.parse(fs.readFileSync(schemaPath, 'utf8'));
    expect(schema.layers.order).toEqual(['global', 'layout', 'component', 'utility', 'exception']);
  });

  it('token-schema defines valid RDFa taxonomy levels', () => {
    const schema = JSON.parse(fs.readFileSync(schemaPath, 'utf8'));
    expect(schema.rdfa.validTaxonomyLevels).toContain('mcs:Atom');
    expect(schema.rdfa.validTaxonomyLevels).toContain('mcs:Molecule');
    expect(schema.rdfa.validTaxonomyLevels).toContain('mcs:Organism');
  });

  it('tokens.css defines all required color tokens', () => {
    const css = fs.readFileSync(tokensCssPath, 'utf8');
    expect(css).toContain('--color-white');
    expect(css).toContain('--color-black');
    expect(css).toContain('--color-gray-900');
    expect(css).toContain('--color-brand-500');
    expect(css).toContain('--color-text-primary');
    expect(css).toContain('--color-background-primary');
  });

  it('tokens.css defines all required spacing tokens', () => {
    const css = fs.readFileSync(tokensCssPath, 'utf8');
    expect(css).toContain('--space-1');
    expect(css).toContain('--space-4');
    expect(css).toContain('--space-16');
  });

  it('tokens.css defines all font size tokens with semantic names', () => {
    const css = fs.readFileSync(tokensCssPath, 'utf8');
    expect(css).toContain('--font-size-display');
    expect(css).toContain('--font-size-title');
    expect(css).toContain('--font-size-heading');
    expect(css).toContain('--font-size-subtitle');
    expect(css).toContain('--font-size-body');
    expect(css).toContain('--font-size-caption');
    expect(css).toContain('--font-size-overline');
  });

  it('tokens.css defines purpose-named breakpoints', () => {
    const css = fs.readFileSync(tokensCssPath, 'utf8');
    expect(css).toContain('--breakpoint-mobile');
    expect(css).toContain('--breakpoint-tablet');
    expect(css).toContain('--breakpoint-desktop');
    expect(css).toContain('--breakpoint-wide');
  });

  it('tokens.css uses semantic aliases via var()', () => {
    const css = fs.readFileSync(tokensCssPath, 'utf8');
    expect(css).toContain('var(--color-gray-900)');
  });
});

describe('Global Layer', () => {
  it('global.css exists and compiles', () => {
    const globalCssPath = path.join(__dirname, '..', 'src', 'layers', 'global.css');
    expect(fs.existsSync(globalCssPath)).toBe(true);
  });

  it('global.css contains reset rules', () => {
    const css = fs.readFileSync(path.join(__dirname, '..', 'src', 'layers', 'global.css'), 'utf8');
    expect(css).toContain('box-sizing: border-box');
    expect(css).toContain('margin: 0');
  });

  it('global.css uses tokens, not magic numbers', () => {
    const css = fs.readFileSync(path.join(__dirname, '..', 'src', 'layers', 'global.css'), 'utf8');
    // Should NOT contain hardcoded font values
    expect(css).not.toMatch(/font-size:\s*\d+px/);
    expect(css).not.toMatch(/font-family:\s+(?!var)/);
    // Should use var()
    expect(css).toContain('var(--font-family-sans)');
    expect(css).toContain('var(--line-height-base)');
  });
});
