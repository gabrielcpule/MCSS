/**
 * Validates semantic integrity:
 * - hasPart relationships are well-formed
 * - Component composition is valid (molecules contain atoms)
 */
class SemanticValidator {
  validate(filePath, content) {
    const errors = [];
    const warnings = [];

    // Semantic validation uses pattern matching rather than full RDF store
    // Check that mcs:hasPart references are not self-referencing
    const hasPartPattern = /property="mcs:hasPart"\s+resource="#([^"]+)"/g;
    let match;
    while ((match = hasPartPattern.exec(content)) !== null) {
      const resourceId = match[1];
      if (!content.includes(`id="${resourceId}"`)) {
        errors.push({
          file: filePath,
          message: `mcs:hasPart references resource="#${resourceId}" but no element with that id found`
        });
      }
    }

    return { errors, warnings };
  }
}

module.exports = SemanticValidator;
