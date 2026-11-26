from pathlib import Path

ENTRY_WORD = "Scrollcoma"
TARGET = Path("/output/entry.txt")


def write_entry() -> None:
    output_dir = TARGET.parent
    output_dir.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(ENTRY_WORD, encoding="utf-8")


if __name__ == "__main__":
    write_entry()
