# trunk-ignore(ruff/F403)
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout

from gui.handler.startpage import StartPage
from gui.handler.gamepage import GamePage
from src.Game.Game import Game

# from gui.handler.endpage import EndPage


class MainHandler(QMainWindow):
    def __init__(self):
        super(MainHandler, self).__init__()
        self.setWindowTitle("Kniffel")

        # Erstellen eines zentralen Widgets und Layouts
        self.central_widget = QWidget()
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

        # Initialisieren der ersten Seite
        self.current_page = None
        self.startPage = StartPage(self.showGamePage)
        self.showNextPage(self.startPage)

    def showNextPage(self, newPage):
        if self.current_page:
            self.current_page.hide()

        self.current_page = newPage
        self.layout.addWidget(self.current_page)
        self.current_page.show()

    def showGamePage(self):
        self.showNextPage(
            GamePage(
                self.showNextPage,
                Game(self.startPage.players),
            )
        )
