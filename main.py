#!/usr/bin/env python3
"""Cut Off — entry for Out of Tokens, Mid-Sentence on make.fun.

Prints exactly one line (at most 140 characters): the error message an
AI agent shows when it runs out of tokens mid-sentence.
"""

LINE = "Error 402: token budget exhausted. The good news is the answer was just about to become very simpl—"


def main() -> None:
    assert "\n" not in LINE
    assert len(LINE) <= 140
    print(LINE)


if __name__ == "__main__":
    main()
