from itertools import starmap

from advent import Advent


class Solution(Advent, year=2024, day=1):
    def __init__(self, data: str) -> None:
        parsed = [*map(int, data.split())]
        self.left = parsed[0::2]
        self.right = parsed[1::2]

    def part_1(self):
        return sum(starmap(lambda x, y: abs(x - y), zip(*map(sorted, (self.left, self.right)))))

    def part_2(self):
        # count = functools.cache(self.right.count)
        # caching is pointless because in the actual data the values on the left do not repeat
        return sum(map(lambda x: x * self.right.count(x), self.left))
