#!/usr/bin/env node
/**
 * Generates src/layers/utility.css from token-schema.json.
 * Every utility class maps to a defined token — no hand-authored overrides.
 */
const fs = require('fs');
const path = require('path');

const schemaPath = path.join(__dirname, '..', 'src', 'tokens', 'token-schema.json');
const outputPath = path.join(__dirname, '..', 'src', 'layers', 'utility.css');

const schema = JSON.parse(fs.readFileSync(schemaPath, 'utf8'));
const { utilities } = schema;

const lines = [
  '/* ============================================',
  ' * Layer 4: Utility — Single-Purpose Override Classes',
  ' * AUTO-GENERATED from token-schema.json — DO NOT EDIT',
  ' * Prefix: u-*',
  ' * Rules: One property per class, all use !important, immutable',
  ' * ============================================ */',
  ''
];

// Map schema utility keys to CSS properties
const propertyMap = {
  'text-align': 'text-align',
  'font-weight': 'font-weight',
  'display': 'display',
  'margin': 'margin',
  'padding': 'padding',
  'visually-hidden': null // special handling
};

const valueMap = {
  // font-weight needs numeric values for the properties
  'regular': 'var(--font-weight-regular)',
  'medium': 'var(--font-weight-medium)',
  'semibold': 'var(--font-weight-semibold)',
  'bold': 'var(--font-weight-bold)',
};

for (const [key, config] of Object.entries(utilities)) {
  const { values } = config;

  if (key === 'visually-hidden') {
    lines.push(`/* Visually hidden — accessible screen-reader-only content */`);
    lines.push(`.u-visually-hidden {`);
    lines.push(`  position: absolute !important;`);
    lines.push(`  width: 1px !important;`);
    lines.push(`  height: 1px !important;`);
    lines.push(`  overflow: hidden !important;`);
    lines.push(`  clip: rect(0, 0, 0, 0) !important;`);
    lines.push(`  white-space: nowrap !important;`);
    lines.push(`}`);
    lines.push('');
    continue;
  }

  const propName = propertyMap[key] || key;

  for (const val of values) {
    const className = `u-${key.replace('-', '-')}-${val}`;
    const cssValue = valueMap[val] || val;

    // Special: margin/padding-0
    if (['margin', 'padding'].includes(key) && val === '0') {
      lines.push(`.u-${key}-0 { ${propName}: 0 !important; }`);
    } else if (key === 'font-weight') {
      lines.push(`.u-font-${val} { ${propName}: ${cssValue} !important; }`);
    } else if (key === 'display') {
      lines.push(`.u-${val} { ${propName}: ${val} !important; }`);
    } else {
      lines.push(`.u-text-${val} { ${propName}: ${val} !important; }`);
    }
  }
  lines.push('');
}

fs.writeFileSync(outputPath, lines.join('\n') + '\n');
console.log(`Generated ${outputPath}`);
