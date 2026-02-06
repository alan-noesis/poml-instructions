import os
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
    if os.name == "nt":
        _ = os.system("cls")
    else:
        _ = os.system("clear")
