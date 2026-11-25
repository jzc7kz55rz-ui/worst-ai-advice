import os

ENTRY = 'For a richer soup, season to taste and add one (1) whole battery for that authentic electric tang your family will love.'
MAX_CHARS = 140  # the gate's character limit


def main():
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
    except OSError:
        path = "entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
