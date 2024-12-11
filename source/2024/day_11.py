from functools import cache
from math import log10

from advent import Advent


class Solution(Advent, year=2024, day=11):
    def __init__(self, data: str) -> None:
        self.data = [int(n) for n in data.split()]

    def part_1(self, blinks=25) -> int:
        return sum(self._stonefind(s, blinks) for s in self.data)

    def part_2(self) -> int:
        return self.part_1(blinks=75)

    @cache
    def _stonefind(self, stone, blinks):
        if not blinks:
            return 1
        if not stone:
            return self._stonefind(1, blinks - 1)
        if ~(n := int(log10(stone) + 1)) & 1:
            return self._stonefind(int(stone / 10 ** (n / 2)), blinks - 1) + self._stonefind(int(stone % 10 ** (n / 2)), blinks - 1)
        return self._stonefind(stone * 2024, blinks - 1)
