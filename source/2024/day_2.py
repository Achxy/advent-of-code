from operator import sub

from advent import Advent


class Solution(Advent, year=2024, day=2):
    def __init__(self, data: str) -> None:
        self.data = [[int(n) for n in m.split()] for m in data.splitlines()]

    def part_1(self) -> int:
        return sum(self._safe_level(*v) for v in (zip(d, d[1:]) for d in self.data))

    def _safe_level(self, *values: tuple[int, int]):
        (a, b), *_ = values
        pattern = self._sgn(a - b)
        for a, b in values:
            if not 1 <= abs(a - b) <= 3 or pattern != self._sgn(a - b):
                pattern = self._sgn(a - b)
                return 0
        return 1

    def _sgn(self, n):  # https://w.wiki/CNWy
        return -1 if n < 0 else 1
