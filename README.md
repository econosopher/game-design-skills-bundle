# Game Design Skills Bundle

This is econosopher's fork of [Stanislav Stankovic's game-design-skills-bundle](https://github.com/Stanestane/game-design-skills-bundle). The imported baseline is `85d5c6545afd0988de5ef1ee7d95e67edd8f5a7b`. Stan's 61 skill names and upstream history remain intact.

The fork adapts the bundle using [OpenAI's Astra guidance](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra) and a separate substantive claim review. It is not officially Astra-certified. The original baseline had no repository-wide license; this fork does not add one or relicense upstream material.

Use the [catalog](game-design-skill-catalog.md) to select a skill. Each skill has a focused `SKILL.md` and conditional references for its detailed method. The bundle covers creative direction, design choices, player research hypotheses, progression, monetization, social features, prototypes, production planning and visual artifacts.

- [Astra audit and validation](docs/astra-audit.md)
- [Per-skill dispositions](docs/astra-skill-dispositions.json)
- [Approved substantive decisions](docs/substantive-decisions.md)
- [Archive checks and hashes](docs/bundle-validation.json)

## Packaging

Skill folders are the authored source. Matching `.skill` ZIP archives are in `package-skills/`. Use the host application's supported skill installer and discovery location. Browser and image tools depend on the host's available capabilities and policies; these skills do not authorize a different browser or silently install dependencies.

```sh
python3 tools/bundle.py check
python3 tools/bundle.py build
python3 -m unittest discover -s tools -p 'test_*.py'
```

These commands use the Python standard library. Optional renderers have their own dependencies. The local functional checks do not establish cross-platform rendering parity.

A separate proposal adds `game-economy`, grounded in Phillip Black's public work. It is independent of this bundle adaptation. Keep both proposals open for review against this fork; no upstream proposal or notification is part of this work.
