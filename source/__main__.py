from pathlib import Path

SOURCE = Path(__file__).parent
GLOB_PATTERN = "day_*.py"


def get_all_solutions():
    for mod in SOURCE.glob(GLOB_PATTERN):
        stem = mod.stem
        yield getattr(__import__(stem), "Solution")
