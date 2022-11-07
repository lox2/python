class Cell:

    def __init__(self)  -> None:
        self.alive = False

    def is_alvie(self) -> bool:
        return self.alive

    def kill(self) -> None:
        self.alive = False

    def revive(self) -> None:
        self.alive = True

    def char(self) -> int:
        if self.alive:
            return 1
        return 0