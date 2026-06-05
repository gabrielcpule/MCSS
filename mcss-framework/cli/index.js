#!/usr/bin/env node
const { program } = require('commander');
const fs = require('fs');
const path = require('path');
const HtmlValidator = require('./validators/html-validator');
const CssValidator = require('./validators/css-validator');
const LayerValidator = require('./validators/layer-validator');
const SemanticValidator = require('./validators/semantic-validator');
const TerminalReporter = require('./reporters/terminal');

const schemaPath = path.join(__dirname, '..', 'src', 'tokens', 'token-schema.json');
const schema = JSON.parse(fs.readFileSync(schemaPath, 'utf8'));

program
  .name('mcss-validate')
  .description('Validate HTML and CSS files against MCSS framework rules')
  .argument('[path]', 'File or directory to validate', process.cwd())
  .option('--strict', 'Fail on warnings as well as errors')
  .option('--html', 'Run HTML checks only (RDFa, accessibility)')
  .option('--css', 'Run CSS checks only (tokens, layers)')
  .action(async (targetPath, options) => {
    const reporter = new TerminalReporter();
    const results = { _path: targetPath };

    const stat = fs.statSync(targetPath);
    const files = stat.isDirectory()
      ? findFiles(targetPath, ['.html', '.css'])
      : [targetPath];

    const htmlFiles = files.filter(f => f.endsWith('.html'));
    const cssFiles = files.filter(f => f.endsWith('.css'));

    if (!options.css) {
      const htmlValidator = new HtmlValidator(schema);
      for (const file of htmlFiles) {
        const content = fs.readFileSync(file, 'utf8');
        results[`HTML: ${path.basename(file)}`] = htmlValidator.validate(file, content);
      }
    }

    if (!options.html) {
      const cssValidator = new CssValidator(schema);
      const layerValidator = new LayerValidator();
      const semanticValidator = new SemanticValidator();

      for (const file of cssFiles) {
        const content = fs.readFileSync(file, 'utf8');
        results[`CSS (tokens): ${path.basename(file)}`] = cssValidator.validate(file, content);
        results[`CSS (layers): ${path.basename(file)}`] = layerValidator.validate(file, content);
        results[`CSS (semantic): ${path.basename(file)}`] = semanticValidator.validate(file, content);
      }
    }

    const score = reporter.report(results, options.strict);
    process.exitCode = score >= 90 ? 0 : 1;
  });

function findFiles(dir, extensions) {
  const results = [];
  const entries = fs.readdirSync(dir, { withFileTypes: true });

  for (const entry of entries) {
    const fullPath = path.join(dir, entry.name);
    if (entry.isDirectory() && entry.name !== 'node_modules' && entry.name !== '.git') {
      results.push(...findFiles(fullPath, extensions));
    } else if (extensions.some(ext => entry.name.endsWith(ext))) {
      results.push(fullPath);
    }
  }

  return results;
}

program.parse();
