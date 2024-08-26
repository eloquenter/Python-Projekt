from PyQt5.QtWidgets import QWidget, QMessageBox

from src.shared.utils import load_ui
from src.Player.Player import Player


class StartPage(QWidget):
    def __init__(self, nextPage):
        self.showNextPage = nextPage
        super(StartPage, self).__init__()
        load_ui(self, "./gui/ui/startseite.ui")

        self.players = []

        # --- ACTIONS ---
        self.player_add_button.clicked.connect(self.addPlayer)
        self.player_remove_button.clicked.connect(self.removePlayer)
        self.start_game_button.clicked.connect(self.startGame)

    # --- ACTION FUNCTIONS ---
    def addPlayer(self):
        player_name = self.player_input.text().strip()

        if player_name:
            self.player_list.addItem(player_name)
            self.player_input.clear()
        else:
            QMessageBox.warning(self, "Fehler", "Spielername darf nicht leer sein!")

    def removePlayer(self):
        selected_items = self.player_list.selectedItems()

        if not selected_items:
            return QMessageBox.warning(self, "Fehler", "Wähle einen Spieler aus!")

        for item in selected_items:
            self.player_list.takeItem(self.player_list.row(item))

    # entries = [listWidget.item(index).text() for index in range(listWidget.count())]

    def startGame(self):
        playerAmount = self.player_list.count()

        self.players = [
            Player(self.player_list.item(index).text())
            for index in range(self.player_list.count())
        ]

        if playerAmount > 0:
            self.showNextPage()
        else:
            return QMessageBox.warning(self, "Fehler", "Erstelle Spieler!")
