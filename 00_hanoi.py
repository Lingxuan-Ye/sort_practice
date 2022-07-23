from typing import List, Tuple


def _hanoi(level: int, from_: str, via: str, to: str) -> None:
    if level > 0:
        _hanoi(level-1, from_=from_, via=to, to=via)
        print(f"from {from_} move to {to}")
        _hanoi(level-1, from_=via, via=from_, to=to)


class Hanoi:

    def __init__(self, level: int, pillars: Tuple[str, str, str]) -> None:
        self.level: int = level
        self.pillars: Tuple[str, str, str] = pillars
        self.__result: List[Tuple[int, int]] = []

    def _run(self, level: int, from_: int, via: int, to: int) -> None:
        if level > 0:
            self._run(level-1, from_=from_, via=to, to=via)
            self.__result.append((from_, to))
            self._run(level-1, from_=via, via=from_, to=to)

    def run(self) -> None:
        self.__result.clear()
        self._run(self.level, from_=0, via=1, to=2)

        print(f"Total Number of Operations: {len(self.__result)}\n")
        for i, (j, k) in enumerate(self.__result):
            print(f"Step {i}:\nfrom {self.pillars[j]} to {self.pillars[k]}\n")


def hanoi(level: int, pillars: Tuple[str, str, str]) -> None:
    Hanoi(level, pillars).run()

if __name__ == "__main__":
    # _hanoi(4, "Pillar A", "Pillar B", "Pillar C")
    hanoi(4, ("Pillar A", "Pillar B", "Pillar C"))
