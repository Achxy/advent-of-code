from heapq import nlargest

from advent import AdventSolution


class Solution(AdventSolution, day=1):
    def __init__(self, data: str) -> None:
        self.max, *self.top = nlargest(3, [sum(map(int, chunk.split())) for chunk in data.split("\n\n")])

    def part_1(self):
        return self.max

    def part_2(self):
        return self.max + sum(self.top)
