import os
import pyperclip
from poml import poml

def load(file, context) -> str:  # type: ignore
    output = poml("poml/" + file, context)
    content: str = output[0]["content"]
    return content

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
