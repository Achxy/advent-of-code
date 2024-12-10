from advent import Advent


class Solution(Advent, year=2024, day=10):
    def __init__(self, data: str) -> None:
        self.data = [[int(p) for p in q] for q in data.splitlines()]
        self.max_x = len(self.data[0])
        self.max_y = len(self.data)
        assert all(len(n) for n in self.data)

    def part_1(self):
        score = 0
        for y in range(self.max_y):
            for x in range(self.max_x):
                if not self.data[y][x]:
                    score += self._embark(x, y, origin=(x, y))
        return score

    def _embark(self, x: int, y: int, value: int = 0, origin=(), visited=set()) -> int:
        if value == 9 and (k := (*origin, x, y)) not in visited:
            visited.add(k)
            return 1
        vp1, score = value + 1, 0
        if x and self.data[y][x - 1] == vp1:
            score += self._embark(x - 1, y, vp1, origin)
        if y and self.data[y - 1][x] == vp1:
            score += self._embark(x, y - 1, vp1, origin)
        if self.max_x > (x + 1) and self.data[y][x + 1] == vp1:
            score += self._embark(x + 1, y, vp1, origin)
        if self.max_y > (y + 1) and self.data[y + 1][x] == vp1:
            score += self._embark(x, y + 1, vp1, origin)
        return score
