import builtins
import os
import sys
from typing import Any, Mapping, cast

import pyperclip

from poml import poml


def load(file, context) -> str:
    frame = poml("poml/" + file, context)
    if hasattr(frame, "content"):
        frame = frame.content
    if (
        isinstance(frame, list)
        and frame
        and isinstance(frame[0], Mapping)
        and "content" in frame[0]
    ):
        frame0 = cast(Mapping[str, Any], frame[0])
        return str(frame0.get("content", ""))
    return str(frame)


def copy(text: str):
    pyperclip.copy(text)
    clear()
    print(text)
    print()


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def input(prompt: str = "") -> str:
    try:
        return builtins.input(prompt)
    except KeyboardInterrupt:
        sys.exit(0)
