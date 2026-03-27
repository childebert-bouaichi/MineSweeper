from dataclasses import dataclass

@dataclass
class Cell:
    row: int
    col: int
    is_mine: bool = False
    is_revealed: bool = False
    adjacent_mines: int = 0
    mark_state: str = " "

    def toggle_mark(self) -> None:
        if self.is_revealed:
            return

        if self.mark_state == " ":
            self.mark_state = "F"
        elif self.mark_state == "F":
            self.mark_state = "?"
        else:
            self.mark_state = " "