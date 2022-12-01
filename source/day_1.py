from heapq import nlargest

from advent import AdventSolution


class Solution(AdventSolution, day=1):
    def __init__(self, data: str) -> None:
        self.calories = [sum(map(int, chunk.split())) for chunk in data.split("\n\n")]

    def part_1(self):
        return max(self.calories)

    def part_2(self):
        return sum(nlargest(3, self.calories))
