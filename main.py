"""Write one funny line to /output/entry.txt: a robot vacuum's excuse
after eating a sock, delivered deadpan as a personnel decision.

The joke: the vacuum denies eating anything — it claims it hired the
sock. The sock was "promoted" to lint and has already clocked in at
the dustbin, which is exactly where a vacuum would send new staff.
"""

import os

# The line is built from its two beats so the denial and the punchline
# stay separately editable: a flat refusal, then the HR reframing.
DENIAL = "I didn't eat your sock"
PROMOTION = "I promoted it to lint, and it's already clocked in at my dustbin."


def build_line() -> str:
    return f"{DENIAL} — {PROMOTION}"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(build_line())


if __name__ == "__main__":
    main()
