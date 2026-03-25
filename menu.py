

import tkinter as tk
from tkinter import Tk, Label, Frame, Button


class MinesweeperMenu:
    def __init__(self):
        self.root = Tk()
        self.root.title("Mines Weeper 💣")
        self.root.minsize(800, 850)

        self.title_label = Label(self.root, text="Menu")
        self.title_label.grid(row=0, column=8, columnspan=1)
        self.title_label.pack()

        self.frame = Frame(self.root)
        self.frame.pack()

        self.play_button = Button(self.frame, text=" jouer ")
        self.play_button.pack()

        self.difficulty_buttonup = Button(self.frame, text=" diff + ")
        self.difficulty_buttonup.pack()
        self.difficulty_buttondwn = Button(self.frame, text=" diff - ")
        self.difficulty_buttondwn.pack()
        
        self.difficulty_buttondwn.grid(row=1, column=0)
        self.difficulty_buttonup.grid(row=1, column=1)
        

        self.quit_button = Button(self.frame, text=" quitter ")
        self.quit_button.pack()

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    menu = MinesweeperMenu()
    menu.run()