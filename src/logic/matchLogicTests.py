import unittest
from matchLogic import (
    getUpperNumberScore,
    getPaschScore,
    getGroseStraseScore,
    getKleineStraseScore,
    getFullHouseScore,
)


class Tests(unittest.TestCase):
    def mainTest(self, key, funtionToTest):
        for i, dice in enumerate(testCases):
            self.assertEqual(funtionToTest(dice), testResults[key][i])

    def testGetUpperNumberScore(self):
        for i, dice in enumerate(testCases):
            self.assertEqual(
                getUpperNumberScore(dice, i + 1), testResults["upperNumbersScore"][i]
            )

    def testGetDreierPaschScore(self):
        for i, dice in enumerate(testCases):
            self.assertEqual(getPaschScore(dice, 3), testResults["dreierpasch"][i])

    def testGetViererPaschScore(self):
        for i, dice in enumerate(testCases):
            self.assertEqual(getPaschScore(dice, 4), testResults["viererpasch"][i])

    def testGetKleineStraseScore(self):
        self.mainTest("kleinestrase", getKleineStraseScore)

    def testGetGroseStraseScore(self):
        self.mainTest("grosestrase", getGroseStraseScore)

    def testGetFullHouseScore(self):
        self.mainTest("fullhouse", getFullHouseScore)


def t(numbers):
    return [{"value": number, "isChangeable": True} for number in numbers]


testCases = [
    t([1, 2, 3, 4, 5]),
    t([5, 4, 2, 3, 1]),
    t([5, 5, 2, 3, 1]),
    t([2, 3, 2, 2, 3]),
    t([4, 3, 2, 1, 4]),
    t([4, 4, 1, 4, 4]),
]

testResults = {
    "upperNumbersScore": [1, 2, 3, -1, -1, -1],
    "dreierpasch": [-1, -1, -1, 12, -1, 17],
    "viererpasch": [-1, -1, -1, -1, -1, 17],
    "kleinestrase": [30, 30, -1, -1, 30, -1],
    "grosestrase": [40, 40, -1, -1, -1, -1],
    "fullhouse": [-1, -1, -1, 25, -1, -1],
}


if __name__ == "__main__":
    unittest.main()
