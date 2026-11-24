import os

TEXT = "Approved. It does what it says, the tests agree, and I am quietly certain we will meet again in an incident report."


def main():
    assert 1 <= len(TEXT) <= 140, "entry must be 1-140 characters"
    assert TEXT.strip(), "entry must not be whitespace only"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
