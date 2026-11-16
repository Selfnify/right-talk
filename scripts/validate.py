import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILL_FILE = ROOT / "skills" / "right-talk" / "SKILL.md"
MAX_LINES = 500


def main():
    if not SKILL_FILE.is_file():
        sys.exit(f"missing {SKILL_FILE}")
    text = SKILL_FILE.read_text(encoding="utf-8").replace("\r\n", "\n")
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not match:
        sys.exit("SKILL.md has no YAML frontmatter")
    fields = {}
    for line in match.group(1).splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip()
    if fields.get("name") != "right-talk":
        sys.exit("frontmatter name must be right-talk")
    if not fields.get("description"):
        sys.exit("frontmatter description is empty")
    if len(text.splitlines()) > MAX_LINES:
        sys.exit(f"SKILL.md is over {MAX_LINES} lines")
    print("SKILL.md is valid")


if __name__ == "__main__":
    main()
