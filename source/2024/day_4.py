from advent import Advent


class Solution(Advent, year=2024, day=4):
    def __init__(self, data: str) -> None:
        self.horizontal = data.splitlines()
        self.vertical = [*map("".join, zip(*self.horizontal))]

    def part_1(self):
        m1, m2 = "XMAS", "SAMX"
        hcount = sum(hstring.count(m1) + hstring.count(m2) for hstring in self.horizontal)
        vcount = sum(vstring.count(m1) + vstring.count(m2) for vstring in self.vertical)
        dcount = 0
        hstr, *_ = self.horizontal
        for p in range(len(self.horizontal) - (len(m1) - 1)):
            for q in range(len(hstr) - (len(m1) - 1)):
                rdia = "".join(self.horizontal[p + x][q + x] for x in range(len(m1)))
                ldia = "".join(self.horizontal[p + x][len(hstr) - 1 - x] for x in range(len(m1)))
                dcount += (rdia in (m1, m2)) + (ldia in (m1, m2))

        print(hcount, vcount, dcount)
        return hcount + vcount + dcount

    def part_2(self): ...


DT = """\
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

print(Solution(DT).part_1())
