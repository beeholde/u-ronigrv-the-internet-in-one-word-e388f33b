from pathlib import Path

WORD = "Scrollcoma"
OUTPUT = Path("/output/entry.txt")


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(WORD, encoding="utf-8")


if __name__ == "__main__":
    main()
