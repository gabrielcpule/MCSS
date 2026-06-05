const fs = require('fs');
const path = require('path');

describe('Layout Layer', () => {
  const layoutCss = fs.readFileSync(
    path.join(__dirname, '..', 'src', 'layers', 'layout.css'), 'utf8'
  );

  it('defines required layout classes', () => {
    expect(layoutCss).toContain('.l-container');
    expect(layoutCss).toContain('.l-grid');
    expect(layoutCss).toContain('.l-stack');
    expect(layoutCss).toContain('.l-center');
    expect(layoutCss).toContain('.l-cluster');
    expect(layoutCss).toContain('.l-switcher');
    expect(layoutCss).toContain('.l-sidebar');
  });

  it('layout classes use only l- prefix', () => {
    const classMatches = layoutCss.matchAll(/\.([a-z]+-[a-zA-Z0-9_-]+)/g);
    for (const match of classMatches) {
      expect(match[1]).toMatch(/^l-/);
    }
  });

  it('layout classes do not style component internals', () => {
    // No color, font, border, background declarations in layout layer
    expect(layoutCss).not.toContain('color:');
    expect(layoutCss).not.toContain('background');
    expect(layoutCss).not.toContain('border');
    expect(layoutCss).not.toContain('font-size');
  });
});

describe('Component Layer Aggregator', () => {
  const componentCss = fs.readFileSync(
    path.join(__dirname, '..', 'src', 'layers', 'component.css'), 'utf8'
  );

  it('imports all 15 atom components', () => {
    const atoms = ['badge', 'label', 'divider', 'text', 'link', 'image',
                   'button', 'input', 'checkbox', 'toggle', 'avatar', 'icon',
                   'spinner', 'tooltip', 'progress'];
    for (const atom of atoms) {
      expect(componentCss).toContain(`atoms/${atom}.css`);
    }
  });

  it('imports all 8 molecule components', () => {
    const molecules = ['card', 'search-form', 'login-form', 'alert',
                       'breadcrumb', 'pagination', 'dropdown', 'navigation'];
    for (const mol of molecules) {
      expect(componentCss).toContain(`molecules/${mol}.css`);
    }
  });
});

describe('Entry Point', () => {
  const entryCss = fs.readFileSync(
    path.join(__dirname, '..', 'src', 'mcss.css'), 'utf8'
  );

  it('imports in correct layer order', () => {
    const layerOrder = ['global', 'layout', 'component', 'utility', 'exception'];
    const positions = layerOrder.map(name => entryCss.indexOf(`layer(${name})`));
    for (let i = 1; i < positions.length; i++) {
      expect(positions[i]).toBeGreaterThan(positions[i - 1]);
    }
  });

  it('imports tokens before layers', () => {
    const tokensPos = entryCss.indexOf('tokens/tokens.css');
    const globalPos = entryCss.indexOf('layers/global.css');
    expect(tokensPos).toBeLessThan(globalPos);
  });
});
