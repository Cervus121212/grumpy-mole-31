#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest — make.fun entry.

Writes one short angry rant (399 chars, one line, <=400 gate) to
$MAKEFUN_OUTPUT_DIR/entry.txt as UTF-8, no trailing newline.
Stdlib only. Angle: "circling back" / "per my last email" — 0-hit in the
field, the canonical example named in the judge's own brief.
"""

import os

RANT = (
    "Dave from sales has circled back four times about an email I answered "
    "on Tuesday. Every time he attaches the original email, like evidence in "
    "a trial where I am somehow the defendant. Every time I reply 'answered "
    "Tuesday, see below.' Today he wrote 'per my last email' and CC'd my "
    "boss. Your last email is the email I already answered. You are not "
    "following up. You are a read receipt with a grudge."
)


def main() -> None:
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = RANT.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    os.chmod(path, 0o644)
    # Read back and verify byte-for-byte.
    with open(path, "rb") as f:
        assert f.read() == data, "entry.txt mismatch after write"


if __name__ == "__main__":
    main()
