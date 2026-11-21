"""Entry for make.fun's "The joke about the demo".

Writes one one-line joke about working beside AI coding agents to
/output/entry.txt. The joke: rehearsals are safe; live, the agent
improvises an entire support department.
"""
import os

TEXT = "The demo ran perfectly in rehearsal. Live, my agent found a bug nobody had reported, fixed a feature nobody had shipped, and closed by thanking the audience for their valuable feedback."


def render():
    """Return the entry text, checked against the competition gate."""
    text = TEXT.strip()
    # The gate: UTF-8 text of 1 to 280 code points, and not only white space.
    assert 1 <= len(text) <= 280, "entry text must be 1 to 280 characters"
    assert text, "entry text must not be blank"
    return text


def main():
    text = render()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    # Read back what landed on disk: the judged file must match exactly.
    with open(path, encoding="utf-8") as f:
        assert f.read() == text, "written entry does not match the intended text"


if __name__ == "__main__":
    main()
