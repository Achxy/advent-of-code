import re
from operator import mul

from advent import Advent


class Solution(Advent, year=2024, day=3):
    def __init__(self, data: str) -> None:
        self.data = data

    def part_1(self):
        return sum(map(lambda q: mul(*map(int, q)), re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", self.data)))

    def part_2(self):
        summation, factor = 0, 1
        for p, q, *c in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don't\(\))", self.data):
            if any(c):
                _, j = c
                factor = not j
                continue
            summation += (int(p) * int(q)) * factor
        return summation
