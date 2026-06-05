const chalk = require('chalk');

class TerminalReporter {
  report(results, strictMode = false) {
    console.log('');
    console.log(chalk.bold(' MCSS Validation Report'));
    console.log(chalk.gray(' ━━━━━━━━━━━━━━━━━━━━━━━━━━━'));

    let totalChecks = 0;
    let passedChecks = 0;

    for (const [name, result] of Object.entries(results)) {
      if (name === '_path') continue;

      const hasErrors = result.errors.length > 0;
      const hasWarnings = result.warnings.length > 0;
      totalChecks++;

      if (!hasErrors && (!hasWarnings || !strictMode)) {
        passedChecks++;
        console.log(` ${chalk.green('✓')} ${name}`);
      } else {
        console.log(` ${chalk.red('✗')} ${name}`);
      }

      for (const err of result.errors) {
        console.log(chalk.red(`   → ${err.file || ''}: ${err.message}`));
      }
      for (const warn of result.warnings) {
        console.log(chalk.yellow(`   → ${warn.file || ''}: ${warn.message}`));
      }
    }

    const score = totalChecks > 0 ? Math.round((passedChecks / totalChecks) * 100) : 100;
    console.log('');
    console.log(` Source: ${results._path || 'unknown'}`);
    console.log(` Checks: ${totalChecks} | Passed: ${passedChecks} | Failed: ${totalChecks - passedChecks}`);
    console.log(chalk.bold(` Compliance score: ${score}%`));
    console.log('');

    return score;
  }
}

module.exports = TerminalReporter;
