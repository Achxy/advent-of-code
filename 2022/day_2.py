from advent import AdventSolution


class Solution(AdventSolution, day=2):
    PLAY = {"A": ["Z", "X", "Y"], "B": ["X", "Y", "Z"], "C": ["Y", "Z", "X"]}

    def __init__(self, data: str) -> None:
        self.data = [line.split() for line in data.splitlines()]

    def part_1(self):
        return sum(self.PLAY[oppo].index(me) * 3 + ord(me) - 87 for oppo, me in self.data)

    def part_2(self):
        return sum((fate := ord(res) - 88) * 3 + ord(self.PLAY[oppo][fate]) - 87 for oppo, res in self.data)
