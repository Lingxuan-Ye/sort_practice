from typing import List, Tuple

import testutils


def _hanoi(level: int, pillars: Tuple[str, str, str]) -> None:
    if level > 0:
        _hanoi(level-1, (pillars[0], pillars[2], pillars[1]))
        print(f"from {pillars[0]} move to {pillars[2]}", end="\n\n")
        _hanoi(level-1, (pillars[1], pillars[0], pillars[2]))


@testutils.timer
def hanoi(level: int, pillars: Tuple[str, str, str]) -> None:
    _hanoi(level, pillars)


class Hanoi:

    def __init__(self, level: int, pillars: Tuple[str, str, str]) -> None:
        self.level: int = level
        self.pillars: Tuple[str, str, str] = pillars
        self.__result: List[int] = []
        # available values:
        # ternary: 01, 02, 10, 12, 20, 21
        # decimal:  1,  2,  3,  5,  6,  7

    def _run(self, level: int, from_: int, via: int, to: int) -> None:
        if level > 0:
            self._run(level-1, from_=from_, via=to, to=via)
            self.__result.append(from_ * 3 + to)
            self._run(level-1, from_=via, via=from_, to=to)

    def run(self) -> None:
        self.__result.clear()
        self._run(self.level, from_=0, via=1, to=2)
        print(f"Total: {len(self.__result)} times", end="\n\n")
        for i, j in enumerate(self.__result):
            from_, to = divmod(j, 3)
            print(
                f"Step {i}:",
                f"from {self.pillars[from_]} to {self.pillars[to]}",
                sep="\n",
                end="\n\n"
            )


@testutils.timer
def hanoi_(level: int, pillars: Tuple[str, str, str]) -> None:
    Hanoi(level, pillars).run()


if __name__ == "__main__":
    hanoi(20, ("Pillar A", "Pillar B", "Pillar C"))
    print("\n\n", end="")
    hanoi_(20, ("Pillar A", "Pillar B", "Pillar C"))
