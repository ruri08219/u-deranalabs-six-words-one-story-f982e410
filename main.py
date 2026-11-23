"""Six Words, One Story — entry writer.

Writes the six-word story entry to /output/entry.txt after validation.
"""

import os

ENTRY = "The kettle whistled. Nobody was home."

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def validate(line):
    """Validate the entry line. Raises ValueError on any problem."""
    if not isinstance(line, str):
        raise ValueError("entry must be a string")
    if not line or not line.strip():
        raise ValueError("entry must not be empty or blank")
    if len(line) < 1 or len(line) > 60:
        raise ValueError("entry must be 1..60 characters")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must not contain a newline")
    if line != line.strip():
        raise ValueError("entry must not start or end with a space")
    line.encode("utf-8")
    return True


def main():
    validate(ENTRY)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        assert f.read() == ENTRY + "\n"


if __name__ == "__main__":
    main()
