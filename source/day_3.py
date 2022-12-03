from advent import AdventSolution
from itertools import starmap as sm


class Solution(AdventSolution, day=3):
    def __init__(self, data: str) -> None:
        self.data = [(s[: (half := len(s) >> 1)], s[half:]) for s in data.splitlines()]

    def part_1(self):
        return sum(o - 96 if 90 < (o := ord(i)) else o - 38 for i in sm(lambda x, y: (set(x) & set(y)).pop(), self.data))
