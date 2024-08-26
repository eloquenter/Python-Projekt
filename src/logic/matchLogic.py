from typing import List


def getUpperNumberScore(dice: List, numberToTest: int):
    result = numberToTest * [x["value"] for x in dice].count(numberToTest)
    if result == 0:
        return -1

    return result


kleineStraseOptions = ["1234", "2345", "3456"]
groseStraseOptions = ["12345", "23456"]


def getDiceSortedString(dice: List):
    dice.sort()
    return "".join([str(s) for s in dice])


def getKleineStraseScore(dice: List):
    dice = [d["value"] for d in dice]

    isKleineStraseExistent = [
        o in getDiceSortedString(dice) for o in kleineStraseOptions
    ].count(True) > 0

    if isKleineStraseExistent:
        return 30

    return -1


def getGroseStraseScore(dice: list):
    dice = [d["value"] for d in dice]

    isGroseStraseExistent = [
        o in getDiceSortedString(dice) for o in groseStraseOptions
    ].count(True) > 0

    if isGroseStraseExistent:
        return 40

    return -1


def getPaschScore(dice: List, pasch: 3 | 4):
    dice = [d["value"] for d in dice]
    dice.sort()

    for x in range(6 - pasch):
        if dice.count(dice[x]) >= pasch:
            return sum(dice)

    return -1


def getFullHouseScore(dice: List):
    dice = [d["value"] for d in dice]
    dice.sort()

    if (
        (dice.count(dice[0]) == 2 and dice.count(dice[3]) == 3)
        or (dice.count(dice[0]) == 3 and dice.count(dice[3]) == 2)
    ) and dice[0] is not dice[3]:
        return 25
    return -1
