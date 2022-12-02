from advent import AdventSolution


class Solution(AdventSolution, day=2, run=True):
    # TODO: There is a pattern here!!!
    PLAY = {"A": ["Z", "X", "Y"], "B": ["X", "Y", "Z"], "C": ["Y", "Z", "X"]}

    def __init__(self, data: str) -> None:
        self.data = [line.split() for line in data.splitlines()]

    def part_1(self):
        score = 0
        for opponent, team in self.data:
            score += (self.PLAY[opponent].index(team) * 3) + (ord(team) - 87)
        return score
