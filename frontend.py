import tkinter as tk
from tkinter import Button, Frame, messagebox
import time

# Backend imports
from backend.board import Board


class Minesweeper:
    def __init__(self):
        self.screen = tk.Tk()
        self.screen.title("Mines Weeper 💣")
        self.screen.minsize(800, 850)

        # Game variables
        self.width = 9
        self.height = 9
        self.mine_count = 10

        self.board: Board = None
        self.buttons: list[list[Button]] = []
        self.game_over = False
        self.first_click = True
        self.start_time = None

        # Top control frame
        self.frame = Frame(self.screen, height=90)
        self.frame.pack(pady=10, fill="x")

        self.difficulty_buttondwn = Button(self.frame, text=" difficulté - ", command=self.grid_down)
        self.play_button = Button(self.frame, text=" rejouer 😃", command=self.new_game)
        self.difficulty_buttonup = Button(self.frame, text=" difficulté + ", command=self.grid_up)
        self.song_button = Button(self.frame, text=" son 🎵 ")
        self.flag_widget = Button(self.frame, text="🚩 0")

        self.centrer_boutons()

        # Start the game
        self.new_game()

        self.screen.bind("<Configure>", self.on_resize)

    def new_game(self):
        """Reset game and create new board"""
        self.game_over = False
        self.first_click = True
        self.start_time = None

        self.board = Board(rows=self.height, cols=self.width, mine_count=self.mine_count)

        # Remove old grid if exists
        for widget in self.screen.winfo_children():
            if isinstance(widget, Frame) and widget != self.frame:
                widget.destroy()

        self.create_grid_buttons()

    def create_grid_buttons(self):
        """Create the grid of clickable buttons"""
        main_frame = Frame(self.screen)
        main_frame.pack(expand=True, pady=10)

        grid_frame = Frame(main_frame)
        grid_frame.pack()

        self.buttons = []

        for i in range(self.height):
            row_buttons = []
            for j in range(self.width):
                btn = Button(
                    grid_frame,
                    width=3,
                    height=1,
                    font=("Arial", 12, "bold"),
                    relief="raised",
                    bg="#c0c0c0"
                )
                btn.bind("<Button-1>", lambda e, r=i, c=j: self.left_click(r, c))
                btn.bind("<Button-3>", lambda e, r=i, c=j: self.right_click(r, c))

                btn.grid(row=i, column=j, padx=1, pady=1)
                row_buttons.append(btn)
            self.buttons.append(row_buttons)

    def left_click(self, row: int, col: int):
        """Handle left click on a cell"""
        if self.game_over:
            return
        self.reveal(row, col)

    def reveal(self, row: int, col: int):
        """Reveal cell using backend logic"""
        if self.first_click:
            self.first_click = False
            self.start_time = time.time()
            self.board.place_mines(row, col)

        safe = self.board.reveal_cell(row, col)

        if not safe:
            self.game_over = True
            self.reveal_all_mines()
            messagebox.showerror("BOOM !", "You lost... 💥")
            return

        self.update_visual_grid()

        if self.board.is_win():
            self.game_over = True
            messagebox.showinfo("Victory !", "Congratulations, you won! 🎉")

    def right_click(self, row: int, col: int):
        """Handle right click (flag / question mark)"""
        if self.game_over or self.first_click:
            return

        self.board.toggle_mark(row, col)
        self.update_visual_grid()

        # Update flag counter
        remaining = self.board.mines_left_estimate()
        self.flag_widget.config(text=f"🚩 {remaining}")

    def update_visual_grid(self):
        """Update all buttons appearance based on backend state"""
        reveal_all = self.game_over
        visible = self.board.get_visible_board(reveal_all=reveal_all)

        number_colors = ["", "blue", "green", "red", "navy", "maroon", "turquoise", "black", "gray"]

        for i in range(self.height):
            for j in range(self.width):
                btn = self.buttons[i][j]
                value = visible[i][j]

                if value == ".":
                    btn.config(text="", bg="#c0c0c0", state="normal")
                elif value == "F":
                    btn.config(text="🚩", bg="#ff9999", state="normal")
                elif value == "?":
                    btn.config(text="?", bg="#ffcc99", state="normal")
                elif value == "*":
                    btn.config(text="💣", bg="red", state="disabled")
                elif value == " ":
                    btn.config(text="", bg="#e0e0e0", state="disabled")
                else:  # number 1-8
                    btn.config(
                        text=value,
                        fg=number_colors[int(value)],
                        bg="#e0e0e0",
                        state="disabled"
                    )

    def reveal_all_mines(self):
        """Reveal all mines when player loses"""
        for i in range(self.height):
            for j in range(self.width):
                if self.board.grid[i][j].is_mine:
                    self.buttons[i][j].config(text="💣", bg="red", state="disabled")

    # ====================== Difficulty controls ======================

    def grid_up(self):
        if self.width < 20:
            self.width += 2
            self.height += 2
            self.mine_count = max(10, int(self.width * self.height * 0.15))
            self.new_game()

    def grid_down(self):
        if self.width > 8:
            self.width -= 2
            self.height -= 2
            self.mine_count = max(10, int(self.width * self.height * 0.15))
            self.new_game()

    def centrer_boutons(self):
        largeur = self.screen.winfo_width() or 800
        centre = largeur // 2

        self.difficulty_buttondwn.place(x=centre - 173, y=25, width=100)
        self.play_button.place(x=centre - 53, y=25, width=120)
        self.difficulty_buttonup.place(x=centre + 87, y=25, width=100)
        self.flag_widget.place(x=centre - 290, y=25, width=100)
        self.song_button.place(x=centre + 197, y=25, width=100)

    def on_resize(self, event):
        self.centrer_boutons()

    def run(self):
        self.screen.mainloop()