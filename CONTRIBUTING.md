# Contributing

Thanks for helping make Claude less annoying.

## Report a leak

Open an issue with the exact phrase Claude used, what you asked, and which rule it should have followed.

## Propose a new rule

Every rule needs three things:

1. The banned phrase or habit
2. Why it wastes the user's time
3. What Claude should do instead

Add a before/after pair to `examples/before-after.md`.

## Pull requests

1. Fork the repo and create a branch
2. Edit `skills/right-talk/SKILL.md`
3. Run the validator:

```bash
python scripts/validate.py
```

4. Update `CHANGELOG.md`
5. Open a PR and fill out the template

## Skill rules

- Keep `SKILL.md` under 500 lines
- Keep the frontmatter `name` as `right-talk`
- Keep the description specific about when the skill should trigger
- Keep `SKILL.md` directly inside `skills/right-talk/`, the uploader rejects anything nested deeper in the zip
