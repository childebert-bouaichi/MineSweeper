# import tkinter as tk

# root = tk.Tk()
# root.title("💣 Projet Mine - Grid")

# # Création de widgets
# label1 = tk.Label(root, text="Case (0,0)", bg="lightblue")
# label2 = tk.Label(root, text="Case (0,1)", bg="lightgreen")
# label3 = tk.Label(root, text="Case (1,0)", bg="orange")
# label4 = tk.Label(root, text="Case (1,1)", bg="pink")

# # Placement avec grid
# label1.grid(row=0, column=0)
# label2.grid(row=0, column=1)
# label3.grid(row=1, column=0)
# label4.grid(row=1, column=1)

# root.mainloop()
# import tkinter as tk
# from tkinter import Tk, Button, Frame


# class Minesweeper:
#     def __init__(self):
#         self.screen = Tk()
#         self.screen.title("Mines Weeper 💣")
#         self.screen.minsize(800, 850)

#         self.largeur = 20
#         self.hauteur = 20

#         self.matrice = [[0 for _ in range(self.hauteur)] for _ in range(self.largeur)]

#         self.creer_boutons()

#     def creer_boutons(self):
#         frame_grille = Frame(self.screen)
#         frame_grille.pack(expand=True)
#         for i in range(self.largeur):
#             for j in range(self.hauteur):
#                 bouton = Button(self.screen, width=2, height=1)
#                 bouton.grid(row=i, column=j)

#     def run(self):
#         self.screen.mainloop()


# if __name__ == "__main__":
#     jeu = Minesweeper()
#     jeu.run()
# import tkinter as tk
# from tkinter import Tk, Button, Frame


# class Minesweeper:
#     def __init__(self):
#         self.screen = Tk()
#         self.screen.title("Mines Weeper 💣")
#         self.screen.minsize(800, 850)

#         self.width = 6
#         self.height = 6

#         self.frame = Frame(self.screen, height=80)        
#         self.frame.pack(pady=10, fill="x")

#         self.difficulty_buttondwn = Button(self.frame, text=" difficulty - ", command=self.grid_down)
#         self.difficulty_buttondwn.place(x=270, y=10, width=80)

#         self.play_button = Button(self.frame, text=" rejouer 😃", command=self.create_grid)
#         self.play_button.place(x=370, y=10, width=100)

#         self.difficulty_buttonup = Button(self.frame, text=" difficulty + ", command=self.grid_up)
#         self.difficulty_buttonup.place(x=490, y=10, width=80)
        
#         self.create_grid()

#     def create_grid(self):
#         for widget in self.screen.winfo_children():
#             if isinstance(widget, Frame) and widget != self.frame:
#                 widget.destroy()

#         main_frame = Frame(self.screen)
#         main_frame.pack(expand=True)

#         grid_frame = Frame(main_frame)
#         grid_frame.pack()

#         for i in range(self.width):
#             for j in range(self.height):
#                 button = Button(grid_frame, width=2, height=1)
#                 button.grid(row=i, column=j)

#     def grid_up(self):
#         if self.height and self.width < 22 :
#             self.width += 4
#             self.height += 4 
#             self.create_grid()
#     def grid_down(self):
#         if self.height and self.width > 10 :
#             self.width -= 4
#             self.height -= 4 
#             self.create_grid()

#     def run(self):
#         self.screen.mainloop()


# if __name__ == "__main__":
#     game = Minesweeper()
#     game.run()
import tkinter as tk
from tkinter import Tk, Button, Frame


class Minesweeper:
    def __init__(self):
        self.screen = Tk()
        self.screen.title("Mines Weeper 💣")
        self.screen.minsize(800, 850)

        self.width = 6
        self.height = 6

        self.frame = Frame(self.screen, height=90)
        self.frame.pack(pady=10, fill="x")

        self.difficulty_buttondwn = Button(self.frame, text=" difficulté - ", command=self.grid_down)
        self.play_button = Button(self.frame, text=" rejouer 😃", command=self.create_grid)
        self.difficulty_buttonup = Button(self.frame, text=" difficulté + ", command=self.grid_up)

        self.centrer_boutons()

        self.create_grid()

        self.screen.bind("<Configure>", self.on_resize)

    def centrer_boutons(self):
        largeur_fenetre = self.screen.winfo_width()
        if largeur_fenetre < 100:
            largeur_fenetre = 800

        centre = largeur_fenetre // 2

        self.difficulty_buttondwn.place(x=centre - 173, y=25, width=100)
        self.play_button.place(x=centre - 53, y=25, width=120)
        self.difficulty_buttonup.place(x=centre + 87, y=25, width=100)

    def on_resize(self, event):
        self.centrer_boutons()

    def create_grid(self):
        for widget in self.screen.winfo_children():
            if isinstance(widget, Frame) and widget != self.frame:
                widget.destroy()

        main_frame = Frame(self.screen)
        main_frame.pack(expand=True)

        grid_frame = Frame(main_frame)
        grid_frame.pack()

        for i in range(self.width):
            for j in range(self.height):
                button = Button(grid_frame, width=2, height=1)
                button.grid(row=i, column=j)

    def grid_up(self):
        if self.width < 22:
            self.width += 4
            self.height += 4
            self.create_grid()

    def grid_down(self):
        if self.width > 10:
            self.width -= 4
            self.height -= 4
            self.create_grid()

    def run(self):
        self.screen.mainloop()


if __name__ == "__main__":
    game = Minesweeper()
    game.run()