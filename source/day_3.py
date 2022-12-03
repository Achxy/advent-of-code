from advent import AdventSolution
from itertools import starmap as sm


class Solution(AdventSolution, day=3):
    def __init__(self, data: str) -> None:
        self.data = data.splitlines()

    def part_1(self):
        arragement = ((set(s[: (h := len(s) >> 1)]) & set(s[h:])).pop() for s in self.data)
        return sum(self.get_priority(x) for x in arragement)

    @staticmethod
    def get_priority(string: str):
        return unc - 96 if 90 < (unc := ord(string)) else unc - 38
