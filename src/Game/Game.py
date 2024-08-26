import random
from typing import List

from src.Player.Player import Player


diceDefault = [{"value": 0, "isChangeable": True} for _ in range(5)]


class Game:
    def __init__(self, players: List[Player]):
        self.players = players
        self.currentPlayerIndex = 0
        self.currentPlayer = players[self.currentPlayerIndex]
        self.round = 1  # Runden von 1-12
        self.leftThrows = 3
        self.dice = diceDefault
        self.diceDefault = [{"value": 0, "isChangeable": True} for _ in range(5)]

    def throwDices(self, setText):
        if self.leftThrows > 0:
            self.leftThrows -= 1
            setText(f"Versuche: {self.leftThrows}")
            self.dice = [self.helper_getDiceValue(x) for x in self.dice]
            return True
        else:
            return False

    def helper_getDiceValue(self, x):
        if x["isChangeable"]:
            # trunk-ignore(bandit/B311)
            return {"value": random.randint(1, 6), "isChangeable": True}
        else:
            return x

    def reset(self):
        self.leftThrows = 3
        self.dice = diceDefault

    def nextPlayer(self):
        if self.currentPlayer == self.players[-1]:
            self.currentPlayer = self.players[0]
            self.round += 1
        else:
            self.currentPlayer = self.players[self.currentPlayerIndex + 1]
