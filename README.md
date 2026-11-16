# right-talk

[![CI](https://github.com/Selfnify/right-talk/actions/workflows/ci.yml/badge.svg)](https://github.com/Selfnify/right-talk/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/Selfnify/right-talk)](https://github.com/Selfnify/right-talk/releases)

A Claude skill that makes Claude stop ragebaiting you.

No more fake confidence, fake friendliness, or victory laps over code that doesn't work.

## What it fixes

| Claude says | What it actually means | What right-talk makes it say |
|---|---|---|
| "You're absolutely right!" | I just spent 10 minutes insisting the opposite | "I was wrong. [what and why]" |
| "Excellent catch!" | You found a bug I introduced | "That's my bug. [what I broke]" |
| "That's the smoking gun!" | I have a theory and zero proof | "Likely cause, not confirmed. Check with [X]." |
| "Wait, actually, the real issue is..." | My last answer was a guess | "My earlier diagnosis was wrong. Verified: [X]. Still guessing: [Y]." |
| "This is a pre-existing issue" | I probably broke it | "Not sure if this predates my change. Check with [X]." |
| "All tests pass!" | I may have rewritten the tests to fit my code | "Ran [command]: [exact results]. Not covered: [gaps]." |
| *(invents a flag, path, or API)* | I'm guessing | "Haven't verified this. Checking [file/docs] first." |

See [`examples/before-after.md`](examples/before-after.md) for full side-by-side replies.

## Install

### Claude.ai

1. Grab `right-talk.zip` from the [latest release](https://github.com/Selfnify/right-talk/releases/latest)
2. Go to the skills upload page and upload the zip

The uploader needs `SKILL.md` directly inside the top-level folder of the zip. The release zip is built that way. Don't zip the whole repo, it will be rejected.

### Claude Code

```bash
git clone https://github.com/Selfnify/right-talk.git
```

```bash
cp -r right-talk/skills/right-talk ~/.claude/skills/
```

## Build the zip yourself

```bash
python scripts/validate.py
```

```bash
python scripts/package.py
```

The zip lands in `dist/right-talk.zip`.

## Repo layout

```
right-talk/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   ├── config.yml
│   │   └── feature_request.md
│   ├── workflows/
│   │   ├── ci.yml
│   │   └── release.yml
│   └── PULL_REQUEST_TEMPLATE.md
├── examples/
│   └── before-after.md
├── scripts/
│   ├── package.py
│   └── validate.py
├── skills/
│   └── right-talk/
│       └── SKILL.md
├── CHANGELOG.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── README.md
└── SECURITY.md
```

## Rules at a glance

1. Never say "You're absolutely right"
2. Never say "Excellent catch"
3. Never say "That's the smoking gun"
4. Never say "Wait, actually, the real issue is..." and stop guessing
5. Never say "This is a pre-existing issue" without proof
6. Never say "All tests pass!" without exact results
7. Stop guessing

Full details live in [`skills/right-talk/SKILL.md`](skills/right-talk/SKILL.md).

## Contributing

Phrase leaking through? Open an issue with the exact phrase and the context it showed up in. See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## License

MIT. See [`LICENSE`](LICENSE).
