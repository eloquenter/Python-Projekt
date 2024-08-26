from PyQt5.QtWidgets import QWidget, QMessageBox

from src.shared.utils import load_ui
from src.logic.matchLogic import (
    getUpperNumberScore,
    getGroseStraseScore,
    getKleineStraseScore,
    getFullHouseScore,
    getPaschScore,
)
from src.Game.Game import Game
from src.Player.Player import Player
from gui.handler.endpage import EndPage


class GamePage(QWidget):
    def __init__(self, nextPage, game: Game):
        self.showNextPage = nextPage
        super(GamePage, self).__init__()
        load_ui(self, "./gui/ui/spielseite.ui")
        self.game = game

        # --- ACTIONS ---

        self.einser_button.clicked.connect(
            lambda: self.processPlayerPick(
                "einser", getUpperNumberScore(self.game.dice, 1)
            )
        )
        self.zweier_button.clicked.connect(
            lambda: self.processPlayerPick(
                "zweier", getUpperNumberScore(self.game.dice, 2)
            )
        )
        self.dreier_button.clicked.connect(
            lambda: self.processPlayerPick(
                "dreier", getUpperNumberScore(self.game.dice, 3)
            )
        )
        self.vierer_button.clicked.connect(
            lambda: self.processPlayerPick(
                "vierer", (getUpperNumberScore(self.game.dice, 4))
            )
        )
        self.fuenfer_button.clicked.connect(
            lambda: self.processPlayerPick(
                "fuenfer", getUpperNumberScore(self.game.dice, 5)
            )
        )
        self.sechser_button.clicked.connect(
            lambda: self.processPlayerPick(
                "sechser", getUpperNumberScore(self.game.dice, 6)
            )
        )

        self.dreierpasch_button.clicked.connect(
            lambda: self.processPlayerPick(
                "dreierpasch", getPaschScore(self.game.dice, 3)
            )
        )
        self.viererpasch_button.clicked.connect(
            lambda: self.processPlayerPick(
                "viererpasch", getPaschScore(self.game.dice, 4)
            )
        )
        self.fullhouse_button.clicked.connect(
            lambda: self.processPlayerPick(
                "fullhouse", getFullHouseScore(self.game.dice)
            )
        )
        self.kleinestrase_button.clicked.connect(
            lambda: self.processPlayerPick(
                "kleinestrase", getKleineStraseScore(self.game.dice)
            ),
        )
        self.grosestrase_button.clicked.connect(
            lambda: self.processPlayerPick(
                "grosestrase",
                getGroseStraseScore(self.game.dice),
            )
        )
        self.kniffel_button.clicked.connect(
            lambda: self.processPlayerPick(
                "kniffel", sum([d["value"] for d in self.game.dice])
            )
        )

        self.throw_trys_label.setText(f"Versuche: {self.game.leftThrows}")
        self.throw_dice_button.clicked.connect(self.throwDiceAction)

        self.setScores(self.game.currentPlayer)
        self.setNameAndRound(self.game.currentPlayer.name, self.game.round)
        self.game.reset()
        self.setDices(self.game.dice)

    def setDices(self, diceValue):
        diceValue = [x["value"] for x in diceValue]
        # TODO lock dice: diceChangeable = [x["isChangeabe"] for x in diceValue]
        self.dice_one.setText(str(diceValue[0]))
        self.dice_two.setText(str(diceValue[1]))
        self.dice_three.setText(str(diceValue[2]))
        self.dice_four.setText(str(diceValue[3]))
        self.dice_five.setText(str(diceValue[4]))

    def setScores(self, player: Player):

        scores = player.scores
        lowerscore = player.getLowerScore()
        upperscore = player.getUpperScore()
        totalscore = player.getTotalScore()
        self.helper_setButton(self.einser_button, scores["einser"])
        self.helper_setButton(self.zweier_button, scores["zweier"])
        self.helper_setButton(self.dreier_button, scores["dreier"])
        self.helper_setButton(self.vierer_button, scores["vierer"])
        self.helper_setButton(self.fuenfer_button, scores["fuenfer"])
        self.helper_setButton(self.sechser_button, scores["sechser"])
        self.helper_setButton(self.dreierpasch_button, scores["dreierpasch"])
        self.helper_setButton(self.viererpasch_button, scores["viererpasch"])
        self.helper_setButton(self.fullhouse_button, scores["fullhouse"])
        self.helper_setButton(self.kleinestrase_button, scores["kleinestrase"])
        self.helper_setButton(self.grosestrase_button, scores["grosestrase"])
        self.helper_setButton(self.kniffel_button, scores["kniffel"])

        self.sum_top.setText(f"Summe Oben: {upperscore}")
        self.sum_bottom.setText(f"Summe Unten: {lowerscore}")
        self.sum_total.setText(f"Summe Gesamt: {totalscore}")

    def helper_setButton(self, buttonGUI, value):
        if value == -1:
            buttonGUI.setText(str(0))
            buttonGUI.setEnabled(False)
            return
        if value != 0:
            buttonGUI.setText(str(value))
            buttonGUI.setEnabled(False)

        else:
            buttonGUI.setText("Wählen")
            buttonGUI.setEnabled(True)

    def setNameAndRound(self, playerName, round):
        self.player_name.setText(playerName)
        self.round_label.setText(str(round))

    def setupPlayer(self):
        self.setScores(self.game.currentPlayer)
        self.setNameAndRound(self.game.currentPlayer.name, self.game.round)
        self.game.reset()
        self.setDices(self.game.dice)
        self.throw_trys_label.setText(f"Versuche: {self.game.leftThrows}")

    def processPlayerPick(self, pickedKey, getScoreResult):
        if self.game.dice == self.game.diceDefault:
            return QMessageBox.warning(self, "Fehler", "Würfel erst!")

        self.game.currentPlayer.scores[pickedKey] = getScoreResult

        self.game.nextPlayer()

        if self.game.round == 13:
            self.showNextPage(EndPage(self.game.players))
            return

        self.setupPlayer()

    def throwDiceAction(self):
        if not self.game.throwDices(self.throw_trys_label.setText):
            QMessageBox.warning(self, "Fehler", "Du hast schon alle Würfe verbraucht!")

        self.setDices(self.game.dice)
