# Astra adaptation and validation

This fork adapts Stanislav Stankovic's [game-design-skills-bundle](https://github.com/Stanestane/game-design-skills-bundle), based on upstream commit `85d5c6545afd0988de5ef1ee7d95e67edd8f5a7b`. The 61 original skill names and upstream connection are retained. No repository-wide license was present at that baseline; this change does not add one or claim to relicense upstream material.

The instruction review follows [OpenAI's Astra article](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra): give the model useful domain knowledge and decision criteria, make activation specific, and load detailed material when needed. Long prescribed sequences and full-report templates become conditional guidance. This is a maintained fork with bounded evaluation, not official Astra certification.

Instruction refactoring is committed separately from the approved substantive changes described in [the decision register](substantive-decisions.md). Moving a claim into a reference is not a factual validation of that claim. The retained leaderboard rules remain design guidance and are not independently established empirical laws.

## Per-skill coverage

[astra-skill-dispositions.json](astra-skill-dispositions.json) records all 61 skills, entrypoint sizes, description sizes and dispositions. Entrypoints decreased from 69,726 to 16,114 whitespace-delimited words. This measures entrypoint size, not total repository size or token savings in a real task. Detailed references remain available. Twenty-three skills also received approved substantive changes.

The catalog now indexes every existing skill and mirrors its current activation description. The separately proposed `game-economy` skill is independent of these source changes. Its catalog addition is near the introduction; this branch's edits update existing entries and add omitted ones. Integration must retain the union of 62 unique names and their separate directories and archives.

## Checks performed on 2026-09-13

- All 61 entrypoints pass the skill-creator YAML/frontmatter validator. Relative Markdown and referenced source paths resolve under the package checker.
- All 61 rebuilt `.skill` archives match their source files byte for byte. Archives exclude generated caches and reject symlinks. The package checker also checks unsafe and duplicate archive paths.
- Six offline regression tests pass: deterministic rebuilding, source drift, missing references, symlink rejection, unsafe/duplicate archive paths, cache exclusion, and missing-renderer behavior are covered across those six tests.
- All six upstream Python helpers parse. Synthetic executions pass for branch-map SVG, HTML moodboard generation, JPG/HTML moodboard generation and one-page Markdown/PDF generation. SVG parses; JPG dimensions and one-page PDF structure were checked. The JPG fixture was visually inspected. These are functional smoke tests, not comprehensive visual or cross-platform validation.
- The PNG browser helper no longer installs system packages or browser binaries automatically. Its missing-dependency behavior is tested without launching a browser. Actual browser rendering and live image downloads were not exercised; use the host's authorized browser and installed dependencies.
- An independent model walkthrough read all 61 entrypoints, supplied one positive and one nearby negative prompt for each, and executed eight synthetic tasks spanning behavior prompts, prototype histories, creative options, onboarding, budget, core loops, motivations and passes. This is routing review, not measured runtime activation accuracy.
- Six further answers exercised low-return pass value, unsupported audience shares, unfinished-task claims, accurate external attribution, supported behavioral evidence and incentive-confounded personality inference. The pass case reused a guide example and is a regression check. Five wording contradictions found during review were corrected, including universal randomness rankings and forced unique bottlenecks.

Package hashes are in [bundle-validation.json](bundle-validation.json). Commands to repeat the structural checks:

```sh
python3 tools/bundle.py check
python3 -m unittest discover -s tools -p 'test_*.py'
```

The model walkthrough is a small, single-run review. It does not establish broad superiority to the original bundle, validate every scientific claim, or prove that a specific host will activate every skill correctly. Read the separate local installation receipt for exact installed commits and host discovery evidence; repository validation alone is not installation proof.

Outgoing authored files, archives and new commit contents were reviewed for private paths, client identifiers, internal links and credential patterns. Public files contain shareable methods, public sources and synthetic examples. The source/profile review and confidential evidence are kept outside this repository.
