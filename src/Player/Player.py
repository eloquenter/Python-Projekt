from PyQt5.QtWidgets import QMessageBox


class Player:
    def __init__(self, name):
        self.name: str = name
        self.isBonusShown = False
        self.scores = {
            "einser": 0,
            "zweier": 0,
            "dreier": 0,
            "vierer": 0,
            "fuenfer": 0,
            "sechser": 0,
            "dreierpasch": 0,
            "viererpasch": 0,
            "fullhouse": 0,
            "kleinestrase": 0,
            "grosestrase": 0,
            "kniffel": 0,
        }
        self.upperscores = [
            "einser",
            "zweier",
            "dreier",
            "vierer",
            "fuenfer",
            "sechser",
        ]

        self.lowerscores = [
            "dreierpasch",
            "viererpasch",
            "fullhouse",
            "kleinestrase",
            "grosestrase",
            "kniffel",
        ]

    def getUpperScore(self):
        return self.getScore(self.upperscores)

    def getLowerScore(self):
        return self.getScore(self.lowerscores)

    def getScore(self, score):
        result = 0
        score = [self.scores[key] for key in score]

        for s in score:
            if s is not -1:
                result += s

        return result

    def getTotalScore(self):
        score = self.getUpperScore() + self.getLowerScore()
        if self.getUpperScore() >= 63:
            score += 35
            if self.isBonusShown is False:
                self.isBonusShown = True
                QMessageBox.warning(self, "Fehler", "Du hast den Bonus erhalten!")

        return score
