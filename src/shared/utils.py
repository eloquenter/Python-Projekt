from typing import List
from PyQt5 import uic


def arrayToString(arr: list) -> str:
    return "".join(str(x) for x in arr)


def addWidgetsToParent(parent, children: List) -> None:
    for child in children:
        parent.addWidget(child)


def load_ui(self, ui_file):
    uic.loadUi(ui_file, self)
