from Cell import Cell
from utils import refactor

class Field:

    def __init__(self, x: int, y: int, rule_to_alive: int, rule_to_kill: tuple) -> None:
        self.field = [[Cell() for i in range(x)] for i in range(y)]
        self.rule_to_alive = rule_to_alive
        self.rule_to_kill = rule_to_kill

    def get_field(self) -> list:
        return self.field

    def create_cell(self, x: int, y: int) -> None:
        self.field[y][x].revive()

    def near(self, x: int, y: int, field: list) -> int:
        counter = 0
        char_field = field
        for y_pos in range(y - 1, y + 2):
            for x_pos in range(x - 1, x + 2):
                try:
                    if char_field[y_pos][x_pos]:
                        counter += 1
                except:
                     continue

        if char_field[y][x] == 1:
            return counter - 1
        return counter

    def logic(self) -> None:
        char_field = refactor(self.field)
        for y in range(len(self.field)):
            for x in range(len(self.field[0])):
                # if char_field[y][x] == 0 and self.near(x, y) == self.rule_to_alive:
                #     self.field[y][x].revive()
                # elif char_field[y][x] == 1 and self.near(x, y) > self.rule_to_kill[1] or self.near(x, y) < self.rule_to_kill[0]:
                #     self.field[y][x].kill()
                if char_field[y][x] == 0 and self.near(x, y, char_field) == 3:
                    self.field[y][x].revive()
                if char_field[y][x] == 1 and (self.near(x, y, char_field) > 3 or self.near(x, y, char_field) < 2):
                    self.field[y][x].kill()
