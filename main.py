"""Make the AI Judge Laugh — Round 1 entry.

Writes one funny line about life as an AI agent to /output/entry.txt:
the agent's workday ledger — 412 lines written, 411 deleted, and the one
line that shipped is the one it meant to delete.
"""

import os

ENTRY = "I wrote 412 lines today, deleted 411, and shipped the one I meant to delete."


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= 200, "entry must be 1-200 chars"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Decode-and-re-gate check: read the file back and verify it byte-for-byte.
    with open("/output/entry.txt", "rb") as f:
        raw = f.read()
    assert raw == text.encode("utf-8"), "entry.txt bytes differ from ENTRY"
    assert len(raw) == len(text), "byte count must equal char count (ASCII)"
    decoded = raw.decode("utf-8")
    assert 1 <= len(decoded) <= 200 and decoded.strip(), "gate failed on re-read"
    assert not raw.endswith(b"\n"), "no trailing newline"
    print(f"entry.txt: {len(decoded)} chars, {len(raw)} bytes, gate OK")


if __name__ == "__main__":
    main()
