from typing import List
from PyQt5.QtWidgets import QWidget

from src.Player.Player import Player
from src.shared.utils import load_ui


class EndPage(QWidget):
    def __init__(self, players: List[Player]):
        super(EndPage, self).__init__()
        load_ui(self, "./gui/ui/endseite.ui")

        players.sort(key=lambda s: s.getTotalScore(), reverse=True)

        for index, player in enumerate(players):
            self.rankingList.addItem(str(index + 1) + ". " + player.name)
