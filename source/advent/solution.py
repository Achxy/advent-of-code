from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path

DATA = Path(__file__).parent / "data"


class AdventSolution(ABC):
    __slots__ = ("__day__",)

    def __init_subclass__(cls, *, day: int | None = None, **kwargs) -> None:
        if day:
            cls.__day__ = day
            cls.__initialize_solution()
        super().__init_subclass__(**kwargs)

    @classmethod
    def __initialize_solution(cls):
        if cls.__module__ != "__main__":
            return
        cls.form().run_and_benchmark()

    @classmethod
    def form(cls):
        day = cls.__day__
        if day is None:
            raise RuntimeError("day must be provided to use form classmethod")
        data = cls.__get_text(day)
        self = cls(data)
        return self

    def run_and_benchmark(self):
        # TODO: Make this fancier with colors and stuff
        for routine in [self.part_1, self.part_2]:
            print(routine.__name__, "returned", routine())

    @staticmethod
    def __get_text(day):
        file = f"day_{day}.txt"
        with (DATA / file).open("r") as fp:
            return fp.read().strip()

    @abstractmethod
    def __init__(self, data: str) -> None:
        ...

    @abstractmethod
    def part_1(self):
        ...

    @abstractmethod
    def part_2(self):
        ...
