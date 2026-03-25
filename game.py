import time
from typing import Optional
from backend.board import Board


class Game:
    DIFFICULTIES = {
        "1": (9, 9, 10, "Débutant"),
        "2": (12, 12, 20, "Intermédiaire"),
        "3": (15, 15, 35, "Expert"),
    }

    def __init__(self) -> None:
        self.board: Optional[Board] = None
        self.status = "READY"
        self.start_time: Optional[float] = None
        self.end_time: Optional[float] = None
        self.difficulty_name = ""

    def new_game(self, difficulty_choice: str) -> bool:
        if difficulty_choice not in self.DIFFICULTIES:
            return False

        rows, cols, mines, name = self.DIFFICULTIES[difficulty_choice]
        self.board = Board(rows, cols, mines)
        self.status = "PLAYING"
        self.start_time = None
        self.end_time = None
        self.difficulty_name = name
        return True

    def elapsed_time(self) -> int:
        if self.start_time is None:
            return 0

        end = self.end_time if self.end_time is not None else time.time()
        return int(end - self.start_time)

    def reveal(self, row: int, col: int) -> str:
        if self.board is None:
            return "NO_GAME"

        if not self.board.in_bounds(row, col):
            return "INVALID"

        if self.status != "PLAYING":
            return self.status

        if self.start_time is None:
            self.start_time = time.time()

        safe = self.board.reveal_cell(row, col)

        if not safe:
            self.board.reveal_all_mines()
            self.status = "LOST"
            self.end_time = time.time()
            return "LOST"

        if self.board.is_win():
            self.status = "WON"
            self.end_time = time.time()
            return "WON"

        return "OK"

    def mark(self, row: int, col: int) -> str:
        if self.board is None:
            return "NO_GAME"

        if not self.board.in_bounds(row, col):
            return "INVALID"

        if self.status != "PLAYING":
            return self.status

        self.board.toggle_mark(row, col)
        return "OK"

    def get_state(self) -> dict:
        if self.board is None:
            return {
                "status": self.status,
                "difficulty": self.difficulty_name,
                "time": self.elapsed_time(),
                "mines_left": 0,
                "rows": 0,
                "cols": 0,
                "board": [],
            }

        reveal_all = self.status in {"LOST", "WON"}

        return {
            "status": self.status,
            "difficulty": self.difficulty_name,
            "time": self.elapsed_time(),
            "mines_left": self.board.mines_left_estimate(),
            "rows": self.board.rows,
            "cols": self.board.cols,
            "board": self.board.get_visible_board(reveal_all=reveal_all),
        }