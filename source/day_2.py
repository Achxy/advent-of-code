from advent import AdventSolution


class Solution(AdventSolution, day=2):
    # TODO: There is a pattern here!!!
    # Do complement wrapping so that the index is referenced
    # will do it later :-)
    PLAY = {"A": ["Z", "X", "Y"], "B": ["X", "Y", "Z"], "C": ["Y", "Z", "X"]}

    def __init__(self, data: str) -> None:
        self.data = [line.split() for line in data.splitlines()]

    def part_1(self):
        score = 0
        for opponent, team in self.data:
            score += self.PLAY[opponent].index(team) * 3 + ord(team) - 87
        return score

    def part_2(self):
        score = 0
        for opponent, result in self.data:
            fate = ord(result) - 88
            score += (fate * 3) + ord(self.PLAY[opponent][fate]) - 87
        return score
