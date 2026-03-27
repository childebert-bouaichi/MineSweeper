import random
from typing import List, Tuple
from backend.cell import Cell


class Board:
    def __init__(self, rows: int, cols: int, mine_count: int) -> None:
        self.rows = rows
        self.cols = cols
        self.mine_count = mine_count
        self.first_click = True
        self.grid: List[List[Cell]] = [
            [Cell(r, c) for c in range(cols)] for r in range(rows)
        ]

    def in_bounds(self, row: int, col: int) -> bool:
        return 0 <= row < self.rows and 0 <= col < self.cols

    def neighbors(self, row: int, col: int) -> List[Tuple[int, int]]:
        result = []

        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == 0 and dc == 0:
                    continue

                nr = row + dr
                nc = col + dc

                if self.in_bounds(nr, nc):
                    result.append((nr, nc))

        return result

    def place_mines(self, safe_row: int, safe_col: int) -> None:
        forbidden = {(safe_row, safe_col)}
        forbidden.update(self.neighbors(safe_row, safe_col))

        candidates = [
            (r, c)
            for r in range(self.rows)
            for c in range(self.cols)
            if (r, c) not in forbidden
        ]

        if len(candidates) < self.mine_count:
            raise ValueError("Trop de mines pour cette grille.")

        for r, c in random.sample(candidates, self.mine_count):
            self.grid[r][c].is_mine = True

        self.calculate_adjacent_mines()
        self.first_click = False

    def calculate_adjacent_mines(self) -> None:
        for r in range(self.rows):
            for c in range(self.cols):
                cell = self.grid[r][c]

                if cell.is_mine:
                    cell.adjacent_mines = -1
                    continue

                count = 0
                for nr, nc in self.neighbors(r, c):
                    if self.grid[nr][nc].is_mine:
                        count += 1

                cell.adjacent_mines = count

    def reveal_cell(self, row: int, col: int) -> bool:
        if not self.in_bounds(row, col):
            return True

        cell = self.grid[row][col]

        if cell.is_revealed or cell.mark_state == "F":
            return True

        if self.first_click:
            self.place_mines(row, col)
            cell = self.grid[row][col]

        cell.is_revealed = True
        cell.mark_state = " "

        if cell.is_mine:
            return False

        if cell.adjacent_mines == 0:
            self.flood_fill(row, col)

        return True

    def flood_fill(self, row: int, col: int) -> None:
        for nr, nc in self.neighbors(row, col):
            neighbor = self.grid[nr][nc]

            if neighbor.is_revealed:
                continue
            if neighbor.mark_state == "F":
                continue
            if neighbor.is_mine:
                continue

            neighbor.is_revealed = True
            neighbor.mark_state = " "

            if neighbor.adjacent_mines == 0:
                self.flood_fill(nr, nc)

    def toggle_mark(self, row: int, col: int) -> None:
        if self.in_bounds(row, col):
            self.grid[row][col].toggle_mark()

    def reveal_all_mines(self) -> None:
        for row in self.grid:
            for cell in row:
                if cell.is_mine:
                    cell.is_revealed = True

    def is_win(self) -> bool:
        for row in self.grid:
            for cell in row:
                if not cell.is_mine and not cell.is_revealed:
                    return False
        return True

    def count_flags(self) -> int:
        return sum(
            1
            for row in self.grid
            for cell in row
            if cell.mark_state == "F"
        )

    def mines_left_estimate(self) -> int:
        return self.mine_count - self.count_flags()

    def get_visible_board(self, reveal_all: bool = False) -> List[List[str]]:
        visible_grid: List[List[str]] = []

        for row in self.grid:
            visible_row: List[str] = []

            for cell in row:
                if reveal_all or cell.is_revealed:
                    if cell.is_mine:
                        visible_row.append("*")
                    elif cell.adjacent_mines == 0:
                        visible_row.append(" ")
                    else:
                        visible_row.append(str(cell.adjacent_mines))
                else:
                    if cell.mark_state == "F":
                        visible_row.append("F")
                    elif cell.mark_state == "?":
                        visible_row.append("?")
                    else:
                        visible_row.append(".")

            visible_grid.append(visible_row)

        return visible_grid