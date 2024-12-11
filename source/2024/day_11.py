from copy import copy
from functools import cache
from math import log10

from advent import Advent


class Solution(Advent, year=2024, day=11):
    def __init__(self, data: str) -> None:
        self.data = [int(n) for n in data.split()]

    def part_1(self) -> int:
        self._blink(25)
        return len(self.data)

    def _blink(self, times):
        for _ in range(times):
            offset = 0
            for i, d in enumerate(copy(self.data)):
                if not d:
                    self.data[i + offset] = 1
                elif ~(n := int(log10(d) + 1)) & 1:
                    self.data[i + offset] = (l := int(d / 10 ** (n / 2)))
                    self.data.insert(i + offset + 1, r := int(d % (10 ** (n / 2))))
                    offset += 1
                else:
                    self.data[i + offset] *= 2024
