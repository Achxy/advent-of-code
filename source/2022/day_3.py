from advent import Advent


class Solution(Advent, year=2022, day=3):
    def __init__(self, data: str) -> None:
        self.data = data.splitlines()

    def part_1(self):
        arragement = ((set(s[: (h := len(s) >> 1)]) & set(s[h:])).pop() for s in self.data)
        return sum(self.get_priority(x) for x in arragement)

    def part_2(self):
        arrangement = (map(set, m) for m in zip(*[iter(self.data)] * 3, strict=True))
        return sum(self.get_priority((x & y & z).pop()) for x, y, z in arrangement)

    @staticmethod
    def get_priority(string: str):
        return unc - 96 if 90 < (unc := ord(string)) else unc - 38
