import pathlib
import zipfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILL_DIR = ROOT / "skills" / "right-talk"
DIST = ROOT / "dist"
OUT = DIST / "right-talk.zip"


def main():
    DIST.mkdir(exist_ok=True)
    with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(SKILL_DIR.rglob("*")):
            if path.is_file():
                archive.write(path, path.relative_to(SKILL_DIR.parent).as_posix())
    print(OUT)


if __name__ == "__main__":
    main()
