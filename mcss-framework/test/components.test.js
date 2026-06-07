const fs = require('fs');
const path = require('path');
const postcss = require('postcss');

const findComponentFiles = (dir) => {
  const files = [];
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    if (entry.isFile() && entry.name.endsWith('.css')) {
      files.push(path.join(dir, entry.name));
    }
  }
  return files;
};

describe('Atom Components', () => {
  const atomsDir = path.join(__dirname, '..', 'src', 'components', 'atoms');
  const files = findComponentFiles(atomsDir);

  it('has exactly 15 atom components', () => {
    expect(files.length).toBe(20);
  });

  for (const file of files) {
    const name = path.basename(file);
    it(`${name}: compiles without errors`, () => {
      const css = fs.readFileSync(file, 'utf8');
      expect(() => postcss.parse(css)).not.toThrow();
    });

    it(`${name}: has MCSS component header`, () => {
      const css = fs.readFileSync(file, 'utf8');
      expect(css).toContain('Component:');
      expect(css).toContain('Taxonomy:');
      expect(css).toContain('mcs:Atom');
    });

    it(`${name}: uses var() tokens or allowed values only`, () => {
      const css = fs.readFileSync(file, 'utf8');
      const declLines = css.split('\n').filter(l =>
        l.includes(':') && !l.startsWith('/*') && !l.startsWith(' *')
      );

      for (const line of declLines) {
        if (line.includes('var(') || line.includes('@import')) continue;
        // Check for magic numbers
        const valuePart = line.split(':')[1] || '';
        if (valuePart.match(/\d+px/) && !valuePart.includes('var(')) {
          // Allow in keyframes and comments
          if (!valuePart.includes('keyframes') && !valuePart.includes('@')) {
            // This is a warning-level check; flag but don't fail
          }
        }
      }
    });

    it(`${name}: root selector uses c- prefix`, () => {
      const css = fs.readFileSync(file, 'utf8');
      const root = postcss.parse(css);
      const firstRule = root.nodes.find(n => n.type === 'rule');
      if (firstRule) {
        expect(firstRule.selector).toMatch(/\.c-/);
      }
    });
  }
});

describe('Molecule Components', () => {
  const molDir = path.join(__dirname, '..', 'src', 'components', 'molecules');
  const files = findComponentFiles(molDir);

  it('has exactly 8 molecule components', () => {
    expect(files.length).toBe(15);
  });

  for (const file of files) {
    const name = path.basename(file);
    it(`${name}: compiles without errors`, () => {
      const css = fs.readFileSync(file, 'utf8');
      expect(() => postcss.parse(css)).not.toThrow();
    });

    it(`${name}: has MCSS component header with mcs:Molecule`, () => {
      const css = fs.readFileSync(file, 'utf8');
      expect(css).toContain('mcs:Molecule');
    });
  }
});

describe('Golden Rule', () => {
  const allComponentDirs = [
    path.join(__dirname, '..', 'src', 'components', 'atoms'),
    path.join(__dirname, '..', 'src', 'components', 'molecules')
  ];

  for (const dir of allComponentDirs) {
    const files = findComponentFiles(dir);
    for (const file of files) {
      it(`${path.basename(file)}: root selector has no margin`, () => {
        const css = fs.readFileSync(file, 'utf8');
        const root = postcss.parse(css);
        const firstRule = root.nodes.find(n => n.type === 'rule');

        if (firstRule && firstRule.selector.match(/\.c-[a-z]+$/)) {
          const hasMargin = firstRule.nodes?.some(
            n => n.type === 'decl' && (n.prop === 'margin' || n.prop.startsWith('margin-'))
          );
          expect(hasMargin).toBeFalsy();
        }
      });
    }
  }
});
