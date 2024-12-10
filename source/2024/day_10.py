from advent import Advent


class Solution(Advent, year=2024, day=10):
    def __init__(self, data: str) -> None:
        self.data = [[int(p) for p in q] for q in data.splitlines()]
        self.max_x = len(self.data[0])
        self.max_y = len(self.data)

    def part_1(self, remember=True):
        return sum(self._embark(x, y, 0, (x, y), set(), remember) for y in range(self.max_y) for x in range(self.max_x) if not self.data[y][x])

    def part_2(self):
        return self.part_1(remember=False)

    def _embark(self, x, y, val, ori, vi, rem):
        if val == 9 and (k := (*ori, x, y)) not in vi:
            return (vi.add(k) if rem else None) or 1
        return sum(self._embark(nx, ny, val + 1, ori, vi, rem) for nx, ny in [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)] if 0 <= nx < self.max_x and 0 <= ny < self.max_y and self.data[ny][nx] == val + 1)
